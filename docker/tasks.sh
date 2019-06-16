#!/bin/sh

# To run this functions
# chmod +x docker/tasks.sh
# source docker/tasks.sh
# build
# run
function build(){
        docker-compose -f docker/docker-compose.yml build
}


function con(){
        docker-compose -f docker/docker-compose.yml run coc ash
}

function up(){
        docker-compose -f docker/docker-compose.yml up
}


function remi(){
        docker rmi -f $(docker images|grep "<none>"|awk '{print $3}')
}

function stop(){
        docker stop $(docker ps -a -q)
}

function rem(){
        docker rm $(docker ps -a -q)
}
