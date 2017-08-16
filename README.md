# 7330 Final Project - Repository
## Work done by Kouvaris, Farrugia, Fash

### ATN: The main initialization script in this repository currently uses Unix conventions and will only work on Unix-like machines (MacOS & Linux). Windows users can follow along manually and achieve the same result.

### 1 : Installing MongoDB Locally
Users can download the database instance at https://www.mongodb.com/download-center#community.
Windows users can find convetions explained [here](https://github.com/htpeter/dbmg_project/blob/master/Intro%20to%20MongoDB.pdf) 

### 2 : Startup MongoDB Local Instance

Make sure /data/db directory is created. Now run "mongod" and it should startup the server.

### 3 : Run (pull_import_data.py)[https://github.com/htpeter/dbmg_project/blob/master/pull_import_data.py]

This script will download and unzip the data, format the files, and upload them to your MongoDB local instance. You will then have a database "dbmg" with 5 tables of the FSQ data!

### 4 : Play w/ the data and try running some of our analysis.


