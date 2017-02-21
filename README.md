# mfbf-report-reader
[![Build Status](https://travis-ci.org/shadiakiki1986/mfbf-report-reader.svg?branch=master)](https://travis-ci.org/shadiakiki1986/mfbf-report-reader)
Read csv of exported marketflow risk margin report and output it as yml

# Installation: linux
Using [pew](https://github.com/berdario/pew)
```bash
sudo apt install python-pip
pip install pew
# append to ~/.bashrc : export PATH="$PATH:/home/shadi/.local/bin"
pew new -d -r requirements.txt MFBF_REPORT_READER
```

#Usage
```bash
pew in MFBF_REPORT_READER python main.py test/standard.csv
```
This would output the data to the console as yml

# Testing
```bash
pew in MFBF_REPORT_READER python TestParser.py
```
