# 音声文字起こし
## 文字に起こすまでの流れ
1. 音声ファイル(mp3 or mp4)を作成
2. 音声ファイルをwav形式に変換
3. wav形式の音声ファイルをtxtファイルに文字起こしする
## 環境構築
### 音声ファイルを作成
- [Windows ボイスレコーダー](https://apps.microsoft.com/detail/9WZDNCRFHWKN?hl=ja-jp&gl=JP)を使って、ボイスをファイルにする。
### windowsにwslをインストールする(このあとのコマンドを実行するため)
- [WSLを使用してWindowsにLinuxをインストールする方法](https://learn.microsoft.com/ja-jp/windows/wsl/install)を参考にして、WSLをWindowsにインストールする。
### 音声ファイルの形式(mp3, mp4など）をwav形式に変換する方法
```bash
sudo apt install ffmpeg
ffmpeg -i "test_speech.mp3" -f wav "test_speech.wav"
```
### インストール
```bash
# 仮想環境の作成
python3 -m venv venv
# 仮想環境のアクティブ化
source venv/bin/activate
# 音声認識に必要なパッケージのインストール
sudo apt install portaudio19-dev
python3 -m pip install -U pip setuptools
python3 -m pip install -r requirements.txt
```
## サンプルプログラムの実行
```bash
python3 recognition.py
(recognition.pyは音声ファイル(wav形式)を読み込み、テキストファイル(audio_text.txt)に文字起こしするプログラムです)
```

