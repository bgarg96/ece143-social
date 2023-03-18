# ECE 143: Group 13

## Table of contents

1. [Overview](#ProjectOverview)
2. [Repository Structure](#RepositoryStructure)
   - [Datasets](#Datasets)
   - [Source Code](#SourceCode)
   - [Jupyter Notebook](#JupyterNotebook)
   - [Deploy app](#deploy-the-dashboard)
3. [Third Party Modules](#ThirdPartymodules)
4. [Implementation](#Implementation)
5. [Presentation](#Presentation)

## Project Overview
Our proposed problem statement is to assess the efficacy of social media influencers as a marketing medium for businesses. We propose to study, analyze and predict which social media platform is most effective for a particular business segment and which influencers provide the best marketing reach for a given type of product in a particular demographic.
In this project we plan to do an exploratory data analysis of statistics of recent social media influencers, social media platforms and key attributes that help identify the best influencer, social media platform and type of content for a particular product to be marketed in a given demographic. We propose to analyze trends such as views, comments, likes on various social media platforms that can act as key indicators of the marketing reach of a particular influencer and predict the best influencer for various businesses. We will present visualizations into top influencers for a given demographic and type of product.

## Repository Structure
      root
         │
         ├───data
         │   ├───Instagram
         │   │       Instagram_Dec.csv
         │   │       Instagram_Nov.csv
         │   │       Instagram_Oct.csv
         │   │       Instagram_Sep.csv
         │   │
         │   ├───TikTok
         │   │       TikTok_Dec.csv
         │   │       TikTok_Nov.csv
         │   │       TikTok_Oct.csv
         │   │       TikTok_Sep.csv
         │   │
         │   └───Youtube
         │           Youtube_Dec.csv
         │           Youtube_Nov.csv
         │           Youtube_Oct.csv
         │           Youtube_Sep.csv
         │
         ├───docs
         │      action_items.txt
         │
         │
         ├───scripts
         │       lint.sh
         │
         └───src
               config.py
               data_visualization.py
               platforms.ipynb
               platforms.py
               streamlit_app.py
               uts.py


### Datasets
We use the following dataset: https://www.kaggle.com/datasets/ramjasmaurya/top-1000-social-media-channels.
The dataset contains information regarding different social media platforms, the influencers on them, the type of content they promote, subscribers, viewer, comment and like count, demographic information.

The `data` folder contains:

- [Instagram/Instagram_*month*.csv](data/Instagram/) contains all the pre-processed csv's for Instagram
- [Youtube/Youtube_*month*.csv](data/Youtube/) contains all the pre-processed csv's for Youtube
- [TikTok/TikTok_*month*.csv](data/TikTok/) contains all the pre-processed csv's for TikTok

### Source Code

Linting: All code that's pushed to main goes linting checks. We recommend everyone to install pre-commit hooks, so that any commit is lint - approved. The linting config file is [.pre-commit-config.yaml](.pre-commit-config.yaml).

The src directory has all the source code:
 - config.py : has all the configurable variables for the dataset configuration.
 - data_visualization.py : contains all the datavisualization functions. These functions use an input dataframe and output plots.
 - platforms.py : contains the social media class and methods to process and filter data.
 - streamlit_app.py : contains the webapp code and UI bindings to back-end.
 - uts.py : contains utility helper functions for backend logic.

### Jupyter Notebook

The [Jupyter Notebook](src/platforms.ipynb) has all the plotting code. All analyzed data is stored as one cell for easy reproducibility.

### Deploy the dashboard
Run `streamlit run src/streamlit_app.py` to deploy the dashboard.

## Third Party Modules

The third party modules used are as listed below.

- numpy
- pandas
- jupyter
- matplotlib
- seaborn
- streamlit
- matplotlib_venn

## Pre Processing
The CSVs are processed to have uniform column names across platform for easy modularization.

## Implementation

We used a conda virtual environment with the 3.9.6 python version to work on.
Make sure you are set up to use Python version - 3.9.6

- Install all required libraries using conda
- Run the streamlit app for live interactive UI using the command: streamlit run ./streamlit_app.py. Please ensure you are in the src directry when you run this command.

Jupyter Notebook -

- Run compete notebook or particular cells of [`platforms.ipynb`](src/platforms.ipynb) for viewing the plots.

## Presentation

Final Presentation - [Link to Presentation](https://docs.google.com/presentation/d/1uyYdID_O2hJ5Uu_wthjF_jv1YBesf483JXhHCWh-K0Y/edit?usp=sharing)
