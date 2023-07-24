# import streamlit_authenticator as stauth

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
# print(hashed_passwords)

import yaml

# Load the existing data
with open('test.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# Update the data
config['key'] = '개씨발'

# Write the data back to the file
with open('test.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
