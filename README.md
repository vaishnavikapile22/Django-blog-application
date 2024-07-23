Social Networking Application with Django REST Framework

Overview

This project is a social networking application built using Django and Django REST Framework (DRF). It includes basic functionalities for managing posts and comments, with token-based authentication using JWT.

Features

User Registration: Allows users to register with a username and password.

Authentication: Token-based authentication using JWT.

CRUD Operations: Create, read, update, and delete posts and comments.

Permission-Based Access: Users can only modify their own posts and comments or those they have permission to.

Requirements

Python 3.10+

Django 4.x+

Django REST Framework

pip install djangorestframework-simplejwt


MIGRATE AND MIGRATIONS

pip install makemigrations

pip install migrate

CREATESUPERUSER

python manage.py createsuperuser

API Endpoints

Authentication

*User Registration

URL: /api/register/

Method: POST

Request Body:

{
  "username": "your_username",
  "password": "your_password"
}

#output
![Screenshot (113)](https://github.com/user-attachments/assets/8f1201fa-448e-4928-a18f-94a7b491f821)


*Obtain Token

URL: /api/token/

Method: POST

Body:
{
  "username": "your_username",
  "password": "your_password"
}

#output

![Screenshot (114)](https://github.com/user-attachments/assets/3522e8a8-a2e6-4cf5-97fd-bd4e84426b1e)


*Refresh Token

URL: /api/token/refresh/

Method: POST

Body:
{
  "refresh": "your_refresh_token"
}

#output


![Screenshot (122)](https://github.com/user-attachments/assets/8b404416-d5c5-469e-8a46-f101456d6e11)


*List

URL: /api/posts/

Method: GET to list

#output
![Screenshot (115)](https://github.com/user-attachments/assets/fb8ea267-12ba-49e2-b584-f1e0762d3b7e)


*Create Posts

URL: /api/posts/

Method: POST

 Authorization: OAuth2.0: Bearer <your_access_token>

Body:
{
  "title": "Post Title",
  "content": "Post content"
}

#output


![Screenshot (123)](https://github.com/user-attachments/assets/364505c3-827a-472f-a4e5-56e935e04c59)


*Retrieve

URL: /api/posts/<post_id>

method : GET

 Authorization: OAuth2.0: Bearer <your_access_token>

#output

![Screenshot (117)](https://github.com/user-attachments/assets/8ae2da38-e781-4087-8107-78e7621fe9ea)


*UPDATE

URL: /api/posts/<post_id>

method : PUT

 Authorization: OAuth2.0: Bearer <your_access_token>

 Body:
 
  {
  "title": "Updated Title",
  "content": "Updated content"
}


 #output
![Screenshot (118)](https://github.com/user-attachments/assets/218e386d-61e7-4523-ae43-2fc90850956b)


 *DELETE

 URL: /api/posts/<post_id>

method : DELETE

 Authorization: OAuth2.0: Bearer <your_access_token>

 #output

![Screenshot (121)](https://github.com/user-attachments/assets/31278791-2d27-4163-8ff9-e1041631d2ad)



#comments

create comments

 URL: /api/posts/<post_id>/comments/

method : post

 Authorization: OAuth2.0: Bearer <your_access_token>

 #output
![Screenshot (119)](https://github.com/user-attachments/assets/a1862b06-5096-4c8b-80e7-3302608aa4e5)


*Retrive single comments

 URL: /api/posts/<post_id>/comments/<comment_id>

method : post

 Authorization: OAuth2.0: Bearer <your_access_token>

 Body:
 {
  "text": "Comment text"
}

 #output

![Screenshot (120)](https://github.com/user-attachments/assets/b2d1d210-eb71-4751-94f1-860c23a1f920)


*Update comments

 URL: /api/posts/<post_id>/comments/<comment_id>

method : PUT

 Authorization: OAuth2.0: Bearer <your_access_token>

 Body:
 {
  "text": "Updated comment text"
}



 *Delete

 URL: /api/posts/<post_id>/comments/<comment_id>

method : Delete

 Authorization: OAuth2.0: Bearer <your_access_token>




