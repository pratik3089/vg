from pathlib import WindowsPath
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# # Basic Page Configurations to to make GUI a little better
st.set_page_config(page_title="Video Game Sales Data",
                   page_icon="bar_chart",
                   layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# Adding Header
st.title("Video Games Sales Dashboard")
st.image("tp.png")

# Adding Side bar along with width and height field for some plots
st.sidebar.header('Interactive Dashboard `version 3.12`')


st.sidebar.write(
    "change height and width of the last plot")
width = st.sidebar.slider("Width", min_value=6, max_value=20, value=10)
height = st.sidebar.slider("Height", min_value=1, max_value=10, value=3)


# Loading data and removing null values
data = pd.read_csv("C:\\Users\\pbarv\\OneDrive\\Desktop\\wsup\\vgsales.csv")
data = data.dropna()  # dropping null values

st.markdown('##')

# # 1 Some Basic information about data like total number of entries
st.subheader('METRICS:')
c0, c1, c2, c3 = st.columns(4)  # creating 4 containers for metrics
c0.metric("Total Videogames", len(data))
c1.metric("Total Genre", len(data['Genre'].unique()))
c2.metric("Total Publishers", len(data['Publisher'].unique()))
c3.metric("Total Platforms", len(data['Platform'].unique()))

st.markdown('##')

# # 2 Checkbox to show dataset
st.subheader('DATA_INFO')
if st.checkbox("Show Data"):
    st.write(data)

# # 3 Total data data distribution according to Platform or Genre accornding to the selection
op = st.selectbox("Select one of the following", ["Platform", "Genre"])
st.subheader(op + " wise data distribution")
st.bar_chart(data[op].value_counts(), height=400, use_container_width=True)

# # 4  Videogames Sales Data by years
# figsize is used to change the width and height of plots
fig, ax = plt.subplots(figsize=(width, height))
st.subheader("Salesdata by Year")
op1 = st.multiselect(
    "Select Sales Category", ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"], default="Global_Sales")
group1 = data.groupby('Year').sum()  # Grouping the data by Years
ax.plot(group1[op1], label=op1)
ax.set_xlabel("Years")
ax.set_ylabel("Sales in Million")
ax.legend()
st.pyplot(fig)

st.markdown('##')

# # 5 PieCharts of various SalesData record
left, right = st.columns(2)  # creating 2 container/columns for Piecharts

# # 5.1 PieChart of Salesdata by region
left.subheader("SalesData by Region")
lst = []
plt.figure(2)  # assigning figure number to plot for using in later
for i in data.columns[6:-1]:
    # Calculting total sales data of region and appending it into list
    lst.append(sum(data[i]))

mylabels = data.columns[6:-1]
plt.pie(lst, labels=mylabels, autopct='%1.1f%%')
plt.legend()
plt.tight_layout()
left.pyplot(plt.figure(2))

st.markdown('##')

# # 5.2 Piechart of Salesdata by Genre
right.subheader("Salesdata by Genre")
plt.figure(3)
group1 = data.groupby('Genre').sum()  # Grouping data by Genre
mlabels = data["Genre"].unique()
plt.pie(group1["Global_Sales"], labels=mlabels, autopct='%1.1f%%')
plt.legend()
plt.tight_layout()
right.pyplot(plt.figure(3))

st.markdown('##')

# # 6 Genre wise Average Sales
st.subheader("Genre wise average Sales")
cols = list(data.columns[6:])
op3 = st.multiselect(
    "Select Region ", data.columns[6:], default=cols)
# Grouping data by Genre by using method of mean
result = data.groupby(['Genre']).mean()
st.bar_chart(result[op3], height=350, use_container_width=True)







