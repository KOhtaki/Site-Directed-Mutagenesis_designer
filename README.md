# Site-Directed-Mutagenesis_designer
## 使用前に
”SDM_designer”は”Biopython”を利用しています。使用前に”Biopython”のインストールを行ってください。
```
pip install biopython
```

## 使い方
### 1.コードのダウンロード
右上の”Code”ボタンからzip形式でプログラムのコードをダウンロードしてください。
### 2.プログラムの立ち上げ(windowsの場合)
ダウンロードが完了したら、解凍し、解凍後のファイルを開いてください。<br>
エクスプローラー上部のpathが記載されている所に”cmd”と入力してコマンドプロントを起動してください。<br>
起動後のコマンドプロントの作業場所が解凍後のファイルになっていることを確認したら、以下のコマンドを入力してください。<br>
```
python SDM_designer.py
```
エラーメッセージが表示されずに立ち上がればプログラムの立ち上げが完了です。<br>
もしエラーメッセージが表示された場合は以下を疑ってください。
- 作業場所が解凍後のファイルになっていない。
- 解凍後のファイルから”SDM_designer.py”を移動している。
- パッケージ”Biopython”がお使いのPCにインストールされていない。
### 3.元になる塩基配列の選択
"Open the original seqence"の"open"ボタンをクリックし、元になる塩基配列が記録されているFASTAファイルを選択してください。<br>
もしくは、"Direct input of sequence data"の項目をチェックした後に、右側の大きな欄に元になる塩基配列を直接入力。"open"ボタンをクリックして下さい。
