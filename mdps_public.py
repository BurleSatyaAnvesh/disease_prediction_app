import pickle
import streamlit as st
from streamlit_option_menu import option_menu


def load_models():
    
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
    
    return diabetes_model, heart_disease_model, parkinsons_model


    
# Load models
diabetes_model, heart_disease_model, parkinsons_model = load_models()

# Boolean flag to track whether the name has been entered
name_entered = False

# Ask for user's name if not entered
if not name_entered:
    user_name = st.text_input("Please enter your name")

# Check if user_name is not empty
if user_name:
    name_entered = True
    st.write(f"Hi, {user_name}!")




# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Instructions', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Feedback','About'],
                           icons=['info', 'activity','heart','person', 'star', 'question'],
                           default_index=0)


if selected == 'Feedback':
    st.title('Feedback')
    st.write("We value your feedback! Please share your thoughts, suggestions, or any issues you encountered whidfsdfdsffdsfsle using our system.")
    st.markdown("""Please share your feedback in this mail ***satyaburle2003@gmail.com***
                feel free provide your feedback""")


    
if selected == 'Instructions':
    

    st.title('Instructions')
    st.write("Welcome to the Multiple Disease Prediction System! This website allows you to predict three different diseases: Diabetes, Heart Disease, and Parkinson's Disease. To get started, please select one of the prediction options from the sidebar.")
    
    st.header("Instructions for Multiple Disease Prediction System")
    st.markdown("""
    1. **Navigation:**
        - **Sidebar Navigation:** Use the sidebar on the left-hand side of the screen to navigate between different prediction options.
          - **Instructions:** Provides guidance on how to use the system effectively (you're currently viewing this page).
          - **About:** Information about the website and its purpose.
          - **Diabetes Prediction:** Predicts the likelihood of diabetes based on input parameters.
          - **Heart Disease Prediction:** Predicts the likelihood of heart disease based on input parameters.
          - **Parkinson's Prediction:** Predicts the likelihood of Parkinson's disease based on input parameters.

    2. **Disease Prediction:**
        - **Diabetes Prediction:**
            - **Input Parameters:** Fill in the required details such as Gender, Number of Pregnancies, Glucose Level, Blood Pressure, etc.
            - **Prediction:** Click the "Diabetes Test Result" button to see the prediction result.
            - **Outcome:** The system will display whether the person is diabetic or not, along with any related issues or precautions.
        - **Heart Disease Prediction:**
            - **Input Parameters:** Similar to diabetes prediction, provide necessary details such as Age, Gender, Cholesterol level, etc.
            - **Prediction:** Click the relevant button to see the prediction result.
            - **Outcome:** The system will indicate whether the person is likely to have heart disease and provide relevant information.
        - **Parkinson's Disease Prediction:**
            - **Input Parameters:** Input required details such as Age, Gender, Tremors, Rigidity, etc.
            - **Prediction:** Click the appropriate button to view the prediction outcome.
            - **Outcome:** The system will determine the likelihood of Parkinson's disease based on the provided information.

    3. **Interpretation:**
        - **Prediction Result:** After clicking the prediction button, the system will display the diagnosis along with any associated issues, precautions, or recommended actions.
        - **Further Action:** Depending on the prediction outcome, the system may suggest further medical consultation, lifestyle changes, or precautions.

    4. **Feedback:**
        - **Email Input:** After viewing the prediction result, you can provide your email for further communication or documentation purposes.

    5. **About:**
        - **About Section:** For additional information about the Multiple Disease Prediction System, you can refer to the "About" section provided in the sidebar.
    """)

    # Display images for diseases
    st.subheader("Diseases")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("diabetes.jpg", caption="Diabetes", use_column_width=True)
    with col2:
        st.image("heart.jpg", caption="Heart Disease", use_column_width=True)
    with col3:
        st.image("parkinsons.jpg", caption="Parkinson's Disease", use_column_width=True)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Gender', ['Male', 'Female'])

    with col1:
        if gender == 'Male':
            Pregnancies = st.text_input('Number of Pregnancies', value='0')
        else:
            Pregnancies = st.text_input('Number of Pregnancies')

        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')

    
    
    # code for Prediction
    diab_diagnosis = ''
    pregnancies = ''
    glucose = ''
    vitals = ''
    bmi = ''
    bp = ''
    ins = ''
    choles=''
    chp=''
    heartrate = ''
    vessels = ''
    precaution = ''
    full = ''
    fo1 = ''
    fo2 = ''
    fo3 = ''
    fo4 = ''
    fo5 = ''
    fo6 = ''
    fo7 = ''
    fo8 = ''
    fo9 = ''
    fo10 =''
    fo11 =''
    fo12 =''
    fo13 =''
    fo14 =''
    
    
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = '***THE PERSON IS DIABETIC***'
          st.success(diab_diagnosis)
          precaution='***ISSUES***'
          st.success(precaution)
          if (int(Pregnancies) > 3):
              pregnancies = 'Pregnancies are More than 3 '
              st.success(pregnancies)
          if (int(Glucose) > 100 or int(Glucose) < 70) :
              if (int(Glucose) > 100):
                  glucose = 'Glucose level is more'
                  st.success(glucose)
              else:
                  glucose = 'Glucose level is less'
                  st.success(glucose)
          if (int(BloodPressure) > 100 or int(BloodPressure)<60):
              if(int(BloodPressure)>100):
                  bp =  'BloodPressure is High'
                  st.success(bp)
              else:
                  bp = 'BloodPressure is Low'
                  st.success(bp)
          if (int(Age)>=18):
              if(float(BMI)<18.5):
                  bmi = 'BMI = Under weight'
                  st.success(bmi)
              elif(float(BMI) == 18.5 and float(BMI) <= 24.9):
                  bmi = 'BMI = Normal Weight '
                  st.success(bmi)
              elif( float(BMI) == 25 and float(BMI) <= 29.9):
                  bmi = 'BMI = Over Weight'
                  st.success(bmi)
              else:
                  bmi = 'BMI = Obesity'
                  st.success(bmi)
          if (int(Insulin)>200):
              ins='insulin level is not in normal range'
              st.success(ins)
          if (int(Insulin)== 0):
              ins='Insulin deficiency'
              st.success(ins)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)
          
        else:
          diab_diagnosis = '***THE PERSON IS NOT DIABETIC***'
          st.success(diab_diagnosis)
          precaution='***BUT SOME ISSUES***'
          st.success(precaution)
          if (int(Pregnancies) > 3):
              pregnancies = 'Pregnancies are More than 3'
              st.success(pregnancies)
          if (int(Glucose) > 100 or int(Glucose) < 70) :
              if (int(Glucose) > 100):
                  glucose = 'Glucose level is more1'
                  st.success(glucose)
              else:
                  glucose = 'Glucose level is less'
                  st.success(glucose)
          if (int(BloodPressure) > 100 or int(BloodPressure)<60):
              if(int(BloodPressure)>100):
                  bp =  'BloodPressure is High'
                  st.success(bp)
              else:
                  bp = 'BloodPressure is Low1'
                  st.success(bp)
          if (int(Age)>=18):
              if(float(BMI)<18.5):
                  bmi = 'BMI = Under weight'
                  st.success(bmi)
              elif(float(BMI) == 18.5 and float(BMI) <= 24.9):
                  bmi = 'BMI = Normal Weight '
                  st.success(bmi)
              elif( float(BMI) == 25 and float(BMI) <= 29.9):
                  bmi = 'BMI = Over Weight'
                  st.success(bmi)
              else:
                  bmi = 'BMI = Obesity'
                  st.success(bmi)
          if (int(Insulin)>200):
              ins='Insulin level is not in normal range'
              st.success(ins)
          if (int(Insulin)== 0):
              ins='Insulin deficiency'
              st.success(ins)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)

          vitals = '***REMAINING VITALS ARE NOT PROBLEMATIC AT PRESENT BUT TAKE CARE***'
          st.success (vitals)
        
    
    




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = '***THE PERSON IS HAVING HEART DISEASE***'
          st.success(heart_diagnosis)
          precaution='***ISSUES***'
          st.success(precaution)
          if (int(trestbps) > 100 or int(trestbps)<=60):
              if(int(trestbps)>100):
                  bp =  'BloodPressure is High'
                  st.success(bp)
              else:
                  bp = 'BloodPressure is Low'
                  st.success(bp)
          if (int(age) <= 19 or int(age) >= 20):
              if(int(age)<= 19):
                  if(int(chol)>170):
                      choles = 'Cholestrol is high'
                      st.success(choles)
              if(int(age)>=20):
                  if(int(chol)>200):
                      choles = 'Cholestrol is high'
                      st.success(choles) 
          if (int(cp)>2):
              chp = 'More chest pains recored (dangerous)'
              st.success(chp)
          if (int(thalach)>100):
              heartrate =' Heart rate is abnormal/more'
              st.success(heartrate)
          if (int(slope)<2 or int(slope)>3):
              if(int(slope)==0):
                  vessels='There is a blockage in the blood flow'
                  st.success(vessels)
              if(int(slope)>2):
                  vessels='Blood flow is less'
                  st.success(vessels)
              if(int(slope)<3):
                  vessels='Fast blood flow'
                  st.success(vessels)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)
        else:
          heart_diagnosis = '***THE PERSON DOES NOT HAVE HEART DISEASE***'
          st.success(heart_diagnosis)
          precaution='***BUT SOME ISSUES***'
          st.success(precaution)
          if (int(trestbps) > 100 or int(trestbps)<=60):
              if(int(trestbps)>100):
                  bp =  'BloodPressure is High'
                  st.success(bp)
              else:
                  bp = 'BloodPressure is Low'
                  st.success(bp)
          if (int(age) <= 19 or int(age) >= 20):
              if(int(age)<= 19):
                  if(int(chol)>170):
                      choles = 'Cholestrol is high'
                      st.success(choles)
              if(int(age)>=20):
                  if(int(chol)>200):
                      choles = 'Cholestrol is high'
                      st.success(choles) 
          if (int(cp)>2):
              chp = 'More chest pains recored (dangerous)'
              st.success(chp)
          if (int(thalach)>100):
              heartrate =' Heart rate is abnormal/more'
              st.success(heartrate)
          if (int(slope)<2 or int(slope)>3):
              if(int(slope)==0):
                  vessels='There is a blockage in the blood flow'
                  st.success(vessels)
              if(int(slope)>2):
                  vessels='Blood flow is less'
                  st.success(vessels)
              if(int(slope)<3):
                  vessels='Fast blood flow'
                  st.success(vessels)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)
          vitals = '***REMAINING VITALS ARE NOT PROBLEMATIC AT PRESENT BUT TAKE CARE***'
          st.success (vitals)
        
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP [Fo(Hz)]')
        
    with col2:
        fhi = st.text_input('MDVP [Fhi(Hz)]')
        
    with col3:
        flo = st.text_input('MDVP [Flo(Hz)]')
        
    with col4:
        Jitter_percent = st.text_input('MDVP [Jitter(%)]')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP [Jitter(Abs)]')
        
    with col1:
        RAP = st.text_input('MDVP [RAP]')
        
    with col2:
        PPQ = st.text_input('MDVP [PPQ]')
        
    with col3:
        DDP = st.text_input('Jitter [DDP]')
        
    with col4:
        Shimmer = st.text_input('MDVP [Shimmer]')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP [Shimmer(dB)]')
        
    with col1:
        APQ3 = st.text_input('Shimmer [APQ3]')
        
    with col2:
        APQ5 = st.text_input('Shimmer [APQ5]')
        
    with col3:
        APQ = st.text_input('MDVP [APQ]')
        
    with col4:
        DDA = st.text_input('Shimmer [DDA]')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "***THE PERSON HAS PARKINSON'S DISEASE***"
          st.success(parkinsons_diagnosis)
          precaution='***ISSUES***'
          st.success(precaution)
          if (float(HNR) < 28.333 or float(fhi) > 755.25 or  float(Jitter_percent) > 0.00571 or float(Jitter_Abs) > 0.00008 or float(RAP) > 0.00374 or float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ3) > 0.02185 or float(APQ5) > 0.03194 or float(APQ) > 0.01958 or float(DDA) > 0.02086 or float(NHR) > 0.02510 or float(RPDE) > 0.617 or float(DFA) > 0.818 or float(spread1) > -5.440 or float(spread2) > -4.137 or float(D2) > 3.671 or float(PPE) > 0.09221):
              full='Vocal dysfunction'
              st.success(full)
          if (float(fo) > 255.66):
              fo1='Jitter'
              st.success(fo1)
          if (float(fhi) > 755.25 or float(fhi) < 102.145):
              fo2='Vocal fold tension / Stiffness'
              st.success(fo2)
          if (float(flo) > 226.778):
              fo3='Vocal impairment, Reduced to produce low-frequency sounds'
              st.success(fo3)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(RPDE) > 0.617 or float(DDA) > 0.02086 or float(Jitter_percent) > 0.00571 or float(Jitter_Abs) > 0.00008 or float(RAP) > 0.00374 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ5) > 0.03194 or float(APQ) > 0.01958):
              fo4='Increased vocal irregularity'
              st.success(fo4)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(spread2) > -4.137 or float(spread1) > -5.440 or float(DFA) > 0.818 or float(DDA) > 0.02086 or float(fo) > 255.66 or float(APQ) > 0.01958 or float(RAP) > 0.00374 or float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ3) > 0.02185):
              fo5='Vocal Instability'
              st.success(fo5)
          if (float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(APQ3) > 0.02185 or float(APQ5) > 0.03194 or float(APQ) > 0.01958):
              fo6='Vocal petrubation'
              st.success(fo6)
          if (float(DDA) > 0.02086):
              fo7='Dysphonia'
              st.success(fo7)
          if (float(NHR) > 0.02510):
              fo8='increased levels of noise relative to harmonics in their voice'
              st.success(fo8)
          if (float(HNR) < 28.333):
              fo9='Reduced vocal clarity and potentially higher background noise levels'
              st.success(fo9)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(DFA) > 0.818 or float(RPDE) > 0.617):
              fo10='Vocal complexity'
              st.success(fo10)
          if (float(spread1) > -5.440):
              fo11='Typical vocal behaviour'
              st.success(fo11)
          if (float(fo) < 88.333):
              fo12 ='potential worsening of vocal impairment and may indicate advanced disease progression or increased severity of symptoms'
              st.success(fo12)
          if (float(fhi) < 102.145):
              fo13 ='Reduced vocal fold vibratory range'
              st.success(fo13)
          if (float(flo) < 65.476):
              fo14 ='Reduced vocal fold vibration or breathiness'
              st.success(fo14)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)
            
          
        else:
          parkinsons_diagnosis = "***THE PERSON DOES NOT HAVE PARKINSON'S DISEASE***"
          st.success(parkinsons_diagnosis)
          precaution='***BUT SOME ISSUES***'
          st.success(precaution)
          if (float(HNR) < 28.333 or float(fhi) > 755.25 or  float(Jitter_percent) > 0.00571 or float(Jitter_Abs) > 0.00008 or float(RAP) > 0.00374 or float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ3) > 0.02185 or float(APQ5) > 0.03194 or float(APQ) > 0.01958 or float(DDA) > 0.02086 or float(NHR) > 0.02510 or float(RPDE) > 0.617 or float(DFA) > 0.818 or float(spread1) > -5.440 or float(spread2) > -4.137 or float(D2) > 3.671 or float(PPE) > 0.09221):
              full='Vocal dysfunction'
              st.success(full)
          if (float(fo) > 255.66):
              fo1='Jitter'
              st.success(fo1)
          if (float(fhi) > 755.25 or float(fhi) < 102.145):
              fo2='Vocal fold tension / Stiffness'
              st.success(fo2)
          if (float(flo) > 226.778):
              fo3='Vocal impairment, Reduced to produce low-frequency sounds'
              st.success(fo3)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(RPDE) > 0.617 or float(DDA) > 0.02086 or float(Jitter_percent) > 0.00571 or float(Jitter_Abs) > 0.00008 or float(RAP) > 0.00374 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ5) > 0.03194 or float(APQ) > 0.01958):
              fo4='Increased vocal irregularity'
              st.success(fo4)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(spread2) > -4.137 or float(spread1) > -5.440 or float(DFA) > 0.818 or float(DDA) > 0.02086 or float(fo) > 255.66 or float(APQ) > 0.01958 or float(RAP) > 0.00374 or float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(Shimmer) > 0.03411 or float(Shimmer_dB) > 0.282 or float(APQ3) > 0.02185):
              fo5='Vocal Instability'
              st.success(fo5)
          if (float(PPQ) > 0.00248 or float(DDP) > 0.01122 or float(APQ3) > 0.02185 or float(APQ5) > 0.03194 or float(APQ) > 0.01958):
              fo6='Vocal petrubation'
              st.success(fo6)
          if (float(DDA) > 0.02086):
              fo7='Dysphonia'
              st.success(fo7)
          if (float(NHR) > 0.02510):
              fo8='increased levels of noise relative to harmonics in their voice'
              st.success(fo8)
          if (float(HNR) < 28.333):
              fo9='Reduced vocal clarity and potentially higher background noise levels'
              st.success(fo9)
          if (float(PPE) > 0.09221 or float(D2) > 3.671 or float(DFA) > 0.818 or float(RPDE) > 0.617):
              fo10='Vocal complexity'
              st.success(fo10)
          if (float(spread1) > -5.440):
              fo11='Typical vocal behaviour'
              st.success(fo11)
          if (float(fo) < 88.333):
              fo12 ='potential worsening of vocal impairment and may indicate advanced disease progression or increased severity of symptoms'
              st.success(fo12)
          if (float(fhi) < 102.145):
              fo13 ='Reduced vocal fold vibratory range'
              st.success(fo13)
          if (float(flo) < 65.476):
              fo14 ='Reduced vocal fold vibration or breathiness'
              st.success(fo14)
          medicine = '***MEDICINE REQUIRED***'
          st.success(medicine)
          vitals = '***REMAINING VITALS ARE NOT PROBLEMATIC AT PRESENT BUT TAKE CARE***'
          st.success (vitals)

if selected == 'About':
    st.title('About')
    st.write("""
    Welcome to the Multiple Disease Prediction System! This web application is designed to provide predictive analysis for three major diseases: Diabetes, Heart Disease, and Parkinson's Disease.

    **Purpose:**
    The primary purpose of this system is to assist individuals in assessing their risk of developing these diseases based on various input parameters. By leveraging machine learning models trained on relevant medical data, we aim to offer users valuable insights into their health status and encourage proactive measures for disease prevention and management.

    **Features:**
    - **Prediction:** Users can input their personal health information, such as gender, age, medical history, and vital signs, to obtain predictions regarding their susceptibility to different diseases.
    - **Interpretation:** The system interprets the prediction results and provides actionable insights, including potential health risks, precautionary measures, and recommended next steps.
    - **User-Friendly Interface:** Our interface is designed to be intuitive and user-friendly, ensuring a seamless experience for users of all backgrounds.
    - **Privacy:** We prioritize user privacy and data security, adhering to strict protocols for handling sensitive medical information.

    **Disclaimer:**
    Please note that the predictions generated by this system are based on statistical analysis and machine learning algorithms trained on historical medical data. While we strive to provide accurate predictions, the results should not be considered a substitute for professional medical advice. We recommend consulting a qualified healthcare professional for personalized diagnosis and treatment recommendations.

    **Contact Us:**
    If you have any questions, feedback, or concerns about the Multiple Disease Prediction System, please feel free to reach out to us at ***20bq1a0430@vvit.net***. Your input is invaluable as we continue to improve and refine our services.
    """)
