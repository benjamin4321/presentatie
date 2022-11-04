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


#Dashboard

#Achtergrond streamlit
achtergrond = ''' <style> body { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); background-size: cover; } </style> ''' 

#Radioknoppen in de sidebar die navigatie over de pagina mogelijk maken. 
pages = st.sidebar.radio('Pagina', options=['Home','Terrein Kaart', 'Ritteninformatie', 'Conclusie'])
st.markdown(achtergrond, unsafe_allow_html=True)

if pages == 'Home':
    st.markdown("**Klimaatneutraal rijden**")
    st.markdown("Met dit dashboard wordt geprobeerd een zo een compleet mogelijk beeld te weergeven van de ontwikkeling van de energievraag van logistieke bedrijven en de knelpunten in het netwerk. Omdat er al een tekort is aan capaciteit op het elektriciteitsnetwerk, is de verwachting dat de aanleg van nieuwe aansluitingen door de netbeheerder tot wel 8 jaar kan duren. Daarom is het belangrijk om nu alvast in kaart te brengen wat de verwachtte energievraag is (hoeveel, waar en wanneer) in de toekomstige situatie zodat we ons op tijd kunnen voorbereiden en logistieke vervoerders niet hoeven te wachten met het aanschaffen van elektrische voertuigen omdat er onvoldoende netwerkcapaciteit beschikbaar is. Dat zou de energietransitie onnodig remmen.")
    #st.markdown("Welkom op het dashboard van groep 22. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")
    st.image("hva.png", width=None ,output_format='auto')
    st.markdown(achtergrond, unsafe_allow_html=True

elif pages == 'Terrein Kaart':
    st.subheader('Dataset Student Performance')
    st.markdown("In de kaart zijn de energiebehoeftes van Schiphol tradepark en WFO per gebouw weergegeven. Hiermee gaan we een geschatte energievraag analyseren van op basis van voertuigregistraties. Op basis van publieke data en deelse CBS data. Wordt een inschatting gemaakt hoe de energiebehoefte/voorraad op bedrijventerreinen.")
    st.dataframe(data=students, use_container_width=False)
    st.subheader('Beschrijving van de gegevens in het dataframe door middel van de describe functie.')
    st.markdown("Hierin is te zien dat er geen data ontbreekt. De nulwaardes horen in het dataframe.")
    st.dataframe(data=students_describe, use_container_width=False)
    st.subheader('Vergelijking tussen de cijferschalen van Portugal en Nederland.')
    st.image("Cijfers.png", output_format='auto')
    st.subheader('Dataframe na aanpassen voor voldoende en onvoldoende resultaten.')
    st.dataframe(data=students2, use_container_width=False)
    st.subheader("Correlatietabel van de dataset 'Student Performance'.")
    st.markdown("Correlatie geeft de mate van samenhang tussen twee variabelen weer, ofwel in hoeverre twee variabelen elkaar beïnvloeden. De correlatie wordt uitgedrukt in de correlatiecoëfficiënt. De waarde van de correlatiecoëfficiënt ligt tussen -1 en +1. Een positieve correlatiecoëfficiënt geeft aan dat dat de variabelen beiden in dezelfde richting veranderen. Een negatieve correlatiecoëfficiënt geeft aan dat de variabelen precies het tegenovergestelde van elkaar doen. Een correlatiecoëfficiënt van 0 geeft aan dat er geen verband is tussen de variabelen.")
    st.write(figc)
    st.markdown("P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.")
    st.markdown("Bron Dataset: https://www.kaggle.com/datasets/devansodariya/student-performance-data")

elif pages == 'Ritteninformatie':
    st.subheader("Informatie over ritten")
    st.markdown("Voor enkele transporteurs is hieronder een schatting van wat de energievraag zou zijn in het geval van dat de ritten door een elektrische vrachtwagen zou worden uitgevoerd. Hierbij gaan we de vraag hoeveel elektriciteit er nodig zou zijn om de rit uit te voeren, en of dit op een bedrijventerrein kan worden gedaan of langs de snelweg.")
    st.plotly_chart(fig1), 
    st.markdown("In de onderstaande grafiek is de verdeling van de leeftijden op de scholen weergegeven."), st.plotly_chart(fig2), st.markdown("In de onderstaande grafiek is te zien dat de vrouwelijke studenten meer voldoendes hebben gehaald, echter zijn er wel meer vrouwelijke studenten in de dataset opgenomen."), st.plotly_chart(fig7), st.markdown("In de onderstaande grafiek is te zien dat het gemiddelde eindcijfer bij de mannelijke studenten hoger is."), st.plotly_chart(fig3), st.markdown("In de onderstaande grafiek zijn de behaalde cijfers per periode te zien. De twee grafieken hierna laten hetzelfde zien, maar dan per geslacht."), st.plotly_chart(fig4), st.plotly_chart(fig5), st.plotly_chart(fig6), st.markdown("De volgende twee grafieken geven aan dat het opleidingsniveau van de ouder wel degelijk invloed heeft op het behaalde resultaat van het kind."), st.plotly_chart(fig8), st.plotly_chart(fig14), st.markdown("De Onderstaande grafiek laat zien dat vrouwelijke leerlingen meer tijd besteden aan het studeren."),st.plotly_chart(fig9), st.markdown("In de onderstaande grafiek is het verschil tussen de behaalde resultaten te zien. De mannelijke studenten scoren beter bij het zelfde aantal studieuren."), st.plotly_chart(fig10), st.plotly_chart(fig11), st.markdown("De onderstaande grafiek toont aan dat absentie invloedt heeft op het behaalde cijfer, vooral voor mannen. De vrouwelijke studenten presenteren beter als ze een aantal keer absent zijn geweest dan mannen die lessen gemist hebben."), st.plotly_chart(fig12), st.plotly_chart(fig13)

elif pages == 'Conclusie':
    st.markdown('Bedankt voor het bezoeken.')
    st.markdown('Groep 16, 19, 22')
                


# In[ ]:




