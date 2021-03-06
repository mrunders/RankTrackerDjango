# RankTracker project

This is a better version of my previous app https://github.com/mrunders/rankTracker

This is a small application that can store and calculate statistics for ranked.

I think this app is generic acconrding to all game conteinning heros and maps.

## How to install

### Requirements
Use of VirtualEnv is nice if you must use different version of django/python in your computeur, you can get virtualenv here: https://virtualenv.pypa.io/en/stable/.

To setup this app you must have python3 and django environnement installed, recommanded version for python is 3.5.4 and django is 2.5.0.
otherwise just follow this link and install python3: https://www.python.org/ and this one for django: https://www.djangoproject.com/.
There are file named `requirement.txt` at the root of the project that contains all dependencies the app will need, make sure to install all dependencies.

Docker is friendly too.

### Install the app
 Notting is required, you have all the sources ready and installed.

### Run the app
just write `python ./manage.py runserver`
if you have some issues with database you must run `python ./manage.py makemigrations && python ./manage.py migrate`.

## How to use this app
There are three ways to setup data:
Accounts, Heros and Maps have the same setup, so i will explain for one, lets add some maps:

- The first way is create admin account using `python ./manange.py createsuperuser` follow the steps and go on http://localhost:8000/admin/ and insert all data with the django admin panel.
- The seconde way is to go on `settings.py` file and there are 3 list named ACCOUNTS, MAPS and HEROS, fill out these list and go on http://localhost:8000/reset/.
- The last way is to go on these link and fill out the formular http://localhost:8000/accounts/, http://localhost:8000/maps/ and http://localhost:8000/heros/.

Account fonctionnality is not functionnal, so for now ignore it.
You can run the app without screen, but it's a bit hugly, you can insert your screens on statis/img/ folders.

Now you have Data installed you can use the app here http://localhost:8000/tracker/:
The screen is split in 5 parts:

### The first part is on the left
You can select which account you are playing (if like me you have multiple accounts).
This functionnality is not implemented so ignore it.

### The seconde part is the main 
The Huge table in the middle (he is empty for you)
There are 5 columns:
- When you played (in fact it is when you submit the form)
- Your current rank (is equal with the value named rank in the form)
- The variation is how many point you have gain/lose according with the previous game
- Where you played your game (just one map)
- With heros (you can select multiple heros)

### The next part is the form
You can select your rank (user -1 +1 -5 +5 -25 +25 button to adjuste your rank between games).
You can alse full out the form without any problemes.

### The next part is the Filter
If you must sort your table with witch heros or map you played, it's here.
You can sort By maps, By hero or by both.

### The last part is statistics
This is not implemented, ignore.

------

Here is the app (2018/06/25).

![alt text](https://raw.githubusercontent.com/mrunders/RankTrackerDjango/master/doc/screen.png "hello there")
