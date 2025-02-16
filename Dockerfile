# Use the official ROS 2 Humble base image (which runs on Ubuntu 22.04).
FROM ros:humble-ros-base-jammy

# Update apt and install additional packages you might need:
# - build-essential: basic compiler tools
# - python3-colcon-common-extensions: helps build ROS 2 packages with colcon
# - git: so you can clone repos
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-colcon-common-extensions \
    git \
 && rm -rf /var/lib/apt/lists/*

# Ensure that every time a new shell is opened, ROS is automatically sourced.
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# This is the default command. It just runs bash when the container starts.
CMD [ "bash" ]
