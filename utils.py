"""
Utility functions: column detection, Excel export, data loading
"""

import io
import pandas as pd
import streamlit as st
from datetime import datetime
from translations import t


DEMO_DATA = {
    "المنتج": ["منتج أ", "منتج ب", "منتج ج", "منتج أ", "منتج ب", "منتج ج", "منتج أ", "منتج ب", "منتج ج", "منتج أ", "منتج د", "منتج د", "منتج هـ", "منتج هـ"],
    "المبيعات": [1200, 800, 1500, 900, 2000, 1100, 1800, 1300, 1700, 2200, 950, 1400, 600, 1150],
    "الكمية": [30, 20, 40, 25, 50, 28, 45, 33, 42, 55, 22, 35, 15, 28],
    "المنطقة": ["شمال", "جنوب", "شمال", "غرب", "جنوب", "غرب", "شمال", "جنوب", "غرب", "شمال", "شرق", "شرق", "جنوب", "شمال"],
    "الشهر": ["يناير", "يناير", "فبراير", "فبراير", "مارس", "مارس", "أبريل", "أبريل", "مايو", "مايو", "يونيو", "يونيو", "يوليو", "يوليو"],
    "التقييم": [4.5, 3.8, 4.9, 4.1, 4.7, 3.5, 4.8, 4.2, 4.6, 5.0, 3.9, 4.3, 3.2, 4.0],
}

DEMO_COL_MAP = {
    "sales": "المبيعات",
    "product": "المنتج",
    "region": "المنطقة",
    "date": "الشهر",
    "quantity": "الكمية",
}


@st.cache_data
def load_data(file) -> tuple:
    """Load data from uploaded file with error handling."""
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")
        if df.empty:
            return None, "empty"
        return df, None
    except Exception as e:
        return None, str(e)


def detect_columns(df: pd.DataFrame) -> dict:
    """Auto-detect important columns by name matching."""
    cols = {c.strip().lower(): c for c in df.columns}
    mapping = {}

    keywords_map = {
        "sales": [
            "مبيعات", "sales", "revenue", "إيرادات", "المبيعات",
            "القيمة", "value", "amount", "المبلغ", "الإجمالي",
            "total", "price", "سعر", "income", "دخل",
        ],
        "product": [
            "منتج", "product", "item", "المنتج", "الصنف",
            "name", "اسم", "الاسم", "category", "فئة", "التصنيف",
        ],
        "region": [
            "منطقة", "region", "area", "المنطقة", "city",
            "مدينة", "location", "الموقع", "فرع", "branch",
            "country", "دولة", "محافظة", "state",
        ],
        "date": [
            "شهر", "month", "date", "تاريخ", "الشهر",
            "التاريخ", "year", "سنة", "فترة", "period",
            "quarter", "ربع", "week", "أسبوع",
        ],
        "quantity": [
            "كمية", "quantity", "الكمية", "qty", "عدد",
            "count", "units", "وحدات",
        ],
    }

    for key, keywords in keywords_map.items():
        for kw in keywords:
            if kw in cols:
                mapping[key] = cols[kw]
                break

    if "sales" not in mapping:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            mapping["sales"] = numeric_cols[0]

    return mapping


def get_api_key() -> str:
    """Get API key from st.secrets with fallback to empty string."""
    try:
        return st.secrets.get("CLAUDE_API_KEY", "")
    except Exception:
        return ""


def generate_excel_report(df: pd.DataFrame, col_map: dict, lang: str = "ar") -> io.BytesIO:
    """Export professional Excel report with RTL formatting and colors."""
    output = io.BytesIO()
    is_rtl = (lang == "ar")

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        sheet_data_name = t("excel_sheet_data", lang)
        df.to_excel(writer, sheet_name=sheet_data_name, index=False, startrow=2)
        wb = writer.book
        ws_data = writer.sheets[sheet_data_name]
        if is_rtl:
            ws_data.right_to_left()

        title_fmt = wb.add_format({
            "bold": True, "font_size": 16, "font_color": "#0ea5e9",
            "font_name": "Cairo", "align": "right" if is_rtl else "left",
        })
        header_fmt = wb.add_format({
            "bold": True, "bg_color": "#0f172a", "font_color": "#ffffff",
            "border": 1, "align": "center", "font_name": "Cairo", "font_size": 11,
        })
        cell_fmt = wb.add_format({
            "border": 1, "align": "center", "font_name": "Cairo", "font_size": 10,
        })
        number_fmt = wb.add_format({
            "border": 1, "align": "center", "font_name": "Cairo",
            "font_size": 10, "num_format": "#,##0",
        })

        ws_data.write(0, 0, t("excel_report_title", lang), title_fmt)
        ws_data.write(1, 0, t("excel_report_date", lang, d=datetime.now().strftime("%Y-%m-%d")),
                      wb.add_format({"font_color": "#64748b", "font_name": "Cairo", "font_size": 9}))

        for col_idx, col_name in enumerate(df.columns):
            ws_data.write(2, col_idx, col_name, header_fmt)
            ws_data.set_column(col_idx, col_idx, 18)

        sales_col = col_map.get("sales")
        for row_idx in range(len(df)):
            for col_idx, col_name in enumerate(df.columns):
                val = df.iloc[row_idx, col_idx]
                if col_name == sales_col and isinstance(val, (int, float)):
                    ws_data.write(row_idx + 3, col_idx, val, number_fmt)
                else:
                    ws_data.write(row_idx + 3, col_idx, val, cell_fmt)

        sheet_summary_name = t("excel_sheet_summary", lang)
        ws_summary = wb.add_worksheet(sheet_summary_name)
        if is_rtl:
            ws_summary.right_to_left()

        summary_title_fmt = wb.add_format({
            "bold": True, "font_size": 14, "font_color": "#0ea5e9",
            "font_name": "Cairo", "bottom": 2, "bottom_color": "#0ea5e9",
        })
        label_fmt = wb.add_format({
            "bold": True, "font_name": "Cairo", "font_size": 11,
            "bg_color": "#1e293b", "font_color": "#e2e8f0",
            "border": 1, "align": "right" if is_rtl else "left",
        })
        value_fmt = wb.add_format({
            "font_name": "Cairo", "font_size": 11, "num_format": "#,##0",
            "border": 1, "align": "center", "bg_color": "#0f172a",
            "font_color": "#0ea5e9", "bold": True,
        })

        ws_summary.set_column(0, 0, 25)
        ws_summary.set_column(1, 1, 20)
        ws_summary.write(0, 0, t("excel_summary_title", lang), summary_title_fmt)
        ws_summary.write(0, 1, "", summary_title_fmt)

        if sales_col and sales_col in df.columns:
            stats = [
                (t("excel_total_sales", lang), df[sales_col].sum()),
                (t("excel_avg_sales", lang), df[sales_col].mean()),
                (t("excel_max", lang), df[sales_col].max()),
                (t("excel_min", lang), df[sales_col].min()),
                (t("excel_records", lang), len(df)),
                (t("excel_std", lang), df[sales_col].std()),
            ]
            for i, (label, value) in enumerate(stats, start=2):
                ws_summary.write(i, 0, label, label_fmt)
                ws_summary.write(i, 1, value, value_fmt)

            product_col = col_map.get("product")
            if product_col and product_col in df.columns:
                top = df.groupby(product_col)[sales_col].sum().sort_values(ascending=False)
                row = len(stats) + 3
                ws_summary.write(row, 0, t("excel_best_product", lang), label_fmt)
                ws_summary.write(row, 1, f"{top.index[0]}", wb.add_format({
                    "font_name": "Cairo", "font_size": 11,
                    "border": 1, "align": "center", "bold": True,
                    "font_color": "#10b981",
                }))

    output.seek(0)
    return output
