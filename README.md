# faceRecognizerAPI
```
$ git clone https://github.com/developer-onizuka/faceRecognizerAPI
$ cd faceRecognizerAPI
$ docker build . -t 192.168.1.5:5000/face_recognizer-api:1.0.0
$ docker push 192.168.1.5:5000/face_recognizer-api:1.0.0 
$ kubectl apply -f faceRecognizerAPI.yaml
```
```
$ curl -X POST -F img=@/home/vagrant/Downloads/_image.jpg http://192.168.33.223:5000/facerecognizer
{ "facePostions":[(196, 343, 314, 225)] }
```
