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
```bash
pew in ENV python3 convert.py
```
This would read newrisk.csv and write it as newrisk.yml
