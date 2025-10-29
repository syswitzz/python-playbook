A virtual environment is an isolated Python environment (or directories on your pc) that contains its own Python interpreter, site-packages directory, and dependencies, allowing different projects to use different versions of libraries without conflicts

// create a venv
python3 -m venv env_name   # venv is module so we use -m

// activate a venv
source env/bin/activate

// deactivate
deactivate

// check installed packages
pip list

// save all dependecies in a requirements.txt file
pip freeze > requirements.txt

// install all dependecies in a requirements.txt file
pip install -r requirements.txt
