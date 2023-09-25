# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images_ros2/create_ros_image.Dockerfile.em
FROM ros:humble-ros-base-jammy

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    python3-colcon-common-extensions \
    python3-colcon-mixin \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/ros/rosdep/sources.list.d/20-default.list

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# install ros2 packages and dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    curl \
    wget \
    python3-pip \
    ros-$ROS_DISTRO-foxglove-bridge \
    && rm -rf /var/lib/apt/lists/*

# install software required to run graphical applications
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# install pip packages
RUN pip install --upgrade numpy && \
    pip install opencv-python

# Source setup.bash of ROS2 humble
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# RUN rosdep update && \
#     rosdep install

# Copy the ros_entrypoint.sh script from ros:ros-base
COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh

# Set the ros_entrypoint.sh script as the entry point
ENTRYPOINT ["/ros_entrypoint.sh"]

# Create a new workspace folder for ROS2
RUN mkdir -p /root/ros2_ws/src

# Set the new workspace folder as the working directory
WORKDIR /root/ros2_ws