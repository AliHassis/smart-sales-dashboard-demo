"""
Plotly chart builder functions
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from translations import t

CHART_THEME = {
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "font": {"family": "Cairo", "color": "#94a3b8"},
    "xaxis": {"gridcolor": "#1e293b", "zerolinecolor": "#1e293b"},
    "yaxis": {"gridcolor": "#1e293b", "zerolinecolor": "#1e293b"},
    "colorway": ["#0ea5e9", "#f59e0b", "#10b981", "#f43f5e", "#8b5cf6", "#06b6d4"],
}


def create_bar_chart(data: pd.DataFrame, product_col: str, sales_col: str) -> go.Figure:
    fig = px.bar(
        data, x=product_col, y=sales_col,
        color=sales_col,
        color_continuous_scale=["#0f172a", "#0ea5e9"],
        text=sales_col,
    )
    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        marker_line_width=0,
    )
    fig.update_layout(
        **CHART_THEME,
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(t=10, b=10, l=0, r=0),
        height=300,
    )
    return fig


def create_pie_chart(data: pd.DataFrame, region_col: str, sales_col: str) -> go.Figure:
    fig = px.pie(
        data, values=sales_col, names=region_col,
        hole=0.55,
        color_discrete_sequence=["#0ea5e9", "#f59e0b", "#10b981", "#f43f5e", "#8b5cf6"],
    )
    fig.update_traces(textposition="outside", textinfo="label+percent")
    fig.update_layout(
        **CHART_THEME,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2),
        margin=dict(t=10, b=30, l=0, r=0),
        height=300,
    )
    return fig


def create_line_chart(data: pd.DataFrame, date_col: str, sales_col: str, product_col: str = None) -> go.Figure:
    if product_col and product_col in data.columns:
        fig = px.line(
            data, x=date_col, y=sales_col, color=product_col,
            markers=True,
            color_discrete_sequence=["#0ea5e9", "#f59e0b", "#10b981", "#f43f5e", "#8b5cf6"],
        )
    else:
        fig = px.line(data, x=date_col, y=sales_col, markers=True)
    fig.update_traces(line_width=2.5, marker_size=8)
    fig.update_layout(
        **CHART_THEME,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(t=10, b=10, l=0, r=0),
        height=280,
        yaxis_title=None,
        xaxis_title=None,
    )
    return fig


def create_pareto_chart(data: pd.DataFrame, product_col: str, sales_col: str, lang: str = "ar") -> go.Figure:
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=data[product_col], y=data[sales_col],
            name=t("sales_label", lang),
            marker_color="#0ea5e9",
            text=data[sales_col].apply(lambda x: f"{x:,.0f}"),
            textposition="outside",
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=data[product_col], y=data["cumulative_pct"],
            name=t("cumulative_pct", lang),
            mode="lines+markers+text",
            line=dict(color="#f59e0b", width=2.5),
            marker=dict(size=8),
            text=data["cumulative_pct"].apply(lambda x: f"{x:.0f}%"),
            textposition="top center",
            textfont=dict(color="#f59e0b", size=10),
        ),
        secondary_y=True,
    )

    fig.add_hline(
        y=80, line_dash="dash", line_color="#f43f5e",
        annotation_text="80%", annotation_position="bottom right",
        secondary_y=True,
    )

    fig.update_layout(
        **CHART_THEME,
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        margin=dict(t=10, b=10, l=0, r=0),
        height=300,
        yaxis_title=None,
    )
    fig.update_yaxes(
        title_text=None, secondary_y=False,
        gridcolor="#1e293b", zerolinecolor="#1e293b",
    )
    fig.update_yaxes(
        title_text=None, secondary_y=True,
        range=[0, 105], gridcolor="rgba(0,0,0,0)",
    )
    return fig


def create_heatmap(pivot: pd.DataFrame) -> go.Figure:
    fig = px.imshow(
        pivot,
        color_continuous_scale=[[0, "#0f172a"], [0.5, "#0ea5e9"], [1, "#f59e0b"]],
        aspect="auto",
        text_auto=True,
    )
    fig.update_layout(
        **CHART_THEME,
        margin=dict(t=10, b=10, l=0, r=0),
        height=260,
        yaxis_title=None,
        xaxis_title=None,
    )
    return fig
