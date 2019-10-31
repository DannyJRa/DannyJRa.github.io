docker run -p 8891:8080 mltooling/ml-workspace:latest

docker run -d -p 8891:8080 --name "ml-workspace" -v "${PWD}:/workspace" mltooling/ml-workspace:latest