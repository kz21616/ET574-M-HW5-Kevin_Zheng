# ET574-M-HW5-Kevin_Zheng

Wine Quality Chart



# title 

This application is a "Wine Quality chart" built using Python and wxPython.

The purpose of this program is to allow users to load a dataset and visualize the relationship between wine characteristics (such as alcohol content) and wine quality using an interactive scatter plot.

The dataset used is from the UCI Machine Learning Repository:
- Wine Quality Dataset (Red Wine)

It helps users explore how different chemical properties of wine relate to its quality score.



# features

- Simple graphical user interface (GUI) built with **wxPython**
- Button-based file loading system
- Automatically reads and processes the wine dataset
- Extracts key features:
- Alcohol content (`alcohol`)
- Quality score (`quality`)
- Generates a scatter plot using **Matplotlib**
- Includes error handling for missing or incorrect data
- Displays results in a separate plot window

# user interaction

1. The user opens the application
2. Clicks the "Open Wine Quality" button
3. The program loads the data
4. A scatter plot appears showing:
   - Alcohol (X-axis)
   - Quality (Y-axis)


# technologies used

This project uses wxPython for the GUI, 
Pandas for processing the information from the CSV file,
Numpy for the numerical operations and
Matplotlib for the creation of the plot


# installation 

Follow these steps to install the required dependencies:

1. Install Python
Make sure you have Python 3.10 or higher installed.

python --version

2. Install the required libraries

pip install wxPython, Pandas, Numpy, Matplotlib

or

python -m pip install wxPython, Pandas, Numpy, Matplotlib

or 

py -m pip install wxPython, Pandas, Numpy, Matplotlib


# running the application

To obtain the data chart the user just needs to run this code and click on the 
"Open Wine Quality" button in the center of the popup screen.

# dataset information

The wine quality information was obtained from the UCI machine learning repository
which contains information about wine quality in red and white wine as well as other
information not included in this graph. Additional information can be found in the 
link below:

https://archive.ics.uci.edu/dataset/186/wine+quality