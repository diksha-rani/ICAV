#Importing required libraries
from flask import Flask
from flask_restful import Api,Resource
import csv

#created an flask app
app = Flask(__name__)
#created an API object
api=Api(app)
class API_One(Resource):
    def get(self,rows):
        try:
            data_csv=[]
            #reading data from csv file 
            with open('books.csv','r') as f:
                data = csv.reader(f)
                datalines=list(data)
                #creating a header list
                headers = [datalines[0][x] for x in range(0,10)]
                
                for row in range(1,rows+1):
                    data_csv.append({headers[0]:datalines[row][0],
                    headers[1]:datalines[row][1],
                    headers[2]:datalines[row][2],
                    headers[3]:datalines[row][3],
                    headers[4]:datalines[row][4],
                    headers[5]:datalines[row][5],
                    headers[6]:datalines[row][6],
                    headers[7]:datalines[row][7],
                    headers[8]:datalines[row][8],
                    headers[9]:datalines[row][9]}
                    )

            return {"books":data_csv}
        
        except Exception as e:
            return {"Message":'Something went Wrong!'}

class API_Two(Resource):
    def get(self,filter_data):
        try:
            data_csv=[]
            #reading data from csv file
            with open('books.csv','r') as f:
                data = csv.reader(f)
                datalines=list(data)
                #creating a header list
                headers = [datalines[0][x] for x in range(0,10)]
                for row in range(1,len(datalines)):
                    if filter_data in datalines[row]:
                        data_csv.append({headers[0]:datalines[row][0],
                    headers[1]:datalines[row][1],
                    headers[2]:datalines[row][2],
                    headers[3]:datalines[row][3],
                    headers[4]:datalines[row][4],
                    headers[5]:datalines[row][5],
                    headers[6]:datalines[row][6],
                    headers[7]:datalines[row][7],
                    headers[8]:datalines[row][8],
                    headers[9]:datalines[row][9]}
                    )
            if len(data_csv)==0:
                return {"Message":"No data found!"}
            else:
                return {"books":data_csv}
        except Exception as e:
            return {"Message":"Something went Wrong!"}

api.add_resource(API_One,"/<int:rows>")
api.add_resource(API_Two,"/filter/<string:filter_data>")
app.run(debug=True)
