"""
Sales data analysis — DEMO version (simplified / hardcoded results)
"""

import pandas as pd
from translations import t


def compute_kpis(df: pd.DataFrame, sales_col: str) -> dict:
    """Compute basic KPI metrics (demo — simple calculations only)."""
    if sales_col not in df.columns:
        return {}
    s = df[sales_col]
    return {
        "total": s.sum(),
        "avg": s.mean(),
        "max": s.max(),
        "min": s.min(),
        "median": s.median(),
        "count": len(df),
        "std": 0.0,
    }


def build_summary(df: pd.DataFrame, col_map: dict, lang: str = "ar") -> str:
    """Build a basic text summary (demo — limited detail)."""
    lines = [t("summary_records", lang, n=len(df))]

    s_col = col_map.get("sales")
    if s_col and s_col in df.columns:
        s = df[s_col]
        lines.append(t("summary_total", lang, v=f"{s.sum():,.0f}"))
        lines.append(t("summary_avg", lang, v=f"{s.mean():,.0f}"))

    return "\n".join(lines)


def compute_product_sales(df: pd.DataFrame, product_col: str, sales_col: str) -> pd.DataFrame:
    """Aggregate sales by product (demo)."""
    return (
        df.groupby(product_col)[sales_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def compute_region_sales(df: pd.DataFrame, region_col: str, sales_col: str) -> pd.DataFrame:
    """Aggregate sales by region (demo)."""
    return df.groupby(region_col)[sales_col].sum().reset_index()


def compute_trend(df: pd.DataFrame, date_col: str, sales_col: str, product_col: str = None) -> pd.DataFrame:
    """Compute sales trend (demo — no product breakdown)."""
    return df.groupby(date_col)[sales_col].sum().reset_index()


def compute_pareto(df: pd.DataFrame, product_col: str, sales_col: str) -> pd.DataFrame:
    """Compute Pareto data (demo)."""
    pareto = (
        df.groupby(product_col)[sales_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    pareto["cumulative_pct"] = (pareto[sales_col].cumsum() / pareto[sales_col].sum() * 100).round(1)
    return pareto


def compute_heatmap_pivot(df: pd.DataFrame, product_col: str, region_col: str, sales_col: str) -> pd.DataFrame:
    """Create pivot table for heatmap (demo)."""
    return df.pivot_table(
        index=product_col, columns=region_col, values=sales_col,
        aggfunc="sum", fill_value=0,
    )


def compute_statistics(df: pd.DataFrame, sales_col: str, lang: str = "ar") -> pd.DataFrame:
    """Compute descriptive statistics (demo — basic only)."""
    if sales_col not in df.columns:
        return pd.DataFrame()
    desc = df[sales_col].describe()
    indicators = [
        t("stat_count", lang), t("stat_mean", lang),
        t("stat_min", lang), t("stat_max", lang),
    ]
    values = [
        f"{desc['count']:.0f}", f"{desc['mean']:,.2f}",
        f"{desc['min']:,.2f}", f"{desc['max']:,.2f}",
    ]
    return pd.DataFrame({
        t("stat_indicator", lang): indicators,
        t("stat_value", lang): values,
    })
