


import pickle
import streamlit as st
import numpy as np



# Loading the saved model
heart_model = pickle.load(open("C:/Users/hakke/OneDrive/Desktop/Heart_Attack_Prediction/saved_models/Heart_Attack_Prediction_Final_Model.sav", 'rb'))  # Add the correct path

# Function to convert selected categories to binary values
def convert_to_binary(selected_categories):
    binary_values = [1 if selection == 'Yes' else 0 for selection in selected_categories]
    return binary_values

# Function to convert selected gender to binary
def convert_to_binary_gen(selected_categories):
    binary_values = [1 if selection == 'Male' else 0 for selection in selected_categories]
    return binary_values

# Function to convert selected values to binary based on categories
def convert_it_to_binary(selected_value, categories):
    binary_values = [1 if item in selected_value else 0 for item in categories]
    return binary_values

# Sidebar for navigation
#with st.sidebar:
#   selected = st.selectbox('Navigation', ['Heart Attack Prediction'])


st.sidebar.title('Navigation')
selected = st.sidebar.selectbox('Go To', ['Home', 'Heart Attack Prediction'])

if selected == 'Home':
    st.title('Welcome to Heart Attack Prediction in Youth Application')
    st.write('This application helps in predicting the likelihood of a heart attack based on various factors.')
    try:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRJGKQYmewqDUZ69lmVJ4pfNqt6NE71Y1nDw&usqp=CAU')
    except Exception as e:
        st.error(f"Error loading image: {e}")
# Display input fields based on selected navigation option
# Display input fields based on selected navigation option
elif selected == 'Heart Attack Prediction':
    st.title('Heart Attack Prediction using ML')
    
    # Getting the input data from the user
    # Age categories
    age_categories = ['Age: 18-24', 'Age: 25-29', 'Age: 30-34', 'Age: 35-39', 'Age: 40-44', 'Age: 45-49', 'Age: 50-54', 'Age: 55-59']
    selected_categories_age = st.multiselect('Select Age Categories:', age_categories)
    
    # Race categories
    race_categories = ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White']
    selected_categories_race = st.multiselect('Select Race Categories:', race_categories)
    
    # General health categories
    genhealth_categories = ['Excellent', 'Fair', 'Good', 'Poor', 'Very good']
    selected_categories_genhealth = st.multiselect('Select General Health Categories:', genhealth_categories)
    
    # BMI input
    ##*******************
    weight = st.text_input('Enter weight in kilograms')
    height = st.text_input('Enter height in meters')
    #BMI = st.text_input('Enter BMI Value:')
    
    # Smoking categories
    smoking_categories = ['Yes', 'No']
    selected_categories_smoking = st.multiselect('Do you smoke?', smoking_categories)
    
    # Alcohol drinking categories
    alcoholdrinking_categories = ['Yes', 'No']
    selected_categories_alcoholdrinking = st.multiselect('Do you have drinking habits?', alcoholdrinking_categories)

    # Stroke categories
    stroke_categories = ['Yes', 'No']
    selected_categories_stroke = st.multiselect('Have you ever experienced a stroke?', stroke_categories)

    # Difficulty in walking categories
    diffwalking_categories = ['Yes', 'No']
    selected_categories_diffwalking = st.multiselect('Do you feel any difficulty in walking?', diffwalking_categories)

    # Gender categories
    sex_categories = ['Male', 'Female']
    selected_categories_sex = st.multiselect('Select Gender:', sex_categories)
    
    # Diabetic categories
    diabetic_categories = ['Yes', 'No']
    selected_categories_diabetic = st.multiselect('Do you have diabetes or have you been diagnosed with diabetes in the past?', diabetic_categories)
    
    # Physical activity categories
    physicalactivity_categories = ['Yes', 'No']
    selected_categories_physicalactivity = st.multiselect('Do you incorporate regular physical activity into your daily routine?', physicalactivity_categories)

    # SleepTime input
    SleepTime = st.text_input('Enter sleep time (hours):')
    
    # Asthma categories
    asthma_categories = ['Yes', 'No']
    selected_categories_asthma = st.multiselect('Do you have asthma, or have you been diagnosed with asthma in the past?', asthma_categories)

    # Kidney disease categories
    kidneydisease_categories = ['Yes', 'No']
    selected_categories_kidneydisease = st.multiselect('Do you have kidney disease, or have you been diagnosed with kidney disease in the past?', kidneydisease_categories)

    # Skin cancer categories
    skincancer_categories = ['Yes', 'No']
    selected_categories_skincancer = st.multiselect('Have you ever been diagnosed with skin cancer or had any suspicious moles or lesions checked by a healthcare professional?', skincancer_categories)

    # Code for Prediction:
    heart_diagnosis = ''
    precautions = []
  

    # Creating a button for prediction
    if st.button('Heart Attack Test Result'):
        try:
            # Validate and convert BMI to float
            weight = float(weight)
            height = float(height)
            BMI_value = weight / (height * height)
            # Validate and convert SleepTime to float
            SleepTime_value = float(SleepTime) if SleepTime.strip() else None
            
            if BMI_value is not None and SleepTime_value is not None:
                # Convert selected categories to binary values
                selected_categories_age_binary = convert_it_to_binary(selected_categories_age, age_categories)
                selected_categories_race_binary = convert_it_to_binary(selected_categories_race, race_categories)
                selected_categories_genhealth_binary = convert_it_to_binary(selected_categories_genhealth, genhealth_categories)
                selected_categories_smoking_binary = convert_to_binary(selected_categories_smoking)
                selected_categories_alcoholdrinking_binary = convert_to_binary(selected_categories_alcoholdrinking)
                selected_categories_stroke_binary = convert_to_binary(selected_categories_stroke)
                selected_categories_diffwalking_binary = convert_to_binary(selected_categories_diffwalking)
                genderValue = convert_to_binary_gen(selected_categories_sex)
                selected_categories_diabetic_binary = convert_to_binary(selected_categories_diabetic)
                selected_categories_physicalactivity_binary = convert_to_binary(selected_categories_physicalactivity)
                selected_categories_asthma_binary = convert_to_binary(selected_categories_asthma)
                selected_categories_kidneydisease_binary = convert_to_binary(selected_categories_kidneydisease)
                selected_categories_skincancer_binary = convert_to_binary(selected_categories_skincancer)
                
                # Make prediction
                heart_prediction =  heart_model.predict([[
                    *selected_categories_age_binary, *selected_categories_race_binary, *selected_categories_genhealth_binary,
                    BMI_value, *selected_categories_smoking_binary, *selected_categories_alcoholdrinking_binary,
                    *selected_categories_stroke_binary, *selected_categories_diffwalking_binary, *genderValue,
                    *selected_categories_diabetic_binary, *selected_categories_physicalactivity_binary,
                    SleepTime_value, *selected_categories_asthma_binary, *selected_categories_kidneydisease_binary,
                    *selected_categories_skincancer_binary
                ]])

                if heart_prediction[0] == 1:
                    heart_diagnosis = "You are prone to heart attack"
                    
                    st.success(heart_diagnosis)  
# Age
                    if 'Age: 50-54' in selected_categories_age or 'Age: 55-59' in selected_categories_age:
                        #precautions.append("Regular health check-ups are essential, especially as you age.")
                        precautions.append("Adopt a heart-healthy lifestyle, including regular exercise and a balanced diet.")
                        
# Race
                    if 'Black' in selected_categories_race or 'Hispanic' in selected_categories_race:
                        #precautions.append("Be aware of heart health risks prevalent in specific racial groups.")
                        precautions.append("Regular screenings and preventive measures are crucial.")

# General Health
                    if 'Fair' in selected_categories_genhealth or 'Poor' in selected_categories_genhealth:
                        precautions.append("Maintain a healthy weight.")
                        precautions.append("Manage stress levels through relaxation techniques or mindfulness practices.")
                        precautions.append("Get regular physical activity.")

# BMI
                    if BMI_value is not None:
                        if BMI_value >= 30:
                            precautions.append("Maintain a healthy weight to reduce the risk of obesity-related heart issues.")
                            precautions.append("Follow a balanced diet rich in fruits, vegetables, and whole grains.")

# Smoking
                    if 'Yes' in selected_categories_smoking:
                        #precautions.append("Quit smoking to reduce the risk of heart disease.")
                        precautions.append("Seek support from healthcare professionals or smoking cessation programs.")

# Alcohol Drinking
                    if 'Yes' in selected_categories_alcoholdrinking:
                        precautions.append("Limit alcohol intake to moderate levels as excessive drinking can increase heart disease risk.")
                        #precautions.append("Be aware of the recommended alcohol consumption guidelines.")

# Stroke
                    if 'Yes' in selected_categories_stroke:
                        precautions.append("Manage hypertension and cholesterol levels to prevent stroke and heart disease.")
                        #precautions.append("Follow prescribed medications and lifestyle changes advised by healthcare providers.")

# Difficulty in Walking
                    if 'Yes' in selected_categories_diffwalking:
                        #precautions.append("Consult healthcare professionals to address mobility issues.")
                        precautions.append("Physical therapy or rehabilitation programs may help improve walking ability.")

# Gender
                    if 'Female' in selected_categories_sex:
                        precautions.append("Women should be aware of unique heart disease symptoms and risk factors.")
                        #precautions.append("Regular screenings and heart-healthy lifestyle choices are crucial for both genders.")

# Diabetic
                    if 'Yes' in selected_categories_diabetic:
                        precautions.append("Manage blood sugar levels through medication, diet, and exercise.")
                        #precautions.append("Regular monitoring and check-ups are essential for diabetic individuals.")

# Physical Activity
                    if 'No' in selected_categories_physicalactivity:
                            #precautions.append("Incorporate regular exercise into your routine to maintain heart health.")
                            precautions.append("Aim for at least 150 minutes of moderate-intensity aerobic activity per week.")

# Sleep Time
                    if SleepTime_value is not None:
                            if SleepTime_value < 7 or SleepTime_value > 9:
                                precautions.append("Ensure adequate sleep duration (7-9 hours per night) to support heart health.")
                                precautions.append("Establish a regular sleep schedule and create a conducive sleep environment.")

# Asthma
                    if 'Yes' in selected_categories_asthma:
                            precautions.append("Manage asthma symptoms effectively with medication and preventive measures.")
                            #precautions.append("Avoid triggers that can exacerbate asthma attacks.")
                        
# Kidney Disease
                    if 'Yes' in selected_categories_kidneydisease:
                            #precautions.append("Monitor kidney function regularly, especially if diagnosed with kidney disease.")
                            precautions.append("Manage blood pressure and blood sugar levels to prevent further kidney damage.")

# Skin Cancer
                    if 'Yes' in selected_categories_skincancer:
                            precautions.append("Practice sun safety measures, including wearing sunscreen and protective clothing.")
                            #precautions.append("Regularly check your skin for any changes or suspicious lesions and seek medical attention if needed.")
                                            
                    st.markdown("# Heart Health Precautions")
                    st.write('Here are some personalized precautions based on the selected factors:')
                    for precaution in precautions:
                        st.write(f"- {precaution}")  

                else:
                    heart_diagnosis = "You are not prone to heart attack"
                    st.success(heart_diagnosis)  
            else:
                st.error("Please enter valid values for BMI and Sleep Time.")
        except Exception as e:
            # Print the error message for debugging
            print("Error occurred:", e)
            # Set a default diagnosis message
            heart_diagnosis = "Error occurred during prediction. Please check input data."
            
            
    
