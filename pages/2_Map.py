import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Maps",
    layout="wide"
)


# =========================
# TITLE
# =========================

st.title("Maps")


# =========================
# LOAD DATA
# =========================

df = pd.read_excel("Data.xlsx")


# =========================
# CREATE MAP
# =========================

m = folium.Map(
    location=[-2.5, 118],
    zoom_start=5,
    tiles="CartoDB dark_matter"
)


# =========================
# ADD MARKERS
# =========================

for _, row in df.iterrows():

    popup_html = f"""
    <div style="
        width: 240px;
        font-family: Arial, sans-serif;
        color: #222;
    ">

        <div style="
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 4px;
        ">
            {row['Kota']}
        </div>

        <div style="
            font-size: 12px;
            color: #777;
            margin-bottom: 15px;
        ">
            Indonesia
        </div>

        <div style="
            display: flex;
            gap: 8px;
            margin-bottom: 12px;
        ">

            <div style="
                flex: 1;
                background: #f3f4f6;
                padding: 10px;
                border-radius: 8px;
            ">
                <div style="
                    font-size: 11px;
                    color: #777;
                ">
                    IXP
                </div>

                <div style="
                    font-size: 20px;
                    font-weight: 700;
                ">
                    {row['IXP']}
                </div>
            </div>

            <div style="
                flex: 1;
                background: #f3f4f6;
                padding: 10px;
                border-radius: 8px;
            ">
                <div style="
                    font-size: 11px;
                    color: #777;
                ">
                    Data Center
                </div>

                <div style="
                    font-size: 20px;
                    font-weight: 700;
                ">
                    {row['Data Center']}
                </div>
            </div>

        </div>

        <div style="
            background: #f3f4f6;
            padding: 10px;
            border-radius: 8px;
        ">
            <div style="
                font-size: 11px;
                color: #777;
            ">
                Landing Point
            </div>

            <div style="
                font-size: 20px;
                font-weight: 700;
            ">
                {row['Landing Point']}
            </div>
        </div>

    </div>
    """

    folium.CircleMarker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],
        radius=8,
        tooltip=row["Kota"],
        popup=folium.Popup(
            popup_html,
            max_width=300
        ),
        fill=True,
        fill_opacity=0.9
    ).add_to(m)


# =========================
# MAP HEIGHT
# =========================

st.markdown(
    """
    <style>
        iframe {
            height: calc(100vh - 150px) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# DISPLAY MAP
# =========================

st_folium(
    m,
    use_container_width=True
)

st.markdown(
    """
    <style>
        [data-testid="stMainBlockContainer"] {
            padding-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)