## Study Organizer

Have you ever been frustrated with scrolling messenger conversation in order to find important information? I also felt that
pain so I decided to create own web-based app to keep everything about studying in one place. After registration proccess you have posibility to create own group or join to existing one. Do not panic when you forget your password or login. I show you how to utilize gmail account to password reset. In group you can start new topic or comment existing. You can also share your reaction using three existing icons. Every group need sometimes to vote about something e.g exam day or choose courses in syllabus for such sitation you can using voting section where question are assigned to specific group. If you want to run app in your local machine follow step by step next paragraph. Keep in mind that I do not focus much on frond-end. I will add extra feature after accomplish javascript and react course.

## Getting started

### Python
First of all check your Python version. We will use Django 3.1 version which requires Python 3.6+
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/python.jpg)

### Database configuration
Then we need to download and configure PostgreSQL as default database. 
#### Windows instalation
Follow below steps:
 1. Go to [this link](https://www.postgresql.org/download/windows/) and install database using graphical installer. Remember to put down `PORT_ADDRESS`, `login` and `password`.
 2. Open psql command 
 ![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/psql_shell.jpg)
 ![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/psql_shell_2.jpg)
 3. Remain first 4 rows default (just press enter) and then put your database password
 4. Create database
 ```shell
 CREATE DATABASE studyorganizer;
 ```
 You can check if database is properly created by type `\l`
 ![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/psql_shell_list.jpg)
 5. create new database user
 ```shell
 CREATE USER studyorganizeruser WITH PASSWORD 'your_password_here';
 ```
 6. modify connection parameters for the user we just created
 ```shell
 ALTER ROLE studyorganizeruser SET client_encoding TO 'utf8';
 ALTER ROLE studyorganizeruser SET default_transaction_isolation TO 'read committed';
 ALTER ROLE studyorganizeruser SET timezone TO 'UTC';
 ```
 7. grant privilages
 ```shell
 GRANT ALL PRIVILEGES ON DATABASE studyorganizer TO studyorganizeruser;
 ```
#### Linux Instalation
I share with you how I conducted installation proccess in my Linux machine. Just open your command prompt and type.
1. Install PostgreSQL
```shell
sudo apt update
sudo apt install postgresql postgresql-contrib
```
2. Change your current user to `postgres` which is default database owner after instalation
```shell
sudo su - postgres
```
3. Run `psql` command
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/linux_shell.jpg)

4. You cal also do step 2 and 3 in one line 
```shell
sudo -u postgres psql
```
5. Next step are the same in Linux as well as Windows so go to step `4.` in Windows instalation

#### Database resources
If you get stuck somewhere check following links:
* [PostgreSQL instalation](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)
* [PostgreSQL instalation](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)


### Install dependencies
First we need to clone repository using following command `git clone https://github.com/margolek/study-organizer.git` or just download and add to desirable directory. I assumpt that you are familiar with Virtual Environment using `venv`, `virtualenv` or Conda distribution. You should create and activate your VE. In Windiws use `ve_name\bin\activate.bat` in case you are using Linux type: `source ve_name/bin/activate` In order to install all requirments from `requirments.txt` file we nedd to use command:
```shell
pip install -r requirments.txt
```
**Warning** If we see this error
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/psycopg2_binary.jpg)
Replace `psycopg2` by `psycopg2-binary` in `requirments.txt` file

### Email
To utilize password reset option you have to create separate gmail account. Follow instaction from link. [Create Gmail account](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)

### Define Env Variables
We want to avoid using hard-coded passwords in our code because everyone will have access to sensitive data when we put them in publib GitHub repository. To achieve this we will use `Env Variables`.

#### Windows setup
 1. Open search field end type `env`. You should see similar option:
 ![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/env.jpg)
 2. Click `Edit the system environment variables` and then `Environment variables` in right button corner.
 3. Replace password by your own predefined during database instalation. In this place define also email password and address.
 ![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/env_password.jpg)
 4. To changes have affect restart you machine.

#### Linux setup
 1. Open console and navigate to home directory using `cd` command
 2. Configure bashrc settings using nano editor `nano ~/.bashrc`
 ![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/bashrc.jpg)
 3. To save changes press `Ctrl+X` and then `Y` to  accept changes.
 4. Restart you machine

#### Resources
* [Windows Env](https://www.youtube.com/watch?v=IolxqkL7cD8&ab_channel=CoreySchafer)
* [Linux Env](https://www.youtube.com/watch?v=5iWhQWVXosU&ab_channel=CoreySchafer)

### Create superuser and migrate database
 1. Populate database with models define in our app via commands: `python manage.py makemigrations` and then `python manage.py migrate`.
 2. Create superuser is pretty straightworward just type `python manage.py createsuperuser` and type necessary information

### Runserver and check out app functionality
To run server use `python manage.py runserver` command

#### Join to existing group or create new one
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/group_list.jpg)
#### Create new topic to discuss in group community
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/create_topic.jpg) 
#### Speak your mind in commend section
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/comments.jpg)
#### React to post interactively
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/gif/ezgif.com-gif-maker.gif)
#### Create a poll to check group opinion
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/poll1.jpg)
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/poll2.jpg)
#### Do not panic when you forget password
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/password_reset.jpg)
#### Manage group requests from your profile
![Alt text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/requests1.jpg)

### Conclusion
I hope you check all this functionalities in your local machine. If you get stuck somewhere or have any questions feel free to contant with me. My e-mail address `margolek555@gmail.com` and discord `Margol#9298`. I will be glad to talk about project and idea how to improve functionality. All the best!

### Resources and inspirations
* https://github.com/devmahmud/Django-Poll-App
* https://github.com/shubham1710/ByteWalk
* https://www.youtube.com/watch?v=sFPcd6myZrY&ab_channel=DennisIvy
* https://www.youtube.com/watch?v=dPoGRYz-n5E&ab_channel=DennisIvy



