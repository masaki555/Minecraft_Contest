# Minecraft Education Edition
# C言語（c1-byod） + Pythonによるプレイヤ自動操作セット

**本プログラムはC演習で利用したc1-byod環境で動作する．**

最終更新日 2024/12/22

---

## ◇MineCraftの初期設定

**※必ず読むこと．設定は不適切な場合, プログラムが正常に動作しない．**

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
| int detectZombie1(void) | 画像処理の結果を取得する．戻り値はint型で，7bitの2進数をint型で返却される．詳細は後述． |
| long detectZombie2(void) | 画像処理の結果を取得する．戻り値はlong型で，15bitの2進数結果をlong型で返却される．詳細は後述． |
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

学習を用いたプレイヤー検出関数．学習ライブラリとしてYOLOを用いて画像からプレイヤーを検出する手法．運営から学習データが提供されているが，もし自分でも学習を行いたい場合は本ページの末尾にある[detectMobs関数で利用する学習データを自分で作成したい方へ](#detectmobs関数で利用する学習データを自分で作成したい方へ)を参照すること．

detectPlayer関数を呼び出すとint型の6桁の値が戻り値として返却される．戻り値はプレイヤーを検出できなかった場合は0，検出した場合は1を返す．検出結果は画面を縦に6分割し，分割した各領域にプレイヤーがいるかの判定を表記する．例えば画面の一番左と一番右にプレイヤーがいれば100001が返却される．  
プレイヤーの検出には,detectPlayer1関数はダイヤのヘルメット,detectPlayer2関数はダイヤのブーツを利用している.  
視野角は50度から60度がおすすめである.視野角が狭いほうが検出しやすくなる.  

### ゾンビ検出関数，detectZombie1関数の仕様

地平線にクロスヘアを合わせた状態で，地面部分にゾンビがいるかを検出を行う．detectZombie1関数はint型が戻り値である．int型の戻り値を2進数であり先頭のビットから画面左上，画面真ん中上・・・・というように各桁でゾンビがいるかの結果が格納されている．各値の詳細は以下の通り．

| 7桁目 | 6桁目 | 5桁目  | 4桁目 | 3桁目 | 2桁目 | 1桁目 |
| :- | - | - | - | - | - | - |
| 地面の左上にゾンビがいれば1，いなければ0となる． | 地面の真ん中上にゾンビがいれば1，いなければ0となる． | 地面の右上にゾンビがいれば1，いなければ0となる． | 地面の左下にゾンビがいれば1，いなければ0となる． | 地面の真ん中下にゾンビがいれば1，いなければ0となる． | 地面の右下にゾンビがいれば1，いなければ0となる． | 1であれば攻撃がヒット，0であれば攻撃が当たってない（精度はよくない） |

例えば，detectZombie関数の戻り値が1010000の場合，地面の左上，右上にゾンビがいる状態となる．また，0100100となると画面中央にゾンビがいるため，ゾンビが接近している可能性がある．そのため攻撃できる可能性があるという事になる．ただし，画面中央にいるからと言って必ず攻撃ができるという訳では無い．

本ライブラリは単純に現状のゾンビ配置からゾンビを倒そうとするとかなり難易度が高い．ゾンビの配置を何らかの手法で記憶させておく必要がある．

また，本ライブラリはC言語から無理やり動作させるため精度が悪い．もちろん精度の悪いなり工夫を入れると事が本コンテストの目的でもある．

### ゾンビ動態検出関数，detectZombie2関数の仕様

利用する場合は**明るさの設定を100**にして利用すること．

detectZombie2関数を呼び出すと15bitの2進数がlong型で返却される．画像検出は以下のURLにある画像の①～⑤ように画面右下，左下，右上，左上，中央の5カ所で動態検知をしている．更にそのエリアの中で遠距離，中距離，近距離の３段階を検出し，これらを15bitの値で管理されている．また，近距離にゾンビがいる場合は攻撃が当たる範囲にいる可能性が高い．

[detectZombie2による動態検出画像](https://oskit-my.sharepoint.com/:i:/g/personal/masaki_obana_oit_ac_jp/EV6amJG9qf9IikoaKJ8ksM8BMUpeWLJ5TaZ6FPEEtqk7Fg?e=Pga4NH) （右クリックから「開く」を選択しないと見れないかも・・・）

戻り値を2進数に変換し，15bitを3bit区切りととなり先頭から右下 ， 左下 ， 右上 ， 左上 ， 中央の順番に遠距離を表記されている．具体的な例は以下の表を参考にすること．

| 状態 | 10進数 | 2進数 |
| :- | - | - |
| 全検出エリアの遠くにゾンビがいる | 18724 |100100100100100 |
| 全検出エリアの中距離にゾンビがいる | 9362 |010010010010010 |
| 全検出エリアの近距離にゾンビがいる | 4681 |001001001001001 |
| 検出エリア中央の近距離にゾンビがいる | 1 |000000000000001 |
| 検出エリア中央に近距離と画面左上の中距離にゾンビがいる | 17 | 000000000010001 |

また，detectZombie2関数には以下のような欠点が存在する．

- 動くものがあるとゾンビがいると検出される可能性がある．具体的にはスポーンブロックの炎のエフェクトや剣を振る動作等．
- 同一の検出エリアにゾンビが複数体いると動態検出の面積が増えてしまい近距離にゾンビがいると検出してしまう.
- 画面中央の検出精度は高いが、周辺の検出精度は低い.
- 境界線をまたぐ場合、画面中央を優先した値を返却することが多い.

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

## detectMobs関数で利用する学習データを自分で作成したい方へ

detectMobs関数で利用している`detectMobs.py`は[YOLOv5](https://github.com/ultralytics/yolov5)という物体検出で敵を認識している.
YOLOは学習させることにより、新しく物体を認識できるようになる. 自分でも学習を行いたい方は以下を読むこと.

1. 学習対象の画像を用意する  
   学習とは大量のデータから特徴を見つけ出す作業のことである.
   YOLOv5は物体検出のAIなので学習には画像が必要である.
   この用意する画像は10枚や20枚では全くデータが不足であり,最低でも100枚の画像が必要になる.(ただし,それでも精度は悪い)  
   もちろん画像は大量にあればあるほど精度は良くなる.
   また,画像も同じシーン(背景や対象の向き等)ばかりだとAIはそのシーンでしか対象を認識できなくなるため,いろんなバリエーションの画像を用意する必要がある.
   例えばヘルメットの認識精度を向上させたいとする.
   この場合,背景が白でダイヤのヘルメットが真正面を向いた画像を1000枚用意したところで,AIは背景が白でダイヤのヘルメットが真正面からしか認識できない.  
   背景が赤になれば認識できなくなり,ダイヤのヘルメットが90度方向転換すると認識できなくなる.  
   これを解消するためには様々な背景,明度,ダイヤのヘルメットとの距離,ダイヤのヘルメットの位置,ダイヤのヘルメットの向きなどを用意する必要がある.  
   また,画像の取得方法だが,Minecraft Education EditionではF2を押してもゲーム内でスクリーンショットが出来ないため,Windows標準のツールでスクリーンショットを取る必要がある.（スクリーンショットは`Win + Shift + S`で撮れる）  

2. 用意した画像に対してアノテーションをする  
  撮影した画像のどこにダイヤのヘルメット,ダイヤのブーツがあるのかを教える必要がある.  
  これは手動で指定する必要がある.  
  アノテーションするツールとしてはlabelImgやVoTT等があるが,今回はlabelImgを紹介する.  
   1. Windows版のlabelImgは[ここをクリック](https://github.com/tzutalin/labelImg/files/2638199/windows_v1.8.1.zip)するとダウンロードできる.zip形式なので展開する必要がある.  
   2. `data/predefined_classes.txt`を開き,一旦中身を全て消す.  
   3. 学習対象のラベル名(ダイヤのヘルメットだと英語でdiamondHelmet)を記述する.  
   4. labelImg.exeを起動し,`Open Dir`から画像が入っているディレクトリを選択し,```フォルダーの選択```をクリックする.  
   5. `Change Save Dir`から結果(アノテーションファイル)の保存先を変更する.(適当にわかりやすい場所へ)  
   6. 左のメニューバーの真ん中あたりにある`PascalVOC`と書いてる部分をクリックして`YOLO`に変更する.  
      **これをしないと全ての作業が無駄になるため必ず確認するように**  
   7. `Create RectBox`をクリックして選択ツールを起動する.
   8. 学習対象の左上にマウスのカーソルを持っていき,左クリックするとそこが支点となり選択ツールが移動する. 
   9. 左クリックしたまま学習対象が全部覆われるようにカーソルを操作し,覆われたら左クリック離す.  
   10. ラベルを選ぶ画面が出るので適当なラベル(ダイヤのヘルメットならdiamondHelmet)を選択し,OKを押す.  
   11. `Save`を押すと保存される.  
   12. `Next Image`で次の画像へ,`Prev Image`で前の画像に移動する. 
   13. これを全ての画像に対して行う.

---

   <details>
   <summary>(参考)labelImgのショートカットキー</summary>
  
   labelImgのショートカットキー  
   時短になるかも  

   - Ctrl + u : フォルダから全ての画像をロード
   - Ctrl + r : デフォルトのアノテーションターゲットディレクトリを変更
   - Ctrl + s : 保存
   - Ctrl + d : 現在のラベルと四角のボックスをコピー
   - Ctrl + Shift + d : 現在の画像を削除
   - Space : 現在の画像に確認済みフラグを付与
   - w : 短形を作成
   - d : 次の画像
   - a : 前の画像
   - del : 選択した短形を削除
   - Ctrl++ : ズームイン
   - Ctrl-- : ズームアウト
   - ↑↓→← : 選択した短形を移動

   </details>

---

3. YOLOに学習させる  
   1. c1-byodで適当なディレクトリ(`yolo`とか)を作成し,cdで移動する.  
   2. 以下のコマンドを打ち,yolov5をダウンロードする.  

      ```sh
      git clone https://github.com/ultralytics/yolov5
      ```

   4. 以下のコマンドを打ち,必要なPythonライブラリをインストールする.  

      ```sh
      cd yolov5
      pip install -r requirements.txt
      ```

   6. mkdirコマンド等を使用して,以下のようなディレクトリ構成にする.

      ```txt
        yolov5
          ┠ data          ← 元からある
            ┠ train       ← 作る
            ┃   ┠ images  ← 作る
            ┃   ┗ labels  ← 作る
            ┠ valid       ← 作る
                ┗ images  ← 作る
      ```

   5. data/train/imagesディレクトリに学習させる画像を,labelsディレクトリにlabelImgで作ったアノテーションファイル(`Change Save Dir`で指定したフォルダに入ってる)を入れる.
   6. data/valid/imagesには学習結果をテストする画像(train/imagesと同じもの)を入れる.
   7. dataディレクトリ内に```data.yaml```ファイルを作成し,以下の内容を記述する.  

      ```yaml
      train: data/train/images # 学習の画像のパス
      val: data/valid/images # 検証用画像のパス

      nc: 2 # (例)学習させるMobの数
      names: [ 'diamondHead', 'diamondBoot' ] # (例)学習対象のMob名
      ```

      ※ 提供しているプログラムではダイヤのヘルメットとダイヤのブーツだけを認識の対象としているためdata.yamlの内容は[このようになっている](https://github.com/masaki555/Minecraft_Contest/blob/main/python/minecraft/yoloFiles/mobs.yaml)が、独自に認識するMobを増やしたり,減らしたりすると提供しているプログラムとの齟齬が発生し上手く動かない可能性がある.
      不具合が発生した場合は各自でプログラムを改修すること. 

   8. 以下のコマンドを実行して学習を開始する.
      ただし,CPUで計算を行うと莫大な時間かかる. 
      枚数やパソコンの性能にもよるが数時間はかかる.  

      ```sh
      python train.py --data data/data.yaml --cfg yolov5s.yaml --weights '' --batch-size 8 --epochs 300
      ```

   9. 学習が完了すると、```runs/train/exp/weights```ディレクトリに```best.pt```ファイルが生成される.
      このbest.ptファイルを```Minecraft_Contest/python/minecraft/yoloFiles/best.pt```ファイルと差し替えるとAIに使用される学習データが差し替えられる.

   (補足)上記の方法だとCPUしか使わないので遅い. 
   学習を早くするにはGPUを使うことをおすすめするが環境構築に手間がかかる.  
   Google Colabなどのサービスを利用すると環境構築なしでGPUを使えるようになるのでオススメである.(無料だと利用制限はあるが)  

