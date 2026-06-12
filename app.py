"""
Smart Sales Dashboard v4.0 — DEMO Version (Bilingual AR/EN)
============================================================
This is the demo/portfolio version.
Excel export is disabled. AI analysis uses a limited summary.
Full version available for purchase.

Run:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import html
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from translations import t
from utils import load_data, detect_columns, get_api_key, DEMO_DATA, DEMO_COL_MAP
from analyzers import (
    compute_kpis, build_summary, compute_product_sales, compute_region_sales,
    compute_trend, compute_pareto, compute_heatmap_pivot, compute_statistics,
)
from charts import (
    create_bar_chart, create_pie_chart, create_line_chart,
    create_pareto_chart, create_heatmap,
)

# ─────────────────────────────────────────────
# 1. Language init
# ─────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

lang = st.session_state.lang
is_rtl = lang == "ar"

# ─────────────────────────────────────────────
# 2. Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title=t("page_title", lang),
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# 3. CSS — RTL or LTR
# ─────────────────────────────────────────────
if is_rtl:
    st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

  html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif !important;
  }

  .main .block-container {
    direction: rtl;
  }

  [data-testid="stSidebar"] > div {
    direction: rtl;
  }

  .js-plotly-plot, .plotly, .plot-container {
    direction: ltr !important;
  }

  .main { background: #0a0f1e; }

  .kpi-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px 24px;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(14,165,233,0.15);
  }
  .kpi-value { font-size: 2rem; font-weight: 900; margin: 8px 0 4px; }
  .kpi-label { font-size: 0.85rem; color: #64748b; }
  .kpi-delta {
    font-size: 0.78rem;
    margin-top: 4px;
    padding: 2px 8px;
    border-radius: 8px;
    display: inline-block;
  }
  .kpi-delta.positive { background: rgba(16,185,129,0.15); color: #10b981; }
  .kpi-delta.negative { background: rgba(244,63,94,0.15); color: #f43f5e; }

  .insight-card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border: 1px solid #0ea5e933;
    border-right: 4px solid #0ea5e9;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    color: #e2e8f0;
    font-size: 0.95rem;
    line-height: 1.7;
  }

  .section-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #1e293b;
  }

  [data-testid="stSidebar"] {
    background: #0f172a;
    border-left: 1px solid #1e293b;
  }

  .no-results {
    text-align: center;
    padding: 40px;
    color: #64748b;
    font-size: 1.1rem;
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    border: 1px dashed #1e293b;
  }

  .status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 16px;
    background: rgba(14,165,233,0.08);
    border-radius: 8px;
    margin-bottom: 16px;
    font-size: 0.8rem;
    color: #64748b;
  }

  .demo-badge {
    background: linear-gradient(135deg, #f59e0b, #f97316);
    color: #000;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 8px;
  }

  [data-testid="stAppDeployButton"] { display: none !important; }
  #MainMenu { visibility: hidden !important; }
  footer { visibility: hidden !important; }
  header { background-color: transparent !important; }

  [data-testid="collapsedControl"] {
    position: fixed !important;
    top: 15px !important;
    left: 15px !important;
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
    background-color: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    padding: 6px !important;
    cursor: pointer !important;
    transition: background-color 0.2s ease, transform 0.2s ease !important;
  }
  [data-testid="collapsedControl"]:hover {
    background-color: #0ea5e9 !important;
    opacity: 1 !important;
    visibility: visible !important;
  }
  [data-testid="collapsedControl"] svg {
    fill: #ffffff !important;
    color: #ffffff !important;
    visibility: visible !important;
  }
  [data-testid="collapsedControl"]:hover svg {
    fill: #ffffff !important;
    color: #ffffff !important;
  }
</style>
""", unsafe_allow_html=True)
else:
    st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', 'Cairo', sans-serif !important;
  }

  .main .block-container {
    direction: ltr;
  }

  [data-testid="stSidebar"] > div {
    direction: ltr;
  }

  .js-plotly-plot, .plotly, .plot-container {
    direction: ltr !important;
  }

  .main { background: #0a0f1e; }

  .kpi-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px 24px;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(14,165,233,0.15);
  }
  .kpi-value { font-size: 2rem; font-weight: 900; margin: 8px 0 4px; }
  .kpi-label { font-size: 0.85rem; color: #64748b; }
  .kpi-delta {
    font-size: 0.78rem;
    margin-top: 4px;
    padding: 2px 8px;
    border-radius: 8px;
    display: inline-block;
  }
  .kpi-delta.positive { background: rgba(16,185,129,0.15); color: #10b981; }
  .kpi-delta.negative { background: rgba(244,63,94,0.15); color: #f43f5e; }

  .insight-card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border: 1px solid #0ea5e933;
    border-left: 4px solid #0ea5e9;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    color: #e2e8f0;
    font-size: 0.95rem;
    line-height: 1.7;
  }

  .section-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #1e293b;
  }

  [data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid #1e293b;
  }

  .no-results {
    text-align: center;
    padding: 40px;
    color: #64748b;
    font-size: 1.1rem;
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    border: 1px dashed #1e293b;
  }

  .status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 16px;
    background: rgba(14,165,233,0.08);
    border-radius: 8px;
    margin-bottom: 16px;
    font-size: 0.8rem;
    color: #64748b;
  }

  .demo-badge {
    background: linear-gradient(135deg, #f59e0b, #f97316);
    color: #000;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 8px;
  }

  [data-testid="stAppDeployButton"] { display: none !important; }
  #MainMenu { visibility: hidden !important; }
  footer { visibility: hidden !important; }
  header { background-color: transparent !important; }

  [data-testid="collapsedControl"] {
    position: fixed !important;
    top: 15px !important;
    right: 15px !important;
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
    background-color: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    padding: 6px !important;
    cursor: pointer !important;
    transition: background-color 0.2s ease, transform 0.2s ease !important;
  }
  [data-testid="collapsedControl"]:hover {
    background-color: #0ea5e9 !important;
    opacity: 1 !important;
    visibility: visible !important;
  }
  [data-testid="collapsedControl"] svg {
    fill: #ffffff !important;
    color: #ffffff !important;
    visibility: visible !important;
  }
  [data-testid="collapsedControl"]:hover svg {
    fill: #ffffff !important;
    color: #ffffff !important;
  }
</style>
""", unsafe_allow_html=True)

# Demo-specific translations
DEMO_TEXTS = {
    "demo_badge": {"ar": "نسخة تجريبية", "en": "DEMO VERSION"},
    "excel_disabled": {
        "ar": "📥 تصدير Excel متوفر في النسخة الكاملة",
        "en": "📥 Excel export available in full version",
    },
    "full_ai_disabled": {
        "ar": "🤖 التحليل المتقدم بالذكاء الاصطناعي متوفر في النسخة الكاملة",
        "en": "🤖 Advanced AI analysis available in full version",
    },
    "get_full": {
        "ar": "🚀 احصل على النسخة الكاملة",
        "en": "🚀 Get the Full Version",
    },
}

def td(key, lang="ar"):
    entry = DEMO_TEXTS.get(key, {})
    return entry.get(lang, entry.get("ar", key))

# ─────────────────────────────────────────────
# 4. Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"<span class='demo-badge'>{td('demo_badge', lang)}</span>", unsafe_allow_html=True)
    st.markdown(f"## {t('settings', lang)}")

    lang_options = {"العربية 🇸🇦": "ar", "English 🇬🇧": "en"}
    current_label = "العربية 🇸🇦" if lang == "ar" else "English 🇬🇧"
    selected_lang_label = st.selectbox(
        t("language_label", lang),
        list(lang_options.keys()),
        index=list(lang_options.values()).index(lang),
    )
    new_lang = lang_options[selected_lang_label]
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

    st.markdown("---")
    st.markdown(f"### {t('upload_data', lang)}")
    uploaded_file = st.file_uploader(
        t("choose_file", lang),
        type=["xlsx", "xls", "csv"],
        help=t("file_help", lang),
    )

    st.markdown("---")
    st.markdown(f"### {t('display_options', lang)}")
    show_raw_data = st.checkbox(t("show_raw_data", lang), value=True)
    show_ai_insights = st.checkbox(t("show_ai_insights", lang), value=True)
    show_heatmap = st.checkbox(t("show_heatmap", lang), value=True)

    st.markdown("---")
    st.markdown(
        f"<div style='text-align:center; color:#475569; font-size:0.75rem;'>"
        f"{t('last_update', lang)}: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        f"</div>",
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# 5. Load data
# ─────────────────────────────────────────────
if uploaded_file:
    df, error = load_data(uploaded_file)
    if error:
        if error == "empty":
            st.error(t("file_empty", lang))
        else:
            st.error(t("file_read_error", lang, e=error))
        st.stop()
    col_map = detect_columns(df)
    using_demo = False
    st.sidebar.success(t("records_loaded", lang, n=len(df)))
else:
    df = pd.DataFrame(DEMO_DATA)
    col_map = DEMO_COL_MAP.copy()
    using_demo = True

if not col_map.get("sales") and not using_demo:
    st.warning(t("cols_not_detected", lang))
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()
    c1, c2, c3, c4 = st.columns(4)
    col_map["sales"] = c1.selectbox(t("col_sales", lang), numeric_cols)
    col_map["product"] = c2.selectbox(t("col_product", lang), all_cols)
    col_map["region"] = c3.selectbox(t("col_region", lang), ["—"] + all_cols)
    col_map["date"] = c4.selectbox(t("col_date", lang), ["—"] + all_cols)
    if col_map["region"] == "—":
        col_map.pop("region")
    if col_map["date"] == "—":
        col_map.pop("date")

SALES = col_map.get("sales")
PRODUCT = col_map.get("product")
REGION = col_map.get("region")
DATE = col_map.get("date")
QUANTITY = col_map.get("quantity")

# ─────────────────────────────────────────────
# 6. Header & status bar
# ─────────────────────────────────────────────
st.markdown(f"# {t('main_title', lang)}")

if using_demo:
    st.info(t("demo_notice", lang))

source_name = t("demo_data", lang) if using_demo else uploaded_file.name
st.markdown(
    f"""<div class='status-bar'>
    <span>{t('source_label', lang)}: {source_name}</span>
    <span>{t('total_records', lang)}: {len(df):,}</span>
    <span>🕐 {datetime.now().strftime('%H:%M — %Y/%m/%d')}</span>
    </div>""",
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# 7. Interactive filters
# ─────────────────────────────────────────────
filter_cols = st.columns(4)
all_label = t("all", lang)

with filter_cols[0]:
    if PRODUCT and PRODUCT in df.columns:
        products = [all_label] + sorted(df[PRODUCT].dropna().unique().tolist())
        selected_product = st.selectbox(t("filter_product", lang), products)
    else:
        selected_product = all_label

with filter_cols[1]:
    if REGION and REGION in df.columns:
        regions = [all_label] + sorted(df[REGION].dropna().unique().tolist())
        selected_region = st.selectbox(t("filter_region", lang), regions)
    else:
        selected_region = all_label

with filter_cols[2]:
    if DATE and DATE in df.columns:
        dates = [all_label] + sorted(df[DATE].dropna().unique().tolist())
        selected_date = st.selectbox(t("filter_period", lang), dates)
    else:
        selected_date = all_label

with filter_cols[3]:
    if SALES and SALES in df.columns:
        min_s = int(df[SALES].min())
        max_s = int(df[SALES].max())
        if min_s < max_s:
            min_val, max_val = st.slider(t("filter_sales_range", lang), min_s, max_s, (min_s, max_s))
        else:
            min_val, max_val = min_s, max_s
            st.info(t("sales_value", lang, v=f"{min_s:,}"))
    else:
        min_val, max_val = 0, 999_999_999

filtered = df.copy()
if selected_product != all_label and PRODUCT:
    filtered = filtered[filtered[PRODUCT] == selected_product]
if selected_region != all_label and REGION:
    filtered = filtered[filtered[REGION] == selected_region]
if selected_date != all_label and DATE:
    filtered = filtered[filtered[DATE] == selected_date]
if SALES and SALES in df.columns:
    filtered = filtered[(filtered[SALES] >= min_val) & (filtered[SALES] <= max_val)]

if filtered.empty:
    st.markdown(
        f"""<div class='no-results'>
        {t('no_results', lang)}<br>
        <span style='font-size:0.85rem'>{t('no_results_hint', lang)}</span>
        </div>""",
        unsafe_allow_html=True,
    )
    st.stop()

# ─────────────────────────────────────────────
# 8. KPI Cards
# ─────────────────────────────────────────────
st.markdown("---")
kpi_cols = st.columns(5)

if SALES and SALES in filtered.columns:
    kpis = compute_kpis(filtered, SALES)
    total = kpis["total"]
    avg = kpis["avg"]
    maximum = kpis["max"]
    median = kpis["median"]
    count = kpis["count"]

    with kpi_cols[0]:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{t('kpi_total_sales', lang)}</div>
          <div class='kpi-value' style='color:#0ea5e9'>{total:,.0f}</div>
          <div class='kpi-label'>{t('currency', lang)}</div>
        </div>""", unsafe_allow_html=True)

    with kpi_cols[1]:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{t('kpi_records', lang)}</div>
          <div class='kpi-value' style='color:#10b981'>{count:,}</div>
          <div class='kpi-label'>{t('deal_record', lang)}</div>
        </div>""", unsafe_allow_html=True)

    with kpi_cols[2]:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{t('kpi_avg_sales', lang)}</div>
          <div class='kpi-value' style='color:#f59e0b'>{avg:,.0f}</div>
          <div class='kpi-label'>{t('per_record', lang)}</div>
        </div>""", unsafe_allow_html=True)

    with kpi_cols[3]:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{t('kpi_median', lang)}</div>
          <div class='kpi-value' style='color:#8b5cf6'>{median:,.0f}</div>
          <div class='kpi-label'>{t('median_value', lang)}</div>
        </div>""", unsafe_allow_html=True)

    with kpi_cols[4]:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{t('kpi_max', lang)}</div>
          <div class='kpi-value' style='color:#f43f5e'>{maximum:,.0f}</div>
          <div class='kpi-label'>{t('best_performance', lang)}</div>
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 9. Charts
# ─────────────────────────────────────────────
st.markdown("---")

col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown(f"<div class='section-title'>{t('chart_by_product', lang)}</div>", unsafe_allow_html=True)
    if PRODUCT and SALES and PRODUCT in filtered.columns:
        by_product = compute_product_sales(filtered, PRODUCT, SALES)
        fig_bar = create_bar_chart(by_product, PRODUCT, SALES)
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info(t("select_product_sales", lang))

with col_right:
    st.markdown(f"<div class='section-title'>{t('chart_by_region', lang)}</div>", unsafe_allow_html=True)
    if REGION and SALES and REGION in filtered.columns:
        by_region = compute_region_sales(filtered, REGION, SALES)
        fig_pie = create_pie_chart(by_region, REGION, SALES)
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info(t("no_region_col", lang))

if DATE and SALES and DATE in filtered.columns:
    st.markdown(f"<div class='section-title'>{t('chart_trend', lang)}</div>", unsafe_allow_html=True)
    trend = compute_trend(filtered, DATE, SALES)
    fig_line = create_line_chart(trend, DATE, SALES)
    st.plotly_chart(fig_line, use_container_width=True)

if PRODUCT and SALES and PRODUCT in filtered.columns:
    st.markdown(f"<div class='section-title'>{t('chart_pareto', lang)}</div>", unsafe_allow_html=True)
    pareto_data = compute_pareto(filtered, PRODUCT, SALES)
    fig_pareto = create_pareto_chart(pareto_data, PRODUCT, SALES, lang)
    st.plotly_chart(fig_pareto, use_container_width=True)

if show_heatmap and PRODUCT and REGION and SALES:
    if all(c in filtered.columns for c in [PRODUCT, REGION, SALES]):
        st.markdown(f"<div class='section-title'>{t('chart_heatmap', lang)}</div>", unsafe_allow_html=True)
        pivot = compute_heatmap_pivot(filtered, PRODUCT, REGION, SALES)
        fig_heat = create_heatmap(pivot)
        st.plotly_chart(fig_heat, use_container_width=True)

# ─────────────────────────────────────────────
# 10. Data table (CSV only — no Excel in demo)
# ─────────────────────────────────────────────
if show_raw_data:
    st.markdown("---")
    st.markdown(f"<div class='section-title'>{t('data_table_title', lang)}</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs([t("tab_filtered", lang), t("tab_stats", lang)])

    with tab1:
        st.dataframe(filtered, use_container_width=True, height=320)

        dl_col1, dl_col2 = st.columns(2)
        with dl_col1:
            csv_data = filtered.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                label=t("download_csv", lang),
                data=csv_data,
                file_name=f"sales_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True,
            )
        with dl_col2:
            st.info(td("excel_disabled", lang))

    with tab2:
        if SALES and SALES in filtered.columns:
            desc_df = compute_statistics(filtered, SALES, lang)
            st.dataframe(desc_df, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────
# 11. AI Section (limited in demo)
# ─────────────────────────────────────────────
if show_ai_insights:
    st.markdown("---")
    st.markdown(f"<div class='section-title'>{t('ai_title', lang)}</div>", unsafe_allow_html=True)

    summary_text = build_summary(filtered, col_map, lang)

    st.markdown(f"""
    <div class='insight-card'>
      <strong>{t('data_summary_label', lang)}</strong><br>
      <pre style='margin:8px 0 0; color:#94a3b8; font-family:Cairo; font-size:0.85rem;'>{summary_text}</pre>
    </div>""", unsafe_allow_html=True)

    st.info(td("full_ai_disabled", lang))

# ─────────────────────────────────────────────
# 12. Footer
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown(f"""
<div style='text-align:center; color:#334155; font-size:0.8rem; padding:16px;'>
    {t('footer_text', lang)}<br>
    <span style='font-size:0.7rem; color:#1e293b;'>{t('footer_powered', lang)}</span><br>
    <span class='demo-badge' style='margin-top:8px;'>{td('demo_badge', lang)}</span>
</div>
""", unsafe_allow_html=True)
