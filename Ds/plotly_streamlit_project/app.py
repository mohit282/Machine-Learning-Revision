import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('D:\VS CODE\ML\Revision\plotly_streamlit_project\Indian_census.csv')

states = list(df['State'].unique())
states.insert(0,'Overall India')

columns = sorted(df.columns[5:])

st.sidebar.title('India Visualiztion')
selected_state = st.sidebar.selectbox('Select your choice',states)

primary = st.sidebar.selectbox('Select primary Parameters',columns)
seconday = st.sidebar.selectbox('Select secondary Parameters',columns)

plot = st.sidebar.button('Plot Graph')

if plot:
    
    if selected_state == 'Overall India':
        pass
    
    else:
        df = df[df['State'] == selected_state]
    
    fig = px.scatter_mapbox(data_frame=df,lat='Latitude',lon='Longitude',size=primary,color=seconday, zoom=4,mapbox_style='open-street-map',width=1000,height=700,hover_name='District')
    st.plotly_chart(fig,use_container_width=True)
    

