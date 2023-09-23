#!/bin/bash
set -e
source /root/.bashrc

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --

if [ ! -e "CONTAINER_INITIALIZED_PLACEHOLDER" ]; then
    echo "-- First container startup --"
    colcon build
    touch "CONTAINER_INITIALIZED_PLACEHOLDER" # <== This placeholder file used in the github action to check when colcon build is done, do not remove
    source "/root/ros2_ws/install/setup.bash"

    ros2 ros2 run py_image_foolery image_creator # <== change to your launch file // comment out if you don't want auto launch
else
    echo "-- Not first container startup --"
    source "/root/ros2_ws/install/setup.bash"

    ros2 ros2 run py_image_foolery image_creator # <== change to your launch file // comment out if you don't want auto launch
fi

exec "$@"
