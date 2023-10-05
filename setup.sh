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

curl -o YOLO.zip -LJO https://github.com/ultralytics/yolov5/archive/refs/heads/master.zip
unzip YOLO.zip
rm -f YOLO.zip
chmod -R 755 yolov5-master

./python.exe -m pip install -r ../python/yolov5-master/requirements.txt

mkdir ./tmp/
touch ./tmp/detect_zombie1.txt
touch ./tmp/detect_zombie2.txt
touch ./tmp/Move_Log.txt
touch ./tmp/Share_Move_Data.txt
touch ./tmp/Share_Camera_Data.txt
touch ./tmp/t_zombie.txt
touch ./tmp/t_creeper.txt
touch ./tmp/detect_zombie3.txt
touch ./tmp/detect_mobs.txt
mkdir ./minecraft/yoloFiles/labels/
touch ./minecraft/yoloFiles/labels/capture.txt