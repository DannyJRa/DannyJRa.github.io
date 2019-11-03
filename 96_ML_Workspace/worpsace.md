# ML Workspace

https://github.com/ml-tooling/ml-workspace#faq

# 

docker run -p 8891:8080 mltooling/ml-workspace:latest

docker run -d -p 8891:8080 --name "ml-workspace2" -v "${PWD}:/workspace" mltooling/ml-workspace:latest


docker build -t workspace .

docker run -d -p 8891:8080 --name "ml-workspace3" -v "${PWD}:/workspace" workspace:latest

docker run -p 8080:8080 mltooling/ml-workspace-spark:latest

docker stop "ml-workspace3"



# Spark

docker run -d -p 8891:8080 --name "WS_spark3" -v "${PWD}:/workspace" mltooling/ml-workspace-spark:latest

