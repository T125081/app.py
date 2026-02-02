import streamlit as st
import pandas as pd
import altair as alt
# import plotly.express as px
# import numpy as np
# import matplotlib.pyplot as plt

st.title('「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」を基にした')

st.header('〈このアプリとは〉')

st.write('調査年月2022年度の統計表「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」から得られるデータを基に、アプリ。')

st.subheader("〈調査の概要 [引用ページより]〉")

st.write('食品循環資源の再生利用等実態調査は、食品製造業、食品卸売業、食品小売業及び外食産業の食品廃棄物等の発生状況を調査し、食品廃棄物等の年間発生量、発生抑制量、減量、再生利用等を提供しています。（５年毎に実施）食品ロス統計調査は、世帯や外食産業の食品ロスの実態を調査し、食品使用量、食品ロス（食べ残し）量、食品ロス率を提供しています。（平成27年度で調査終了）')

st.write('(引用：〈担当機関・課室〉農林水産省　消費統計室, 〈公開年月日時分〉2025-01-31 00:00, 食品循環資源の再生利用等実態調査 確報 令和４年度食品循環資源の再生利用等実態調査 統計表 1 食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率 年度次 | データベース | 統計データを探す | 政府統計の総合窓口, https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&toukei=00500231&bunya_l=04&tstat=000001127995&cycle=8&tclass1=000001127996&tclass2=000001217140&statdisp_id=0002110164&tclass3val=0 〈2026/2/2 参照〉)')

st.header('データ確認')

df = pd.read_csv('FEH_00500231_260202222416 copy.csv')

df["total"] = df[["食品廃棄物等の年間発生量_1)食品リサイクル法で規定している用途への実施量【千t】","食品廃棄物等の年間発生量_熱回収の実施量【千t】","食品廃棄物等の年間発生量_減量した量【千t】","食品廃棄物等の年間発生量_2)その他【千t】","食品廃棄物等の年間発生量_廃棄物としての処分量【千t】","発生抑制の実施量【千t】"]].sum(axis=1)

cols = st.columns(2)

with cols[0]:
    "### 各量の全体量とそれの内訳の比較棒グラフ"

    st.altair_chart(
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X("食品産業:N",title="食品産業計種類"),
            alt.Y("sum(total):Q",title="合計量 【千t】"),
            alt.Color("sum(total):Q",title="各量"),
        )
        .configure_legend(orient="bottom")
    )


# with df.container(border=True, height="stretch"):
#     "### Monthly weather breakdown"
#     ""

#     st.altair_chart(
#         alt.Chart(df)
#         .mark_bar()
#         .encode(
#             alt.X("month(date):O", title="食品産業計種類"),
#             alt.Y("count():Q", title="各割合 【%】").stack("normalize"),
#             alt.Color("weather:N"),
#         )
#         .configure_legend(orient="bottom")
#     )




# with st.sidebar:
#     st.subheader('円グラフに表示する')
#     prod_category = st.multiselect('食品産業計種類を選択してください（複数選択可）', 
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
    

# with cols[1].container(border=True, height="stretch"):
#     "### Weather distribution"

#     st.altair_chart(
#         alt.Chart(df)
#         .mark_arc()
#         .encode(
#             alt.Theta("count()"),
#             alt.Color("weather:N"),
#         )
#         .configure_legend(orient="bottom")
#     )





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