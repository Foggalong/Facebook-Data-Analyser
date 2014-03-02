#!/bin/bash

# Initialising
echo Analysing Facebook Data

# Running data Scraping Python file
echo Scraping data...
python3 scrape.py

# Running analysis with R files
echo Running analysis...
R --no-save < time_graph.r
R --no-save < event_pie.r

echo Analysis complete!
