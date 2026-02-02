import streamlit as st
import pandas as pd
import altair as alt

st.title('調査年月2022年度「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」')

st.header('〈このアプリは何なのか〉')

st.write('調査年月2022年度の統計表「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」から得られるデータを基に、2022年度における食品廃棄物の取り扱い状況を確認する為のアプリ。')

st.subheader("〈調査の概要 [引用ページより]〉")

st.write('食品循環資源の再生利用等実態調査は、食品製造業、食品卸売業、食品小売業及び外食産業の食品廃棄物等の発生状況を調査し、食品廃棄物等の年間発生量、発生抑制量、減量、再生利用等を提供しています。（５年毎に実施）食品ロス統計調査は、世帯や外食産業の食品ロスの実態を調査し、食品使用量、食品ロス（食べ残し）量、食品ロス率を提供しています。（平成27年度で調査終了）')

st.write('(引用データ：〈担当機関・課室〉農林水産省　消費統計室, 〈公開年月日時分〉2025-01-31 00:00, 食品循環資源の再生利用等実態調査 確報 令和４年度食品循環資源の再生利用等実態調査 統計表 1 食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率 年度次 | データベース | 統計データを探す | 政府統計の総合窓口, https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&toukei=00500231&bunya_l=04&tstat=000001127995&cycle=8&tclass1=000001127996&tclass2=000001217140&statdisp_id=0002110164&tclass3val=0 〈2026/2/2 参照〉)')
st.write("")
st.write("")

st.header('〈データ確認〉')

st.write('〈注意　以下見やすさの為の書き換え箇所有り〉')
st.write('総計的な「計」と記入されている物を「総計」')
st.write("[食品製造業_]…(製)")
st.write("[食品卸売業_]…(卸)")
st.write("[食品小売業_]…(小)")
st.write("[外食産業_]…(外)")
st.write("[食品廃棄物等の年間発生量_]…(年)")
st.write("")
st.write("")

st.subheader("各省略箇所について")
st.write("「食品廃棄物等の年間発生量_1)食品リサイクル法で規定している用途への実施量」における食品リサイクル法で規定している用途とは、肥料、飼料、菌床培地、メタン、油脂及び油脂製品、炭化製品（燃料及び還元剤）又はエタノールの原材料としての再生利用である。")
st.write("「食品廃棄物等の年間発生量_2)その他」におけるその他とは、再生利用の実施量として、1)以外の食用品（食品添加物や調味料、健康食品等）、工業資材用（舗装用資材、塗料の原料等）、工芸用等の用途に仕向けた量及び不明のものをいう。")
st.write("「3)再生利用等実施率」において、再生利用等実施率=当該年度の（発生抑制の実施量＋食品リサイクル法で規定している用途への実施量＋熱回収の実施量×0.95＋減量した量）÷当該年度の（発生抑制の実施量＋食品廃棄物等の年間発生量）")
st.write("")
st.write("")

st.subheader("（※　仕様上隠れてしまっている可能性がある個所の表示欄）")
st.write("内訳")
st.write("(年)1)食品リサイクル法で規定している用途への実施量【千t】")
st.write("(年)熱回収の実施量【千t】")
st.write("(年)減量した量【千t】")
st.write("(年)2)その他【千t】")
st.write("(年)廃棄物としての処分量【千t】")
st.write("")
st.write("")
st.write("食品産業計の種類")
st.write("食品産業総計")
st.write("食品製造業総計")
st.write("(製)畜産食料品製造業")
st.write("(製)水産食料品製造業")
st.write("(製)野菜缶詰･果実缶詰･農産保存食料品製造業")
st.write("(製)調味料製造業")
st.write("(製)糖類製造業")
st.write("(製)精穀・製粉業")
st.write("(製)パン・菓子製造業")
st.write("(製)動植物油脂製造業")
st.write("(製)その他の食料品製造業")
st.write("(製)清涼飲料製造業")
st.write("(製)酒類製造業")
st.write("(製)茶･コーヒー製造業")
st.write("食品卸売業総計")
st.write("(卸)農畜産物・水産物卸売業")
st.write("(卸)食料・飲料卸売業")
st.write("食品小売業総計")
st.write("(小)各種食料品小売業")
st.write("(小)野菜・果実小売業")
st.write("(小)食肉小売業")
st.write("(小)鮮魚小売業")
st.write("(小)酒小売業")
st.write("(小)菓子・パン小売業")
st.write("(小)その他の飲食料品小売業")
st.write("外食産業総計")
st.write("(外)沿海旅客海運業")
st.write("(外)内陸水運業")
st.write("(外)宿泊業")
st.write("(外)飲食店")
st.write("(外)持ち帰り･配達飲食サービス業")
st.write("(外)結婚式場業")
st.write("")
st.write("")

df = pd.read_csv('FEH_00500231_260202222416 copy.csv')

# df["total"] = df[["(年)1)食品リサイクル法で規定している用途への実施量【千t】","(年)熱回収の実施量【千t】","(年)減量した量【千t】","(年)2)その他【千t】","(年)廃棄物としての処分量【千t】"]].sum(axis=1)

cols = [
    "(年)1)食品リサイクル法で規定している用途への実施量【千t】",
    "(年)熱回収の実施量【千t】",
    "(年)減量した量【千t】",
    "(年)2)その他【千t】",
    "(年)廃棄物としての処分量【千t】",
]

df_long = df.melt(
    id_vars=["食品産業"],
    value_vars=cols,
    var_name="内訳",
    value_name="量"
)

df_long["食品産業"] = df_long["食品産業"].astype(str)

order = df_long["食品産業"].unique().tolist()

with st.container():
    st.subheader("【各食品産業種の食品廃棄物等の年間発生量とそれらの内訳の比較の為の棒グラフ】")
    st.altair_chart(
        alt.Chart(df_long)
        .mark_bar()
        .encode(
            alt.X("食品産業:N",sort=order,title="食品産業計の種類"),
            alt.Y("sum(量):Q",title="年間発生量 【千t】"),
            alt.Color("内訳:N",title="内訳"),
        )
        .configure_legend(orient="bottom"),
        use_container_width=True
    )

st.write("")
st.write("")

with st.container():
    st.subheader("【各食品産業種の食品廃棄物等の年間発生量の内訳の各割合の比較の為の棒グラフ】")
    st.altair_chart(
        alt.Chart(df_long)
        .mark_bar()
        .encode(
            alt.X("食品産業:N",sort=order,title="食品産業計の種類"),
            alt.Y("sum(量):Q",stack="normalize",title="各内訳の割合 【%】"),
            alt.Color("内訳:N",title="内訳"),
        )
        .configure_legend(orient="bottom"),
        use_container_width=True
    )

st.write("")
st.write("")

with st.sidebar:
    st.subheader('〈内訳の割合の円グラフを表示する食品産業計種類〉')
    fo_lo_kind = st.selectbox('食品産業計種類を選択してください', 
                         df_long["食品産業"].unique())

df_s = df_long[df_long["食品産業"]==fo_lo_kind]

df_s = df_s.copy()
# df_s["割合"] = df_s["量"] / df_s["量"].sum()

with st.container():
    st.subheader("【各食品産業種の食品廃棄物等の年間発生量の内訳の割合の円グラフ】")
    st.write("〈ページ左上の＞をクリックして開くことができるサイドバーの中で、内訳の割合を確認したい食品産業計種類を選択してください。〉")
    st.altair_chart(
        alt.Chart(df_s)
        .mark_arc()
        .encode(
            alt.Theta("量:Q",stack="normalize"),
            alt.Color("内訳:N",title="内訳"),
            # alt.Tooltip([
            #     alt.Tooltip("内訳:N", title="内訳"),
            #     alt.Tooltip("量:Q", title="量【千t】", format=",.1f"),
            #     alt.Tooltip("割合:Q", title="割合【%】", format=".1%")
            # ])
        )
        .configure_legend(orient="bottom"),
        use_container_width=True
    )