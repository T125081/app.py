import streamlit as st
import pandas as pd
import plotly.express as px

st.title('広告費と売り上げ')

df = pd.read_csv("ad_expense_sales.csv")

# df = pd.DataFrame(data=,
#                    index=df['ad_expense'],
#                    columns=df['sales'])

with st.sidebar:
    st.subheader("抽出条件")
    ct = st.multiselect('製品カテゴリを選択してください（複数選択可）',
                            df["prod_category"].unique())
    md = st.selectbox("広告媒体を選択してください",
                            df["media"].unique())
    
    st.subheader("色分け")
    color =st.selectbox("色分け選択",
                        ["性別","年齢層","季節"])

    if color == '性別':
        color = 'sex'
    elif color == "年齢層":
        color = 'age'
    elif color == "季節":
        color = 'season'
    
    # sx = st.selectbox("性別を選択してください",
    #                         df["sex"].unique())
    # ag = st.selectbox("年齢層を選択してください",
    #                         df["age"].unique())
    # ss = st.selectbox("季節を選択してください",
    #                         df["season"].unique())

df = df[df['prod_category'].isin(ct)]
df = df[df['media']==md]

# st.write('検索された条件下においての表は以下の様になります。')
# st.dataframe(df, width=400, height=220)

# df = df[df['sex']==sx]
# df = df[df['age']==ag]
# df = df[df['season']==ss]

# df.drop('prod_category',axis=1,inplace=True)
# df.drop('media',axis=1,inplace=True)
# df.drop('sex',axis=1,inplace=True)
# df.drop('age',axis=1,inplace=True)
# df.drop('season',axis=1,inplace=True)
# df.set_index('ad_expense',inplace=True)


st.write('検索された条件下においてのグラフは以下の様になります。')
fig = px.scatter(df,
                 x='ad_expense',
                 y='sales',
                 color=color,
                 labels={'ad_expense':'広告費','sales':'売り上げ'},
                 )
st.plotly_chart(fig)


