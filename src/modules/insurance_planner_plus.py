
import math
import streamlit as st
from ..services.insurance import PolicyPlan, simulate_policy
from ..utils.report import to_csv_download

def _annuity_payment(total_amount: float, years: int, periods_per_year: int = 1):
    """Equal installment payout (no discounting, simple split)."""
    n = max(years * periods_per_year, 1)
    return total_amount / n

def render():
    st.subheader("📦 保單贈與壓縮＋分期給付（進階版）")

    # 基礎保費與年期
    c1, c2, c3 = st.columns(3)
    with c1:
        annual_premium = st.number_input("年繳保費", min_value=0.0, step=10_000.0, value=3_000_000.0, key="ipp_ap")
    with c2:
        pay_years = st.number_input("繳費年期（年）", min_value=1, step=1, value=6, key="ipp_py")
    with c3:
        factor = st.slider("90歲現價倍數（示意）", 1.0, 1.6, 1.25, 0.01, key="ipp_factor")

    # 要保人與受益分配
    st.markdown("—")
    st.markdown("#### 受益設計（可指定第二代／第三代比例）")
    c4, c5, c6 = st.columns(3)
    with c4:
        ben_A = st.text_input("受益人A（如：二代）", value="第二代", key="ipp_benA")
        pct_A = st.slider("A 比例(%)", 0, 100, 60, 1, key="ipp_pctA")
    with c5:
        ben_B = st.text_input("受益人B（如：三代）", value="第三代", key="ipp_benB")
        pct_B = st.slider("B 比例(%)", 0, 100-pct_A, 40, 1, key="ipp_pctB")
    with c6:
        payout_years = st.number_input("分期給付年數（年）", min_value=1, step=1, value=10, key="ipp_years")

    # 試算
    res = simulate_policy(PolicyPlan(annual_premium=annual_premium, pay_years=int(pay_years), projected_cash_value_factor=factor))
    total_premium = res["total_premium"]
    cash_value_90 = res["cash_value_90"]
    cp_cash = res["cp_cash_percent"]

    # 贈與壓縮（示意）：保單面額/現價進行分期贈與 vs 一次性現金贈與
    st.markdown("—")
    st.markdown("#### 贈與壓縮對比（示意）")
    gift_cash_once = total_premium  # 假設一次性現金贈與＝總繳保費
    gift_policy_now = annual_premium  # 假設保單規劃使用「逐年贈與保費」
    st.write(f"- **一次性現金贈與基礎**：{gift_cash_once:,.0f} 元")
    st.write(f"- **保單逐年贈與基礎**：{gift_policy_now:,.0f} 元（每年） × {int(pay_years)} 年")

    st.caption("＊實務上請依保單價值、要保人變更時點、保單現金價值、折減條款、最新稅法細節調整。此處為溝通示意。")

    # 分期給付計畫：將 90 歲現價（估）視為可供給付的池子，以比例拆分
    st.markdown("—")
    st.markdown("#### 分期給付試算（以 90 歲現價作為可供給付池）")
    amt_A = cash_value_90 * (pct_A/100)
    amt_B = cash_value_90 * (pct_B/100)
    pay_A = _annuity_payment(amt_A, int(payout_years), periods_per_year=1)
    pay_B = _annuity_payment(amt_B, int(payout_years), periods_per_year=1)

    colA, colB, colC = st.columns(3)
    colA.metric("總繳保費", f"{total_premium:,.0f} 元")
    colB.metric("90歲現價（估）", f"{cash_value_90:,.0f} 元")
    colC.metric("現價CP值（%）", f"{cp_cash:,.1f}%")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**{ben_A}** 受益池：{amt_A:,.0f} 元")
        st.markdown(f"年給（{payout_years}年）：**{pay_A:,.0f} 元／年**")
    with col2:
        st.markdown(f"**{ben_B}** 受益池：{amt_B:,.0f} 元")
        st.markdown(f"年給（{payout_years}年）：**{pay_B:,.0f} 元／年**")

    # 專業話術（摘要版）
    with st.expander("🗣️ 提案話術（可貼到LINE）", expanded=False):
        st.write(f"""
        1) 我們以 **逐年贈與保費** 的方式，降低一次性贈與基礎，搭配未來**要保人變更**與**指定受益**，把保單設計為**跨世代分配工具**。  
        2) 以目前試算，至第90歲的可分配池約 **{cash_value_90:,.0f} 元**；我們先以 **{ben_A} {pct_A}%／{ben_B} {pct_B}%** 的比例切分。  
        3) 給付方式採 **{payout_years} 年年給**：{ben_A} 每年約 **{pay_A:,.0f} 元**；{ben_B} 每年約 **{pay_B:,.0f} 元**。  
        4) 後續可再把比例、年數、要保人／受益人條件，配合家族治理條款進一步精緻化。
        """)

    # 匯出 CSV
    rows = [
        {"項目": "年繳保費", "金額": f"{annual_premium:,.0f}"},
        {"項目": "繳費年期", "金額": f"{int(pay_years)}"},
        {"項目": "總繳保費", "金額": f"{total_premium:,.0f}"},
        {"項目": "90歲現價估", "金額": f"{cash_value_90:,.0f}"},
        {"項目": f"{ben_A} 受益池", "金額": f"{amt_A:,.0f}"},
        {"項目": f"{ben_A} 年給（{int(payout_years)}年）", "金額": f"{pay_A:,.0f}"},
        {"項目": f"{ben_B} 受益池", "金額": f"{amt_B:,.0f}"},
        {"項目": f"{ben_B} 年給（{int(payout_years)}年）", "金額": f"{pay_B:,.0f}"},
    ]
    fname, content = to_csv_download(rows, fieldnames=["項目", "金額"])
    st.download_button("下載CSV（提案摘要）", data=content, file_name=fname, mime="text/csv")
