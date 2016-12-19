# mfbf-report-reader
Read csv of exported marketflow risk margin report and output it as yml

# Installation: linux
Use [pew](https://github.com/berdario/pew)
```bash
sudo apt install python-pip
pip install pew
# append to ~/.bashrc : export PATH="$PATH:/home/shadi/.local/bin"
pew new -d -r requirements.txt ENV
```

#Usage

## converter
```bash
pew in ENV python3 convert/convert.py
```
This would read `convert/newrisk.csv` and write it as `convert/newrisk.yml`

## compare
```bash
php compare/compare.php
```
This would compare `compare/actual.yml` with `compare/expected.yml`

# Testing
```bash
pew workon ENV
python TestParser.py
```
