Django Blog Application

A simple blog application built with Django and Django REST Framework, featuring basic CRUD operations for posts and comments, token-based authentication, and optional frontend integration.

*Features

### Models
1. **Post**
   - Fields: title, content, author, published_date

2. **Comment**
   - Linked to Post
   
   - Fields: author, text, created_date

APIs:
* Create a post

* Retrieve a post

* Update a post

* Delete a post

* Create a comment

* Retrieve a comment

* Update a comment

* Delete a comment

*CRUD operations for posts

List and create comments under each post

Authentication: Token-based authentication using JWT


Prerequisites
Python 3.x
Django 4.x

Django REST Framework

Simple JWT (for token-based authentication)

Postman (for API testing)

Installation
Clone the Repository:

git clone https://github.com/vaishnavikapile22/Django-blog-application.git

pip install -r requirements.txt

Apply for migration

pip install makemgrations

pip install migrate

Create superuser

pip install createsuperuser

Run server

pip install runserver

The application will be accessible at http://127.0.0.1:8000/.

*API Endpoints

#User Registration:

URL: /api/register/

Method: POST

Request Body (POST): 
{
    "username": "gita",
    "password": "1234"
}

#OUTPUT

![Screenshot (113)](https://github.com/user-attachments/assets/cc9d6426-6948-4b28-8609-91815784d1a5)

#Obtain Tokens:

URL: /api/token/

Method: POST

Request body:

{
    "username": "gita",
    "password": "1234"
}

#OUTPUT

![Screenshot (114)](https://github.com/user-attachments/assets/07d3d3ff-ec5f-4628-ae51-e2e2196a5f18)

#Use Tokens:

URL: /api/posts/

Method: POST

Request AUTHARIZATION : OAuth2.0: Bearer your-access-token

body:

{
    "title": "recipes",
    "content": "Heat olive oil in a pot over medium heat, Add onion and garlic, cook until softened, Add tomatoes and cook for 5 minutes, Add broth, bring to a boil, then simmer for 20 minutes, Blend until smooth, stir in basil, and season with salt and pepper"
}


![Screenshot (116)](https://github.com/user-attachments/assets/8828b616-e7c6-4d44-8138-89b971a94b27)


URL: /api/posts/

Method: GET

![Screenshot (115)](https://github.com/user-attachments/assets/8abf828d-77f3-4bfa-bb5c-75d786ec1016)

#Retrevie single post

URL: /api/posts/{post}

Method: POST

AUTHARIZATION : OAuth2.0: Bearer your-access-token

#output

![Screenshot (117)](https://github.com/user-attachments/assets/f98aa643-8db6-4825-865e-c616cb1a8c8c)

#Update Post:

URL: /posts/<post_id>/

Method: PUT

Request Body:

AUTHARIZATION : OAuth2.0: Bearer your-access-token


Request Body:{
    "title": "Updated Title",
    "content": "Updated content of the post.",
    "published_date": "2024-07-22T12:00:00Z"
}


#output


![Screenshot (118)](https://github.com/user-attachments/assets/8ff4357e-c7fa-473e-8f45-654ce89c5c66)


#Delete a Post

AUTHARIZATION : OAuth2.0: Bearer your-access-token

DELETE /api/posts/{post_id}/

#output


*Comments

List Comments for a Post

POST /api/posts/{post_id}/comments/

AUTHARIZATION : OAuth2.0: Bearer your-access-token

Response body:

![Screenshot (119)](https://github.com/user-attachments/assets/78f182ca-0fba-4470-ae51-ad537371c6cd)



GET /api/posts/{post_id}/comments/

![Screenshot (120)](https://github.com/user-attachments/assets/59a4668b-fa37-4062-b522-998a5b421339)

*Update Comment (PUT):

URL: http://127.0.0.1:8000/api/posts/10/comments/5/

Method: PUT

Request Body:

{
  "text": "Updated Comment Text"
}

Authorization: Bearer <your_access_token>

*Delete Comment (DELETE):

URL: http://127.0.0.1:8000/api/posts/<post_pk>/comments/<comment_pk>/

Method: DELETE

Authorization: Bearer <your_access_token>










