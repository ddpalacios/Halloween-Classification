from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "demon3.MOV"),
                                output_file_path=os.path.join(execution_path, "demonstration3")
                                , frames_per_second=29, log_progress=True)
print(video_path)
