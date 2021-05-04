# mycarsforsale
This is a web application developed to sell cars.  
Registered users can create accounts and then post their vehicles for sale or post to the blog.  
Non registered users can view cars posted and filter results.
All post must be approved by the administrator before it can be displayed on the blog.

## Features
* Login/Registration
* Add/Edit/Delete/view cars for sale
* Admin Portal
* Blog
* Add comments on blog topics
* 



## Languags
* DJango
* Python
* HTML/CSS/JS
* Bootstrap
* Jquery


## Windows Setup Install


***STEP 1: Create a virtual environment using python.***

- Install Python 
- Install Virtual Env "pip3 install virtualenv"


***STEP 2: Create a virtual environment using python.***

    Install, Create & Open a virtual environment: Run:  
		- pip3 install virtualenv
		- python3 -m virtualenv cars_env
		- cars_env\Scripts\activate
     
**STEP 3: Clone the repository**

    Get the code base.  Ensure you have git installed & a github profile. Run:
		- git clone repo
      
**STEP 3: Install the application packages**

    After getting the code base, its root will contain a file called, requirements.txt.  Run:
		- pip3 install requirements.txt
		
**STEP 4: Run the application**

    Setup the models & start up the webserver. Run:
    	- python manage.py makemigrations
    	- python manage.py migrate
		- python manage.py runserver