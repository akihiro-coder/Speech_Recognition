# Speech_Recognition
## 環境構築
```bash
# 仮想環境の作成
python -m venv venv
# 仮想環境のアクティブ化
source venv/bin/activate
# 音声認識に必要なパッケージのインストール
sudo apt install portaudio19-dev
python -m pip install -U pip setuptools
python -m pip install -r requirements.txt
```
## サンプルプログラムの実行
```bash
python recognition.py
(recognition.pyは音声ファイル(wav形式)を文字に起こすプログラムです)
```

