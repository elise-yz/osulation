# Import the InferencePipeline object
from inference import InferencePipeline
import cv2
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ROBOFLOW_API_KEY")

def my_sink(result, video_frame):
    if result.get("output2"): # Display an image from the workflow response
        cv2.imshow("Workflow Image", result["output2"].numpy_image)
        cv2.waitKey(1)
    print(result) # do something with the predictions of each frame
    

# initialize a pipeline object
pipeline = InferencePipeline.init_with_workflow(
    api_key=api_key,
    workspace_name="osulation",
    workflow_id="custom-workflow",
    video_reference=0, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    max_fps=30,
    on_prediction=my_sink
)
pipeline.start() #start the pipeline
pipeline.join() #wait for the pipeline thread to finish