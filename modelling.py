import streamlit as st
import pickle
import numpy as np
from docx import Document
from streamlit_option_menu import option_menu

#_________________________________________________________________________________________________
def predict_status(country,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                   delivery_date_year):

    #change the date datatypes "string" to "int"
    item_date_day= int(item_date_day)
    item_date_month= int(item_date_month)
    item_date_year= int(item_date_year)

    delivery_date_day= int(delivery_date_day)
    delivery_date_month= int(delivery_date_month)
    delivery_date_year= int(delivery_date_year)

    #model file of the classification
    with open(r"Classification_model.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[country,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                   delivery_date_year]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0
#-----------------------------------------------------------------------------------------------------------
def predict_selling_price(country,status,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                   delivery_date_year):

    #change the date datatypes "string" to "int"
    item_date_day= int(item_date_day)
    item_date_month= int(item_date_month)
    item_date_year= int(item_date_year)

    delivery_date_day= int(delivery_date_day)
    delivery_date_month= int(delivery_date_month)
    delivery_date_year= int(delivery_date_year)

    #modelfile of the classification
    with open(r"Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[country,status,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                   delivery_date_year]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred

#_____________________________________________STREAMLIT____________________________________________________

st.set_page_config(page_title="Industrial Copper Modeling", 
                   layout="wide")

st.markdown("<h1 style='font-size: 50px; text-align: Center;'>Industrial Copper Modeling ft. Machine Learning</h1>", unsafe_allow_html=True)

SELECT = option_menu(
    menu_title = None,
    options = ["ABOUT","SELLING PRICE PREDICTION","STATUS DETECTION"],
    orientation="horizontal",
    icons=("book","cash","trophy"),
    styles=("font-size"== "15px",
        "text-align"== "center")
    )

if SELECT=="ABOUT":
    with open("about.txt", "r") as file:
        file_contents = file.read()
    file_contents
    

if SELECT == "STATUS DETECTION":

    st.header("PREDICT STATUS (Won / Lose)")
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.322, Max:6.924",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015",format="%0.15f")
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154",format="%0.15f")
    
    with col2:
        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button("PREDICT THE STATUS",use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,delivery_date_year)
        
        if status == 1:
            st.write("### :green[**The Status is WON**]")
            st.balloons()
        else:
            st.write("### :red[**The Status is LOSE**]")

if SELECT == "SELLING PRICE PREDICTION":

    st.header("**PREDICTING SELLING PRICE**")
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        status= st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137",format="%0.15f")
        
    
    with col2:
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button("PREDICT THE SELLING PRICE",use_container_width=True)

    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,
                   quantity_tons_log,customer_log,thickness_log,item_date_day,
                   item_date_month,item_date_year,delivery_date_day,delivery_date_month,delivery_date_year)
        
        
        st.write("### :green[**The Selling Price is :**]",price)
        st.balloons()



st.markdown("---")
st.markdown("Created by: Kamayani 👩‍💻")