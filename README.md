# spotify-genre-prediction
Predicting Music Genres based on Spotify Song Data using a Gradient Boosting Algorithm

## Setup for development (on windows)
1. Install pipenv  
  `pip install --user pipenv`
   In the project folder run  
3. Select the pipenv python interpreter in your IDE
2. In your project directory, run  
  `pipenv install`
  to install all needed dependencies
  
## Data Collection
- Data collection is done using the Spotify Web API
- Details are explained in the [implementation](data_collection/data_collection.ipynb)

## Data Mining Process
Data understanding, preparation, modeling and evaluation of the model are implemented in a single [Jupyter Notebook](model_implementation/crisp_dm_process.ipynb)