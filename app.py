import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv')
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna('').str.split().str.len()
    return df

df = load_data()

# App UI
st.title("CORD-19 Research Papers Explorer")
st.write("Explore trends in COVID-19 scientific literature.")

# Year filter
years = sorted(df['year'].dropna().unique())
if len(years) == 0:
    st.error("No valid years found. Check data cleaning.")
else:
    selected_years = st.slider(
        "Select Year Range",
        int(min(years)),
        int(max(years)),
        (int(min(years)), int(max(years)))
    )

# Filter data
filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

# Display stats
st.write(f"### Showing {len(filtered_df)} papers from {selected_years[0]} to {selected_years[1]}")

# Visualizations
st.header("📊 Visualizations")

# 1. Publications over time (filtered)
st.subheader("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='lightcoral')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# 2. Top Journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
ax.set_xlabel("Number of Papers")
st.pyplot(fig)

# 3. Word Cloud
st.subheader("Word Cloud of Titles")
all_titles = ' '.join(filtered_df['title'].dropna().astype(str))
if all_titles.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
else:
    st.write("No titles available for word cloud.")

# 4. Show sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract']].head(10))

# Download button
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_covid_papers.csv',
    mime='text/csv'
)