import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

names = ["ADMIN", "ADMIN", "ADMIN", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER"];
usernames = ["ADM_001", "ADM_002", "ADM_003", "SHK_001", "SHK_002", "SHK_003", "SHK_004", "SHK_005", "SHK_006"];
passwords = ["ADM_001", "ADM_002", "ADM_003", "SHK_001", "SHK_002", "SHK_003", "SHK_004", "SHK_005", "SHK_006"];

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/  "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)