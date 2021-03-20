#!/bin/sh

wget http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz
tar xavf bunny.tar.gz

wget https://www.eth3d.net/data/delivery_area_rig_undistorted.7z
7z x *.7z -y
