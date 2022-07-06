## flask
import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, jsonify, request
import logging
from time import sleep

from sklearn.metrics import accuracy_score
import joblib as jb
from profanity_check import predict, predict_prob

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
# from sqlalchemy import create engine

app = Flask(__name__, static_url_path='')

from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler


with open('pickles/model.pkl', 'rb') as f:
    gridgb = jb.load(f)
#with open('pickles/gridsvm.pkl', 'rb') as f:
#   gridsvm =joblib.load(f)
#with open('pickles/griddeep.pkl', 'rb') as f:
#   griddeep = joblib.load(f)

gridmodels = {'Gradient Boosted Model': gridgb}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictonesample", methods=["GET", "POST"])  # flask request: bring data back to Form by render jinja template
# @app.route("/predictonesample/<inpdata")
def predictioninput():
    finalresult = ""
    msg = ""
    print("beginning of predictioninput")
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
        "AWND":"",
        "DEP_TIME_BLK":"",
        "CARRIER_NAME":"",
        "DEPARTING_AIRPORT":"" }

# print(request.method)      # initialization here for return "" for GET
    if request.method =="POST":
        print(request.method)
        msg=""
        form_data = request.form

        # validate form data: https://stackoverflow.com/questions/55772012/how-to-validate-html-forms-in-python-flask    
        if form_data["MONTH"]!="" \
        and form_data["DAY_OF_WEEK"]!="" \
        and form_data["DISTANCE_GROUP"]!="" \
        and form_data["SEGMENT_NUMBER"]!="" \
        and form_data["CONCURRENT_FLIGHTS"]!="" \
        and form_data["NUMBER_OF_SEATS"]!="" \
        and form_data["AIRPORT_FLIGHTS_MONTH"]!="" \
        and form_data["AIRLINE_FLIGHTS_MONTH"]!="" \
        and form_data["AIRLINE_AIRPORT_FLIGHTS_MONTH"]!="" \
        and form_data["AVG_MONTHLY_PASS_AIRLINE"]!="" \
        and form_data["FLT_ATTENDANTS_PER_PASS"]!="" \
        and form_data["GROUND_SERV_PER_PASS"]!="" \
        and form_data["PLANE_AGE"]!="" \
        and form_data["PREVIOUS_AIRPORT"]!="" \
        and form_data["PRCP"]!="" \
        and form_data["SNOW"]!="" \
        and form_data["SNWD"]!="" \
        and form_data["TMAX"]!="" \
        and form_data["AWND"]!="" \
        and ((form_data["DEP_TIME_BLK"]=="0001_0559") or (form_data["DEP_TIME_BLK"]=="0600_0659") \
        or (form_data["DEP_TIME_BLK"]=="0700_0759") or (form_data["DEP_TIME_BLK"]=="0800_0859") \
        or (form_data["DEP_TIME_BLK"]=="0900_0959") or (form_data["DEP_TIME_BLK"]=="1000_1059") \
        or (form_data["DEP_TIME_BLK"]=="1100_1159") or (form_data["DEP_TIME_BLK"]=="1200_1259") \
        or (form_data["DEP_TIME_BLK"]=="1300_1359") or (form_data["DEP_TIME_BLK"]=="1400_1459") \
        or (form_data["DEP_TIME_BLK"]=="1500_1559") or (form_data["DEP_TIME_BLK"]=="1600_1659") \
        or (form_data["DEP_TIME_BLK"]=="1700_1759") or (form_data["DEP_TIME_BLK"]=="1800_1859") \
        or (form_data["DEP_TIME_BLK"]=="1900_1959") or (form_data["DEP_TIME_BLK"]=="2000_2059") \
        or (form_data["DEP_TIME_BLK"]=="2100_2159") or (form_data["DEP_TIME_BLK"]=="2200_2259") \
        or (form_data["DEP_TIME_BLK"]=="2300_1359")) \
        and ((form_data["CARRIER_NAME"]=="Alaska_Airlines_Inc") or (form_data["CARRIER_NAME"]=="Allegiant_Air") \
        or (form_data["CARRIER_NAME"]=="American_Airlines_Inc") or (form_data["CARRIER_NAME"]=="American_Eagle_Airlines_Inc") \
        or (form_data["CARRIER_NAME"]=="Atlantic_Southeast_Airlines") or (form_data["CARRIER_NAME"]=="Comair_Inc") \
        or (form_data["CARRIER_NAME"]=="Delta_Air_Lines_Inc") or (form_data["CARRIER_NAME"]=="Endeavor_Air_Inc") \
        or (form_data["CARRIER_NAME"]=="Frontier_Airlines_Inc") or (form_data["CARRIER_NAME"]=="Hawaiian_Airlines_Inc") \
        or (form_data["CARRIER_NAME"]=="JetBlue_Airways") or (form_data["CARRIER_NAME"]=="Mesa_Airlines_Inc") \
        or (form_data["CARRIER_NAME"]=="Midwest_Airline,_Inc") or (form_data["CARRIER_NAME"]=="Spirit_Air_Lines") \
        or (form_data["CARRIER_NAME"]=="Southwest_Airlines_Co") or (form_data["CARRIER_NAME"]=="") \
        or (form_data["CARRIER_NAME"]=="United_Air_Lines_Inc")) \
        and ((form_data["DEPARTING_AIRPORT"]=="Chicago_OHare_International") \
        or (form_data["DEPARTING_AIRPORT"]=="Houston_Intercontinental") \
        or (form_data["DEPARTING_AIRPORT"]=="Los_Angeles_International")):


        # validate form data: https://stackoverflow.com/questions/55772012/how-to-validate-html-forms-in-python-flask

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
 
            MONTH = float(form_data["MONTH"])
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
            DEPARTING_AIRPORT_Chicago_OHare_International = 0
            DEPARTING_AIRPORT_Houston_Intercontinental = 0
            DEPARTING_AIRPORT_Los_Angeles_International = 0 

            if departing_airport == "Chicago_OHare_International":
                DEPARTING_AIRPORT_Chicago_OHare_International = 1
                principal_component =  -6.56495097883342
            elif departing_airport == "Houston_Intercontinental":
                DEPARTING_AIRPORT_Houston_Intercontinental = 1
                principal_component =  1.36621931293239
            elif departing_airport == "Los_Angeles_International":
                DEPARTING_AIRPORT_Los_Angeles_International = 1
                principal_component =  24.2476116804298
            else:
                msg = msg + "Departing Airport is not selected! "

            

            test_inputs = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
            test_inputs[0][56] = DEPARTING_AIRPORT_Chicago_OHare_International
            test_inputs[0][57] = DEPARTING_AIRPORT_Houston_Intercontinental
            test_inputs[0][58] = DEPARTING_AIRPORT_Los_Angeles_International
            test_inputs[0][59] = principal_component

            test_array = np.asarray(test_inputs, dtype=np.float32)
            print(test_array)


            # 2) StandardScaler(): dummied fields + other integer fields
            X_train = pd.read_csv("data\X_train_data.csv")   # should be from DB?
            X_scaler = StandardScaler().fit(X_train)
            test_array_scaled = X_scaler.transform(test_array)

            gridgb_predictions = gridgb.predict(test_array_scaled) # error 500: Failed to load resources: the server responed with a status of 500 (INTERNAL SERVER ERROR)
            final = gridgb_predictions
        #   gridsvm_predictions = gridsvm.predict(test_array_scaled)
        #   griddeep_predictions = griddeep.predict(test_array_scaled)

        #   all_predictions = zip(gridlr_predictions, gridsvm_predictions, griddeep_predictions)
        #    all_predictions = zip(gridgb_predictions)
        #    final_predictions = []
        #    for tup in all_predictions:
        #       final_predictions.append( max( set(list(tup)), key=list(tup).count ) )
        
        #       final=final_predictions[0]

            if final == 1:
                finalresult = "Late"
            else:
                finalresult = "On-Time"
        else:
            msg = msg + "Please complete inputs"

    return render_template("modelprediction.html", prediction = finalresult)
#    return render_template("modelprediction.html", prediction = finalresult, msg=msg, form_data=form_data)
    
if __name__ == '__main__':
    app.run()


