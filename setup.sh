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

# unzip yolov5.zip -d YOLO
# rm -f yolov5.zip
# chmod -R 705 YOLO

# cd yolov5
# mv -f -u ./yolov5-master ../
# cd ../
# rm -f -d yolov5
