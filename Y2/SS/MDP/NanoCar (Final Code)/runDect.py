from tryDect import Detect
m=0 # when m == 'q', the camera will stop
detect=Detect()
class_id = detect.main(m)

print(int(class_id))

