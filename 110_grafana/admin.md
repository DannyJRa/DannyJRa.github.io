mkdir data # creates a folder for your data
ID=$(id -u) # saves your user id in the ID variable

# starts grafana with your user id and using the data folder


docker run -d --user $ID --volume "$PWD/data:/var/lib/grafana" --net="host" -p 3000:3000 grafana/grafana:7.3.1