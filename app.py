import streamlit as st
import pandas as pd
import  pickle




st.write("""
    ## Dragon real estate
    
    This app predicts house price predictions
    
    
""")

st.write('---')


# Header of Specify Input Parameters
st.sidebar.header('Specify Input Feature parameters')



def user_input():
    CRIM = st.sidebar.slider('CRIM', 0.006320, 88.976200, 3.701291)
    ZN = st.sidebar.slider('ZN', 0.000000,100.000000,11.209158)
    INDUS = st.sidebar.slider('INDUS', 0.460000,27.740000,11.191535)
    CHAS = st.sidebar.slider('CHAS', 0.000000,1.000000,0.069307)
    NOX = st.sidebar.slider('NOX', 0.385000,0.871000,0.556955)
    RM = st.sidebar.slider('RM', 3.561000,8.780000,6.287829)
    AGE = st.sidebar.slider('AGE', 2.900000,100.000000,69.517327)
    DIS = st.sidebar.slider('DIS', 1.129600,12.126500,3.771664)
    RAD = st.sidebar.slider('RAD', 1.000000,24.000000,9.680693)
    TAX = st.sidebar.slider('TAX', 187.000000,711.000000,411.079208)
    PTRATIO = st.sidebar.slider('PTRATIO', 12.600000,22.000000,18.449752)
    B = st.sidebar.slider('B', 0.320000,396.900000,355.956312)
    LSTAT = st.sidebar.slider('LSTAT', 1.920000,37.970000,13.017252)

    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input()



# Main Panel


Pkl_Filename = "picklefile.pkl"
with open(Pkl_Filename, 'rb') as file:
    MODEL = pickle.load(file)


#Predict the output
prediction = MODEL.predict(df)



# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')



st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')



