import streamlit as st
import getpass, os

st.set_page_config(layout='wide')



def main():
    st.title("YARA RULE DETECTOR")
    st.subheader("\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0\U0001F9A0")
    st.write("\n")
    st.subheader("For all your digital viral needs.")
    st.write("\n")
    st.write("\n")
    st.subheader("\U0001F448Please choose an option from the sidebar on the left.")

if __name__ == "__main__":
    username = getpass.getuser()
    domain_username = os.getenv('USERDOMAIN') + "\\" + username
    if 'pwcglb' in domain_username.lower():
        main()