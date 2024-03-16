import joblib
import numpy as np
import streamlit as st
import wget


model_name = "RF_Loan_model.joblib"
file_url_alternative = "https://github.com/mevlutkoz/Streamlit/blob/main/RF_Loan_model.joblib"
file_url = "https://raw.githubusercontent.com/mevlutkoz/Streamlit/RF_Loan_model.joblib"
wget.download(file_url_alternative)
model = joblib.load(model_name)


def prediction(Gender,Married,Dependents,
         Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
         LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        if Married == "Yes":
            Married = 1
        else:
            Married = 0

        if Education == "Graduate":
            Education = 0
        else:
            Education = 1
        
        if Self_Employed == "Yes":
            Self_Employed = 1
        else:
            Self_Employed = 0

        if Credit_History == "Outstanding Loan":
            Credit_History = 1
        else:
            Credit_History = 0   
        
        if Property_Area == "Rural":
            Property_Area = 0
        elif Property_Area == "Semi Urban":
            Property_Area = 1  
        else:
            Property_Area = 2  
        Total_Income =    np.log(ApplicantIncome + CoapplicantIncome)

        prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed,LoanAmount, Loan_Amount_Term, Credit_History, Property_Area,Total_Income]])
        print(print(prediction))

        if prediction==0:
            pred = "Rejected"

        else:
            pred = "Approved"
        return pred      


def main():
    # This is Front-End of the website

    st.title("Welcome to Loan Prediction App")
    st.header("You need to provide required information below for prediction")

    Gender = st.selectbox("Gender",("Male","Female"))
    Married = st.selectbox("Married", ("Yes","No"))
    Dependents = st.number_inputs("Dependents")
    Education = st.selectbox("Education", ("Graduate","Not Graduate"))
    Self_Employed = st.selectbox("Self Employed", ("Yes","Noe"))
    ApplicantIncome = st.number_input("Income")
    CoapplicantIncome = st.number_input("Coapplicant Income")
    LoanAmount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("LoanAmount")
    Credit_History = st.selectbox("Credit History",("Outstanding Loan", "No Outstanding Loan"))
    Property_Area = st.selectbox("Property Area", ("Rural", "Urban", "Semi Urban"))

    if st.button("Predict"):
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)

        if result == "Approved":
            st.success("Your Loan Application is Approved")
        else:
            st.error("Fukara piç")
        
if __name__ == "__name__":
    main()


