# Homework 10 

git clone https://github.com/ak256-ak/Homework10.git

cd Homework10/event_manager_project

# virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install dependencies

pip install -r requirements.txt


# Run the application
cd avneetgrewal@Avneets-MacBook-Air event_manager_project 
uvicorn app.main:app --reload

# Go to Google 

http://127.0.0.1:8000/docs

# Register a User 

Use the register endpoint to add a new user

{
  "username": "testuser",
  "password": "testpassword"
}

Please updated the testuser each time.

