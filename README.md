# Land Management System using POS consensus over Blockchain
## Group no-11
Members:
1. Aman Saxena(2021H1030120H)
2. Chirag Jain(2021H1030072H)
3. Manas Srivastava(2021H1030078H)
4. Sahitya Ratan(2021H1030100H)

Folder: A1_Group_No_11.zip
> Module: 
* app -> backend.app

## Features: 

1. To register new users to the system with previously owned property

2. The user should be able to buy and sell the property

3. To improve the security of the blockchain, incorporate a consensus algorithm that has been assigned to the group

4. Implementation of Merkle root to calculate the hash of all the transactions in a block

5. To be able to view the transaction history that is related to a property

## Steps to run the project:

Step 1. set up a venv
   ```
   python -m pip install virtualenv
   python -m venv env
   env\Scripts\activate
   ```

Step 2. Set up requiremets
```
   pip install requests
   pip install Flask
   pip install -U flask-cors
   pip install pubnub
   ```

Step 3. Start program
```
   python -m backend.app


set "PEER=True"
set FLASK_DEBUG=1
set FLASK_ENV=devlopment
cd ./Ass1  
python -m backend.app
```

## To push and pull changes on GitHub
Step 1. Git Push
```
   git add \*
   git status
   git commit -m "message"
   git push origin
   ```

Step 2. Git Pull
```
   git pull origin
   ```
