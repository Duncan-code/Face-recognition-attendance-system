import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-54ba0-default-rtdb.firebaseio.com/"
})

ref = db.reference('STAFF')

data = {
   "567":
       {
           "Name": "ELION MUSK",
           "Position": "Staff",
           "Gender": "Male",
           "Starting year": 2022,
           "Total attendance": 0,
           "Years worked": 1,
           "Last_attendance_time": "2023-01-09 10:27:34"
       },
    "789":
        {
            "Name": "DUNCAN IMBENZI",
            "Position": "Staff",
            "Gender": "Male",
            "Starting year": 2022,
            "Total attendance": 0,
            "Years worked": 1,
            "Last_attendance_time": "2023-01-09 10:27:34"
        },
    "6758":
        {
            "Name": "LAMECK KAMBI",
            "Position": "Staff",
            "Gender": "Male",
            "Starting year": 2022,
            "Total attendance": 0,
            "Years worked": 1,
            "Last_attendance_time": "2023-01-09 10:27:34"
        },
     "7338":
        {
            "Name": "IGNATIUS KUBENDE",
            "Position": "Staff",
            "Gender": "Male",
            "Starting year": 2022,
            "Total attendance": 0,
            "Years worked": 1,
            "Last_attendance_time": "2023-01-09 10:27:34"
        },
     "784":
        {
            "Name": "ISAAC KEGA",
            "Position": "Staff",
            "Gender": "Male",
            "Starting year": 2022,
            "Total attendance": 0,
            "Years worked": 1,
            "Last_attendance_time": "2023-01-09 10:27:34"
        },
    "45678":
        {
            "Name": "BARACK OBAMA",
            "Position": "Staff",
            "Gender": "Male",
            "Starting year": 2022,
            "Total attendance": 0,
            "Years worked": 1,
            "Last_attendance_time": "2023-01-09 10:27:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)