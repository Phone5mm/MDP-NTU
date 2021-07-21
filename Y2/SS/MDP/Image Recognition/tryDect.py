import re
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import time

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

class Detect():
    
    
    def load_labels(self, path='labels.txt'):
        """Loads the labels file. Supports files with or without index numbers."""
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            labels = {}
            for row_number, content in enumerate(lines):
                pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
                if len(pair) == 2 and pair[0].strip().isdigit():
                    labels[int(pair[0])] = pair[1].strip()
                else:
                    labels[row_number] = pair[0].strip()
        return labels

    def set_input_tensor(self, interpreter, image):
        """Sets the input tensor."""
        tensor_index = interpreter.get_input_details()[0]['index']
        input_tensor = interpreter.tensor(tensor_index)()[0]
        input_tensor[:, :] = np.expand_dims((image - 255) / 255, axis=0)

    def get_output_tensor(self, interpreter, index):
        """Returns the output tensor at the given index."""
        output_details = interpreter.get_output_details()[index]
        tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
        return tensor

    def detect_objects(self, interpreter, image, threshold):
        """Returns a list of detection results, each a dictionary of object info."""
        self.set_input_tensor(interpreter, image)
        interpreter.invoke()
        # Get all output details
        boxes = self.get_output_tensor(interpreter, 0)
        classes = self.get_output_tensor(interpreter, 1)
        scores = self.get_output_tensor(interpreter, 2)
        count = int(self.get_output_tensor(interpreter, 3))

        results = []
        for i in range(count):
            if scores[i] >= threshold:
                result = {
                    'bounding_box': boxes[i],
                    'class_id': classes[i],
                    'score': scores[i]
                }
                results.append(result)
        return results
#{{'name':'yellow_right', 'id': 14}, {'name':'yellow_z', 'id':15},{'name':'bulls_eye','id':16}]

    def image_map(self,class_id):
        ids={
            0: 6,
            1: 2,
            2: 14,
            3:7,
            4:5,
            5:12,
            6:8,
            7:4,
            8:11,
            9:9,
            10:1,
            11:13,
            12:10,
            13:3,
            14:15,
            15:0,
            16:16
        }
        return ids.get(class_id,None)

    def main(self, m):
        start_time = time.time()
        labels = self.load_labels()
        interpreter = Interpreter('detect.tflite')
        interpreter.allocate_tensors()
        _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']
        cap = cv2.VideoCapture(0)
        camera_time = time.time()
        camera_start_time = camera_time - start_time
        print("camera_start_time: ",camera_start_time)
        
        detect_start_time =time.time()
        detect_number=0
        checkList=[]
        
        while cap.isOpened():
            ret, frame = cap.read()
            img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (320, 320))
            res = self.detect_objects(interpreter, img, 0.6)
            print(res)

            for result in res:
                ymin, xmin, ymax, xmax = result['bounding_box']
                xmin = int(max(1, xmin * CAMERA_WIDTH))
                xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
                ymin = int(max(1, ymin * CAMERA_HEIGHT))
                ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)
                cv2.putText(frame, labels[int(result['class_id'])], (xmin, min(ymax, CAMERA_HEIGHT - 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('Pi Feed', frame)
            check_detect_time = time.time()
            zero_detect_time = check_detect_time - detect_start_time
            if zero_detect_time<5:
                if detect_number<5:
                    if res!=[]:
                        if res[0]['score'] >0.80:
                            checkList.append(res[0]['class_id'])
                            detect_number =detect_number+1
                else:
                    detect_end_time=time.time()
                    detect_time=detect_end_time -detect_start_time
                    print("detect_time: ", detect_time)
                    cap.release()
                    cv2.destroyAllWindows()
                    m=max(checkList, key=checkList.count)
                    img_id=self.image_map(m)
                    return img_id
            elif(detect_number>0):
                detect_end_time = time.time()
                detect_time = detect_end_time - detect_start_time
                print("detect_time: ", detect_time)
                cap.release()
                cv2.destroyAllWindows()
                m = max(checkList, key=checkList.count)
                print(checkList)
                img_id = self.image_map(m)
                return img_id

            else:
                cap.release()
                cv2.destroyAllWindows()
                m = 16
                #m = max(checkList, key=checkList.count)
                img_id=self.image_map(m)
                return img_id
        if cv2.waitKey(10) & 0xFF == ord('q'):
               cap.release()
               cv2.destroyAllWindows()
               m=16
               img_id = self.image_map(m)
               return img_id


