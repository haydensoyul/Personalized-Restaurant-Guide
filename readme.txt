## Personalized restaurant guide ##

provide how many times I have chosen each menu
allow me to try a new one or go with my usual (safe) bet

It provides my review and information per each menu:
- # of orders: the number of times that I ordered this menu in this restaurant
- % of orders: the ratio of choosing this menu over all menu in this restaurant
- Rating (1-5): Rating of how much I liked this menu. 1: worst, 5: best.
- Spiciness (1-5): Spiciness level. 1: mildest, 5: most spicy
- Remarks: Any note to remember.

It reminds me how many times I ordered each menu. Based on the # and % of orders, I can choose the menu that I like the most, or I can choose the one that I never tried, or else.

It allows me to add note to remind me what to ask or avoid
   -- for example, make it less spicy, remove mustard
   -- for example, do not order this menu again (too spicy for me)

For rating and spiciness, I implemented this web app to calculate weighted moving average. It is simple to calculate and does not require memories to store all the previous entries. Also, it is a good respresentation of latest trend. 

WMA (weighted moving average) = 0.9 * PW (preveious WMA) + 0.1 * CE (current entry)

Programming languages used:
Python3, HTML

Libraries used:
flask, sqlite3, jinja2

Things to improve:

I could have added more informations such as calrie level, sugar (glucose) level. But as for a prototype, I did not include those to keep it simple and focus on showing my innovative concept.

I could implemnt the web app to allow users to add restaurant information (menu, pictures, etc.). I could also implement the web app to import restaurant and menu information from public source (e.g., search engine, maps, conventional restaurant guide, etc.). However, these are not the innovative part of my app challenge idea.

### To Install Virtual Environment

We use a module named virtualenv which is a tool to create isolated Python environments. virtualenv creates a folder that contains all the necessary executables to use the packages that a Python project would need.

Create Python virtual environment:
pip install virtualenv

Go to the local directory where you want to create your Flask app.

Activate a virtual environment:
virtualenv venv
source ./venv/bin/activate


### To run the server

source ./venv/bin/activate
python3 app.py

### To open the web app
http://<my web server URL>
