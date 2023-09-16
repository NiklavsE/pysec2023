# TASK 1
1. Install Python 2.7 (or different version of python 3)
```
sudo apt install python2
```
2. Install Python 3.x
```
sudo apt install python3.11
```
3. Demonstrate how to switch between different versions of Python
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1
```
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
```
`python --version`
```
Python 3.11.5
```
`sudo update-alternatives --config python`
```
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path                 Priority   Status
------------------------------------------------------------
  0            /usr/bin/python3      3         auto mode
  1            /usr/bin/python2      1         manual mode
  2            /usr/bin/python3      2         manual mode
Press <enter> to keep the current choice[*], or type selection number: 1
```
`python --version`
```
Python 2.7.18
```