import pandas as pd
import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("Data.csv")
heightlist=df["Height(Inches)"].tolist()
weightlist=df["Weight(Pounds)"].tolist()

heightMean=statistics.mean(heightlist)
weightMean=statistics.mean(weightlist)

heightMode=statistics.mode(heightlist)
weightMode=statistics.mode(weightlist)

heightMedian=statistics.median(heightlist)
weightMedian=statistics.median(weightlist)

hsd=statistics.stdev(heightlist)
wsd=statistics.stdev(weightlist)

heightfsds,heightfsde=heightMean-hsd,heightMean+hsd
heightssds,heightssde=heightMean-(2*hsd),heightMean+(2*hsd)
heighttsds,heighttsde=heightMean-(3*hsd),heightMean+(3*hsd)

heightfsds,heightfsde=heightMean-hsd,heightMean+hsd
heightssds,heightssde=heightMean-(2*hsd),heightMean+(2*hsd)
heighttsds,heighttsde=heightMean-(3*hsd),heightMean+(3*hsd)

