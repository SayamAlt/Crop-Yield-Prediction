#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib


# In[2]:


model = joblib.load('model.pkl')
model


# In[3]:


app = Flask(__name__)


# In[4]:


items = ['Cassava', 'Maize', 'Plantains and others', 'Potatoes',
        'Rice, paddy', 'Sorghum', 'Soybeans', 'Sweet potatoes', 'Wheat',
        'Yams']
areas = ['Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia',
        'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
        'Bangladesh', 'Belarus', 'Belgium', 'Botswana', 'Brazil',
        'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Canada',
        'Central African Republic', 'Chile', 'Colombia', 'Croatia',
        'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
        'Eritrea', 'Estonia', 'Finland', 'France', 'Germany', 'Ghana',
        'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras',
        'Hungary', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Italy',
        'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lebanon',
        'Lesotho', 'Libya', 'Lithuania', 'Madagascar', 'Malawi',
        'Malaysia', 'Mali', 'Mauritania', 'Mauritius', 'Mexico',
        'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal',
        'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Norway',
        'Pakistan', 'Papua New Guinea', 'Peru', 'Poland', 'Portugal',
        'Qatar', 'Romania', 'Rwanda', 'Saudi Arabia', 'Senegal',
        'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan',
        'Suriname', 'Sweden', 'Switzerland', 'Tajikistan', 'Thailand',
        'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Kingdom',
        'Uruguay', 'Zambia', 'Zimbabwe']
val1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
val2 = [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
         26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
         39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
         52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
         65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
         78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
         91,  92,  93,  94,  95,  96,  97,  98,  99, 100]
crops = dict(zip(items,val1))
nations = dict(zip(areas,val2))


# In[5]:


@app.route("/")
def home():
    return render_template('home.html',regions=nations,items=crops)


# In[6]:


@app.route("/predict", methods=['GET','POST'])
def predict():
    country = request.form['area']
    area = nations[country]
    crop = request.form['item']
    item = crops[crop]
    year = request.form['year']
    rainfall = request.form['avg_annual_rainfall_mm']
    pesticides = request.form['pesticides_tonnes']
    temp = request.form['avg_temp']
    
    predictions = model.predict([[
        area,
        item,
        year,
        rainfall,
        pesticides,
        temp
    ]])
    
    output = predictions[0]*69979.655
    output = abs(round(output,2))
    output = format(output,',')
    return render_template('home.html',prediction_text="Your net crop area yield is {} square feet.".format(output),regions=nations,items=crops)


# In[ ]:


if __name__ == '__main__':
    app.run(port=8080)

