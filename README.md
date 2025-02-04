## Installation

```
Install  Python >= 3.7.9
git clone https://github.com/qyum/ObjectDetection.git # clone recursively
cd yolov8_tracking
pip install -r requirements.txt  # install dependencies
```

## Tracking

```bash
$ python track.py --yolo-weights yolov8n.pt     # bboxes only
                                 yolov8n-seg.pt  # bboxes + segmentation masks
```

<details>
<summary>Methods 2</summary>

```bash
$ python track.py --tracking-method botsort
                                    deepocsort
                                    strongsort
                                    ocsort
                                    bytetrack
                                    
```

</details>

<details>
<summary>Method 3</summary>



```bash
$ python track.py --source 0                               # webcam
                           img.jpg                         # image
                           vid.mp4                         # video
                           path/                           # directory
                           path/*.jpg                      # glob
                           'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```