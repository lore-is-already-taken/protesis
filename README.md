# What is this?
this is a linux interface that recieve and analyce the data from a USB and sent it via web socket

**please read this README (gosh) before running your program**


## how to run?
first of all you need to initialice your virtual enviroment
```
python -m venv venv
```
then you have to initialice it, in linux this is
```
. venv/bin/activate
```
now, you have to install the dependencies
```
pip install -r requirements
```
now you can start to editing or execute the program

## Enviroment
Thi project is developed using a RaspberryPi model 3b+. I encountered some problems running the dependencies and to solve the issues you must install some things
**(asumming you have your virtual enviroment active)**
```
sudo apt-get update
```
```
sudo apt-get install build-essential
```
```
pip install --upgrade pip
```
