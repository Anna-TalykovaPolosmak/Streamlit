import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

# Чтение данных из CSV
user_data = pd.read_csv("users.csv").set_index("name").T.to_dict()
authenticator = Authenticate(user_data, "cookie", "secret", 30)

# Авторизация
name, auth_status = authenticator.login()
if auth_status:
    with st.sidebar:
        st.write(f"Привет, {name}!")
        menu_option = st.radio("Меню", ["Главная", "Фото", "О нас"])
        authenticator.logout("Выйти")

    if menu_option == "Главная":
        st.title("Добро пожаловать!")
    elif menu_option == "Фото":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://example.com/cat1.jpg", caption="Кот 1")
        with col2:
            st.image("https://example.com/cat2.jpg", caption="Кот 2")
        with col3:
            st.image("https://example.com/cat3.jpg", caption="Кот 3")
    elif menu_option == "О нас":
        st.write("Информация о проекте")
elif auth_status is False:
    st.error("Неверные учетные данные")
elif auth_status is None:
    st.warning("Введите логин и пароль")
