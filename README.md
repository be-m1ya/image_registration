# image_registration
テンプレートマッチングを用いて画像レジストレーションしてみました.
空と雲の画像でやってみました(可視画像と赤外画像).

### 目的
多少違う画像でも,最も似ている点をテンプレートマッチングで見つけて画像レジストレーションできないか？

### 手法
・2つの画像でテンプレートマッチングしそうな範囲を適当に選択.
・その領域の中で一方の画像と最も似ている領域を一方の画像から探し,2つの画像の対応する点を見つける.
・対応する点を使い,アフィン変換による画像レジストレーションを行う.

以下に画像を踏まえて結果まで載せています.

[テンプレートマッチングを用いた画像レジストレーションをした](https://qiita.com/21_kar1n/items/31bbd221e7aa603bc586)

### 使用方法
```python:
$ python3 main.py -im1 <img1.png> -im2 <img2.png>
```
