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
![Screenshot (113)](https://github.com/user-attachments/assets/ed75c0d1-36f2-4bc3-99a1-da204770fb65)


*Obtain Token

URL: /api/token/

Method: POST

Body:
{
  "username": "your_username",
  "password": "your_password"
}

#output

![Screenshot (114)](https://github.com/user-attachments/assets/499b3067-7ccd-4cc5-8be9-a1503616b557)



*Refresh Token

URL: /api/token/refresh/

Method: POST

Body:
{
  "refresh": "your_refresh_token"
}

#output


![Screenshot (122)](https://github.com/user-attachments/assets/84a3be0b-3c27-4800-82fa-fb1479d07777)


*List

URL: /api/posts/

Method: GET to list

#output
![Screenshot (115)](https://github.com/user-attachments/assets/9e8cf4e0-cb2b-4571-9cc3-4cba68dc7275)


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


![Screenshot (123)](https://github.com/user-attachments/assets/2f0b47d4-ccff-40e5-9416-a9c8841220e5)




*Retrieve

URL: /api/posts/<post_id>

method : GET

 Authorization: OAuth2.0: Bearer <your_access_token>

#output

![Screenshot (117)](https://github.com/user-attachments/assets/3cf631b1-974c-452e-86dd-731718ae465a)


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

![Screenshot (118)](https://github.com/user-attachments/assets/b782b738-cfc6-4603-aadc-6045111ebf7a)




 *DELETE

 URL: /api/posts/<post_id>

method : DELETE

 Authorization: OAuth2.0: Bearer <your_access_token>

 #output

![Screenshot (121)](https://github.com/user-attachments/assets/4c693edc-ed94-4c52-9294-a2f379eecc83)



#comments

create comments

 URL: /api/posts/<post_id>/comments/

method : post

 Authorization: OAuth2.0: Bearer <your_access_token>

 #output
![Screenshot (119)](https://github.com/user-attachments/assets/f66ea12e-c6b5-4859-b649-cf4d8fa574ef)



*Retrive single comments

 URL: /api/posts/<post_id>/comments/<comment_id>

method : post

 Authorization: OAuth2.0: Bearer <your_access_token>

 Body:
 {
  "text": "Comment text"
}

 #output

![Screenshot (120)](https://github.com/user-attachments/assets/909ce8a0-472a-411b-b2b6-8cbad6408c10)


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




