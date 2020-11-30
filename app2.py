import streamlit as st
import pandas as pd
import numpy as np
from sklearn.externals import joblib


from matplotlib import pyplot as plt

LR = joblib.load('LR.pkl')
#predict function

def predictit(dict1):
    test1 = np.array([list(dict1.values())])
    res = LR.predict(test1)[0]
    print('预测结果:\n',res )
    if res < 0:
        res =0
    return "%.2f%%" % (res * 100)

dat = pd.read_csv("admin_data.csv")
dat.drop('Serial No.', axis = 1, inplace = True)
dat = dat.rename(columns={'Chance of Admit ': "admit rate"})

st.title('Can I get in Graduate school ?')

with st.beta_container():
    # test = st.sidebar.checkbox("test")
    Research_ex = 1 if (st.sidebar.selectbox(
        'Any research experience?',
        ['Yes', 'No']) == 'Yes') else 0
    Uni_rating = st.sidebar.selectbox(
        'University Rating ( out of 5 )?',
        [1, 2, 3, 4, 5])

    RecLetter_Strength = st.sidebar.selectbox(
        ' Letter of Recommendation Strength ( out of 5 )',
        [1, 2, 3, 4, 5])
    SOP = st.sidebar.selectbox(
        ' Statement of Purpose and Strength ( out of 5 )',
        [1, 2, 3, 4, 5])
    GRE_Score = st.sidebar.number_input("My GRE Score", format="%d", value=130,
                                        min_value=130, max_value=340)
    TOFEL_Score = st.sidebar.number_input("My TOFEL Score", format="%d", value=0,
                                        min_value=0, max_value=120)
    CGPA = st.sidebar.number_input("My CGPA Score (out of 10)", format="%f", value=0.0,
                                        min_value=0.0, max_value=10.0, step=0.1)

    # check
    # if not (Research_ex and GRE_Score and TOFEL_Score):
    #     st.warning('please complete basic info')
    dic1 = {
        "GRE_Score": GRE_Score,
        "TOFEL_Score": TOFEL_Score,
        "Uni_rating": Uni_rating,
        "SOP": SOP,
        "RecLetter_Strength": RecLetter_Strength,
        "CGPA": CGPA,
        "Research_ex" : Research_ex
    }

    #Start to predict
    if st.sidebar.button("Predict My Chance"):
        empt_list = [k for k, v in dic1.items() if v == None]
        if empt_list:
            for item in empt_list:
                st.sidebar.warning(f"Please fill in {item}")
        else:
            res = predictit(dic1)
            st.sidebar.write(f"Your have {res} of chance to be admitted!")




with st.beta_container():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        x_axis = st.selectbox("##x axis", dat.columns)
    with col2:
        col2.write("vs")
    with col3:
        y_axis = st.selectbox("y axis", dat.columns)
    st.write(f"selected x {x_axis} and y {y_axis}")


    fig, ax = plt.subplots()
    ax.scatter(dat[x_axis],dat[y_axis])
    st.pyplot(fig)


    # fig = plt.scatter(dat[x_axis],dat[y_axis])
    # st.pyplot(fig)

