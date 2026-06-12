"""
Bilingual translation dictionary (Arabic / English)
"""

TRANSLATIONS = {
    # ── Page config ──
    "page_title": {
        "ar": "لوحة تحكم المبيعات الذكية",
        "en": "Smart Sales Dashboard",
    },

    # ── Sidebar ──
    "settings": {
        "ar": "⚙️ الإعدادات",
        "en": "⚙️ Settings",
    },
    "upload_data": {
        "ar": "📂 رفع البيانات",
        "en": "📂 Upload Data",
    },
    "choose_file": {
        "ar": "اختر ملف Excel أو CSV",
        "en": "Choose Excel or CSV file",
    },
    "file_help": {
        "ar": "ارفع ملف يحتوي على بيانات المبيعات",
        "en": "Upload a file containing sales data",
    },
    "display_options": {
        "ar": "🎛️ خيارات العرض",
        "en": "🎛️ Display Options",
    },
    "show_raw_data": {
        "ar": "📋 عرض البيانات الخام",
        "en": "📋 Show Raw Data",
    },
    "show_ai_insights": {
        "ar": "🤖 تحليل الذكاء الاصطناعي",
        "en": "🤖 AI Analysis",
    },
    "show_heatmap": {
        "ar": "🔥 خريطة الحرارة",
        "en": "🔥 Heatmap",
    },
    "ai_settings": {
        "ar": "🔑 إعدادات الذكاء الاصطناعي",
        "en": "🔑 AI Settings",
    },
    "api_key_label": {
        "ar": "مفتاح Claude API",
        "en": "Claude API Key",
    },
    "last_update": {
        "ar": "آخر تحديث",
        "en": "Last update",
    },
    "records_loaded": {
        "ar": "✅ تم تحميل {n} سجل",
        "en": "✅ {n} records loaded",
    },
    "language_label": {
        "ar": "🌐 اللغة / Language",
        "en": "🌐 Language / اللغة",
    },

    # ── Main header ──
    "main_title": {
        "ar": "📊 لوحة تحكم المبيعات الذكية",
        "en": "📊 Smart Sales Dashboard",
    },
    "demo_notice": {
        "ar": "📌 يعرض التطبيق بيانات تجريبية — ارفع ملفك من الشريط الجانبي",
        "en": "📌 Showing demo data — upload your file from the sidebar",
    },
    "source_label": {
        "ar": "📁 المصدر",
        "en": "📁 Source",
    },
    "demo_data": {
        "ar": "بيانات تجريبية",
        "en": "Demo data",
    },
    "total_records": {
        "ar": "📊 إجمالي السجلات",
        "en": "📊 Total Records",
    },

    # ── Filters ──
    "filter_product": {
        "ar": "🏷️ المنتج",
        "en": "🏷️ Product",
    },
    "filter_region": {
        "ar": "🗺️ المنطقة",
        "en": "🗺️ Region",
    },
    "filter_period": {
        "ar": "📅 الفترة",
        "en": "📅 Period",
    },
    "filter_sales_range": {
        "ar": "💰 نطاق المبيعات",
        "en": "💰 Sales Range",
    },
    "all": {
        "ar": "الكل",
        "en": "All",
    },
    "sales_value": {
        "ar": "💰 المبيعات: {v}",
        "en": "💰 Sales: {v}",
    },
    "no_results": {
        "ar": "🔍 لا توجد نتائج مطابقة للفلاتر المحددة",
        "en": "🔍 No results match the selected filters",
    },
    "no_results_hint": {
        "ar": "جرّب تغيير الفلاتر أعلاه للحصول على نتائج",
        "en": "Try changing the filters above to get results",
    },

    # ── KPI Cards ──
    "kpi_total_sales": {
        "ar": "💰 إجمالي المبيعات",
        "en": "💰 Total Sales",
    },
    "kpi_records": {
        "ar": "📦 عدد السجلات",
        "en": "📦 Records Count",
    },
    "kpi_avg_sales": {
        "ar": "📈 متوسط المبيعات",
        "en": "📈 Average Sales",
    },
    "kpi_median": {
        "ar": "📊 الوسيط",
        "en": "📊 Median",
    },
    "kpi_max": {
        "ar": "🏆 أعلى قيمة",
        "en": "🏆 Highest Value",
    },
    "currency": {
        "ar": "ريال",
        "en": "SAR",
    },
    "per_record": {
        "ar": "لكل سجل",
        "en": "per record",
    },
    "median_value": {
        "ar": "القيمة الوسطى",
        "en": "median value",
    },
    "best_performance": {
        "ar": "أفضل أداء",
        "en": "best performance",
    },
    "deal_record": {
        "ar": "صفقة / سجل",
        "en": "deal / record",
    },
    "pct_of_total": {
        "ar": "{pct:.1f}% من الإجمالي",
        "en": "{pct:.1f}% of total",
    },

    # ── Charts ──
    "chart_by_product": {
        "ar": "📦 المبيعات حسب المنتج",
        "en": "📦 Sales by Product",
    },
    "chart_by_region": {
        "ar": "🗺️ توزيع المناطق",
        "en": "🗺️ Region Distribution",
    },
    "chart_trend": {
        "ar": "📅 النمو عبر الزمن",
        "en": "📅 Growth Over Time",
    },
    "chart_pareto": {
        "ar": "📊 تحليل باريتو (80/20) — أهم المنتجات",
        "en": "📊 Pareto Analysis (80/20) — Top Products",
    },
    "chart_heatmap": {
        "ar": "🔥 خريطة الحرارة: المنتج × المنطقة",
        "en": "🔥 Heatmap: Product × Region",
    },
    "select_product_sales": {
        "ar": "يرجى تحديد عمود المنتج والمبيعات",
        "en": "Please select the product and sales columns",
    },
    "no_region_col": {
        "ar": "لا يوجد عمود منطقة",
        "en": "No region column found",
    },
    "sales_label": {
        "ar": "المبيعات",
        "en": "Sales",
    },
    "cumulative_pct": {
        "ar": "النسبة التراكمية %",
        "en": "Cumulative %",
    },

    # ── Data table ──
    "data_table_title": {
        "ar": "📋 جدول البيانات التفصيلي",
        "en": "📋 Detailed Data Table",
    },
    "tab_filtered": {
        "ar": "📄 البيانات المفلترة",
        "en": "📄 Filtered Data",
    },
    "tab_stats": {
        "ar": "📊 ملخص إحصائي",
        "en": "📊 Statistical Summary",
    },
    "download_csv": {
        "ar": "⬇️ تحميل CSV",
        "en": "⬇️ Download CSV",
    },
    "download_excel": {
        "ar": "⬇️ تحميل Excel احترافي",
        "en": "⬇️ Download Professional Excel",
    },
    "stat_count": {"ar": "العدد", "en": "Count"},
    "stat_mean": {"ar": "المتوسط", "en": "Mean"},
    "stat_std": {"ar": "الانحراف المعياري", "en": "Std Dev"},
    "stat_min": {"ar": "الأدنى", "en": "Min"},
    "stat_25": {"ar": "25%", "en": "25%"},
    "stat_median": {"ar": "الوسيط", "en": "Median"},
    "stat_75": {"ar": "75%", "en": "75%"},
    "stat_max": {"ar": "الأعلى", "en": "Max"},
    "stat_indicator": {"ar": "المؤشر", "en": "Indicator"},
    "stat_value": {"ar": "القيمة", "en": "Value"},

    # ── AI Section ──
    "ai_title": {
        "ar": "🤖 تحليل الذكاء الاصطناعي",
        "en": "🤖 AI Analysis",
    },
    "data_summary_label": {
        "ar": "📊 ملخص البيانات الحالية:",
        "en": "📊 Current Data Summary:",
    },
    "analyze_btn": {
        "ar": "🔍 حلّل بالذكاء الاصطناعي",
        "en": "🔍 Analyze with AI",
    },
    "api_key_warning": {
        "ar": "⚠️ يرجى إدخال مفتاح Claude API من الشريط الجانبي",
        "en": "⚠️ Please enter your Claude API key in the sidebar",
    },
    "analyzing": {
        "ar": "🤖 جارٍ التحليل...",
        "en": "🤖 Analyzing...",
    },
    "err_invalid_key": {
        "ar": "❌ مفتاح API غير صالح — تحقق من المفتاح وأعد المحاولة",
        "en": "❌ Invalid API key — check your key and try again",
    },
    "err_rate_limit": {
        "ar": "⏳ تم تجاوز حد الطلبات — انتظر قليلاً وأعد المحاولة",
        "en": "⏳ Rate limit exceeded — wait a moment and try again",
    },
    "err_connection": {
        "ar": "🌐 خطأ في الاتصال — تحقق من اتصال الإنترنت",
        "en": "🌐 Connection error — check your internet connection",
    },
    "err_unexpected": {
        "ar": "❌ خطأ غير متوقع: {e}",
        "en": "❌ Unexpected error: {e}",
    },

    # ── AI Prompt ──
    "ai_prompt": {
        "ar": (
            "أنت محلل بيانات خبير. حلل بيانات المبيعات التالية وأعطني:\n"
            "1. أهم 3 ملاحظات (insights)\n"
            "2. نقاط القوة والضعف\n"
            "3. توصيات عملية لتحسين المبيعات\n"
            "4. أي أنماط أو اتجاهات ملحوظة\n\n"
            "البيانات:\n{data}"
        ),
        "en": (
            "You are an expert data analyst. Analyze the following sales data and provide:\n"
            "1. Top 3 insights\n"
            "2. Strengths and weaknesses\n"
            "3. Actionable recommendations to improve sales\n"
            "4. Any notable patterns or trends\n\n"
            "Data:\n{data}"
        ),
    },

    # ── Summary builder ──
    "summary_records": {"ar": "عدد السجلات: {n}", "en": "Records: {n}"},
    "summary_total": {"ar": "إجمالي المبيعات: {v}", "en": "Total sales: {v}"},
    "summary_avg": {"ar": "متوسط المبيعات: {v}", "en": "Average sales: {v}"},
    "summary_median": {"ar": "الوسيط: {v}", "en": "Median: {v}"},
    "summary_range": {
        "ar": "أعلى قيمة: {max} | أدنى قيمة: {min}",
        "en": "Max: {max} | Min: {min}",
    },
    "summary_std": {"ar": "الانحراف المعياري: {v}", "en": "Std deviation: {v}"},
    "summary_best_product": {"ar": "أفضل منتج: {name} ({v})", "en": "Best product: {name} ({v})"},
    "summary_worst_product": {"ar": "أضعف منتج: {name} ({v})", "en": "Worst product: {name} ({v})"},
    "summary_product_count": {"ar": "عدد المنتجات: {n}", "en": "Product count: {n}"},
    "summary_best_region": {"ar": "أفضل منطقة: {name} ({v})", "en": "Best region: {name} ({v})"},
    "summary_worst_region": {"ar": "أضعف منطقة: {name} ({v})", "en": "Worst region: {name} ({v})"},

    # ── Column detection manual ──
    "cols_not_detected": {
        "ar": "⚠️ لم يتم التعرف على الأعمدة تلقائياً. يرجى تحديدها:",
        "en": "⚠️ Columns not auto-detected. Please select them:",
    },
    "col_sales": {"ar": "عمود المبيعات", "en": "Sales column"},
    "col_product": {"ar": "عمود المنتج", "en": "Product column"},
    "col_region": {"ar": "عمود المنطقة", "en": "Region column"},
    "col_date": {"ar": "عمود الشهر/التاريخ", "en": "Date/Month column"},

    # ── File errors ──
    "file_read_error": {
        "ar": "❌ خطأ في قراءة الملف: {e}",
        "en": "❌ File read error: {e}",
    },
    "file_empty": {
        "ar": "الملف فارغ — لا توجد بيانات",
        "en": "File is empty — no data found",
    },

    # ── Excel report ──
    "excel_report_title": {
        "ar": "📊 تقرير المبيعات الذكي",
        "en": "📊 Smart Sales Report",
    },
    "excel_report_date": {
        "ar": "تاريخ التقرير: {d}",
        "en": "Report date: {d}",
    },
    "excel_sheet_data": {"ar": "البيانات", "en": "Data"},
    "excel_sheet_summary": {"ar": "الملخص", "en": "Summary"},
    "excel_summary_title": {"ar": "📊 ملخص الأداء", "en": "📊 Performance Summary"},
    "excel_total_sales": {"ar": "إجمالي المبيعات", "en": "Total Sales"},
    "excel_avg_sales": {"ar": "متوسط المبيعات", "en": "Average Sales"},
    "excel_max": {"ar": "أعلى قيمة", "en": "Max Value"},
    "excel_min": {"ar": "أدنى قيمة", "en": "Min Value"},
    "excel_records": {"ar": "عدد السجلات", "en": "Records Count"},
    "excel_std": {"ar": "الانحراف المعياري", "en": "Std Deviation"},
    "excel_best_product": {"ar": "🏆 أفضل منتج", "en": "🏆 Best Product"},

    # ── Footer ──
    "footer_text": {
        "ar": "Smart Sales Dashboard v4.0 — تحليل ذكي لبياناتك 📊",
        "en": "Smart Sales Dashboard v4.0 — Smart analytics for your data 📊",
    },
    "footer_powered": {
        "ar": "Powered by Streamlit + Plotly + Claude AI",
        "en": "Powered by Streamlit + Plotly + Claude AI",
    },
}


def t(key: str, lang: str = "ar", **kwargs) -> str:
    """Get translated string. Falls back to Arabic if key/lang missing."""
    entry = TRANSLATIONS.get(key, {})
    text = entry.get(lang, entry.get("ar", key))
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text
