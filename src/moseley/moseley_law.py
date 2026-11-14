# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% ../notebooks/03_moseley-law.ipynb #3ebaf924
# moseley_law.py

import numpy as np 

def moseley_law(E_K_alpha_keV): 
    '''Square root form of Moseley's law. 
    
    Args: 
        E_K_alfa_keV (float or array of floats): K_alpha peak energy in keV 
        
    Example: 
        moseley_law(6.40)
        
    Returns: 
        Z (float or array of floats): predicted atomic number 
        
    ''' 
    Z = 1 + np.sqrt(1000 * E_K_alpha_keV / 10.2) 
    
    return Z 
