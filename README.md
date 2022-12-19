# CS-340-T2840

CS 340 README


About the Project/Project Title
	This project is a Jupyter Dash site built on top of a MongoDB database that serves to show users information about Grazioso Salvare’s rescue animals. This project runs on a CRUD Python module which allows authenticated users to use CRUD operations on a database within MongoDB. 
	The contents of the site include a table database with a drop down menu to only show certain types of rescue animals such as water, mountain, or disaster rescue animals. Below the table are two visualizations of the data including a geolocation map and a pie chart of each breed within each type selected. 
	MongoDB was used as the model component of the development for its specific ability to work well with Python and by extension Jupyter Dash sites since MongoDB stores data in JSON-like form, making the CSV of the animal shelter flexible and easily scalable for the site’s interface.
	The Dash framework that provides the view and controller structure for the web application is an open source Python framework for building full stack web apps purely in Python, and it has been further integrated with Jupyter as JupyterDash to be written and ran through Jupyter Notebook.

Motivation
	This project exists to help the users of the site quickly organize and visualize information such as the locations of any animal, see how many of a certain type of rescue animal they have, and see the percentages of breeds overall or within each category. 

Getting Started
	To set up a copy of this project locally, the CSV of the animal shelter must be downloaded and imported as a database into MongoDB. The authenticated user aacuser with the password 123 is then created (password can be edited however one wishes,  these just must also be changed in the Python file as well). The Python CRUD file and Jupyter Dash site notebook should be opened together in the same file in Jupyter, through which then the notebook can be run to display the table and two visualizations.

Installation
	Jupyter Notebook and MongoDB are required for this project and can both be installed using pip install commands within an administrator terminal.
