# digital-frame

# Raspberry Pi setup steps

Use Raspberry Imager to install Raspian image, with login/pass, ssh enabled, and wifi setup done
When logged in and up and running need to install these:
sudo apt install vim (for me)
sudo apt install feh
sudo apt install imagemagick
sudo apt install byobu (for accessing it all remotely) (also maybe no longer needed with display access and xset -display stuff)
Probably need to install some python libraries
sudo apt install fbi (maybe if I decide to use this, need to research it)
ps aux
top
htop
pstree
pip3 install picframe
need to download, then chmod the python script

# Notes to consider

I want to make it run as a daemon and/or service so it will start all by itself
It should check time of day or something to shut off display and image at night
Should every so often check the synology folder for updates
maybe keep has table of images that are local to compare to synology folder
maybe make the table a hash table of hashes for values. So, if an image was renamed or something, it would still see it as double
feh doesnt do crossfade, does fbi? if not, look into pi3d
need to change hostname and check if it clashes

# Usefule sites

https://www.byobu.org/
https://pypi.org/project/python-daemon/
http://manpages.ubuntu.com/manpages/bionic/man1/fbi.1.html
https://www.thedigitalpictureframe.com/how-to-set-up-your-raspberry-pi-for-your-digital-picture-frame/
https://pypi.org/project/picframe/
https://stackoverflow.com/questions/41582334/how-do-i-change-the-hostname-using-python-on-a-raspberry-pi/49284621
https://dpbl.wordpress.com/2017/02/12/a-tutorial-on-python-daemon/
https://pypi.org/project/synology-api/

# Useful commands

xset -display ${DISPLAY} dpms force off
xset -display ${DISPLAY} dpms force on

hash:
sha1sum {filename}




   22  sudo apt install vim
   25  sudo chmod +x run.sh 
   26  ./run.sh 
   36  sudo apt install feh
   37  feh sunset-quotes-21-1586531574.jpg 
   39  xrandr --query
   40  sudo apt install imagemagick
   43  display sunset-quotes-21-1586531574.jpg 
   44  byobu
   46  echo $DISPLAY
   47  export DISPLAY=:0.0
   49  xrandr --query
   51  display sunset-quotes-21-1586531574.jpg 
   52  feh sunset-quotes-21-1586531574.jpg 
