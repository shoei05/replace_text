import openpyxl
import os
import glob
import shutil

# --- 設定 ---
excel_folder = 'replace_rule'  # 置換ルールを定義したExcelファイルがあるフォルダ名
input_folder = 'input'         # 修正したいファイルがあるフォルダ名
output_folder = 'output'        # 修正後のファイルを保存するフォルダ名
done_folder = 'done'           # 処理済みのファイルを移動するフォルダ名
# ----------------------

# Excelファイルのパスを取得
excel_files = glob.glob(os.path.join(excel_folder, '*.xlsx'))
if not excel_files:
    print("エラー: replace_rule フォルダに .xlsx ファイルが見つかりません。")
    exit()
excel_path = excel_files[0]

# Excelファイルを読み込み、置換ルールを辞書に格納
wb = openpyxl.load_workbook(excel_path)
sheet = wb.active
replace_dict = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    if row[0] is not None and row[1] is not None:
        replace_dict[str(row[0])] = str(row[1])

# 出力フォルダと処理済みフォルダが存在しない場合は作成
os.makedirs(output_folder, exist_ok=True)
os.makedirs(done_folder, exist_ok=True)

# テキストファイルと字幕ファイルを一括処理
for file_path in glob.glob(os.path.join(input_folder, '*.txt')) + glob.glob(os.path.join(input_folder, '*.srt')):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 置換ルールに基づいてテキストを修正
    for key, value in replace_dict.items():
        text = text.replace(key, value)

    # 修正後のテキストをファイルに保存
    output_file_path = os.path.join(output_folder, os.path.basename(file_path))
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(text)

    # 処理後のファイルを done フォルダに移動
    shutil.move(file_path, os.path.join(done_folder, os.path.basename(file_path)))

print("置換が完了しました！")
