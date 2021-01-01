# hello_world_docker
This project is sample example of how we can run a python project on docker. 

 - The directory templates contains all .html files we want to display (that is specific for this example)
 - The main.py is the python file that we run
 - The File requirements contains all python packages to install
 - The file Dockerfile contains all instructions to build our docker image
 
 To run this project run this cmd on your terminal :
 - sudo docker build -t hello_world . # this to build our docker image
 - sudo docker run -p 5000:5000 hello_world:latest # this to run the latest image and create our docker container
 

 
 
