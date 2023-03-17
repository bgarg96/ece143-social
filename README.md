# ECE 143: Group 13

## Table of contents

1. [Overview](#ProjectOverview)
2. [Repository Structure](#RepositoryStructure)
   - [Datasets](#Datasets)
   - [Source Code](#SourceCode)
   - [Jupyter Notebook](#JupyterNotebook)
   - [Graphs](#Graphs)
3. [Third Party Modules](#ThirdPartymodules)
4. [Implementation](#Implementation)
5. [Presentation](#Presentation)

## Project Overview

Social media and influencing is $15B market.



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
               platforms.py
               streamlit_app.py
               uts.py
               

### Datasets

The `data/` folder contains:

- [Instagram/Instagram_*month*.csv](data/Instagram/) contains all the pre-processed csv's for Instagram
- [Youtube/Youtube_*month*.csv](data/Youtube/) contains all the pre-processed csv's for Youtube




### Source Code

Linting: All code that's pushed to main goes linting checks. We recommend everyone to install pre-commit hooks, so that any commit is lint - approved. The linting config file is [.pre-commit-config.yaml](.pre-commit-config.yaml).

To install

Source code for all data scraping and data analysis files are within the `src/` folder. [Link to Folder](src/)

Data scraping files:

- [wsBids.py](src/wsBids.py) is the web scraper

Pre-Processing files:

- [dataframe.py](src/dataframe.py) - Return a class object to load any dataset as a d_frame.
- [load_datasets.py](src/load_datasets.py) - Loads datasets using dataframe class.

Data processing files:

- [batsman_stats.py](src/batsman_stats.py) - Obtains basic batsman stats from the data.
- [player_performance.py](src/player_performance.py) - Collates player statistics to plot graphs.
- [bid_VS_performance.py](src/bid_VS_performance.py) - Calculate teams W:L ratio and total auction spending per year and plot their graph.
- [bowler_stats.py](src/bowler_stats.py) - Extracts bowler statistics for the given bowler
- [innings.py](src/innings.py) - Extracts information about bowlers given a match and innings
- [data_process.py](src/data_process.py) - Helper class to read and process the CSV files
- [city_toss_winner.py](src/city_toss_winner.py) - Derives relation between the city and toss winning ratios
- [team_toss_winner.py](src/team_toss_winner.py) - Determines a co relation between team winner Vs toss winner of a match.
- [tosswiner_choice.py](src/team_toss_winner.py) - Estimates the best inning choice for each team given they win the toss.

### Jupyter Notebook

The [Jupyter Notebook](src/plot_support_book.ipynb) has all the plotting code. All analyzed data is stored as one cell for easy reproducibility.

### Graphs

The [`Graphs`](graphs/) folder has images as `.png` of all the analysis plots computed.

## Third Party Modules

The third party modules used are as listed below. They are included as [`requirements.txt`](requirements.txt).

- requests
- numpy
- pandas
- jupyter
- matplotlib
- seaborn
- BeautifulSoup

## Pre Processing
The CSVs are processed to have uniform column names across platform for easy modularization.

## Implementation

We used a conda virtual environment with the 3.9.13 python version to work on.
Make sure you are set up to use Python version - 3.9.13

Install all required libraries -

```
pip install -r requirements.txt
```

Auction Data Web Scarping -

Run create_auction_data() in wsBids.py
```
python -c 'import wsBids; wsBids.create_auction_data()'
```

Source Code for analysis -

- Run any python files from within `src/` folder

```
src % python batsman_stats.py
```

Jupyter Notebook -

- Run compete notebook or particular cells of [`plot_support_book.ipynb`](src/plot_support_book.ipynb) for viewing the plots.

## Presentation

Final Presentation - [Link to Presentation](/Presentation/Final_Presentation.pdf)


Explain your file structure, how to run your code, and name all third-party modules you are using.
