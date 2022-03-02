<h1 align="center">Netflix<h1/>

# 	OTT streaming platform


## Table of contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Run](#run)
- [Technology](#technology)
- [Features](#features)
- [Database Models](#database)

## Introduction

A streaming service built with Python Django that provides a wide range of award-winning TV shows, movies, anime, documentaries, and other content.


NOTE: Please read the RUN section before opening an issue.

## Demo

<p align="center">
<img src="https://imgur.com/fqpAj62.png"/>
<img src="https://imgur.com/qDyCbxT.png"/>
<img src="https://imgur.com/uyY2AUI.png"/>
<img src="https://imgur.com/blX9Tdh.png"/>
<img src="https://imgur.com/HZsTxnT.png"/>
<img src="https://imgur.com/Zzw7878.png"/>
<img src="https://imgur.com/4LnuNzz.png"/>
<img src="https://imgur.com/KJfJUdu.png"/>
<img src="https://imgur.com/ThCy4S6.png"/>
<img src="https://imgur.com/7wsAWZB.png"/>
<img src="https://imgur.com/Pu8Wet6.png"/>
<img src="https://imgur.com/CL5W2RP.png"/>
</p>


The app provides a wide range of award-winning TV series, movies, animation, and documentaries.

In order to access the admin panel on "/admin"

## Run


- SQLITE_URI: this is the connection string of your Sqlite database.

Now you can run "python manage.py runserver" in the terminal and the application should work.

## Technology

The application is built with:

- Django version 4.0.2
- Sqlite version 3.31.1
- Ionicons version 5.5.2


## Features

The application displays an online store that contains products.

Users can do the following:

- Create account, login or logout
- Create profiles
- Watch movies, animation, TV series and documentaries.

Admins can do the following:

- View all the information stored in the database. They can view/add/edit/delete contents, products and categories.

## Database

All the models can be found in the models directory created using sqlite DB.

### User:

- username (String)
- password (String)


### Movie:

- title (String)
- imagePath (String)
- description (String)
- type (String)
- category (String)
- createdAt (Date)

  
### Profile:
  
- name (String)
- category (String)  
  
  

[Alan Chriss Antony](https://github.com/alanchrissantony)
