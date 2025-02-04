You just need to following up the step to run command.

## Installation

```
Install  Python >= 3.7.9
git clone https://github.com/qyum/ObjectDetection.git # clone recursively
cd yolov8_tracking
pip install -r requirements.txt  # install dependencies
```

## Tracking

Run the command to see the Multi object detection in real time


Methods 1:

```bash
$ python track.py --yolo-weights yolov8n.pt     # bboxes only
                                 yolov8n-seg.pt  # bboxes + segmentation masks
```

Methods 2:

```bash
$ python track.py --tracking-method botsort     
                                    deepocsort
                                    strongsort
                                    ocsort
                                    bytetrack
                                    
```



Method 3:


```bash
$ python track.py --source 0                               # webcam
                           img.jpg                         # image
                           vid.mp4                         # video
                           path/                           # directory
                           path/*.jpg                      # glob
                           'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```