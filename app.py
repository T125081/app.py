import streamlit as st
import pandas as pd
import altair as alt

st.title('「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」を基にした')

st.header('〈このアプリとは〉')

st.write('調査年月2022年度の統計表「食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率」から得られるデータを基に、アプリ。')

st.subheader("〈調査の概要 [引用ページより]〉")

st.write('食品循環資源の再生利用等実態調査は、食品製造業、食品卸売業、食品小売業及び外食産業の食品廃棄物等の発生状況を調査し、食品廃棄物等の年間発生量、発生抑制量、減量、再生利用等を提供しています。（５年毎に実施）食品ロス統計調査は、世帯や外食産業の食品ロスの実態を調査し、食品使用量、食品ロス（食べ残し）量、食品ロス率を提供しています。（平成27年度で調査終了）')

st.write('(引用：〈担当機関・課室〉農林水産省　消費統計室, 〈公開年月日時分〉2025-01-31 00:00, 食品循環資源の再生利用等実態調査 確報 令和４年度食品循環資源の再生利用等実態調査 統計表 1 食品産業における食品廃棄物等の年間発生量、発生抑制の実施量及び再生利用等実施率 年度次 | データベース | 統計データを探す | 政府統計の総合窓口, https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&toukei=00500231&bunya_l=04&tstat=000001127995&cycle=8&tclass1=000001127996&tclass2=000001217140&statdisp_id=0002110164&tclass3val=0 〈2026/2/2 参照〉)')

st.header('データ確認')

st.write('総計的な「計」と記入されている物を「総計」、\n[食品製造業_]…(製)\n[食品卸売業_]…(卸)\n[食品小売業_]…(小)\n[外食産業_]…(外)\n[食品廃棄物等の年間発生量_]…(年)\n')


df = pd.read_csv('FEH_00500231_260202222416 copy.csv')

df["total"] = df[["(年)1)食品リサイクル法で規定している用途への実施量【千t】","(年)熱回収の実施量【千t】","(年)減量した量【千t】","(年)2)その他【千t】","(年)廃棄物としての処分量【千t】"]].sum(axis=1)

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
    st.subheader("各量の全体量とそれの内訳の比較の為の棒グラフ")    
    st.altair_chart(
        alt.Chart(df_long)
        .mark_bar()
        .encode(
            alt.X("食品産業:N",sort=order,title="食品産業計種類"),
            alt.Y("sum(量):Q",title="合計量 【千t】"),
            alt.Color("内訳:N",title="内訳"),
        )
        .configure_legend(orient="bottom"),
        use_container_width=True
    )

with st.container():
    st.subheader("各量の内訳の比較の為の棒グラフ")
    st.altair_chart(
        alt.Chart(df_long)
        .mark_bar()
        .encode(
            alt.X("食品産業:N",sort=order,title="食品産業計種類"),
            alt.Y("sum(量):Q",stack="normalize",title="各割合 【%】"),
            alt.Color("内訳:N",title="内訳"),
        )
        .configure_legend(orient="bottom"),
        use_container_width=True
    )

with st.sidebar:
    st.subheader('円グラフに表示する')
    fo_lo_kind = st.selectbox('食品産業計種類を選択してください', 
                         df_long["食品産業"].unique())

df_s = df_long[df_long["食品産業"]==fo_lo_kind]

df_s = df_s.copy()
# df_s["割合"] = df_s["量"] / df_s["量"].sum()

with st.container():
    st.subheader("内訳の円グラフ")
    st.write("〈ページ左上の＞をクリックして開くことができるサイドバーの中で、内訳を確認したい食品産業計種類を選択してください。〉")
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


# 以下の要素を１つ以上含めること：
# ✓ アプリの概要‧目的‧使い方の説明
# ✓ データの確認（件数、期間、対象など）
# ✓ 可視化結果の簡単な解釈や説明