from enum import Enum
import requests
import streamlit as st

URL = 'http://127.0.0.1:8000/get-news/'


class Company(Enum):
    provectus = 'Provectus'
    corcentric = 'Corcentric'


st.set_page_config(
    page_title="Company News",
    page_icon=":newspaper:",
)


def send_news_request(company_name: str) -> str:
    try:
        response = requests.post(url=URL + company_name)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        # st.write("Response content:", response.content)  # Debugging statement
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return 'Error'


st.title(':newspaper: Company news')

with st.form('input_form'):
    option = st.selectbox(
        'Select company',
        [company.value for company in Company],
        index=None,
        placeholder='...'
    )

    st.write('You selected:', option)

    submitted = st.form_submit_button('Submit')

    if submitted:
        with st.spinner('Now just wait ;)'):
            response = send_news_request(option)
            st.toast('Answer was made')
            st.write(response)
