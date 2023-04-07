import cv2
from src.face_recognition import detect_faces

camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()

        if not success:
            break
        else:
            # detect faces in the frame
            faces = detect_faces(frame)

            # draw a green rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # send a message to the socket with the face detection data
            num_faces = len(faces)
            for (x, y, w, h) in faces:
                data = {'x': x, 'y': y, 'w': w, 'h': h, 'num_faces': num_faces}
                yield 'data: %s\n\n' % str(data)

            # encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # yield the frame in the HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
