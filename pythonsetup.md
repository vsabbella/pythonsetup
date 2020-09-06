1. Package manger pip
2. Creating virtual environments
   1. install virtual virtual environment tool : sudo python  -m pip install virtualenv
   2. Create a virtual environment: virtualenv rates
   3. Create a virtual environment with python3 interpreter: virtualenv -p python3 rates_py3
   4.  source rates_py3/bin/activate or . rates_py3/bin/activate - . indicates the system to retrieve shell scripts from the folder mentioned
   5. Use pip with python as best practise.
   6. List the packages - python -m pip list
   7. Install a package : Install requests :python -m pip install request.
   8. Show where a package is installed : python -m pip show requests
   9. Install box package: python -m pip install python-box
   10. Export dependendent packages to a file : python -m pip freeze > requirements.txt
   11. Import all dependent packages : python -m pip install -r requirements.txt

3. Clone a package from git 
   1. git clone https://github.com/pallets/flask
   2. Editable install package for debugging/development: python -m pip install -e flask