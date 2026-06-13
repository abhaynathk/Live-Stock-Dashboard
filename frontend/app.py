import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# Configuration
# -----------------------------
API = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Stock AI Agent",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock AI Agent")
st.markdown("Analyze live stock prices using FastAPI + Yahoo Finance")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Stock Search")

symbol = st.sidebar.text_input(
    "Enter Stock Symbol",
    value="AAPL"
).upper()

analyze = st.sidebar.button("Analyze Stock")


# -----------------------------
# Main Logic
# -----------------------------
if analyze:

    with st.spinner("Fetching stock data..."):

        # -------------------------
        # Get Current Stock Data
        # -------------------------
        try:
            response = requests.get(f"{API}/stock/{symbol}", timeout=10)

            if response.status_code == 200:
                stock = response.json()

            else:
                st.error(f"❌ API Error ({response.status_code})")
                st.json(response.json())
                st.stop()

        except requests.exceptions.ConnectionError:
            st.error(
                "❌ Cannot connect to FastAPI backend.\n\n"
                "Please make sure FastAPI is running:\n\n"
                "```bash\n"
                "uvicorn backend.app:app --reload\n"
                "```"
            )
            st.stop()

        except requests.exceptions.Timeout:
            st.error("Request timed out.")
            st.stop()

        except Exception as e:
            st.error(str(e))
            st.stop()

        # -------------------------
        # Get Historical Data
        # -------------------------
        try:

            history_response = requests.get(
                f"{API}/history/{symbol}",
                timeout=10
            )

            if history_response.status_code == 200:
                history = history_response.json()

            else:
                st.error("Unable to fetch historical data.")
                st.stop()

        except Exception as e:
            st.error(str(e))
            st.stop()

    # -----------------------------
    # Company Name
    # -----------------------------
    st.header(stock.get("company", symbol))

    # -----------------------------
    # Metrics
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Price",
        stock.get("current_price", "N/A")
    )

    col2.metric(
        "Open",
        stock.get("open", "N/A")
    )

    col3.metric(
        "Previous Close",
        stock.get("previous_close", "N/A")
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Day High",
        stock.get("day_high", "N/A")
    )

    col5.metric(
        "Day Low",
        stock.get("day_low", "N/A")
    )

    col6.metric(
        "Volume",
        f"{stock.get('volume', 0):,}"
        if stock.get("volume") else "N/A"
    )

    col7, col8 = st.columns(2)

    col7.metric(
        "52 Week High",
        stock.get("fifty_two_week_high", "N/A")
    )

    col8.metric(
        "52 Week Low",
        stock.get("fifty_two_week_low", "N/A")
    )

    # -----------------------------
    # Market Cap
    # -----------------------------
    st.subheader("Market Information")

    market_cap = stock.get("market_cap")

    if market_cap:
        st.write(f"**Market Cap:** {market_cap:,}")
    else:
        st.write("Market Cap: N/A")

    # -----------------------------
    # Historical Chart
    # -----------------------------
    st.subheader("Historical Price")

    df = pd.DataFrame(history)

    if not df.empty:

        df["Date"] = pd.to_datetime(df["Date"])

        fig = go.Figure()

        fig.add_trace(
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name="Price"
            )
        )

        fig.update_layout(
            height=650,
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.warning("No historical data available.")

    # -----------------------------
    # Raw JSON (Debug)
    # -----------------------------
    with st.expander("View API Response"):
        st.json(stock)