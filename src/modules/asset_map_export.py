
import io
import streamlit as st
import matplotlib.pyplot as plt

def render():
    st.subheader("🗺️ 資產構成輸出（PNG）")
    st.write("根據『傳承圖／資產盤點』清單，輸出簡易構成圖。")

    items = st.session_state.get("asset_items", [])
    if not items:
        st.info("目前清單為空。請先到「🗺️ 傳承圖」頁籤新增資產項目。")
        return

    # 彙總各分類金額
    agg = {}
    for r in items:
        cat = r.get("cat","其他")
        val = float(r.get("val",0))
        agg[cat] = agg.get(cat, 0) + val

    cats = list(agg.keys())
    vals = [agg[c] for c in cats]

    # 單一圖（不得設定特定顏色）
    fig, ax = plt.subplots()
    ax.bar(cats, vals)
    ax.set_title("資產分類構成（估值）")
    ax.set_ylabel("金額（元）")
    plt.xticks(rotation=15)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    st.image(buf)

    st.download_button("下載PNG", data=buf.getvalue(), file_name="asset_composition.png", mime="image/png")
