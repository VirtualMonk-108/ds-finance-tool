# Import required libraries
import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

# Function to download data as an excel file
def get_table_download_link(df):
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="results.xlsx">Download results as Excel</a>'

st.title('Dropshipping Cost Analysis')

# Sidebar for user inputs
with st.sidebar:
    # Input boxes for product name and AliExpress URL
    product_name = st.text_input('Product Name', 'Enter product name here...')
    aliexpress_url = st.text_input('AliExpress URL', 'Enter URL here...')
    
    # Sliders for other inputs
    product_cost = st.slider('Product Cost', 0.0, 50.0, 10.0, 0.5)
    shipping_cost = st.slider('Shipping Cost', 0.0, 50.0, 5.0, 0.5)
    facebook_marketing = st.slider('Facebook Marketing Spend (Total)', 0.0, 1000.0, 100.0, 10.0)
    tiktok_marketing = st.slider('TikTok Marketing Spend (Total)', 0.0, 1000.0, 100.0, 10.0)
    google_ads_marketing = st.slider('Google Ads Marketing Spend (Total)', 0.0, 1000.0, 100.0, 10.0)
    other_costs = st.slider('Other Costs per Sale', 0.0, 50.0, 2.0, 0.5)
    selling_price = st.slider('Selling Price', 10.0, 100.0, 30.0, 0.5)

# Calculations
total_marketing_spend = facebook_marketing + tiktok_marketing + google_ads_marketing
marketing_spend_per_sale = total_marketing_spend / (selling_price - product_cost - shipping_cost)
gross_profit = selling_price - (product_cost + shipping_cost)
net_profit = gross_profit - (marketing_spend_per_sale + other_costs)
break_even_sales = marketing_spend_per_sale / gross_profit
required_sales_for_500_profit = 500 / net_profit
required_sales_for_1000_profit = 1000 / net_profit
required_sales_for_2500_profit = 2500 / net_profit

# Split the main screen area into 1/3 and 2/3 portions for graph and results respectively.
col1, col2 = st.columns((5, 5))

# Display the line graph in the first column (left side)
with col1:
    # Line Graph for Income vs Expenditure
    expenditure_values = [product_cost, shipping_cost, marketing_spend_per_sale, other_costs]
    income_values = [selling_price] * 4
    labels = ['Product', 'Shipping', 'Marketing', 'Other']
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(labels, income_values, label='Income', color='green', marker='o')
    ax.plot(labels, expenditure_values, label='Expenditure', color='red', marker='o')
    ax.set_title('Income vs Expenditure per Sale')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    st.pyplot(fig)

# Display the results in the second column (right side)
with col2:
    st.subheader('Results')
    st.write(f'Product Name: {product_name}')
    st.write(f'AliExpress URL: {aliexpress_url}')
    st.write(f'Gross Profit per Sale: ${gross_profit:.2f}')
    st.write(f'Net Profit per Sale: ${net_profit:.2f}')
    st.write(f'Break-Even Sales: {break_even_sales:.2f} sales to break even on marketing costs')
    st.write(f'Required Sales for $500 Profit: {required_sales_for_500_profit:.0f} sales')
    st.write(f'Required Sales for $1000 Profit: {required_sales_for_1000_profit:.0f} sales')
    st.write(f'Required Sales for $2500 Profit: {required_sales_for_2500_profit:.0f} sales')

    # Create dataframe for results
    data = {
        'Product Name': [product_name],
        'AliExpress URL': [aliexpress_url],
        'Gross Profit per Sale': [gross_profit],
        'Net Profit per Sale': [net_profit],
        'Break-Even Sales': [break_even_sales],
        'Required Sales for $500 Profit': [required_sales_for_500_profit],
        'Required Sales for $1000 Profit': [required_sales_for_1000_profit],
        'Required Sales for $2500 Profit': [required_sales_for_2500_profit]
    }
    df = pd.DataFrame(data)
    
    # Download results as excel file
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
