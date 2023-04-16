!#/bin/bash
sudo docker stop rdsconnect
sudo docker rm rdsconnect
sudo docker rmi rds
sudo docker build . -t rds
sudo docker run -d --name rdsconnect rds
sudo docker cp rdsconnect:/opt/City.csv ./
