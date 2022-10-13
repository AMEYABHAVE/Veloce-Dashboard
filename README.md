# Veloce-Dashboard
This Repository contains all the files required for data collection in an IC engine and hardcoded for a custom Dashboard systemm
Veloce Racing Dashboard Software Devlopement

This repo is dedicated to devlopement of DASHBOARD software using Python & Kivy.

Make your own branches if you want to make changes and send pull request.
DO NOT COMMIT to MASTER BRANCH!!!
PLEASE COMMENT ALL FILES BEFORE COMMITING.
___________________________________________________________________________________
To completely uninstall kivy:

python -m pip uninstall kivy
python -m pip uninstall kivy.deps.sdl2
python -m pip uninstall kivy.deps.glew
python -m pip uninstall kivy.deps.gstreamer
python -m pip uninstall image
___________________________________________________________________________________
To install specific version of kivy:

python -m pip install "kivy[base]==2.0.0"
___________________________________________________________________________________
To install kivy on Raspberry(desktop):

sudo apt update
sudo apt install python3-setuptools git-core python3-dev

sudo apt update
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev
   
  python -m pip install "kivy[base]"
___________________________________________________________________________________
