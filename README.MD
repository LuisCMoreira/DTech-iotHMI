

pip install -r .\requirements.txt --no-user -t ./packages


docker build -t hmiapp .

docker tag hmiapp <repo-name>/tflaskhmi:latest

docker push <repo-name>/tflaskhmi:latest

docker pull <repo-name>/tflaskhmi:latest

docker run -p 8080:5004 -v "$(pwd)/logs:/app/logs" -v "$(pwd)/config:/app/config" --name tflaskhmi hmiapp


