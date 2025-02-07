You just need to following up the step to execute the command

# Installation

```
Install  Python == 3.7.9
git clone https://github.com/qyum/ObjectDetection.git # clone recursively

#Create a virtual environment & activate it in python.

  python -m venv myenv  
 .\myenv\Scripts\activate 

cd MultiObjectDetection
pip install -r requirements.txt  # install dependencies 
```

# Detection on Yolo8

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

# Detection on Yolov11 
## dependencies

```bash
Install  Python >= 3.8.0
Then follow installation step


``` 

## Run the following command to get detection using custom trained checkpoint of yolov11
```bash

python sample.py   #custom video

```
## sample video
 ```bash

[Watch the video](https://drive.google.com/file/d/1L_zt4amJM5Bd8a4Lm05DYxO8ObzVtppp/view?usp=sharing)
[Watch the video](https://drive.google.com/file/d/1tcVEL6ysjf6xYE7yYcZZzg0K1o53HEdK/view?usp=sharing)


```
