[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PHlm5I7RKGSgA07_FKkPMpXAqzSbAwog?usp=sharing)

[解説記事](https://plaza.umin.ac.jp/shoei05/index.php/2024/05/25/2518/) / [GPTs](https://chatgpt.com/g/g-oBq9SnKDY-replace-text )

# replace_text

Excel で定義したルールを用いてテキストファイルの誤字を自動修正する Python スクリプトです。 

## Excel で作った表で誤字を一括修正

このスクリプトは、Excel で作成した置換ルールに基づいて、テキストファイル (.txt) や字幕ファイル (.srt) 内の誤字を自動的に修正する Python スクリプトです。Google Colaboratory (Colab) 環境でも動作するように設計されています。

### 機能

* Excel ファイルに誤字と修正後の正しい表記をリストアップし、置換ルールとして使用します。
* テキストファイルと字幕ファイルの両方に対応しています。
* 修正後のファイルは自動的にダウンロードされます。

### 使用方法

#### Google Colab
- [Open with Colab](https://colab.research.google.com/drive/1PHlm5I7RKGSgA07_FKkPMpXAqzSbAwog?usp=sharing)

1. **修正ルールを Excel で作成:** A列に修正前の文字列、B列に修正後の文字列を記述した Excel ファイル (.xlsx) を作成します。
2. **Colab でコードを実行:** このリポジトリにある .ipynb ファイルを Google Colab にアップロードして実行します。
3. **ファイルをアップロード:** 実行後、表示される指示に従って、作成した Excel ファイルと修正したいテキストファイルをアップロードします。
4. **修正完了:** スクリプトが自動的に誤字を修正し、修正後のファイルをダウンロードします。

### コードの詳細

.ipynb ファイルには、Python スクリプトが含まれています。スクリプトは、`openpyxl` ライブラリを使用して Excel ファイルを読み込み、置換ルールを辞書に格納します。次に、入力フォルダ内のテキストファイルと字幕ファイルをループ処理し、置換ルールに基づいてテキストを修正します。修正後のテキストは出力フォルダに保存され、Colab 環境からダウンロードできます。

### ローカル環境での実行

スクリプトはローカル環境でも実行できます。その場合は、以下の手順に従ってください。

1. **リポジトリのクローン:** ターミナルを開き、以下のコマンドを実行してリポジトリをクローンします。

   ```bash
   git clone https://github.com/shoei05/replace_text.git
   ```
2. **仮想環境の作成 (推奨):**  クローンしたリポジトリのディレクトリに移動し、仮想環境を作成します (Python のバージョンやライブラリの依存関係を分離するために推奨されます)。

   ```bash
   cd replace_text
   python -m venv env_replace_text 
   ```
3. **仮想環境の有効化:**

   * **Windows:**
     ```bash
     env_replace_text \Scripts\activate
     ```
   * **macOS/Linux:**
     ```bash
     source env_replace_text/bin/activate
     ```
     
4. **必要なライブラリのインストール:**  `requirements.txt` ファイルを使用して必要なライブラリをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

5. **フォルダ構成:**  `replace_text` ディレクトリ内に以下のフォルダ構成を作成します。

   ```bash
   replace_text
   ├── replace_text.py
   ├── replace_rule
   │   └── replace_rules.xlsx  # 置換ルールを定義したExcelファイル（名前は任意）
   ├── input
   │  └── (修正したい.txtファイルと.srtファイルを置く) 
   ├── output (自動で生成)
   │  └── (修正後の.txtファイルと.srtファイルが格納される) 
   ├── done (自動で生成)
   │   └── (元ファイルは処理後にこちらに移動)
   ├── README.md                   # このファイル
   └── requirements.txt            # 必要なパッケージリスト
   ```

6. **スクリプトの実行:**  `replace_text` ディレクトリで、以下のコマンドを実行します。

   ```bash
   python replace_text.py
   ```
処理が完了すると、 `output`フォルダに修正後のファイルが作成され、 `done` ファイルが自動で生成され、元ファイルはこちらに移動されます。

### 注意点

* Excel ファイルは .xlsx 形式である必要があります。
* テキストファイルと字幕ファイルは UTF-8 エンコーディングである必要があります。

### ライセンス

このスクリプトは MIT ライセンスで公開されています。
このプロジェクトは、自由に使用、改変、再配布することができます。もし、コードを使用する場合は、元の作者への謝辞を含めていただければ幸いです。 

---
**謝辞:** 

例) このコードは、[shoei05](https://github.com/shoei05) によって作成されました。 

--- 

