import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import math
# 機械学習用
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split

##ファイルの読み込み /Users/takatoshiinaoka/Downloads/fukuoka-efc-dep-fusic-data
df1 = pd.read_parquet("201807-043398656781-043398656781.parquet")
# df2= pd.read_parquet("")
# df3= pd.read_parquet("")

##ファイル情報の出力
print(df1.info())

##ファイルの中身の出力
df1.sample(10)

# print(df7.columns)

##ファイルの読み込み /Users/takatoshiinaoka/Downloads/fukuoka-efc-dep-fusic-data
df1 = pd.read_parquet("/Users/takatoshiinaoka/Desktop/django/dec_team_a/app/201807-043398656781-043398656781.parquet")
d=df1.sample(5)
#print("d"+str(d))

#dfの作成
C=["論理名", "例", "データ型", "データ数", "ユニーク数", "欠損値の数"]
I=df1.columns
data_def=pd.DataFrame(index=I, columns=C)
dic_name={'id':"データの連番ID", 'payer_account_id':"支払い元AWSアカウントの識別子", 'usage_account_id':"利用AWSアカウントの識別子", 'product_code':"使用リソースコード",
    'usage_type':"使用状況の詳細", 'operation':"オペレーション", 'line_item_type':"請求の種類", 'pricing_unit':"単位", 'amount':"使用量",
    'blend_rate':"平均コストレート", 'blend_cost':"平均コスト", 'unblend_rate':"適応前コストレート", 'unblend_cost':"適応前コスト",
    'ondemand_rate':"オンデマンドレート", 'ondemand_cost':"オンデマンドコスト", 'calculate_at':"計算日時", 'billing_at':"請求年月",
    'created_at':"データ作成日時", 'updated_at':"データ更新日時", 'pricing_term':"オンデマンドorリザーブド", 'billing_cost':"請求コスト", 'owned':"自身のAWSアカウントでのリザーブド適応かどうか",
    'actual_cost':"原価コスト", 'exchange_rate_id':"為替レート情報ID", 'reservation_arn':"リザーブドARN"}
def create_data_def(data_def, df):
    for i in data_def.index:
        data_def.at[i, "論理名"]=dic_name[i]
        data_def.at[i, "例"]=df.at[0, i]
        data_def.at[i, "データ型"]=type(df.at[0, i])
        data_def.at[i, "データ数"]=df[i].count()
        data_def.at[i, "ユニーク数"]=len(df[i].unique())
        data_def.at[i, "欠損値の数"]=df[i].isnull().sum()

create_data_def(data_def, df1)
print("data_def "+str(data_def))