import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import chi2

for _ in range(10):
    st.sidebar.write('\n')
# n = st.sidebar.number_input(label='Enter the degree of freedom',min_value=1, max_value=1000)
n = st.sidebar.slider(label='Select degree of freedom',min_value=1, max_value=100)

if n is not None:
    # Define the range of x values
    x = np.arange(0,100,0.01)
    # Calculate chi-square distribution for the given degrees of freedom
    y = chi2.pdf(x, n)
    
    # Plot the chi-square distribution
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'Chi-Square Distribution (df={n})', color='red', linewidth=3)
    ax.set_title(f'Chi-Square Distribution with {n} Degrees of Freedom')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()
    ax.grid(True)

    # Display the plot in Streamlit
    st.markdown('## Visualization')
    st.pyplot(fig)

    # Display the selected degrees of freedom
    st.markdown(f"### Degree of Freedom : {n}")