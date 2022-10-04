# -*- coding: utf-8 -*-
"""
E:\Education\SLIIT\Year 04\IT4010 - Research Project\19. DATA

@author: Anuththara
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
correct_responses
commission_errors
omission_errors
mean_reaction_time

'''

###############################################################################

df1  = pd.read_csv("AA4.csv")

x = df1[['id']]
y = df1[['commission_errors']]
plt.scatter(x, y, c ="blue")

x2 = df1[['id']]
y2 = df1[['omission_errors']]
plt.scatter(x2, y2, c ="red")

plt.xlabel("ID")
plt.ylabel("Blue = CE, Red = OE")
plt.title("AA5 --> TCR = 19")

df1.plot(kind='scatter',x='id',y='correct_responses', c ="orange", title="AA4") # scatter plot
df1.plot(kind='scatter',x='id',y='mean_reaction_time', c ="green", title="AA4") # scatter plot

###############################################################################

df2  = pd.read_csv("AA5.csv")

df2.plot(kind='scatter',x='id',y='commission_errors', c ="blue") # scatter plot

x2 = df2[['id']]
y2 = df2[['omission_errors']]
plt.scatter(x2, y2, c ="red")

plt.xlabel("ID")
plt.ylabel("Blue = CE, Red = OE")
plt.title("AA5 --> TCR = 19")

df2.plot(kind='scatter',x='id',y='correct_responses', c ="orange", title="AA5") # scatter plot
df2.plot(kind='scatter',x='id',y='mean_reaction_time', c ="green", title="AA5") # scatter plot
