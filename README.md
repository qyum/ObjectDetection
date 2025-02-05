You just need to following up the step to execute the command

## Installation

```
Install  Python >= 3.7.9
git clone https://github.com/qyum/ObjectDetection.git # clone recursively
cd yolov8_tracking
pip install -r requirements.txt  # install dependencies
```

## Detection

Run the command to see the Multi object detection in real time


Methods 1:

```bash
 python main.py --yolo-weights   yolov8n.pt     # bboxes only   (webcam)
                                 yolov8n-seg.pt  # bboxes + segmentation masks (webcam)
```

Methods 2:

```bash
python main.py --tracking-method    botsort     
                                    deepocsort
                                    strongsort
                                    ocsort
                                    bytetrack
                                    
```



Method 3:


```bash
python main.py --source    0                               # webcam
                           img.jpg                         # image
                           vid.mp4                         # video
                           path/                           # directory
                           'https://youtube/xyz'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```