import pandas as pd

# CSVファイルを読み込む
file_path = 'sample_data_jp.csv'
sample_data = pd.read_csv(file_path)

# 1. ユーザー名とメールアドレスの列を削除
data_cleaned = sample_data.drop(['ユーザー名', 'メールアドレス'], axis=1)

# 2. 商品名でデータをソート
data_sorted = data_cleaned.sort_values(by='製品名')

# 3. 各商品ごとに個数と価格の小計を計算し、小計行を追加する
# 商品名ごとのグループを作成して小計を計算
subtotal_data = data_sorted.groupby('製品名').apply(lambda x: pd.Series({
    '個数': x['個数'].sum(),
    '価格': x['価格'].sum()  # x['個数'].dot(x['価格'])
})).reset_index()

# 小計行を'小計'という製品名でマーク
subtotal_data['製品名'] = subtotal_data['製品名'] + 'の小計'

# 元のデータと小計データを結合
final_data = pd.concat([data_sorted, subtotal_data]).sort_values(by='製品名', kind='mergesort')

# 4. 新しい `data.csv` ファイルに結果を書き出す
output_file_path = 'data.csv'
final_data.to_csv(output_file_path, index=False)  # インデックスは書き出さない

