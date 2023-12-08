import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('D:/Christ University/Internship/project-eisystem/trained_model.sav', 'rb'))



def loan_prediction(input_data):
    

    
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):

      return 'Loan not approved'
    else:
      return 'Loan approved'
  
    
  
def main():
    
   
    st.title('Loan Status Prediction Web App')
    
    
    Gender = st.text_input('Gender(Male:1,Female:0)')
    Married  = st.text_input('Married(No:0,Yes:1)')
    Dependents = st.text_input('Dependents')
    Education = st.text_input('Education(Graduate:1,Not Graduate:0)')
    Self_Employed = st.text_input('Self_Employed(No:0,Yes:1)')
    ApplicantIncome  = st.text_input('ApplicantIncome')
    CoapplicantIncome  = st.text_input('CoapplicantIncome')
    LoanAmount = st.text_input('LoanAmount')
    Loan_Amount_Term = st.text_input('Loan_Amount_Term')
    Credit_History  = st.text_input('Credit_History')
    Property_Area = st.text_input('Property_Area(Rural:0,Semiurban:1,Urban:2)')
    
   
    status = ''
    
    
    if st.button('Loan Status'):
        status = loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area ])
        
        
    st.success(status)
    
    
     
    
if __name__ == '__main__':
    main()