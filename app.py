## flask
import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, jsonify, request
import logging
from time import sleep

# from sklearn.metrics import accuracy_score
# from sklearn.externals import joblib

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
# from sqlalchemy import create engine

app = Flask(__name__, static_url_path='')

# from keras.models import Sequential
# from keras.layers import Dense
# from sklearn.preprocessing import MinMaxScaler

#number_of_features=15
# def create_network(optimizer='rmsprop'):
#   network = models.Sequential()
#   network.add(layers.Dense(units=16, activation='relu', input_shape=(number_of_features,)))
#   network.add(layers.Dense(units=2, activation='softmax'))
#   network.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
#   return network
# ValueError: Error when checking input; expected dense_112_input to have shape (15,), but got array with shape (1,)

# with open('pickles/gridlr.pkl', 'rb') as f:
#    gridlr = joblib.load(f)
#with open('pickles/gridsvm.pkl', 'rb') as f:
#   gridsvm =joblib.load(f)
#with open('pickles/griddeep.pkl', 'rb') as f:
#   griddeep = joblib.load(f)

# gridmodels = {'Logistic Regression': gridlr,
#              'Linear Support Vector Machine':  gridsvm,
#              'Deep Neural Network Learning': griddeep
#             }

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/development")
# def development():
# #  #<1> get the static graph picture from AWS S3 bucket - save in Jupyter Notebook and stored in AWS S3
# #  #<2> use plotly dynamically generate graph
#   return render_template("modeldevelopment.html")

@app.route("/predictonesample", methods=["GET", "POST"])  # flask request: bring data back to Form by render jinja template
# @app.route("/predictonesample/<inpdata")
def predictioninput():
    if request.method=="GET":
        return render_template("predictonesample.html")
    # <input> 153 columns
    finalresult = ""
    msg = ""
    form_data = { "MONTH":"",
        "DAY_OF_WEEK":"",
        "DISTANCE_GROUP":"",
        "SEGMENT_NUMBER":"",
        "CONCURRENT_FLIGHTS":"",
        "NUMBER_OF_SEATS":"",
        "AIRPORT_FLIGHTS_MONTH":"",
        "AIRLINE_FLIGHTS_MONTH":"",
        "AIRLINE_AIRPORT_FLIGHTS_MONTH":"",
        "AVG_MONTHLY_PASS_AIRPORT":"",
        "AVG_MONTHLY_PASS_AIRLINE":"",
        "FLT_ATTENDANTS_PER_PASS":"",
        "GROUND_SERV_PER_PASS":"",
        "PLANE_AGE":"",
        "PREVIOUS_AIRPORT":"",
        "PRCP":"",
        "SNOW":"",
        "SNWD":"",
        "TMAX":"",
        "AWND":"" }

# print(request.method)      # initialization here for return "" for GET
    if request.method =="POST":
        print(request.method)
        form_data = request.form
    # 1) dummy : dropdowns(occupation, applyloanreason): selected =1 unselected = 0
    # MONTH = float(request.form["MONTH"]) # is key not function form["inputdata2"] form("inputdata2")
    # DAY_OF_WEEK = float(request.form["DAY_OF_WEEK"])
    # DISTANCE_GROUP = float(request.form["DISTANCE_GROUP"])
    # SEGMENT_NUMBER = float(request.form["SEGMENT_NUMBER"])
    # CONCURRENT_FLIGHTS = float(request.form["CONCURRENT_FLIGHTS"])
    # NUMBER_OF_SEATS = float(request.form["NUMBER_OF_SEATS"])
    # AIRPORT_FLIGHTS_MONTH = float(request.form["AIRPORT_FLIGHTS_MONTH"])
    # AIRLINE_FLIGHTS_MONTH = float(request.form["AIRLINE_FLIGHTS_MONTH"])
    # AIRLINE_AIRPORT_FLIGHTS_MONTH = float(request.form["AIRLINE_AIRPORT_FLIGHTS_MONTH"])
    # AVG_MONTHLY_PASS_AIRPORT = float(request.form["AVG_MONTHLY_PASS_AIRPORT"])
    # AVG_MONTHLY_PASS_AIRLINE = float(request.form["AVG_MONTHLY_PASS_AIRLINE"])
    # FLT_ATTENDANTS_PER_PASS = float(request.form["FLT_ATTENDANTS_PER_PASS"])
    # GROUND_SERV_PER_PASS = float(request.form["GROUND_SERV_PER_PASS"])
    # PLANE_AGE = float(request.form["PLANE_AGE"])
    # PREVIOUS_AIRPORT = float(request.form["PREVIOUS_AIRPORT"])
    # PRCP = float(request.form["PRCP"])
    # SNOW = float(request.form["SNOW"])
    # SNWD = float(request.form["SNWD"])
    # TMAX = float(request.form["TMAX"])
    # AWND = float(request.form["AWND"])
        while not (form_data["MONTH"]):
            sleep(1)
        app.logger.debug(form_data["MONTH"])
        MONTH = float(form_data["MONTH"])
        # is key not function form["inputdata2"] form("inputdata2")
        DAY_OF_WEEK = float(form_data["DAY_OF_WEEK"])
        DISTANCE_GROUP = float(form_data["DISTANCE_GROUP"])
        SEGMENT_NUMBER = float(form_data["SEGMENT_NUMBER"])
        CONCURRENT_FLIGHTS = float(form_data["CONCURRENT_FLIGHTS"])
        NUMBER_OF_SEATS = float(form_data["NUMBER_OF_SEATS"])
        AIRPORT_FLIGHTS_MONTH = float(form_data["AIRPORT_FLIGHTS_MONTH"])
        AIRLINE_FLIGHTS_MONTH = float(form_data["AIRLINE_FLIGHTS_MONTH"])
        AIRLINE_AIRPORT_FLIGHTS_MONTH = float(form_data["AIRLINE_AIRPORT_FLIGHTS_MONTH"])
        AVG_MONTHLY_PASS_AIRPORT = float(form_data["AVG_MONTHLY_PASS_AIRPORT"])
        AVG_MONTHLY_PASS_AIRLINE = float(form_data["AVG_MONTHLY_PASS_AIRLINE"])
        FLT_ATTENDANTS_PER_PASS = float(form_data["FLT_ATTENDANTS_PER_PASS"])
        GROUND_SERV_PER_PASS = float(form_data["GROUND_SERV_PER_PASS"])
        PLANE_AGE = float(form_data["PLANE_AGE"])  
        PREVIOUS_AIRPORT = float(form_data["PREVIOUS_AIRPORT"])
        PRCP = float(form_data["PRCP"])
        SNOW = float(form_data["SNOW"]) 
        SNWD = float(form_data["SNWD"])
        TMAX = float(form_data["TMAX"])
        AWND = float(form_data["AWND"])

        # DEP_TIME_BLK = request.form["DEP_TIME_BLK"]    # Bad request -- The browser (or proxy) sent a request that this server could not understand
        # DEP_TIME_BLK = request.form.get('DEP_TIME_BLK') # works
        dep_time_blk = form_data["DEP_TIME_BLK"]
        DEP_TIME_BLK_0001_0559 = 0
        DEP_TIME_BLK_0600_0659 = 0
        DEP_TIME_BLK_0700_0759 = 0
        DEP_TIME_BLK_0800_0859 = 0
        DEP_TIME_BLK_0900_0959 = 0
        DEP_TIME_BLK_1000_1059 = 0
        DEP_TIME_BLK_1100_1159 = 0
        DEP_TIME_BLK_1200_1259 = 0
        DEP_TIME_BLK_1300_1359 = 0
        DEP_TIME_BLK_1400_1459 = 0
        DEP_TIME_BLK_1500_1559 = 0
        DEP_TIME_BLK_1600_1659 = 0
        DEP_TIME_BLK_1700_1759 = 0
        DEP_TIME_BLK_1800_1859 = 0
        DEP_TIME_BLK_1900_1959 = 0
        DEP_TIME_BLK_2000_2059 = 0
        DEP_TIME_BLK_2100_2159 = 0
        DEP_TIME_BLK_2200_2259 = 0
        DEP_TIME_BLK_2300_2359 = 0
        
        if dep_time_blk == "0001_0559": 
            DEP_TIME_BLK_0001_0559 = 1
        elif dep_time_blk == "0600-0659":
            DEP_TIME_BLK_0600_0659 = 1
        elif dep_time_blk == "0700-0759":
            DEP_TIME_BLK_0700_0759 = 1
        elif dep_time_blk == "0800-0859":
            DEP_TIME_BLK_0800_0859 = 1
        elif dep_time_blk == "0900-0959":
            DEP_TIME_BLK_0900_0959 = 1
        elif dep_time_blk == "1000-1059":
            DEP_TIME_BLK_1000_1059 = 1
        elif dep_time_blk == "1100-1159":
            DEP_TIME_BLK1100_1159 = 1
        elif dep_time_blk == "1200-1259":
            DEP_TIME_BLK_1200_1259 = 1
        elif dep_time_blk == "1300-1359":
            DEP_TIME_BLK_1300_1359 = 1
        elif dep_time_blk == "1400-1459":
            DEP_TIME_BLK_1400_1459 = 1
        elif dep_time_blk == "1500-1559":
            DEP_TIME_BLK_1500_1559 = 1
        elif dep_time_blk == "1600-1659":
            DEP_TIME_BLK_1600_1659 = 1
        elif dep_time_blk == "1700-1759":
            DEP_TIME_BLK_1700_1759 = 1
        elif dep_time_blk == "1800-1859":
            DEP_TIME_BLK_1800_1859 = 1
        elif dep_time_blk == "1900-1959":
            DEP_TIME_BLK_1900_1959 = 1
        elif dep_time_blk == "2000-2059":
            DEP_TIME_BLK_2000_2059 = 1
        elif dep_time_blk == "2100-2159":
            DEP_TIME_BLK_2100_2159 = 1
        elif dep_time_blk == "2200-2259":
            DEP_TIME_BLK_2200_2259 = 1
        elif dep_time_blk == "2300-2359":
            DEP_TIME_BLK_2300_2359 = 1
        else:
            msg =  "Time Block is not selected! "

        # carrier_name = request.form.get('CARRIER_NAME') # works
        carrier_name = form_data["CARRIER_NAME"]
        CARRIER_NAME_Alaska_Airlines_Inc = 0
        CARRIER_NAME_Allegiant_Air = 0
        CARRIER_NAME_American_Airlines_Inc = 0
        CARRIER_NAME_American_Eagle_Airlines_Inc = 0
        CARRIER_NAME_Atlantic_Southeast_Airlines = 0
        CARRIER_NAME_Comair_Inc = 0
        CARRIER_NAME_Delta_Air_Lines_Inc = 0
        CARRIER_NAME_Endeavor_Air_Inc = 0
        CARRIER_NAME_Frontier_Airlines_Inc = 0
        CARRIER_NAME_Hawaiian_Airlines_Inc = 0
        CARRIER_NAME_JetBlue_Airways = 0
        CARRIER_NAME_Mesa_Airlines_Inc = 0
        CARRIER_NAME_Midwest_Airline,_Inc = 0
        CARRIER_NAME_SkyWest_Airlines_Inc = 0
        CARRIER_NAME_Southwest_Airlines_Co = 0
        CARRIER_NAME_Spirit_Air_Lines = 0
        CARRIER_NAME_United_Air_Lines_Inc = 0

        if carrier_name == "Alaska_Airlines_Inc": 
            CARRIER_NAME_Alaska_Airlines_Inc = 1
        elif carrier_name == "Allegiant_Air":
            CARRIER_NAME_Allegiant_Air = 1
        elif carrier_name == "American_Airlines_Inc":
            CARRIER_NAME_American_Airlines_Inc = 1
        elif carrier_name == "American_Eagle_Airlines_Inc":
            CARRIER_NAME_American_Eagle_Airlines_Inc = 1
        elif carrier_name == "Atlantic_Southeast_Airlines":
            CARRIER_NAME_Atlantic_Southeast_Airlines = 1
        elif carrier_name == "Comair_Inc":
            CARRIER_NAME_Comair_Inc = 1
        elif carrier_name == "Delta_Air_Line_Inc":
            CARRIER_NAME_Delta_Air_Lines_Inc = 1
        elif carrier_name == "Endeavor_Air_Inc":
            CARRIER_NAME_Endeavour_Air_Inc = 1
        elif carrier_name == "Frontier_Airlines_Inc":
            CARRIER_NAME_Frontier_Airlines_Inc = 1
        elif carrier_name == "Hawaiian_Airlines_Inc":
            CARRIER_NAME_Hawaiian_Airlines_Inc = 1
        elif carrier_name == "JetBlue_Airways":
            CARRIER_NAME_JetBlue_Airways = 1
        elif carrier_name == "Mesa_Airlines_Inc":
            CARRIER_NAME_Mesa_Airlines_Inc = 1
        elif carrier_name == "Midwest_Airline,_Inc":
            CARRIER_NAME_Midwest_Airlines_Inc = 1
        elif carrier_name == "SkyWest_Airlines_Inc":
            CARRIER_NAME_SkyWest_Airlines_Inc = 1
        elif carrier_name == "Southwest_Airlines_Co":
            CARRIER_NAME_Southwest_Airlines_Co = 1
        elif carrier_name == "Spirit_Air_Lines":
            CARRIER_NAME_Spirit_Air_Lines = 1
        elif carrier_name == "United_Air_Lines_Inc":
            CARRIER_NAME_United_Air_Lines_Inc = 1
        else:
            msg = msg + "Carrier Name is not selected! "

        departing_airport = form_data["DEPARTING_AIRPORT"]
        DEPARTING_AIRPORT_Adams_Field = 0
        DEPARTING_AIRPORT_Albany_International = 0
        DEPARTING_AIRPORT_Albuquerque_International_Sunport = 0
        DEPARTING_AIRPORT_Anchorage_International = 0
        DEPARTING_AIRPORT_Atlanta_Municipal = 0
        DEPARTING_AIRPORT_Austin___Bergstrom_International = 0
        DEPARTING_AIRPORT_Birmingham_Airport = 0
        DEPARTING_AIRPORT_Boise_Air_Terminal = 0
        DEPARTING_AIRPORT_Bradley_International = 0
        DEPARTING_AIRPORT_Charleston_International = 0
        DEPARTING_AIRPORT_Chicago_Midway_International = 0
        DEPARTING_AIRPORT_Chicago_OHare_International = 0
        DEPARTING_AIRPORT_Cincinnati_Northern_Kentucky_International = 0
        DEPARTING_AIRPORT_Cleveland_Hopkins_International = 0
        DEPARTING_AIRPORT_Dallas_Fort_Worth_Regional = 0
        DEPARTING_AIRPORT_Dallas_Love_Field = 0
        DEPARTING_AIRPORT_Des_Moines_Municipal = 0
        DEPARTING_AIRPORT_Detroit_Metro_Wayne_County = 0
        DEPARTING_AIRPORT_Douglas_Municipal = 0
        DEPARTING_AIRPORT_El_Paso_International = 0
        DEPARTING_AIRPORT_Eppley_Airfield = 0
        DEPARTING_AIRPORT_Fort_Lauderdale_Hollywood_International = 0
        DEPARTING_AIRPORT_Friendship_International = 0
        DEPARTING_AIRPORT_General_Mitchell_Field = 0
        DEPARTING_AIRPORT_Greater_Buffalo_International = 0
        DEPARTING_AIRPORT_Greenville_Spartanburg = 0
        DEPARTING_AIRPORT_Hollywood_Burbank_Midpoint = 0
        DEPARTING_AIRPORT_Honolulu_International = 0
        DEPARTING_AIRPORT_Houston_Intercontinental = 0
        DEPARTING_AIRPORT_Indianapolis_Muni_Weir_Cook = 0
        DEPARTING_AIRPORT_Jacksonville_International = 0
        DEPARTING_AIRPORT_James_M_Cox_Dayton_International = 0
        DEPARTING_AIRPORT_John_F_Kennedy_International = 0
        DEPARTING_AIRPORT_Kahului_Airport = 0
        DEPARTING_AIRPORT_Kansas_City_International = 0
        DEPARTING_AIRPORT_Keahole = 0
        DEPARTING_AIRPORT_Kent_County = 0
        DEPARTING_AIRPORT_LaGuardia = 0
        DEPARTING_AIRPORT_Lambert_St_Louis_International = 0
        DEPARTING_AIRPORT_Lihue_Airport = 0
        DEPARTING_AIRPORT_Logan_International = 0
        DEPARTING_AIRPORT_Long_Beach_Daugherty_Field = 0
        DEPARTING_AIRPORT_Los_Angeles_International = 0
        DEPARTING_AIRPORT_Louis_Armstrong_New_Orleans_International = 0
        DEPARTING_AIRPORT_McCarran_International = 0
        DEPARTING_AIRPORT_McGhee_Tyson = 0
        DEPARTING_AIRPORT_Memphis_International = 0
        DEPARTING_AIRPORT_Metropolitan_Oakland_International = 0
        DEPARTING_AIRPORT_Miami_International = 0
        DEPARTING_AIRPORT_Minneapolis_St_Paul_International = 0
        DEPARTING_AIRPORT_Myrtle_Beach_International = 0
        DEPARTING_AIRPORT_Nashville_International = 0
        DEPARTING_AIRPORT_Newark_Liberty_International = 0
        DEPARTING_AIRPORT_Norfolk_International = 0
        DEPARTING_AIRPORT_Northwest_Arkansas_Regional = 0
        DEPARTING_AIRPORT_Ontario_International = 0
        DEPARTING_AIRPORT_Orange_County = 0
        DEPARTING_AIRPORT_Orlando_International = 0
        DEPARTING_AIRPORT_Palm_Beach_International = 0
        DEPARTING_AIRPORT_Palm_Springs_International = 0
        DEPARTING_AIRPORT_Pensacola_Regional = 0
        DEPARTING_AIRPORT_Philadelphia_International = 0
        DEPARTING_AIRPORT_Phoenix_Sky_Harbor_International = 0
        DEPARTING_AIRPORT_Piedmont_Triad_International = 0
        DEPARTING_AIRPORT_Pittsburgh_International = 0
        DEPARTING_AIRPORT_Port_Columbus_International = 0
        DEPARTING_AIRPORT_Portland_International = 0
        DEPARTING_AIRPORT_Portland_International_Jetport = 0
        DEPARTING_AIRPORT_Puerto_Rico_International = 0
        DEPARTING_AIRPORT_Raleigh_Durham_International = 0
        DEPARTING_AIRPORT_Reno_Tahoe_International = 0
        DEPARTING_AIRPORT_Richmond_International = 0
        DEPARTING_AIRPORT_Rochester_Monroe_County = 0
        DEPARTING_AIRPORT_Ronald_Reagan_Washington_National = 0
        DEPARTING_AIRPORT_Sacramento_International = 0
        DEPARTING_AIRPORT_Salt_Lake_City_International = 0
        DEPARTING_AIRPORT_San_Antonio_International = 0
        DEPARTING_AIRPORT_San_Diego_International_Lindbergh_Fl = 0
        DEPARTING_AIRPORT_San_Francisco_International = 0
        DEPARTING_AIRPORT_San_Jose_International = 0
        DEPARTING_AIRPORT_Sanford_NAS = 0
        DEPARTING_AIRPORT_Savannah_Hilton_Head_International = 0
        DEPARTING_AIRPORT_Seattle_International = 0
        DEPARTING_AIRPORT_Southwest_Florida_International = 0
        DEPARTING_AIRPORT_Spokane_International = 0
        DEPARTING_AIRPORT_Standiford_Field = 0
        DEPARTING_AIRPORT_Stapleton_International = 0
        DEPARTING_AIRPORT_Syracuse_Hancock_International = 0
        DEPARTING_AIRPORT_Tampa_International = 0
        DEPARTING_AIRPORT_Theodore_Francis_Green_State = 0
        DEPARTING_AIRPORT_Truax_Field = 0
        DEPARTING_AIRPORT_Tucson_International = 0
        DEPARTING_AIRPORT_Tulsa_International = 0
        DEPARTING_AIRPORT_Washington_Dulles_International = 0
        DEPARTING_AIRPORT_Will_Rogers_World = 0
        DEPARTING_AIRPORT_William_P_Hobby = 0
        
        if departing_airport == "Adams_Field": 
            DEPARTING_AIRPORT_Adams_Field = 1
            principal_component = -1.93634827120755
        elif departing_airport == "Albany_International":
            DEPARTING_AIRPORT_Albany_International = 1
            principal_component = -20.6857635066734
        elif departing_airport == "Albuquerque_International_Sunport":
            DEPARTING_AIRPORT_Albuquerque_International_Sunport= 1
            principal_component = 12.4098287419658
        elif departing_airport == "Anchorage_International":
            DEPARTING_AIRPORT_Anchorage_International= 1
            principal_component = 54.6533611888066
        elif departing_airport == "Atlanta_Municipal":
            DEPARTING_AIRPORT_Atlanta_Municipal = 1
            principal_component = -9.69077073431462
        elif departing_airport == "Austin___Bergstrom_International":
            DEPARTING_AIRPORT_Austin___Bergstrom_International = 1
            principal_component = 3.685302933223
        elif departing_airport == "Birmingham_Airport":
            DEPARTING_AIRPORT_Birmingham_Airport = 1
            principal_component = -7.36054971676666
        elif departing_airport == "Boise_Air_Terminal":
            DEPARTING_AIRPORT_Boise_Air_Terminal = 1
            principal_component = 21.6624209089084
        elif departing_airport == "Bradley_International":
            DEPARTING_AIRPORT_Bradley_International = 1
            principal_component = -21.7728838546612
        elif departing_airport == "Charleston_International":
            DEPARTING_AIRPORT_Charleston_International = 1
            principal_component = -14.0437395702385
        elif departing_airport == "Chicago_Midway_International":
            DEPARTING_AIRPORT_Chicago_Midway_International = 1
            principal_component =  -6.71071011579775
        elif departing_airport == "Chicago_OHare_International":
            DEPARTING_AIRPORT_Chicago_OHare_International = 1
            principal_component =  -6.56495097883342
        elif departing_airport == "Cincinnati_Northern_Kentucky_International":
            DEPARTING_AIRPORT_Cincinnati_Northern_Kentucky_International = 1
            principal_component =  -9.67605043845804
        elif departing_airport == "Cleveland_Hopkins_International":
            DEPARTING_AIRPORT_Cleveland_Hopkins_International = 1
            principal_component =  -12.5927965683037
        elif departing_airport == "Dallas_Fort_Worth_Regional":
            DEPARTING_AIRPORT_Dallas_Fort_Worth_Regional = 1
            principal_component =  2.93248139706982
        elif departing_airport == "Dallas_Love_Field":
            DEPARTING_AIRPORT_Dallas_Love_Field = 1
            principal_component =  2.75761130025719
        elif departing_airport == "Des_Moines_Municipal":
            DEPARTING_AIRPORT_Des_Moines_Municipal = 1
            principal_component =  -0.800378638961914
        elif departing_airport == "Detroit_Metro_Wayne_County":
            DEPARTING_AIRPORT_Detroit_Metro_Wayne_County = 1
            principal_component =  -11.132963276105
        elif departing_airport == "Douglas_Municipal":
            DEPARTING_AIRPORT_Douglas_Municipal = 1
            principal_component =  -13.2449589592801
        elif departing_airport == "El_Paso_International":
            DEPARTING_AIRPORT_El_Paso_International = 1
            principal_component =  12.3168841378474
        elif departing_airport == "Eppley_Airfield":
            DEPARTING_AIRPORT_Eppley_Airfield = 1
            principal_component =  1.44339162943537
        elif departing_airport == "Fort_Lauderdale_Hollywood_International":
            DEPARTING_AIRPORT_Fort_Lauderdale_Hollywood_International = 1
            principal_component =  -13.6442243234769
        elif departing_airport == "Friendship_International":
            DEPARTING_AIRPORT_Friendship_International = 1
            principal_component =  -17.6723701585087
        elif departing_airport == "General_Mitchell_Field":
            DEPARTING_AIRPORT_General_Mitchell_Field = 1
            principal_component =  -6.61476204502319
        elif departing_airport == "Greater_Buffalo_International":
            DEPARTING_AIRPORT_Greater_Buffalo_International = 1
            principal_component =  -15.7673025014165
        elif departing_airport == "Greenville_Spartanburg":
            DEPARTING_AIRPORT_Greenville_Spartanburg = 1
            principal_component =  -11.9546480209898
        elif departing_airport == "Hollywood_Burbank_Midpoint":
            DEPARTING_AIRPORT_Hollywood_Burbank_Midpoint = 1
            principal_component =  24.1868211147305
        elif departing_airport == "Honolulu_International":
            DEPARTING_AIRPORT_Honolulu_International = 1
            principal_component =  64.2568546251237
        elif departing_airport == "Houston_Intercontinental":
            DEPARTING_AIRPORT_Houston_Intercontinental = 1
            principal_component =  1.36621931293239
        elif departing_airport == "Indianapolis_Muni_Weir_Cook":
            DEPARTING_AIRPORT_Indianapolis_Muni_Weir_Cook = 1
            principal_component =  -8.09307188497662
        elif departing_airport == "Jacksonville_International":
            DEPARTING_AIRPORT_Jacksonville_International = 1
            principal_component =  -12.2948186774707
        elif departing_airport == "James_M_Cox_Dayton_International":
            DEPARTING_AIRPORT_James_M_Cox_Dayton_International = 1
            principal_component =  -10.1604759598199
        elif departing_airport == "John_F_Kennedy_International":
            DEPARTING_AIRPORT_John_F_Kennedy_International = 1
            principal_component =  -20.6252556318339
        elif departing_airport == "Kahului_Airport":
            DEPARTING_AIRPORT_Kahului_Airport = 1
            principal_component =  62.7877211513013
        elif departing_airport == "Kansas_City_International":
            DEPARTING_AIRPORT_Kansas_City_International = 1
            principal_component =  0.349589415000413
        elif departing_airport == "Keahole":
            DEPARTING_AIRPORT_Keahole = 1
            principal_component =  62.4488614640596
        elif departing_airport == "Kent_County":
            DEPARTING_AIRPORT_Kent_County = 1
            principal_component =  -8.98277100224804
        elif departing_airport == "LaGuardia":
            DEPARTING_AIRPORT_LaGuardia = 1
            principal_component =  -20.5322222476569
        elif departing_airport == "Lambert_St_Louis_International":
            DEPARTING_AIRPORT_Lambert_St_Louis_International = 1
            principal_component =  -3.97343396212939
        elif departing_airport == "Lihue_Airport":
            DEPARTING_AIRPORT_Lihue_Airport = 1
            principal_component =  65.6518818014635
        elif departing_airport == "Logan_International":
            DEPARTING_AIRPORT_Logan_International = 1
            principal_component =  -23.4662522662917
        elif departing_airport == "Long_Beach_Daugherty_Field":
            DEPARTING_AIRPORT_Long_Beach_Daugherty_Field = 1
            principal_component =  23.9960457618483
        elif departing_airport == "Los_Angeles_International":
            DEPARTING_AIRPORT_Los_Angeles_International = 1
            principal_component =  24.2476116804298
        elif departing_airport == "Louis_Armstrong_New_Orleans_International":
            DEPARTING_AIRPORT_Louis_Armstrong_New_Orleans_International = 1
            principal_component =  -3.71862726590094
        elif departing_airport == "McCarran_International":
            DEPARTING_AIRPORT_McCarran_International = 1
            principal_component =  20.9046990220783
        elif departing_airport == "McGhee_Tyson":
            DEPARTING_AIRPORT_McGhee_Tyson = 1
            principal_component =  -10.2165578340641
        elif departing_airport == "Memphis_International":
            DEPARTING_AIRPORT_Memphis_International = 1
            principal_component =  -4.20283932101914
        elif departing_airport == "Metropolitan_Oakland_International":
            DEPARTING_AIRPORT_Metropolitan_Oakland_International = 1
            principal_component =  27.8985493704798
        elif departing_airport == "Miami_International":
            DEPARTING_AIRPORT_Miami_International = 1
            principal_component =  -13.4984999836519
        elif departing_airport == "Minneapolis_St_Paul_International":
            DEPARTING_AIRPORT_Minneapolis_St_Paul_International = 1
            principal_component =  -1.37975814190118
        elif departing_airport == "Myrtle_Beach_International":
            DEPARTING_AIRPORT_Myrtle_Beach_International = 1
            principal_component =  -15.184517232287
        elif departing_airport == "Nashville_International":
            DEPARTING_AIRPORT_Nashville_International = 1
            principal_component =  -7.54215926180698
        elif departing_airport == "Newark_Liberty_International":
            DEPARTING_AIRPORT_Newark_Liberty_International = 1
            principal_component =  -20.2329977974255
        elif departing_airport == "Norfolk_International":
            DEPARTING_AIRPORT_Norfolk_International = 1
            principal_component =  -18.046207251953
        elif departing_airport == "Northwest_Arkansas_Regional":
            DEPARTING_AIRPORT_Norwest_Arkansas_Regional = 1
            principal_component =  0.0696049629819364
        elif departing_airport == "Ontario_International":
            DEPARTING_AIRPORT_Ontario_International = 1
            principal_component =  23.4365361800502
        elif departing_airport == "Orange_County":
            DEPARTING_AIRPORT_Orange_County = 1
            principal_component =  23.7182595694605
        elif departing_airport == "Orlando_International":
            DEPARTING_AIRPORT_Orlando_International = 1
            principal_component =  -12.5712829971084
        elif departing_airport == "Palm_Beach_International":
            DEPARTING_AIRPORT_Palm_Beach_International = 1
            principal_component =  -13.7277060334484
        elif departing_airport == "Palm_Springs_International":
            DEPARTING_AIRPORT_Palm_Springs_International = 1
            principal_component =  22.3511198653878
        elif departing_airport == "Pensacola_Regional":
            DEPARTING_AIRPORT_Pensacola_Regional = 1
            principal_component =  -6.7991666924273
        elif departing_airport == "Philadelphia_International":
            DEPARTING_AIRPORT_Philadelphia_International = 1
            principal_component =  -19.1221761524601
        elif departing_airport == "Phoenix_Sky_Harbor_International":
            DEPARTING_AIRPORT_Phoenix_Sky_Harbor_International = 1
            principal_component =  17.8755061076626
        elif departing_airport == "Piedmont_Triad_International":
            DEPARTING_AIRPORT_Piedmont_Triad_International = 1
            principal_component =  -14.2737444755896
        elif departing_airport == "Pittsburgh_International":
            DEPARTING_AIRPORT_Pittsburgh_International = 1
            principal_component =  -14.1659903189665    
        elif departing_airport == "Port_Columbus_International":
            DEPARTING_AIRPORT_Port_Columbus_International = 1
            principal_component =  -11.5050716207843
        elif departing_airport == "Portland_International":
            DEPARTING_AIRPORT_Portland_International = 1
            principal_component =  27.9418038643646
        elif departing_airport == "Portland_International_Jetport":
            DEPARTING_AIRPORT_Portland_International_Jetport = 1
            principal_component =  -24.2213864038255
        elif departing_airport == "Puerto_Rico_International":
            DEPARTING_AIRPORT_Puerto_Rico_International = 1
            principal_component =  -27.4611527952877
        elif departing_airport == "Raleigh_Durham_International":
            DEPARTING_AIRPORT_Raleigh_Durham_International = 1
            principal_component =  -15.4246073873283
        elif departing_airport == "Reno_Tahoe_International":
            DEPARTING_AIRPORT_Reno_Tahoe_International = 1
            principal_component =  25.3730884720862
        elif departing_airport == "Richmond_International":
            DEPARTING_AIRPORT_Richmond_International = 1
            principal_component =  -16.9537692747924
        elif departing_airport == "Rochester_Monroe_County":
            DEPARTING_AIRPORT_Rochester_Monroe_County = 1
            principal_component =  -16.8389220619619
        elif departing_airport == "Ronald_Reagan_Washington_National":
            DEPARTING_AIRPORT_Ronald_Reagan_Washington_National = 1
            principal_component =  -17.2930866986965
        elif departing_airport == "Sacramento_International":
            DEPARTING_AIRPORT_Sacramento_International = 1
            principal_component =  27.2271610315139
        elif departing_airport == "Salt_Lake_City_International":
            DEPARTING_AIRPORT_Salt_Lake_City_International = 1
            principal_component =  17.5249649138303
        elif departing_airport == "San_Antonio_International":
            DEPARTING_AIRPORT_San_Antonio_International = 1
            principal_component =  4.5113566804389
        elif departing_airport == "San_Diego_International_Lindbergh_Fl":
            DEPARTING_AIRPORT_San_Diego_International_Lindbergh_Fl = 1
            principal_component =  23.0784606020781
        elif departing_airport == "San_Francisco_International":
            DEPARTING_AIRPORT_San_Francisco_International = 1
            principal_component =  28.0566969916995
        elif departing_airport == "San_Jose_International":
            DEPARTING_AIRPORT_San_Jose_International = 1
            principal_component =  27.6338305395653
        elif departing_airport == "Sanford_NAS":
            DEPARTING_AIRPORT_Sanford_NAS = 1
            principal_component =  -12.6706122500012
        elif departing_airport == "Savannah_Hilton_Head_International":
            DEPARTING_AIRPORT_Savannah_Hilton_Head_International = 1
            principal_component =  -12.8493455044447
        elif departing_airport == "Seattle_International":
            DEPARTING_AIRPORT_Seattle_International = 1
            principal_component =  27.5750323590786
        elif departing_airport == "Southwest_Florida_International":
            DEPARTING_AIRPORT_Southwest_Florida_International = 1
            principal_component =  -12.06204007351
        elif departing_airport == "Spokane_International":
            DEPARTING_AIRPORT_Spokane_International = 1
            principal_component =  22.7989778612633
        elif departing_airport == "Standiford_Field":
            DEPARTING_AIRPORT_Standiford_Field = 1
            principal_component =  -8.57054282380411
        elif departing_airport == "Stapleton_International":
            DEPARTING_AIRPORT_Stapleton_International = 1
            principal_component =  10.4866316867009
        elif departing_airport == "Syracuse_Hancock_International":
            DEPARTING_AIRPORT_Syracuse_Hancock_International = 1
            principal_component =  -18.4061179833928
        elif departing_airport == "Tampa_International":
            DEPARTING_AIRPORT_Tampa_International = 1
            principal_component =  -11.3430747852302
        elif departing_airport == "Theodore_Francis_Green_State":
            DEPARTING_AIRPORT_Theodore_Francis_Green_State = 1
            principal_component =  -23.0199140469318
        elif departing_airport == "Truax_Field":
            DEPARTING_AIRPORT_Truax_Field = 1
            principal_component =  -5.18409538809567
        elif departing_airport == "Tucson_International":
            DEPARTING_AIRPORT_Tucson_International = 1
            principal_component =  16.8638814864607
        elif departing_airport == "Tulsa_International":
            DEPARTING_AIRPORT_Tulsa_International = 1
            principal_component =  1.65473605100322
        elif departing_airport == "Washington_Dulles_International":
            DEPARTING_AIRPORT_Washington_Dulles_International = 1
            principal_component =  -16.8762376312366
        elif departing_airport == "Will_Rogers_World":
            DEPARTING_AIRPORT_Will_Rogers_World = 1
            principal_component =  3.39907362894442
        elif departing_airport == "William_P_Hobby":
            DEPARTING_AIRPORT_William_P_Hobby = 1
            principal_component =  1.31946738882159
        else:
            msg = msg + "Departing Airport is not selected! "

        

        test_inputs = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0]]


        # !!! below order can't be changed
        test_inputs[0][0] = MONTH
        test_inputs[0][1] = DAY_OF_WEEK
        test_inputs[0][2] = DISTANCE_GROUP
        test_inputs[0][3] = SEGMENT_NUMBER
        test_inputs[0][4] = CONCURRENT_FLIGHTS
        test_inputs[0][5] = NUMBER_OF_SEATS
        test_inputs[0][6] = AIRPORT_FLIGHTS_MONTH
        test_inputs[0][7] = AIRLINE_FLIGHTS_MONTH
        test_inputs[0][8] = AIRLINE_AIRPORT_FLIGHTS_MONTH
        test_inputs[0][9] = AVG_MONTHLY_PASS_AIRPORT
        test_inputs[0][10] = AVG_MONTHLY_PASS_AIRLINE
        test_inputs[0][11] = FLT_ATTENDANTS_PER_PASS
        test_inputs[0][12] = GROUND_SERV_PER_PASS
        test_inputs[0][13] = PLANE_AGE
        test_inputs[0][14] = PREVIOUS_AIRPORT
        test_inputs[0][15] = PRCP
        test_inputs[0][16] = SNOW
        test_inputs[0][17] = SNWD
        test_inputs[0][18] = TMAX
        test_inputs[0][19] = AWND
        test_inputs[0][20] = DEP_TIME_BLK_0001_0559
        test_inputs[0][21] = DEP_TIME_BLK_0600_0659
        test_inputs[0][22] = DEP_TIME_BLK_0700_0759
        test_inputs[0][23] = DEP_TIME_BLK_0800_0859
        test_inputs[0][24] = DEP_TIME_BLK_0900_0959
        test_inputs[0][25] = DEP_TIME_BLK_1000_1059
        test_inputs[0][26] = DEP_TIME_BLK_1100_1159
        test_inputs[0][27] = DEP_TIME_BLK_1200_1259
        test_inputs[0][28] = DEP_TIME_BLK_1300_1359
        test_inputs[0][29] = DEP_TIME_BLK_1400_1459
        test_inputs[0][30] = DEP_TIME_BLK_1500_1559
        test_inputs[0][31] = DEP_TIME_BLK_1600_1659
        test_inputs[0][32] = DEP_TIME_BLK_1700_1759
        test_inputs[0][33] = DEP_TIME_BLK_1800_1859
        test_inputs[0][34] = DEP_TIME_BLK_1900_1959
        test_inputs[0][35] = DEP_TIME_BLK_2000_2059
        test_inputs[0][36] = DEP_TIME_BLK_2100_2159
        test_inputs[0][37] = DEP_TIME_BLK_2200_2259
        test_inputs[0][38] = DEP_TIME_BLK_2300_2359
        test_inputs[0][39] = CARRIER_NAME_Alaska_Airlines_Inc
        test_inputs[0][40] = CARRIER_NAME_Allegiant_Air
        test_inputs[0][41] = CARRIER_NAME_American_Airlines_Inc
        test_inputs[0][42] = CARRIER_NAME_American_Eagle_Airlines_Inc
        test_inputs[0][43] = CARRIER_NAME_Atlantic_Southeast_Airlines
        test_inputs[0][44] = CARRIER_NAME_Comair_Inc
        test_inputs[0][45] = CARRIER_NAME_Delta_Air_Lines_Inc
        test_inputs[0][46] = CARRIER_NAME_Endeavor_Air_Inc
        test_inputs[0][47] = CARRIER_NAME_Frontier_Airlines_Inc
        test_inputs[0][48] = CARRIER_NAME_Hawaiian_Airlines_Inc
        test_inputs[0][49] = CARRIER_NAME_JetBlue_Airways
        test_inputs[0][50] = CARRIER_NAME_Mesa_Airlines_Inc
        test_inputs[0][51] = CARRIER_NAME_Midwest_Airline,_Inc
        test_inputs[0][52] = CARRIER_NAME_SkyWest_Airlines_Inc
        test_inputs[0][53] = CARRIER_NAME_Southwest_Airlines_Co
        test_inputs[0][54] = CARRIER_NAME_Spirit_Air_Lines
        test_inputs[0][55] = CARRIER_NAME_United_Air_Lines_Inc
        test_inputs[0][56] = DEPARTING_AIRPORT_Adams_Field
        test_inputs[0][57] = DEPARTING_AIRPORT_Albany_International
        test_inputs[0][58] = DEPARTING_AIRPORT_Albuquerque_International_Sunport
        test_inputs[0][59] = DEPARTING_AIRPORT_Anchorage_International
        test_inputs[0][60] = DEPARTING_AIRPORT_Atlanta_Municipal
        test_inputs[0][61] = DEPARTING_AIRPORT_Austin___Bergstrom_International
        test_inputs[0][62] = DEPARTING_AIRPORT_Birmingham_Airport
        test_inputs[0][63] = DEPARTING_AIRPORT_Boise_Air_Terminal
        test_inputs[0][64] = DEPARTING_AIRPORT_Bradley_International
        test_inputs[0][65] = DEPARTING_AIRPORT_Charleston_International
        test_inputs[0][66] = DEPARTING_AIRPORT_Chicago_Midway_International
        test_inputs[0][67] = DEPARTING_AIRPORT_Chicago_OHare_International
        test_inputs[0][68] = DEPARTING_AIRPORT_Cincinnati_Northern_Kentucky_International
        test_inputs[0][69] = DEPARTING_AIRPORT_Cleveland_Hopkins_International
        test_inputs[0][70] = DEPARTING_AIRPORT_Dallas_Fort_Worth_Regional
        test_inputs[0][71] = DEPARTING_AIRPORT_Dallas_Love_Field
        test_inputs[0][72] = DEPARTING_AIRPORT_Des_Moines_Municipal
        test_inputs[0][73] = DEPARTING_AIRPORT_Detroit_Metro_Wayne_County
        test_inputs[0][74] = DEPARTING_AIRPORT_Douglas_Municipal
        test_inputs[0][75] = DEPARTING_AIRPORT_El_Paso_International
        test_inputs[0][76] = DEPARTING_AIRPORT_Eppley_Airfield
        test_inputs[0][77] = DEPARTING_AIRPORT_Fort_Lauderdale_Hollywood_International
        test_inputs[0][78] = DEPARTING_AIRPORT_Friendship_International
        test_inputs[0][79] = DEPARTING_AIRPORT_General_Mitchell_Field
        test_inputs[0][80] = DEPARTING_AIRPORT_Greater_Buffalo_International
        test_inputs[0][81] = DEPARTING_AIRPORT_Greenville_Spartanburg
        test_inputs[0][82] = DEPARTING_AIRPORT_Hollywood_Burbank_Midpoint
        test_inputs[0][83] = DEPARTING_AIRPORT_Honolulu_International
        test_inputs[0][84] = DEPARTING_AIRPORT_Houston_Intercontinental
        test_inputs[0][85] = DEPARTING_AIRPORT_Indianapolis_Muni_Weir_Cook
        test_inputs[0][86] = DEPARTING_AIRPORT_Jacksonville_International
        test_inputs[0][87] = DEPARTING_AIRPORT_James_M_Cox_Dayton_International
        test_inputs[0][88] = DEPARTING_AIRPORT_John_F_Kennedy_International
        test_inputs[0][89] = DEPARTING_AIRPORT_Kahului_Airport
        test_inputs[0][90] = DEPARTING_AIRPORT_Kansas_City_International
        test_inputs[0][91] = DEPARTING_AIRPORT_Keahole
        test_inputs[0][92] = DEPARTING_AIRPORT_Kent_County
        test_inputs[0][93] = DEPARTING_AIRPORT_LaGuardia
        test_inputs[0][94] = DEPARTING_AIRPORT_Lambert_St_Louis_International
        test_inputs[0][95] = DEPARTING_AIRPORT_Lihue_Airport
        test_inputs[0][96] = DEPARTING_AIRPORT_Logan_International
        test_inputs[0][97] = DEPARTING_AIRPORT_Long_Beach_Daugherty_Field
        test_inputs[0][98] = DEPARTING_AIRPORT_Los_Angeles_International
        test_inputs[0][99] = DEPARTING_AIRPORT_Louis_Armstrong_New_Orleans_International
        test_inputs[0][100] = DEPARTING_AIRPORT_McCarran_International
        test_inputs[0][101] = DEPARTING_AIRPORT_McGhee_Tyson
        test_inputs[0][102] = DEPARTING_AIRPORT_Memphis_International
        test_inputs[0][103] = DEPARTING_AIRPORT_Metropolitan_Oakland_International
        test_inputs[0][104] = DEPARTING_AIRPORT_Miami_International
        test_inputs[0][105] = DEPARTING_AIRPORT_Minneapolis_St_Paul_International
        test_inputs[0][106] = DEPARTING_AIRPORT_Myrtle_Beach_International
        test_inputs[0][107] = DEPARTING_AIRPORT_Nashville_International
        test_inputs[0][108] = DEPARTING_AIRPORT_Newark_Liberty_International
        test_inputs[0][109] = DEPARTING_AIRPORT_Norfolk_International
        test_inputs[0][110] = DEPARTING_AIRPORT_Northwest_Arkansas_Regional
        test_inputs[0][111] = DEPARTING_AIRPORT_Ontario_International
        test_inputs[0][112] = DEPARTING_AIRPORT_Orange_County
        test_inputs[0][113] = DEPARTING_AIRPORT_Orlando_International
        test_inputs[0][114] = DEPARTING_AIRPORT_Palm_Beach_International
        test_inputs[0][115] = DEPARTING_AIRPORT_Palm_Springs_International
        test_inputs[0][116] = DEPARTING_AIRPORT_Pensacola_Regional
        test_inputs[0][117] = DEPARTING_AIRPORT_Philadelphia_International
        test_inputs[0][118] = DEPARTING_AIRPORT_Phoenix_Sky_Harbor_International
        test_inputs[0][119] = DEPARTING_AIRPORT_Piedmont_Triad_International
        test_inputs[0][120] = DEPARTING_AIRPORT_Pittsburgh_International
        test_inputs[0][121] = DEPARTING_AIRPORT_Port_Columbus_International
        test_inputs[0][122] = DEPARTING_AIRPORT_Portland_International
        test_inputs[0][123] = DEPARTING_AIRPORT_Portland_International_Jetport
        test_inputs[0][124] = DEPARTING_AIRPORT_Puerto_Rico_International
        test_inputs[0][125] = DEPARTING_AIRPORT_Raleigh_Durham_International
        test_inputs[0][126] = DEPARTING_AIRPORT_Reno_Tahoe_International
        test_inputs[0][127] = DEPARTING_AIRPORT_Richmond_International
        test_inputs[0][128] = DEPARTING_AIRPORT_Rochester_Monroe_County
        test_inputs[0][129] = DEPARTING_AIRPORT_Ronald_Reagan_Washington_National
        test_inputs[0][130] = DEPARTING_AIRPORT_Sacramento_International
        test_inputs[0][131] = DEPARTING_AIRPORT_Salt_Lake_City_International
        test_inputs[0][132] = DEPARTING_AIRPORT_San_Antonio_International
        test_inputs[0][133] = DEPARTING_AIRPORT_San_Diego_International_Lindbergh_Fl
        test_inputs[0][134] = DEPARTING_AIRPORT_San_Francisco_International
        test_inputs[0][135] = DEPARTING_AIRPORT_San_Jose_International
        test_inputs[0][136] = DEPARTING_AIRPORT_Sanford_NAS
        test_inputs[0][137] = DEPARTING_AIRPORT_Savannah_Hilton_Head_International
        test_inputs[0][138] = DEPARTING_AIRPORT_Seattle_International
        test_inputs[0][139] = DEPARTING_AIRPORT_Southwest_Florida_International
        test_inputs[0][140] = DEPARTING_AIRPORT_Spokane_International
        test_inputs[0][141] = DEPARTING_AIRPORT_Standiford_Field
        test_inputs[0][142] = DEPARTING_AIRPORT_Stapleton_International
        test_inputs[0][143] = DEPARTING_AIRPORT_Syracuse_Hancock_International
        test_inputs[0][144] = DEPARTING_AIRPORT_Tampa_International
        test_inputs[0][145] = DEPARTING_AIRPORT_Theodore_Francis_Green_State
        test_inputs[0][146] = DEPARTING_AIRPORT_Truax_Field
        test_inputs[0][147] = DEPARTING_AIRPORT_Tucson_International
        test_inputs[0][148] = DEPARTING_AIRPORT_Tulsa_International
        test_inputs[0][149] = DEPARTING_AIRPORT_Washington_Dulles_International
        test_inputs[0][150] = DEPARTING_AIRPORT_Will_Rogers_World
        test_inputs[0][151] = DEPARTING_AIRPORT_William_P_Hobby
        test_inputs[0][152] = principal_component


    #   test_array = np.asarray(test_inputs, dtype=np.float32)

        # 2) MinMaxScaler(): dummied fields + other integer fields
    #   X_train = pd.read_csv("data\HomeEquityLoans_X_train.csv")   # should be from DB?
    #   X_scaler = MinMaxScaler().fit(X_train)
    #   test_array_scaled = X_scaler.transform(test_array)

    #   gridlr_predictions = gridlr.predict(test_array_scaled) # error 500: Failed to load resources: the server responed with a status of 500 (INTERNAL SERVER ERROR)
    #   gridsvm_predictions = gridsvm.predict(test_array_scaled)
    #   griddeep_predictions = griddeep.predict(test_array_scaled)

    #   all_predictions = zip(gridlr_predictions, gridsvm_predictions, griddeep_predictions)

    #   final_predictions = []
    #   for tup in all_predictions:
    #       final_predictions.append( max( set(list(tup)), key=list(tup).count ) )
    #       final=final_predictions[0]

    #    if final == 1:
    #        finalresult = "Late"
    #    else:
    #        finalresult = "On-Time"

    #    return render_template("modelprediction.html", prediction = finalresult, msg=msg, form_data=form_data)
    return render_template("predictonesample.html",prediction="flask_return")

if __name__ == '__main__':
    app.run()


