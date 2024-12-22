# Minecraft Education Edition
# C言語（c1-byod） + Pythonによるプレイヤ自動操作セット

**本プログラムはC演習で利用したc1-byod環境で動作する．**

最終更新日 2024/12/22

---

## ◇MineCraftの初期設定

**※必ず読むこと．設定は不適切な場合,プログラムが正常に動作しない．**

本プログラムはPythonのDirectInputを利用しカメラを操作する．そのためフルキーボードゲームプレイを`ON`に設定する必要がある．ゲーム画面から

`【Esc → 設定 → キーボード&マウス → フルキーボードゲームプレイをONにする】`

※（MINECRAFTと表示されている）タイトルメニューにある「設定」ボタンからも設定する．

プログラムを起動する際は，上記の方法で視点操作の感度を予め確認すること．またカメラの速度はスムース回転スピードを設定することで調整することができる．設定値は5程度がよいかと思われるが作成するプログラムによって調整すること．

また，ディスプレイは1980x1080のディスプレイを要し，テキスト，アプリ，その他の項目のサイズを100%にしておく必要がある．

`【デスクトップ右クリック → ディスプレイ設定 → テキスト，アプリ，その他の項目のサイズを変更する → 100%】`

---

## ◇Botプログラムのダウンロード方法，実行・停止方法

### ダウンロード方法

c1-byod上で以下のコマンドを実行するとダウンロードできる．フォルダは好きなところで良いが，ここでは「```~/```」に展開するとする．

``` sh
cd ~/
git clone https://github.com/masaki555/Minecraft_Contest.git
chmod -R 755 Minecraft_Contest
cd Minecraft_Contest/
./setup.sh
chmod -R 755 python
```

上記のコマンドを実行すると```~/Minecraft_Contest/```というディレクトリが作成され，このディレクトリの中でプログラムをCプログラムを作成する事となる．また，```~/Minecraft_Contest/```の中にはtestbot.cというプログラムが置かれており，こちらを参考にプログラムを書くこと．ただし，かなり初心者が書いた出来の悪いサンプルプログラムなので，皆さんはこれを賢いBotプログラムに修正するようにすること．また，以下にMinecraft_Contestフォルダのフォルダ構造を記載しておく．

``` file
  📁Minecraft_Contest       // 作成したMinecraft_Contestフォルダ
   ┗ 📁python               // Botを動かすために必要なpythonファイル関係
   ┗ 📁docker               // yoloをコンテナで動かす環境（試作）
     📃 control.c           // C言語からpythonを呼び出すために必要なライブラリ
     📃 control.h           // control.cファイルのヘッダファイル
     📃 testbot.c           // botプログラムのサンプル．このプログラムを参考にbotプログラムを書く
     📃 readme.md           // botプログラムの説明
     📃 requirements.txt    // setup.sh実行時に必要
     📃 setup.sh            // 初回セットアップ時に実行するshellプログラム
```

### ライブラリのアップデート

提供するライブラリは現在試行錯誤の段階であり，モジュールがアップデートされる場合がある．その場合は以下のコマンドでモジュールをアップデートすることができる．ダウンロードした個所が「```~/```」であった場合

``` sh
cd ~/
git pull
```

とするとアップデートする事ができる．ただし，提供するプログラムやファイルを編集するとアップデートできない場合がある．

### コンパイル方法

コンパイルは以下のコマンドでコンパイルする．ここではtestbot.cプログラムを自分で作成したプログラムとしてコンパイルし，minebot.exeという実行ファイルを作成する．

```sh
cd ~/
cd Minecraft_Contest
gcc -O2 -o minebot.exe testbot.c control.c
```

コンパイルするとminebot.exeという実行ファイルが作成される．またC演習ではccというコマンドで実行していたが，本botライブラリではgccコマンドを利用する事に注意が必要である．

### 実行方法

プログラムを実行する際には以下の手順で実行する．

1. Minecraftを起動しマップを選択する．マップはTeamsで配布するマップを利用する*．
2. c1-byodをアクティブ化し，作成したプログラムを実行する.
3. botプログラムを実行する．

*マップはご自身で作成して頂いても結構だが，コンテスト本番では．Teamsで合配布するマップを利用する．またマップを作成する際には【チート→「天候の変化」を「OFF」】に設定しておくこと．

プログラムを実行すると自動でx20,y20の位置に横幅900，縦幅1080にMinecraftのゲーム画面が自動調整される．本ライブラリは画像処理を用いてゾンビを判定しているため，指定されたデスクトップの場所（x20,y20から横幅900，縦幅1080）でMinecraftを起動させる必要がある．

また，Minecraftを最小化した状態で，Botプログラムを動かすと正常に動作しない．Minecraftは最小化するとリソース節約のため動作停止し，起動するまでに時間がかかるため，Botの初期化処理等が正常に動作しない．

※稀にerror:detectPlayerという表示されるが，その場合は再度プログラムを実行すること．

### 停止方法

プログラムを停止する際には「F12」を押す（連打する）と停止させることができる．停止できたらc1-byod上に終了コード送信と表示される．

※上記でも停止しない場合はc1-byod上で`【Ctrl + C】`で強制終了できるが，ゾンビプロセスが発生する可能性がある．その場合はPCを再起動する等で対応すること．

---

## ◇Botプログラムの作成方法

### プログラム作成手順

ダウンロードしたMinecraft_Contestフォルダの中にプログラムを作成する必要がある．Minecraft_Contestフォルダの中にtestbot.cを改変して頂いても，新たにファイルを作成して頂いても結構である．その時に[コンパイル方法](#コンパイル方法)でも注意したようにgccコマンドを使う事と，control.cを同時にコンパイルする必要がある．

Botプログラムでは必ず実行しなければいけない命令が以下となる．実行しなければいけないプログラム（関数）はコメントを参考にしてほしい．また，Botプログラムを書く個所は以下のプログラムのwhile文のコメントの範囲となる．

```C
#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
  　/*変数を定義する*/
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止する．
        /*ここからBotプログラムを書く*/

        /*ここまでBotプログラムを書く*/
        sleep_time(0.1);
    }
}
```

### ライブラリの関数一覧

関数一覧．

| 戻値 関数名(引数) | 説明 |
| :- | - |
| void init(void) | Botプログラム初期設定関数．Minecraftのウィンドウ位置，サイズを強制的にx20，y20の横幅920，縦幅1080のする．また，マウスの初期位置を記憶する．またプレイヤーの移動を監視するプログラムを起動する． |
| void exePython(void) | Botプログラム初期設定関数．画像処理プログラムが実行される．|
| int detectPlayer1(void) | 画面を6分割して左から順に検出した場所を1にする．戻り値はint型で，例えば100001だと左端と右端に検出された状態．詳細は後述． |
| int detectPlayer2(void) | 画面を6分割して左から順に検出した場所を1にする．戻り値はint型で，例えば100001だと左端と右端に検出された状態．詳細は後述． |
| void attackLeft(void) | 左クリック．0.01秒間隔で入力されるが，実際にはもう少し遅い． |
| void attackLeft_long(void) | 左クリック．1.50秒間入力される. |
| void attackLeft_continuous(int n) | 左クリックを指定した回数入力する．0.01秒間隔で入力される. |
| void eat(int n) | 指定した番号のアイテムを使用する(食べる/飲む). |
| void downKey(char* key) | 指定したキーを下げた状態にする(upKeyが実行されるまで押しっぱなし).※1 |
| void upKey(char* key) | 指定したキーを上げた状態にする.※1 |
| void pushKey(char* key) | 指定したキーを押す.※1 |
| void sleep_time(double time) | timeで指定した時間（単位は秒,ミリ秒も指定できる）だけ処理を停止する. |
| void moveForward(double time) | 前進する．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveLeft(double time) | 左に動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveRight(double time) | 右に動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveBack(double time) | 後進する．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveForwardLeft(double time) | 左斜め前に動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveForwardRight(double time) | 右斜め前に動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveBackLeft(double time) | 左斜め後ろに動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveBackRight(double time) | 右斜め後ろに動く．timeで指定した時間（単位は秒,ミリ秒も指定できる）動く． |
| void moveJump(int times) | ジャンプする．timesで指定した時間，連続でジャンプし続ける．大体1秒に1回ジャンプする． |
| void moveDash(int times) | ダッシュする．timesで指定した時間(単位は秒,整数でのみ指定できる)動く． |
| void cameraDown(double time) | カメラを下にtimeで指定した時間（単位は秒,ミリ秒も指定できる）動かす．※2 |
| void cameraLeft(double time) | カメラを左にtimeで指定した時間（単位は秒,ミリ秒も指定できる）動かす．※2 |
| void cameraRight(double time) | カメラを右にtimeで指定した時間（単位は秒,ミリ秒も指定できる）動かす．※2 |
| void cameraUp(double time) | カメラを上にtimeで指定した時間（単位は秒,ミリ秒も指定できる）動かす．※2 |


※1 アルファベットは半角小文字,数字や記号は半角で指定する.Shiftキーは"shift",Ctrlキーは"ctrl",スペースキーは"space",エンターキーは"enter",矢印キーの左キー(マイクラ内の表記は左手)は"left",右キー(マイクラ内の表記は右手)は"right",上キーは"up",下キーは"down"である.Wキーを押したい場合はpushKey("w");のようにして使う.  
「中心を見る」に割り当てられているキーは本番の環境だと使用できないため,キーボードレイアウト設定を変更し,Pキーなどに変更する必要がある.
同様に,テンキーも使用することができない.  

※2 値は0.24以上である必要がある．動作後は1秒以上カメラ以外の動作を行わなければカメラが動作しない場合がある．Botのアルゴリズムを実装するwhile文の最初のカメラ動作を実行すると，正常に動作しない場合がある．

例えば以下のようなプログラムを記載するとc1-byod環境でF12キーを押さない限り前進し続けるプログラムとなる．

```C
#include <stdio.h>
#include <unistd.h>
#include "control.h"

int main(int argc, char *argv[]){
    init();          //Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    exePython();     //画像処理プログラムを実行する関数．
    while(rk){       //無限loopする．rkはF12キーを押すと0となり，プログラムが停止する．
        /*ここからBotプログラムを書く*/

           moveForward(1.2); //1.2秒前進する

        /*ここまでBotプログラムを書く*/
        sleep_time(0.1);
    }
}
```

### プレイヤー検出関数，detectPlayer1関数,detectPlayer2関数の仕様

学習を用いたプレイヤー検出関数．学習ライブラリとしてYOLOを用いて画像からプレイヤーを検出する手法．

detectPlayer関数を呼び出すとint型の6桁の値が戻り値として返却される．戻り値はプレイヤーを検出できなかった場合は0，検出した場合は1を返す．検出結果は画面を縦に6分割し，分割した各領域にプレイヤーがいるかの判定を表記する．例えば画面の一番左と一番右にプレイヤーがいれば100001が返却される．  
プレイヤーの検出には,detectPlayer1関数はダイヤのヘルメット,detectPlayer2関数はダイヤのブーツを利用している.  
視野角は50度から60度がおすすめである.視野角が狭いほうが検出しやすくなる.  

## 更なる改良を行いたい方へ

本ライブラリはpythonで書いたMinecraft操作プログラムをC言語から実行するBotライブラリとなっている．このような構造になっている目的はC演習Ⅰで学習した内容を用いてBotプログラムを作成する事であるが，もし力量がある方はPythonプログラムの改変をして頂いても問題ない．Pythonプログラムは以下のフォルダに存在する．また，新しいpythonプログラムを作成して頂いても問題ない．ただし，コンテスト時には必ずC言語で書かれたコードを実行すること．

また，pythonプログラムを改変する場合，今後運営から提供されるアップデートは実行しないこと．実行すると最悪，改変したcontrol.cやpythonファイル等の全てモジュールが削除される．

```file
  📁Minecraft_Contest      // 一番最初のフォルダ
   ┗📁python          // この上にはMinecraft_Contestフォルダがある．
     ┗📁minecraft       // このminecraftフォルダにpythonコードが入っている．
       ┗📃Control.py
         📃clickLeft.py
         📃clickRight.py
         :
         :
         :
         📃pushKey.py
         📃test.py
```
