# spotify-genre-prediction
Trying to predict the genre of songs based on the audio features provided by the tracks api using a machine learning model

## Setup for development
1. Set up a python virtual environment  
   In the project folder run  
   `python3 -m venv env`
2. Activate the virtual environment (do this everytime you do anything!)  
   `.\env\Scripts\activate`  
   If this doesn't work, try running  
   `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`  
3. To install the required packages run  
   `python -m pip install -r requirements.txt`
4. Create a ".env" file in the root directory and add the current API Key from our OneNote like this:  
   `API_KEY=xxxxx`

## Doing regular development
- Always activate the virtual environment first using  
  `.\env\Scripts\activate`
- To ensure you have all the right packages installed, run  
  `python -m pip install -r requirements.txt`
- If you install new packages use  
  `python -m pip freeze > requirements.txt`  
  to add the package to the requirements file

## How to use Jupyter in VSCode
- You can open the Python Interactive Window from the command palette by running  
  `Jupyter: Create Interactive Window`
- You can create a new Jupyter Notebook from the command palette by running  
  `Jupyter: Create New Blank`