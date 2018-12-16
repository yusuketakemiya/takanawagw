# portfolio

# Docuke Build

docker build -t debian_flask .

# debug

docker run --name flask -p 8081:80 -v ./server:/flask -i -t debian_flask /bin/bash