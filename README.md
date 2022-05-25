# faceRecognizerAPI

The faceRecognizer is a Web API thru HTTP Post. You can post a image file to get the coordinate of faces.<br>
You can use it in the following cases, for example.<br>

<img src="https://github.com/developer-onizuka/Diagrams/blob/main/faceRecognizerAPI/Copy%20of%20rabbitMQ.drawio.png" width="720">


# 0. Deploy Pod and Service
# 0-1. Deploy the GPU Driver DaemonSet thru GPU Operator
> https://github.com/developer-onizuka/gpu-operator4

# 0-2. Deploy faceRecognizerAPI
It will be deployed on one of the GPU Nodes with the Nvidia Device Plugin.
```
$ git clone https://github.com/developer-onizuka/faceRecognizerAPI
$ cd faceRecognizerAPI
$ docker build . -t 192.168.1.5:5000/face_recognizer-api:1.0.0
$ docker push 192.168.1.5:5000/face_recognizer-api:1.0.0 
$ kubectl apply -f faceRecognizerAPI.yaml
```

# 1. HTTP Post image file with cURL
```
$ curl -X POST -F img=@/home/vagrant/Downloads/_image.jpg http://face-recognizer-api-svc:5000/facerecognizer
{
  "facePositions": [
    [
      196, 
      343, 
      314, 
      225
    ]
  ]
}
```

# 2. How to write Python Code to Post image file
```
import requests
import json

inputFile = "/home/vagrant/Downloads/_image.jpg"

url = "http://face-recognizer-api-svc:5000/facerecognizer"
files_data = open(inputFile, 'rb').read()
data = {'img': (inputFile, files_data, 'image/jpeg')}
response = requests.post(url, files=data)

json_dict = json.loads(response.text)
facePositions = json_dict['facePositions']
```
