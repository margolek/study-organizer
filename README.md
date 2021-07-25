## Study Organizer

Have you ever been frustrated with scrolling messenger conversation in order to find important information? I also felt that
pain so I decided to create own web-based app to keep everything about studying in one place. After registration proccess you have posibility to create own group or join to existing one. Do not panic when you forget your password or login. I show you how to utilize gmail account to password reset. In group you can start new topic or comment existing. You can also share your reaction using three existing icons. Every group need sometimes to vote about something e.g exam day or choose courses in syllabus for such sitation you can using voting section where question are assigned to specific group. If you want to run app in your local machine follow step by step next paragraph. Keep in mind that I do not focus much on frond-end. I will add extra feature after accomplish javascript and react course.

## Getting started
First of all check your Python version. We will use Django 3.1 version which requires Python 3.6+
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/img/python.jpg)

Then we need to download and configure PostgreSQL as default database. If you are Windows user go to [this link](https://www.postgresql.org/download/windows/) and install database using graphical installer. I share with you how I conducted installation proccess in my Linux machine.
1. Install PostgreSQL
```shell
sudo apt update
```
```shell
sudo apt install postgresql postgresql-contrib
```
2. Creating a new role
```shell
sudo -u postgres createuser --interactive
```
3. Create a new database
```shell
sudo -u postgres createdb studyorganizer

```
4. Open PostgreSQL prompt using new role
```shell
sudo adduser username_here

```
```shell
sudo -u username_here psql
```
5. 

## Reactions
![Alt Text](https://github.com/margolek/study-organizer/blob/master/studyOrganizer/static/gif/ezgif.com-gif-maker.gif)
