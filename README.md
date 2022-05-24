# faceRecognizerAPI

# 0. Deploy Pod and Service
```
$ git clone https://github.com/developer-onizuka/faceRecognizerAPI
$ cd faceRecognizerAPI
$ docker build . -t 192.168.1.5:5000/face_recognizer-api:1.0.0
$ docker push 192.168.1.5:5000/face_recognizer-api:1.0.0 
$ kubectl apply -f faceRecognizerAPI.yaml
```

# 1. HTTP Post with cURL
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

# 2. How to write Python Code
```
url = "http://face-recognizer-api-svc:5000/facerecognizer"
files_data = open(inputFile, 'rb').read()
data = {'img': (inputFile, files_data, 'image/jpeg')}
response = requests.post(url, files=data)

json_dict = json.loads(response.text)
facePositions = json_dict['facePositions']
```
