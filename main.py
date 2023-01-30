import streamlit as st

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)
st.text('🎈Streamlit 프로토타입 만들기')
st.title('📌Title을 입력하세요.')
import pandas as pd

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)
st.dataframe(df_stocks)

symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

#symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
#st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)


st.line_chart(df_index, x='Date')

df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()

for symbol in df_stocks['Symbol'].unique():
	df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)

st.line_chart(df_chart, x='Date')


symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
symbol_list.insert(0, 'Date')

st.line_chart(df_chart[symbol_list], x='Date')

import datetime

st.write('검색 기간을 설정해 주세요.')
start_day = st.date_input( '시작 일자', datetime.date(2022, 1, 1))

end_day = st.date_input(
	 '종료 일자',
	 datetime.date(2022, 12, 31))

st.write(f'검색 기간 : {start_day} ~ {end_day}')
st.line_chart(df_index[(df_index['Date'] >= str(start_day)) & (df_index['Date'] <= str(end_day))], x='Date')