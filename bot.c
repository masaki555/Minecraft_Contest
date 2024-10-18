#include "control.h"
#include <stdio.h>
#include <unistd.h>

void zombie2(long int z2[]);
void z2print(long int z2[]);
void mobjudge(long int z2[]);
int repeat(int cnt);
void attack_1(void);
void attack_2(void);
void left(void);
void right(void);

void zombie2(long int z2[]) {
    long int b;
    int i;
    long int k = 1;
    b = detectZombie2();
    printf("%015ld\n", b);
    for (i = 0; i < 15; i++) {
        z2[15 - 1 - i] = b / k % 10;
        k = k * 10;
    }
    k = 1;
    z2print(z2);
    return;
}

void z2print(long int z2[]) {
    if (z2[0] == 1) {
        printf("右下遠 ");
    }
    if (z2[1] == 1) {
        printf("右下中 ");
    }
    if (z2[2] == 1) {
        printf("右下近 ");
    }
    if (z2[3] == 1) {
        printf("左下遠 ");
    }
    if (z2[4] == 1) {
        printf("左下中 ");
    }
    if (z2[5] == 1) {
        printf("左下近 ");
    }
    if (z2[6] == 1) {
        printf("右上遠 ");
    }
    if (z2[7] == 1) {
        printf("右上中 ");
    }
    if (z2[8] == 1) {
        printf("右上近 ");
    }
    if (z2[9] == 1) {
        printf("左上遠 ");
    }
    if (z2[10] == 1) {
        printf("左上中 ");
    }
    if (z2[11] == 1) {
        printf("左上近 ");
    }
    if (z2[12] == 1) {
        printf("中央遠 ");
    }
    if (z2[13] == 1) {
        printf("中央中 ");
    }
    if (z2[14] == 1) {
        printf("中央近 ");
    }
    printf("\n");
}

void mobjudge(long int z2[]) { // 0,1,2 右下 3,4,5 左下 6,7,8 右上 9,10,11 左上 12,13,14 中央   遠い←→近い
    zombie2(z2);
    if (z2[13] == 1 || z2[14] == 1) {       // 中央近・中
    } else if (z2[5] == 1 || z2[11] == 1) { // 左下近・左上近
        left();
    } else if (z2[2] == 1 || z2[8] == 1) { // 右下近・右上近
        right();
    } else if (z2[4] == 1) { // 左下中
        left();
    } else if (z2[1] == 1) { // 右下中
        right();
    } else if (z2[10] == 1) { // 左上中
        left();
    } else if (z2[7] == 1) { // 右上中
        right();
    } else if (z2[3] == 1) { // 左下遠
        left();
    } else if (z2[0] == 1) { // 右下遠
        right();
    } else if (z2[12] == 1) { // 中央遠
    } else if (z2[9] == 1) {  // 左上遠
        left();
    } else if (z2[6] == 1) { // 右上遠
        right();
    } else {
    }
    return;
}

void left(void) {
    printf("視点左\n");
    pushKey("left");
}

void right(void) {
    printf("視点右\n");
    pushKey("right");
}

int repeat(int cnt) { // 定期的に繰り返す
    if (cnt % 3 == 2) {
        attack_2();
        pushKey("l");
    } else {
        attack_1();
    }

    if (cnt % 3 == 0) {
        pushKey("1");
    }
    if (cnt == 40) {
        eat(5);
    }
    if (cnt == 80) {
        eat(6);
    }
    if (cnt >= 40 && (cnt + 8) % 24 == 0) {
        eat(2);
    }
    return cnt;
}

void attack_1(void) { // 後退しながら攻撃
    downKey("s");
    downKey("shift");
    attackLeft_continuous(6);
    upKey("s");
    upKey("shift");
}

void attack_2(void) { // ダッシュしながら攻撃
    downKey("w");
    downKey("ctrl");
    attackLeft_continuous(6);
    upKey("w");
    upKey("ctrl");
}

int main(int argc, char *argv[]) {
    long int z2[15]; // bの値を配列に入れる
    int cnt = 0;     // 視点リセット用

    init();        // Minecraftのゲームコントロール関数．ウィンドウサイズを設定する等を行う．
    setTime();     // Minecraft上で時間を夜にしてくれる．
    exePython();   // 画像処理プログラムを実行する関数．実行結果はdetectZombie，detectZombie2，detectMobs関数で取得できる．
    setSurvival(); // サバイバルモードにする．

    while (rk) { // 無限loopする．rkはF12キーを押すと0となり，プログラムが停止します．
        if (cnt == 0) {
            eat(3);
            eat(4);
            pushKey("p");
        }
        mobjudge(z2); // ゾンビを検出し、画面の移動と攻撃をする。
        cnt = repeat(cnt);
        printf("%d\n", cnt);
        cnt++;
        sleep(0.1);
    }
    setCreative(); // クリエイティブモードにする．
    setMorning();  // 朝にする．
    return 0;
}

/*
・ゲーム
難易度 ノーマル
即時リスポーン オン
持ち物の保持 オン
モブのスポーン オフ
自然再生 オン

・キーボード＆マウス
フルキーボードゲームプレイ オン
スムース回転スピード 15
中心を見る P
右を見る L

スムースに右を見る 右手
スムースに左を見る 左手
攻撃する Q
移動 AWSD
コマンドライン /
ダッシュ ctrl
しゃがみ shift
ホットバースロット1 1キー
ホットバースロット2 2キー
アイテムの使用 E

1 ダイヤの剣
2 焼き鳥
3 再生のポーション
4 力のポーション 攻撃力上昇(8:00)
5 再生のポーション
6 再生のポーション
ダイヤのヘルメット・ダイヤのブーツ

立ち位置:コマンドブロックから斜めに5ブロック離れた場所で、コマンドブロックの方を向いて開始

・ビデオ
明るさ 100
カメラ視点 一人称
手の非表示 オン
視野 60度
手ぶれ オフ
画面の揺れ オフ
雲を表示する オフ
美しい空 オフ
*/
