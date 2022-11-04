#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import numpy as np
import requests
import seaborn
#import json
import plotly.express as px
import plotly.figure_factory as ff
from shapely.geometry import Point
#!pip install missingno
import missingno as msno
import statsmodels.api as sm
#!pip install streamlit
import streamlit as st
from fuzzywuzzy import fuzz


# In[ ]:

#Achtergrond streamlit
achtergrond = ''' <style> body { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); background-size: cover; } </style> ''' 


#Dashboard
pages = st.sidebar.selectbox('Pagina' ,('Home','Terrein Kaart','Verbruik', 'Ritteninformatie datasets'))

if pages == 'Home':
    st.header("**Klimaatneutraal rijden**")
    st.markdown("Met dit dashboard wordt geprobeerd een zo een compleet mogelijk beeld te weergeven van de ontwikkeling van de energievraag van logistieke bedrijven en de knelpunten in het netwerk. Omdat er al een tekort is aan capaciteit op het elektriciteitsnetwerk, is de verwachting dat de aanleg van nieuwe aansluitingen door de netbeheerder tot wel 8 jaar kan duren. Daarom is het belangrijk om nu alvast in kaart te brengen wat de verwachtte energievraag is (hoeveel, waar en wanneer) in de toekomstige situatie zodat we ons op tijd kunnen voorbereiden en logistieke vervoerders niet hoeven te wachten met het aanschaffen van elektrische voertuigen omdat er onvoldoende netwerkcapaciteit beschikbaar is. Dat zou de energietransitie onnodig remmen.")

    #st.markdown("Welkom op het dashboard van groep 22. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")


elif pages == 'Terrein Kaart':
    st.subheader('Kaarten Bedrijventerreinen')
    st.markdown("In de kaart zijn de energiebehoeftes van Schiphol tradepark en WFO per gebouw weergegeven. Hiermee gaan we een geschatte energievraag analyseren van op basis van voertuigregistraties. Op basis van publieke data en deelse CBS data. Wordt een inschatting gemaakt hoe de energiebehoefte/voorraad op bedrijventerreinen.")
    folium_static(mwfo)#Kaart1
    folium_static(mstp)#Kaart2
elif pages == 'Verbruik':
    st.subheader('Energie verbruik per dag')
    st.markdown('In onderstaande velden voer een voertuig ID in om het energieverbruik over een dag van een vrachtwagen te visualiseren.')
    number = st.number_input('Voeg een voertuig ID in', min_value=1, max_value=200, value=1, step=1)

        #Knoppen maken zodat een dag van het jaar gekozen kan worden
    datum_2022 = st.date_input("Kies hier een datum voor het energieprofiel van 2022", datetime.date(2021, 4, 1),
                      min_value = datetime.date(2021, 4, 1), max_value = datetime.date(2021, 4, 30))
    
    elif pages == 'Ritteninformatie datasets':
           st.subheader("Informatie over ritten")
            
    st.markdown("Voorbeelden van ID's in Allevoertuigen: " + voertuig_ids_string)
    st.markdown("Voorbeelden van ID's in December: " + voertuig_ids_december)



