# WebServer HMI

This is a draft for a hmi based on python flask

it is design to run with docker.

## Some Notes for use

cd build

pip install -r .\requirements.txt --no-user -t ./packages


docker build -t hmiapp .

docker tag hmiapp <repo-name>/tflaskhmi:latest

docker push <repo-name>/tflaskhmi:latest

docker pull <repo-name>/tflaskhmi:latest

docker run -p 8080:5004 -v "$(pwd)/logs:/app/logs" -v "$(pwd)/config:/app/config" --name tflaskhmi hmiapp

### Linux scripts are unfinished

