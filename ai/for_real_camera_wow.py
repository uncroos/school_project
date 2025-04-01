import cv2
import tflite_runtime.interpreter as tflite
import numpy as np
import time

try:
    # 1. 모델 로드
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # 얼굴 감지 모델
    interpreter = tflite.Interpreter(model_path='model_unquant.tflite')  # Teachable Machine 모델
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # 2. 외부 웹캠 설정
    cap = cv2.VideoCapture(2)  # 21, 22
    if not cap.isOpened():
        print("Error: Could not open external webcam.")
        exit()

    time.sleep(2)  # 웹캠 초기화 대기

    # 3. 메인 루프
    while True:
        # 3.1. 프레임 캡처
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # 3.2. 얼굴 감지
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # 3.3. 각 얼굴에 대해 처리
        for (x, y, w, h) in faces:
            # 3.3.1. 얼굴 영역 추출 및 전처리
            face_roi = frame[y:y+h, x:x+w]
            resized_face = cv2.resize(face_roi, (224, 224))  # 모델 입력 크기로 조정
            input_data = np.expand_dims(resized_face, axis=0).astype(np.float32)

            # 3.3.2. 모델 추론
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            prediction = np.argmax(output_data[0])

            # 3.3.3. 결과 표시
            if prediction == 0:
                label = "yohan"
                label = "yohan"
                color = (255, 0, 0)  # Blue
            elif prediction == 1:
                label = "jumin"
                color = (0, 255, 0)  # Green
            else:
                label = "Unknown"
                color = (0, 0, 255)  # Red

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # 3.4. 화면에 프레임 표시
        cv2.imshow('Face Recognition', frame)

        # 3.5. 종료 조건
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    # 4. 자원 해제
    if 'cap' in locals() and cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
