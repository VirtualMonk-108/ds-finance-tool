# Import required libraries
import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

# Function to download data as an excel file
# def get_table_download_link(df):
#     towrite = io.BytesIO()
#     downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
#     towrite.seek(0)
#     b64 = base64.b64encode(towrite.read()).decode()
#     return f'<a href="data:application/octet-stream;base64,{b64}" download="results.xlsx">Download results as Excel</a>'

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
    # Bar Graph for Income vs Total Expenditure
    total_expenditure_per_sale = product_cost + shipping_cost + marketing_spend_per_sale + other_costs
    values = [selling_price, total_expenditure_per_sale]
    labels = ['Income', 'Expenditure']
    fig, ax = plt.subplots(figsize=(8,6))

    # Plotting the bars
    ax.bar(labels, values, color=['green', 'red'])

    # Labeling and displaying the graph
    ax.set_title('Income vs Total Expenditure per Sale')
    ax.set_ylabel('Amount ($)')
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
    
    # # Download results as excel file
    # st.markdown(get_table_download_link(df), unsafe_allow_html=True)
# Enhancement 2
# Enhancement 6
# Enhancement 10
# Enhancement 14
# Enhancement 2025-01-01-1
# Enhancement 2025-01-01-4
# Enhancement 2025-01-03-1
# Enhancement 2025-01-03-3
# Enhancement 2025-01-03-4
# Enhancement 2025-01-06-1
# Enhancement 2025-01-06-3
# Enhancement 2025-01-08-2
# Enhancement 2025-01-11-1
# Enhancement 2025-01-12-1
# Enhancement 2025-01-16-3
# Enhancement 2025-01-20-2
# Enhancement 2025-01-26-1
# Enhancement 2025-01-29-1
# Enhancement 2025-02-03-1
# Enhancement 2025-02-04-1
# Enhancement 2025-02-06-3
# Enhancement 2025-02-06-5
# Enhancement 2025-02-07-1
# Enhancement 2025-02-07-4
# Enhancement 2025-02-08-1
# Enhancement 2025-02-10-2
# Enhancement 2025-02-12-2
# Enhancement 2025-02-12-4
# Enhancement 2025-02-12-6
# Enhancement 2025-02-17-1
# Enhancement 2025-02-18-1
# Enhancement 2025-02-18-2
# Enhancement 2025-02-18-3
# Enhancement 2025-02-19-4
# Enhancement 2025-02-20-2
# Enhancement 2025-02-23-1
# Enhancement 2025-02-24-2
# Enhancement 2025-02-26-1
# Enhancement 2025-02-28-1
# Enhancement 2025-02-28-2
# Enhancement 2025-02-28-3
# Enhancement 2025-03-01-1
# Enhancement 2025-03-03-3
# Enhancement 2025-03-03-5
# Enhancement 2025-03-03-6
# Enhancement 2025-03-05-2
# Enhancement 2025-03-06-2
# Enhancement 2025-03-09-2
# Enhancement 2025-03-11-1
# Enhancement 2025-03-13-4
# Enhancement 2025-03-15-1
# Enhancement 2025-03-17-2
# Enhancement 2025-03-19-1
# Enhancement 2025-03-19-2
