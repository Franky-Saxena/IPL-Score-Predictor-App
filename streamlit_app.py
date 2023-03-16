
import streamlit as st
import numpy as np
import pickle

filename = 'lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

st.header('IPL Score Predictor App')
temp_array = list()
teams = ['Select Team', 'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Surisers Hyderabad']

batting_team = st.selectbox('Batting Team:', teams)
if batting_team == 'Chennai Super Kings':
    temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Delhi Daredevils':
    temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Kings XI Punjab':
    temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif batting_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif batting_team == 'Mumbai Indians':
    temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif batting_team == 'Rajasthan Royals':
    temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif batting_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif batting_team == 'Surisers Hyderabad':
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

bowling_team = st.selectbox('Bowling-Team:', teams)
if bowling_team == 'Chennai Super Kings':
    temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Delhi Daredevils':
    temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Kings XI Punjab':
    temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif bowling_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif bowling_team == 'Mumbai Indians':
    temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif bowling_team == 'Rajasthan Royals':
    temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif bowling_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif bowling_team == 'Surisers Hyderabad':
    temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

overs = st.number_input(label='overs', step=0.1, format='%.1f')
runs = st.number_input(label='runs', step=1, format='%i')
wickets = st.number_input(label='wickets', step=1, format='%i')
runs_in_prev_5 = st.number_input(label='runs_in_prev_5', step=1, format='%i')
wickets_in_prev_5 = st.number_input(label='wickets_in_prev_5', step=1, format='%i')

temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

data = np.array([temp_array])
my_prediction = int(regressor.predict(data)[0])

if st.button('Submit'):
    st.balloons()
    st.subheader('Predicted Score is around:')
    st.success(f'[{my_prediction - 10} -{my_prediction + 5}]')
