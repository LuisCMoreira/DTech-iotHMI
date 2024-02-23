@echo off
cd "./build"
docker build -t hmiapp .
cd ..

docker tag hmiapp lcmoreira/tflaskhmi:latest

docker push lcmoreira/tflaskhmi:latest

docker rmi hmiapp
docker rmi lcmoreira/tflaskhmi:latest