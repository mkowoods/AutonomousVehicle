#https://github.com/samjabrahams/tensorflow-on-raspberry-pi
sudo apt-get install python-pip python-dev
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/raw/master/bin/tensorflow-0.10.0-cp27-none-linux_armv7l.whl
sudo pip install tensorflow-0.10.0-cp27-none-linux_armv7l.whl



#https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/pi_examples
sudo apt-get install -y libjpeg-dev

curl https://storage.googleapis.com/download.tensorflow.org/models/inception_dec_2015_stripped.zip -o /tmp/inception_dec_2015_stripped.zip
unzip /tmp/inception_dec_2015_stripped.zip -d tensorflow/contrib/pi_examples/label_image/data/
