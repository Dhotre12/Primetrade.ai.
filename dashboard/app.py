import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="Crypto Trader Sentiment Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('processed_daily_data.csv')
        traders = pd.read_csv('processed_trader_stats.csv')

        # Ensure Date column is datetime
        df['Date'] = pd.to_datetime(df['Date'])

        return df, traders
    except:
        return pd.DataFrame(), pd.DataFrame()

daily_df, trader_df = load_data()

st.title("📊 Market Sentiment & Trader Performance")

if daily_df.empty:
    st.error("Data not found. Please export 'processed_daily_data.csv' and 'processed_trader_stats.csv' first.")

else:
    # --- Sidebar Filters ---
    st.sidebar.header("Filters")

    selected_sentiment = st.sidebar.multiselect(
        "Select Sentiment Class",
        options=daily_df['classification'].dropna().unique(),
        default=daily_df['classification'].dropna().unique()
    )

    filtered_df = daily_df[daily_df['classification'].isin(selected_sentiment)]

    # --- KPI Row ---
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total PnL", f"${filtered_df['Closed PnL'].sum():,.0f}")
    col2.metric("Avg Daily Volume", f"${filtered_df['Size USD'].mean():,.0f}")
    col3.metric("Avg Win Rate", f"{filtered_df['Daily_Win_Rate'].mean()*100:.1f}%")
    col4.metric("Days Observed", filtered_df.shape[0])

    # --- Charts ---

    # 1️⃣ Daily PnL Over Time
    st.subheader("Daily PnL vs Sentiment")

    fig_pnl = px.bar(
        filtered_df,
        x='Date',
        y='Closed PnL',
        color='classification',
        title="Daily Net PnL by Sentiment",
        color_discrete_map={
            'Extreme Fear': 'red',
            'Fear': 'orange',
            'Neutral': 'gray',
            'Greed': 'lightgreen',
            'Extreme Greed': 'green'
        }
    )

    st.plotly_chart(fig_pnl, use_container_width=True)

    # 2️⃣ Scatter: Sentiment vs Volume (FIXED)
    st.subheader("Does Fear Drive Volume?")

    fig_vol = px.scatter(
        filtered_df,
        x='value',
        y='Size USD',
        size='Size USD',   # ✅ FIXED (was 'Trade Count')
        color='classification',
        hover_data=['Date', 'Closed PnL'],
        title="Sentiment Index vs. Trading Volume"
    )

    st.plotly_chart(fig_vol, use_container_width=True)

    # 3️⃣ Cumulative PnL Trend
    st.subheader("Cumulative PnL Over Time")

    fig_cum = px.line(
        filtered_df,
        x='Date',
        y='Cumulative_PnL',
        title="Cumulative Strategy Performance"
    )

    st.plotly_chart(fig_cum, use_container_width=True)

    # 4️⃣ Trader Segments (if available)
    if not trader_df.empty:
        st.subheader("Trader Archetypes")

        fig_trader = px.scatter(
            trader_df,
            x='Total_Trades',
            y='Win_Rate',
            size='Avg_Size',
            color='Segment_Performance',
            log_x=True,
            title="Trader Frequency vs Win Rate"
        )

        st.plotly_chart(fig_trader, use_container_width=True)

st.markdown("---")
st.markdown("Built for Data Analysis Assignment")