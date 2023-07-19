import streamlit as st
import streamlit_authenticator as stauth
import pickle
import pandas as pd

import login as db

users = db.fetch_all_users()
usernames = [user["key"] for user in users]
names =[user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

#authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                  #  "courses_dashbord", "abcdef", cookie_expiry_days=30,hash_type='sha256')

#name, authentification_status, username = authenticator.login("Login","main")

def recommend(classe):
    class_index = classes[classes["Name"] == classe].index[0]
    distances = similarity[class_index]
    class_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_classes = []
    for i in class_list:
        class_id = i[0]
        # fetch poster from API
        recommended_classes.append(classes.iloc[i[0]]["Name"])
    return recommended_classes


class_dict = pickle.load(open('class_dict.pkl','rb'))
classes = pd.DataFrame(class_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('E-Learning Recommender System')

classes_name = classes["Name"].unique()
classes_name_series = pd.Series(classes_name)

selected_class_name = st.selectbox(
    'Choose your favorite course :',
    classes_name_series.values
)

if st.button('Recommend'):
    recommendations = recommend(selected_class_name)
    for i in recommendations:
        st.write(i)
