import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

combined_df = pd.read_csv("../data/combined_df.csv")


combined_df["order_approved_at"] = pd.to_datetime(combined_df["order_approved_at"])
combined_df["order_purchase_timestamp"] = pd.to_datetime(combined_df["order_purchase_timestamp"])
combined_df["order_delivered_customer_date"] = pd.to_datetime(combined_df["order_delivered_customer_date"])

min_date = combined_df["order_approved_at"].min().date()
max_date = combined_df["order_approved_at"].max().date()

with st.sidebar:
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )

main_df = combined_df[
    (combined_df["order_approved_at"] >= str(start_date))
    & (combined_df["order_approved_at"] <= str(end_date))
]

st.title("Proyek Analisis Data: E-Commerce Public Dataset")
st.markdown(
    """
**Pertanyaan Bisnis:** \n
1. Produk kategori apa yang paling banyak terjual dan memberikan revenue tertinggi?
2. Bagaimana distribusi ulasan pelanggan berdasarkan rating, dan apakah ada korelasi antara rating dengan waktu pengiriman?
"""
)

st.subheader("1. Produk Kategori Paling Banyak Terjual dan Memberikan Revenue Tertinggi")

sales_per_category = main_df.groupby('product_category_name_english')['order_id'].count().reset_index()
sales_per_category.columns = ['product_category_name_english', 'total_sales']

revenue_per_category = main_df.groupby('product_category_name_english')['payment_value'].sum().reset_index()
revenue_per_category.columns = ['product_category_name_english', 'total_revenue']

plt.figure(figsize=(12, 6))
plt.bar(sales_per_category['product_category_name_english'], sales_per_category['total_sales'])
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.title('Total Sales per Product Category', fontsize=14)
plt.xticks(rotation=90)
st.pyplot(plt.gcf())

plt.figure(figsize=(12, 6))
plt.bar(revenue_per_category['product_category_name_english'], revenue_per_category['total_revenue'])
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Revenue', fontsize=12)
plt.title('Total Revenue per Product Category', fontsize=14)
plt.xticks(rotation=90)
st.pyplot(plt.gcf())

st.markdown(
    """
**Insight:** \n
- Kategori "bed_bath_table" tercatat sebagai produk paling banyak terjual, yang menunjukkan bahwa kebutuhan rumah tangga sangat populer di kalangan konsumen. Di sisi lain, kategori "health_beauty" menghasilkan revenue tertinggi, mengindikasikan bahwa produk kecantikan dan kesehatan memiliki nilai jual tinggi, meski volume penjualannya lebih rendah dibanding kategori lainnya.
"""
)

st.subheader("2. Distribusi Ulasan Pelanggan Berdasarkan Rating dan Korelasi dengan Waktu Pengiriman")

rating_distribution = main_df['review_score'].value_counts().sort_index().reset_index()
rating_distribution.columns = ['review_score', 'count']

plt.figure(figsize=(10, 6))
plt.bar(rating_distribution['review_score'], rating_distribution['count'])
plt.xlabel('Review Score')
plt.ylabel('Count')
plt.title('Distribution of Customer Reviews by Rating')
st.pyplot(plt.gcf())

main_df['delivery_time_days'] = (main_df['order_delivered_customer_date'] - main_df['order_purchase_timestamp']).dt.days

plt.figure(figsize=(12, 6))
sns.boxplot(x='review_score', y='delivery_time_days', data=main_df)
plt.xlabel('Review Score')
plt.ylabel('Delivery Time (days)')
plt.title('Delivery Time vs. Review Score')
st.pyplot(plt.gcf())

st.markdown(
    """
**Insight:** \n
- Sebagian besar ulasan pelanggan memberikan rating 5 dan 4, menunjukkan kepuasan tinggi, sementara rating 1 cukup signifikan, menandakan ketidakpuasan. Rating rendah 1 dan 2 umumnya terkait dengan waktu pengiriman yang lebih lama dan banyak keterlambatan (outlier hingga 200 hari). Sebaliknya, rating tinggi 4 dan 5 berhubungan dengan pengiriman yang lebih tepat waktu.
"""
)

st.title("Kesimpulan")
st.markdown(
    """
1. Kategori yang paling banyak terjual dan memberikan revenue tertinggi dapat diidentifikasi dari visualisasi di atas. Kategori "bed_bath_table" adalah yang paling populer, dengan jumlah penjualan tertinggi. Hal ini menunjukkan bahwa kebutuhan rumah tangga seperti peralatan tempat tidur dan kamar mandi sangat diminati oleh konsumen. Sementara itu, kategori "health_beauty" menghasilkan revenue tertinggi, meskipun volume penjualannya tidak sebesar kategori lainnya. Ini mengindikasikan bahwa produk di kategori ini memiliki harga rata-rata lebih tinggi, menjadikannya kategori yang berpotensi memberikan margin keuntungan besar.
2. Distribusi ulasan pelanggan berdasarkan rating menunjukkan bagaimana pelanggan menilai produk yang mereka beli. Korelasi antara rating dan waktu pengiriman dapat memberikan wawasan tentang bagaimana waktu pengiriman mempengaruhi kepuasan pelanggan. Mayoritas ulasan pelanggan memberikan rating 5, yang menunjukkan kepuasan tinggi secara keseluruhan. Namun, analisis hubungan antara waktu pengiriman dan rating mengungkapkan bahwa rating rendah 1 atau 2 cenderung terjadi ketika waktu pengiriman lebih lama dan banyak keterlambatan (outlier hingga 200 hari). Sebaliknya, pengiriman yang cepat berkontribusi pada rating lebih tinggi 4 atau 5 (kurang dari 50 hari).
"""
)