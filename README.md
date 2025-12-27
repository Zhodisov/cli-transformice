Need Python 3.12: `https://www.python.org/downloads/release/python-31210/` <br><br>
Need Git: `https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe`<br><br>
Edit `transformice-cli.py` with VSCode and change <br><br>
`u = "Zhodisov"` - Change for transformice username, ex: `J_dcp#1839`<br><br>
`p = ""` - Change for the password account <br><br>
Open cmd in the folder and enter the commands below
```
mkdir temp
cd temp
git clone https://github.com/friedkeenan/pak.git
cd pak
pip install -e .
cd ..
git clone https://github.com/friedkeenan/caseus.git
cd caseus
pip install -e .
cd ..
cd ..
xcopy /e /i /h temp\pak\pak pak
xcopy /e /i /h temp\caseus\caseus caseus
rd /s /q temp
python transformice-cli.py
 ```

https://github.com/user-attachments/assets/e607fa9e-786a-46c7-91f1-bca2cf3b77dc

