# News Database
###About the Logs Analytics Project
Built as part of the Udacity Full Stack Nanodegree, this is an internal reporting tool that uses information from the news database to discover what type of articles the readers prefer. The reporting tool prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database. 

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The program runs from the command line by connecting to that database, using SQL queries to analyze the log data, and then it out the answers to three questions.
