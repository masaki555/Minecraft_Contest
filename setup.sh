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

mkdir ./python/tmp/
touch ./python/tmp/detect_zombie1.txt
touch ./python/tmp/detect_zombie2.txt
touch ./python/tmp/Move_Log.txt
touch ./python/tmp/Share_Move_Data.txt
touch ./python/tmp/Share_Camera_Data.txt
touch ./python/tmp/t_zombie.txt
touch ./python/tmp/t_creeper.txt
touch ./python/tmp/t_simple.txt