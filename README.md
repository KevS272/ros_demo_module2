# ros_demo_module2
A demo module that includes a ROS 2 package to demonstrate inter-container communication in ROS 2.

## Requirements
- Docker Engine
- Docker Compose plugin (If you're using Compose version 1, you need to use "docker-compose" instead of "docker compose" in your commands!)

## Setup
### 1. Clone the repository

### 2. Go into the repository's Docker directory and run Docker Compose up
```bash
cd ros_demo_module1/docker \
&& sudo docker compose up
```

The Docker image gets built and after that, compose will start up a container that automatically builds the Colcon workspace and starts the launch file that was specified in `docker/ros_entrypoint.sh` which gets copied into the image during the build process.

You can stop the nodes at any time using `CTRL` + `C` in the command line. The compose will stop the container (it does not delete it!). This means you can start the container again using `sudo docker compose up`.

If you want to run the container detached, add the `-d` flag to the compose command like this:
```bash
sudo docker compose up -d
```
If you do this, you will have to `sudo docker compose stop` to stop the container or `sudo docker compose down` to completely remove it.