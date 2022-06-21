import pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import sklearn
# from sklearn.linear_model import LogisticRegressionCV
# from sklearn.linear_model import LogisticRegression
 
# loading the trained model
pickle_in = open('streamlit_classifier.pkl', 'rb') 
tree_classifier = pickle.load(pickle_in)
 
# @st.cache()

st.title('Tree Health Classifier')
st.image('forest.jpeg')

st.write('This is a web app to predict whenever tree is healthy or deteriorating based on\
        several features that you can see in the sidebar. Please choose the\
        value of each feature. Click on the Classify button below to\
        see the outcome of the classifier.')

st.sidebar.header('Please adjust the values for the following features')
# Making Sliders and Feature Variables

#def user_input_features():
   

diameter_mm  = st.sidebar.slider(label = 'diameter_mm', min_value = 0.0, max_value = 1000.0 , value = 11516.0, step = 1.0)
height_cm = st.sidebar.slider(label = 'height_cm', min_value = 30.0,max_value = 3000.0 ,value = 1500.0,step = 100.0)
age =  st.sidebar.slider(label = 'age', min_value = 0.0, max_value = 210.0 , value = 50.0,step = 1.0)
broadleaf_dieback_extend_per = st.sidebar.slider(label = 'Percentage of ash dieback', min_value = 0.0, max_value = 100.0, value = 50.0, step = 1.0)
latitude = st.sidebar.slider(label = 'Latitude', min_value = 2.125587 , max_value = 58.477997, value = 25.0)
ammonia = st.sidebar.slider(label = 'Ammonia levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
nitrous_oxide = st.sidebar.slider(label = 'Nitrous oxide levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
sulphur_dioxide = st.sidebar.slider(label = 'Sulphur oxide levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
volatile_organic_compounds = st.sidebar.slider(label = 'Volatile organic compounds levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
particulate_matter_10 = st.sidebar.slider(label = 'PM2.5 levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
particulate_matter_25 = st.sidebar.slider(label = 'PM10 levels', min_value = 0.0, max_value = 150.0, value = 50.0, step = 1.0)
ann_temperature = st.sidebar.slider(label = 'Annual mean temperature in Celcius', min_value =  - 20.0, max_value = 50.0, value = 20.0, step = 1.0)
ann_rainfall = st.sidebar.slider(label = 'Annual mean rainfall in mm', min_value = 0.0, max_value = 2500.0, value = 200.0, step = 1.0)

shoot_death_branch = st.sidebar.selectbox('Select shoot death in branch',('none, or less than 20% loss of density', 
    'outermost shoots only', 'shoots on the middle of the branch',
'innermost parts of the branch', 'middle and inner parts of the branch', 'all over the branch', 'n/a for beach and oak trees'))

defoliation_type = st.sidebar.selectbox('Select defoliation type',('less than 20% loss of density', 'defoliation of lower crown', 'peripheral defoliation',
    'gaps in the lateral branch system', 'large gaps in the lateral branch system', 'spot-like defoliation', 'defoliation of upper crown'
    'mechanicla_damage', 'other'))

broadleaf_dieback_type = st.sidebar.selectbox('Select level of ash dieback (fungal disease)', ('none', 'top of the tree only', 'middle parts of the crown',
    'top and middle', 'branches at the base of the crown', 'throughout the crown', 'bottom and middle of the crown'))
leaf_browning = st.sidebar.selectbox('Select leaf browning', ('none', 'leaf margins only','leaf tips only', 'spots on leaves', 
'scattered leaves entirely brown', 'occasional shoots with all leaves entirely brown'))
leaf_yellowing = st.sidebar.selectbox('Select leaf yellowing', ('none', 'leaf margins chlorotic', 'some shoots or branches chlorotic', 'entire tree yellowish-green',
    'entire tree greenish-yellow', 'entire tree chlorotic'))
overall_discolouration = st.sidebar.selectbox('Select level of overall discolouration', ('0-10% of needles/leaves', '11-25% of needles/leaves', 
    '26-60% of needles/leaves','61-99% of needles/leaves', 'dead trees' ))
damage_butt_stem = st.sidebar.selectbox('Tree damage to butt stem', ('absent', 'present'))
damage_game = st.sidebar.selectbox('Tree damage caused by game animals', ('absent', 'present'))
damage_insect = st.sidebar.selectbox('Tree damage by insects', ('none', 'rare', 'infrequent', 'common', 'abundant'))
damage_fungal = st.sidebar.selectbox('Fungal tree damage ', ('none', 'rare', 'infrequent', 'common', 'abundant'))
damage_abiotic = st.sidebar.selectbox('Tree damage casued by environmental factors', ('absent', 'present'))
damage_man = st.sidebar.selectbox('Tree damage caused by man', ('absent', 'present'))
damage_fire = st.sidebar.selectbox('Select tree damage caused by fire', ('absent', 'present'))
damage_other = st.sidebar.selectbox('Select tree damage caused by other factors', ('absent', 'present'))

                      

#Mapping Feature Labels with Slider Values

features = {
'diameter_mm':diameter_mm,
'height_cm': height_cm,
'shoot_death_branch': shoot_death_branch,
'defoliation_type': defoliation_type,
'broadleaf_dieback_type': broadleaf_dieback_type,
'leaf_browning': leaf_browning,
'leaf_yellowing': leaf_yellowing,
'broadleaf_dieback_extend_per': broadleaf_dieback_extend_per,
'overall_discolouration': overall_discolouration,
'damage_butt_stem': damage_butt_stem,
'damage_game': damage_game,
'damage_insect': damage_insect,
'damage_fungal': damage_fungal,
'damage_abiotic': damage_abiotic,
'damage_man': damage_man,
'damage_fire' : damage_fire,
'damage_other': damage_other,
'ammonia': ammonia,
'nitrous_oxide': nitrous_oxide,
'sulphur_dioxide': sulphur_dioxide,
'volatile_organic_compounds': volatile_organic_compounds,
'particulate_matter_10': particulate_matter_10,
'particulate_matter_25': particulate_matter_25,
'ann_temperature' : ann_temperature,
'ann_rainfall': ann_rainfall,
'latitude': latitude,
'age': age,
} 
# # Converting Features into DataFrame

features_df = pd.DataFrame(features, index=[0])
st.subheading('Input features to be deployed')
st.write(features_df)

df2 = pd.read_csv('data.csv')
#st.write(df2.shape)

df_combo = pd.concat([features_df,df2], ignore_index = True)
st.write(df_combo.shape)
cols_to_dummy = ['shoot_death_branch', 'defoliation_type',
       'broadleaf_dieback_type', 'leaf_browning', 'leaf_yellowing',
       'overall_discolouration',
       'damage_butt_stem', 'damage_game', 'damage_insect', 'damage_fungal',
       'damage_abiotic', 'damage_man', 'damage_fire', 'damage_other']


df_combo = pd.get_dummies(df_combo, columns = cols_to_dummy, drop_first = True)
    
df_combo = df_combo[:1]


 
#     
   # Making predictions 
def predictor(classifier, df_combo):

    prediction = tree_classifier.predict(df_combo)
    if prediction == 0:
        pred =  'Healthy tree'
    else:
        pred = 'Deteriorating tree'
    return pred
    
      
  

if st.button('Classify'):
    result = predictor(tree_classifier, df_combo)
    
    st.write(' Based on feature values, the tree is classed as '+ (result))
     