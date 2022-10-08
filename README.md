1. set up a venv
   python -m pip install virtualenv
   python -m venv env
   env\Scripts\activate

2. Set up requiremets
   pip install requests
   pip install Flask
   pip install -U flask-cors
   pip install pubnub

3. Start program
   python -m backend.app

set "PEER=True"
set FLASK_DEBUG=1
set FLASK_ENV=devlopment
cd ./Ass1  
python -m backend.app

4. Git Push
   git add \*
   git status
   git commit -m "message"
   git push origin

5. Git Pull
   git pull
