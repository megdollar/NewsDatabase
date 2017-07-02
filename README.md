# News Database
### About the Logs Analytics Project:
Built as part of the Udacity Full Stack Nanodegree, this is an internal reporting tool that uses information from the news database to discover what type of articles the readers prefer. The reporting tool prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database. 

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The program runs from the command line by connecting to that database, using SQL queries to analyze the log data, and then it out the answers to three questions.

### Getting Set Up:

#### System Requirements:
1. [Python3](https://www.python.org/)
2. [Vagrant](https://www.vagrantup.com/)
  * This is the software that configures the Virtual machine
3. [Virtual Box](https://www.virtualbox.org/)
  * This is the software that actually runs the virtual machine
  * Allows you to share files between the VM filesystem and your host computer
  * Install the platform package for your OS
  * Don't launch after installing, Vagrant handles this for you

#### Project Setup:
1. Install Python3 
2. Install Vagrant
3. Install Virtual Box
4. Download or Clone the VM configuration from [full-stack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
5. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
6. Unzip the data and place the `newsdata.sql` file into the vagrant directory, which is shared with your VM
7. Download or clone this repository and place `news.py` in the vagrant directory

#### Launch the VM:
1. Inside the Vagrant directory downloaded from the full-stack-nanodegree-vm run this command in your terminal
   `vagrant up`
2. Log in to the VM 
   `vagrant ssh`
3. Change directory to the files and look around
   `cd /vagrant' 'ls' `
   
#### Set Up the Database:
1. Load the data in the local database
   `psql -d news -f newsdata,sql`
  
#### Run the Queries:
1. From the vagrant direcotry inside the VM
   `python3 news.py`
   

