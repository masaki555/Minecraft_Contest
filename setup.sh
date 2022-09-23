curl -o python.zip https://www.python.org/ftp/python/3.9.10/python-3.9.10-embed-amd64.zip
unzip python.zip -d python
rm -f python.zip
chmod -R 705 python

cd python
echo "import site" >> python39._pth

curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
echo "import sys; sys.path.append('')" >> setting.pth

./python.exe get-pip.py
./python.exe -m pip install update

./python.exe -m pip install -r ../requirements.txt