## Google Oauth Get Token Access for your applications

 - With this application, you can request your clients' permissions when building a Gmail application that needs to access Gmail or other Google services."

### Step 1
```
chmod +x ./run_program.py
```

## Step 2, create certificates (if you're in localhost)
 - create a certificate, answer all the requests while you are runing this
```
 openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```


## Step 3, run the run_program
```
./run_program.sh
```

### Requeriments
 - You must install docker in your OS 
