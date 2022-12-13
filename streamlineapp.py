#Import the required Libraries
import json
import streamlit as st
import pickle
import pandas as pd
import base64

scaler1 = pickle.load(open('scaler1.pkl','rb'))


#function to load data
""" def load_data():
    data = pd.read_csv("model_data.csv")
    #data1 = pd.read_csv()
    return data """

#data = load_data()

features = ['store_nbr','city','state','cluster','family','onpromotion','day_of_month','year','month','week_of_year','week_of_year','day_of_week','day_of_year','quarter']

# load the model
@st.cache(persist=True,allow_output_mutation=True)
def load_model():
   with open('decision_tree.pkl','rb') as file:
      RF_model = pickle.load(file)
      return RF_model


#function to load encoder
def load_label_encoder():
   with open("encoder.pkl", 'rb') as file:
      encoder = pickle.load(file) 
      return encoder

label_encoder = load_label_encoder()
model = load_model()

# seprate features and target
""" selected_features = data[features]
target = data['sales'] """

#add background image to th app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image1.jpg')    
# Add a title and intro text
st.title('Store Sales Forcasting')
st.text( 'This is a web app for the forcasting of store sales')
st.markdown('Select your features and click on Submit')

#Form to collect user input
form = st.form(key="information", clear_on_submit=True)

with form:

    cols = st.columns((1, 1))
    date = cols[0].date_input("Enter date of Prediction")
    store_nbr = cols[1].number_input('Enter Store Number between 1 and 54')
    #type1 = cols[0].selectbox("Store Type:", ["Male", "Female", "Robot", "Other"], index=2)
    city = cols[0].selectbox("City:", ['Quito', 'Cayambe', 'Latacunga', 'Riobamba', 'Ibarra',
       'Santo Domingo', 'Guaranda', 'Puyo', 'Ambato', 'Guayaquil',
       'Salinas', 'Daule', 'Babahoyo', 'Quevedo', 'Playas', 'Libertad',
       'Cuenca', 'Loja', 'Machala', 'Esmeraldas', 'Manta', 'El Carmen'], index=0)
    state = cols[1].selectbox("State:", ['Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura',
       'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
       'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
       'El Oro', 'Esmeraldas', 'Manabi'], index=2)
    
    cluster = cols[0].number_input('Enter Cluster Number between 1 and 17')
    family = cols[1].selectbox("Product Family:", ['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS',
       'BREAD/BAKERY', 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS',
       'FROZEN FOODS', 'GROCERY I', 'GROCERY II', 'HARDWARE',
       'HOME AND KITCHEN I', 'HOME AND KITCHEN II', 'HOME APPLIANCES',
       'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE',
       'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE',
       'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY',
       'PREPARED FOODS', 'PRODUCE', 'SCHOOL AND OFFICE SUPPLIES',
       'SEAFOOD'], index=2)
    onpromotion =  st.radio("Is item on Promotion",('YES', 'NO'))
    
    cols = st.columns(2)
    
    submitted = st.form_submit_button(label="Submit")

if submitted:
    st.success("Processing!")
    date= pd.to_datetime(date)
    day_of_month = date.day
    month = date.month
    year = date.year
    week= date.isocalendar().week
    quarter = date.quarter
    #weekday =date.weekday
    quarter = date.quarter
    day_of_year = date.dayofyear
    day_of_week = date.dayofweek
    weekday = date.dayofweek
    

    X_test1= [store_nbr,cluster,day_of_month,year,month,week,weekday,day_of_week,day_of_year,quarter]
    print(X_test1)

    df_new = pd.DataFrame([X_test1],columns=[store_nbr,cluster,day_of_month,year,month,week,weekday,day_of_week,day_of_year,quarter])   
    #print(df_new)
    
    
    encoded_features= [family,city,state,onpromotion]
    encoded_features = label_encoder.fit_transform(encoded_features)
    #print(encoded_features)
    df_new1 = pd.DataFrame([encoded_features],columns=[family,city,state,onpromotion])
    X_test = pd.concat([df_new,df_new1],axis=1)
    scaler1.fit_transform(X_test)
    
    predict = model.predict(X_test)
    #print(predict)
    st.subheader("The Predicted Sales for the day " '{:%d-%m-%Y}' .format(date) )
    
    output= predict[0]
    st.success(output)
    
    st.balloons()