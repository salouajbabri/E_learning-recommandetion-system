import streamlit_authenticator as stauth

import login as db

usernames = ["salouajb", "raghadjb"]
names = ["Saloua Jbabri", "Raghad Jbabri"]
passwords = ["abc123", "123cba"]
hashes_passwords = stauth.Hasher(passwords).generate()

for(username, name, hash_password) in zip(usernames, names, hashes_passwords):
    db.insert_user(username, name, hash_password)



