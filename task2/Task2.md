# Task 2
1. Explore Virtualenv in Python
```
sudo apt install python3.8-venv
```
```
sudo apt install python3.11-venv
```
2. Create multiple Python virtual environments

*Python 3.11*
```
python3.11 -m venv venv3.11
```
```
. venv3.11/bin/activate
```
`python --version`
```
Python 3.11.5
```

*Python 3.8*
```
python3.8 -m venv venv3.8
```
```
. venv3.11/bin/activate
```
`python --version`
```
Python 3.8.10
```
3. Demonstrate the use of PIP having different libraries in each of Python virtual environment

*Python 3.11*
```
. venv3.11/bin/activate
```
```
 pip install google
```
`pip list`
```
Package        Version
-------------- -------
beautifulsoup4 4.12.2
google         3.0.0
pip            23.2.1
setuptools     65.5.0
soupsieve      2.5
```
```
deactivate
```
*Python 3.8*
```
. venv3.8/bin/activate
```
```
pip install pyperclip
```
`pip list`
```
Package       Version
------------- -------
pip           20.0.2
pkg-resources 0.0.0
pyperclip     1.8.2
setuptools    44.0.0
```
```
deactivate
```
4. Explore how requirements.txt can help to organize dependencies and demonstrate usage of it

*Python 3.11*
```
. venv3.11/bin/activate
```
```
pip freeze >> requirements3.11.txt
```
`cat requirements3.11.txt`
```
beautifulsoup4==4.12.2
google==3.0.0
soupsieve==2.5
```
```
deactivate
```

*Python 3.8*
```
. venv3.8/bin/activate
```
```
pip freeze >> requirements3.8.txt
```
`cat requirements3.8.txt`
```
pyperclip==1.8.2
```
```
deactivate
```
