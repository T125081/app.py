import streamlit as st
import pandas as pd
# import plotly.express as px
# import numpy as np
# import matplotlib.pyplot as plt

st.title('全体タイトル')

st.header('説明欄表示')

st.subheader('説明対象')

st.write('説明内容')

st.header('データ確認')

df = pd.read_csv('')

with st.sidebar:
    st.subheader('抽出条件')
    prod_category = st.multiselect('製品カテゴリを選択してください（複数選択可）', 
                                   df['prod_category'].unique())
    media = st.selectbox('広告媒体を選択してください', 
                         df['media'].unique())
    st.subheader('色分け')    
    color = st.selectbox('分類を選択してください',
                      ['性別', '年齢層', '季節'])  
    if color == '性別':
        color = 'sex'
    elif color == '年齢層':
        color = 'age'
    else:
        color = 'season'
    



# 栄養表の各データ
# 年齢別　総合

# df = pd.read_csv('ad_expense_sales.csv')

# with st.sidebar:
#     st.subheader('抽出条件')
#     prod_category = st.multiselect('製品カテゴリを選択してください（複数選択可）', 
#                                    df['prod_category'].unique())
#     media = st.selectbox('広告媒体を選択してください', 
#                          df['media'].unique())
#     st.subheader('色分け')    
#     color = st.selectbox('分類を選択してください',
#                       ['性別', '年齢層', '季節'])  
#     if color == '性別':
#         color = 'sex'
#     elif color == '年齢層':
#         color = 'age'
#     else:
#         color = 'season'

# # st.write(f'{color}が選択されました')

# df = df[df['prod_category'].isin(prod_category)]
# df = df[df['media']==media]

# # st.dataframe(df)

# fig = px.scatter(df, 
#                  x='ad_expense', 
#                  y='sales',
#                  color=color,
#                  labels={'sales':'売上 (万円)', 'ad_expense':'広告費 (万円)'},
#                  range_x=[0, df['ad_expense'].max()*1.1],
#                  range_y=[0, df['sales'].max()*1.1],
#                  trendline='ols'
#                 )
# st.plotly_chart(fig)

# e-Stat（政府統計）のデータを使用
# CSV形式をそのまま使用してOK
# （高度なデータ加工は必須ではありません）

# 以下の要素を3つ以上含めること：
# ✓ アプリの概要‧目的‧使い方の説明
# ✓ データの確認（件数、期間、対象など）
# ✓ データの可視化（最低2種類のグラフ）
# ✓ 比較や傾向が分かる表示（地域差など）
# ✓ 可視化結果の簡単な解釈や説明


# ✓ サイドバー等で条件を変更できる
# ✓ 例：都道府県、年、期間、指標など
# ✓ ユーザ操作でグラフ等の表示が変化する
# ✓ 単位や補足説明を画面上に明示する

# 【授業で扱っていない部品を探す　公式API Reference を調査】
# 条件：最低3つ使用 必須
# 授業コードにない部品を選ぶ
# 機能的に意味のある使い方をする

# 【他アプリから着想を得る　公式サイトGallery / Explore を参照】
# 条件：アイデアを取り入れる 必須
# 優れたデザインや構成を真似ることで、アプリの品質を高めることが目
# 的です。