import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 COVID-19 Research Analysis", layout="wide")

# Title and description
st.title("CORD-19 COVID-19 Research Analysis")
st.write("""
This app provides an interactive analysis of the CORD-19 COVID-19 research dataset.
Explore publication trends, top journals, word frequencies, and more.
""")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\etuna\OneDrive\Documents\metadata.csv')
    important_columns = ['title', 'abstract', 'publish_time', 'authors']
    df_cleaned = df.dropna(subset=important_columns).copy()
    df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
    df_cleaned['year'] = df_cleaned['publish_time'].dt.year
    df_cleaned['abstract_word_count'] = df_cleaned['abstract'].fillna('').apply(lambda x: len(x.split()))
    return df_cleaned

df = load_data()

# Show a sample of the data
st.subheader("Sample of the Data")
st.dataframe(df.head(10))

# Sidebar widgets
st.sidebar.header("Options")
year_range = st.sidebar.slider(
    "Select publication year range",
    int(df['year'].min()), int(df['year'].max()),
    (int(df['year'].min()), int(df['year'].max()))
)
top_n_journals = st.sidebar.slider("Number of top journals to show", 5, 20, 10)

# Filter data by year
df_year = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications over time
st.subheader("Number of Publications per Year")
papers_per_year = df_year['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
papers_per_year.plot(kind='line', marker='o', ax=ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
ax1.set_title("Number of Publications per Year")
st.pyplot(fig1)

# Top journals
st.subheader(f"Top {top_n_journals} Journals by Publication Count")
top_journals = df_year['journal'].value_counts().head(top_n_journals)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax2)
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
ax2.set_title(f"Top {top_n_journals} Journals")
st.pyplot(fig2)

# Word frequency in titles
st.subheader("Most Frequent Words in Titles")
all_titles = ' '.join(df_year['title'].dropna()).lower()
words = re.findall(r'\b\w+\b', all_titles)
common_words = Counter(words).most_common(20)
common_words_df = pd.DataFrame(common_words, columns=['Word', 'Frequency'])
st.dataframe(common_words_df)

# Word cloud
st.subheader("Word Cloud of Paper Titles")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Distribution by source
st.subheader("Distribution of Paper Counts by Source")
source_counts = df_year['source_x'].value_counts().head(15)
fig4, ax4 = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, palette='mako', ax=ax4)
ax4.set_xlabel("Number of Papers")
ax4.set_ylabel("Source")
ax4.set_title("Top 15 Sources")
st.pyplot(fig4)