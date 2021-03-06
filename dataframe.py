import streamlit as st
import pandas as pd
import numpy as np

st.title('Dataframe')

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

#st.dataframe(dataframe.style.highlight_max(axis=0))
st.dataframe(dataframe)

x = st.slider('x') # this is a widget
st.write(x, 'squared is', x * x)

st.text_input('Your name', key='name')
st.session_state.name

# add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# add a slider to the sidebar
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# or even better, call Streamlit functions inside a 'with' block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    st.write(f"You are in {chosen} house!")