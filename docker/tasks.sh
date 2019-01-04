#!/bin/sh

# To run this functions
# chmod +x docker/tasks.sh
# source docker/tasks.sh
# build
# run
function build(){
        docker-compose -f docker/docker-compose.yml build
}


function run(){
        docker-compose -f docker/docker-compose.yml run coc bash
}
