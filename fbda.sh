#!/bin/bash

# Initialising
echo Analysing Facebook Data

# Install Dependencies
# echo Installing dependencies...
# sudo apt-get install r-base python3 pdftk

# Running data Scraping Python file
echo Scraping data...
python3 scrape.py

# Running analysis with R files
echo Running analysis...
R -q --no-save < date_graph.r
R -q --no-save < time_graph.r
R -q --no-save < event_pie.r

# Compiling results
echo Creating report document...
pdftk date_graph.pdf time_graph.pdf event_pie.pdf cat output report.pdf

# Tidying Up the files
echo Tidying Up...
rm date_data.txt
rm event_data.txt
rm event_pie.pdf
rm time_data.txt
rm time_graph.pdf

# Finished!
echo Analysis complete!
