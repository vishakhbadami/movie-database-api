Movie Database API
This is a simple Movie Database API built with Flask and SQLAlchemy. It allows users to perform CRUD operations (Create, Read, Update, Delete) on movies and actors. The project uses an SQLite database, but can be easily adapted for use with other relational databases (e.g., MySQL, PostgreSQL).

Features
Add, update, and retrieve movies.
List all movies with pagination.
Retrieve movie details by ID.
Delete a movie or actor.
Delete an actor only if they are not associated with any movie.
Requirements
Python 3.7 or higher
Flask
Flask-SQLAlchemy
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/movie-api.git
cd movie-api
2. Create and Activate a Virtual Environment (optional but recommended)
bash
Copy code
python -m venv venv
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
3. Install Dependencies
Install the required Python packages by running the following command:

bash
Copy code
pip install -r requirements.txt
requirements.txt:

makefile
Copy code
Flask==2.2.2
Flask-SQLAlchemy==3.0.3
You can create the requirements.txt file using the following command if you want to keep it updated:

bash
Copy code
pip freeze > requirements.txt
4. Initialize the Database
To create the necessary database tables, run the setup.py script:

bash
Copy code
python setup.py
This will create a SQLite database file called movie_db.db.

5. Run the Application
Start the Flask application with the following command:

bash
Copy code
python app.py
By default, the app will run on http://127.0.0.1:5000/.

API Documentation
1. Add or Update Movie (POST /movie)
Request Body (JSON):

json
Copy code
{
    "id": 1,  // Optional, if updating an existing movie
    "name": "Inception",
    "year": 2010,
    "rating": 8.8,
    "genres": "Sci-Fi, Thriller",
    "technicians": "Christopher Nolan"
}
Response:

Success:
json
Copy code
{
    "message": "Movie added successfully!"
}
or
json
Copy code
{
    "message": "Movie updated successfully!"
}
Error:
json
Copy code
{
    "message": "Missing or incorrect data!"
}
2. Get All Movies (GET /movie)
Query Parameters:
page (optional): The page number for pagination (default: 1).
per_page (optional): The number of movies per page (default: 5).
Response (JSON):
json
Copy code
[
    {
        "id": 1,
        "name": "Inception",
        "year": 2010,
        "rating": 8.8,
        "genres": "Sci-Fi, Thriller",
        "technicians": "Christopher Nolan"
    },
    {
        "id": 2,
        "name": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "genres": "Action, Crime, Drama",
        "technicians": "Christopher Nolan"
    }
]
3. Get Movie by ID (GET /movie/<id>)
Request:

URL: GET /movie/1
Response (JSON):

json
Copy code
{
    "id": 1,
    "name": "Inception",
    "year": 2010,
    "rating": 8.8,
    "genres": "Sci-Fi, Thriller",
    "technicians": "Christopher Nolan"
}
4. Delete Movie by ID (DELETE /movie/<id>)
Request:

URL: DELETE /movie/1
Response:

Success:
json
Copy code
{
    "message": "Movie deleted successfully!"
}
Error:
json
Copy code
{
    "message": "Movie not found!"
}
5. Delete Actor by ID (DELETE /actor/<id>)
Request:

URL: DELETE /actor/1
Response:

Success (if actor is not associated with any movie):
json
Copy code
{
    "message": "Actor deleted successfully!"
}
Error (if actor is associated with movies):
json
Copy code
{
    "message": "Cannot delete actor as they are associated with movies."
}
Error (if actor not found):
json
Copy code
{
    "message": "Actor not found!"
}
File Structure
plaintext
Copy code
MovieAPI/
├── app.py            # Flask application and routes
├── database.py       # Database configuration
├── models.py         # SQLAlchemy models (Movie, Actor)
├── setup.py          # Initializes the database
├── requirements.txt  # Project dependencies
└── movie_db.db       # SQLite database file
Troubleshooting
Method Not Allowed: Ensure you're sending the correct HTTP method (GET, POST, DELETE).
404 Not Found: Ensure you're providing the correct URL, especially when fetching data by ID (e.g., /movie/1).
Database Issues: If tables are not created correctly, try re-running the setup.py script or deleting the movie_db.db file to reset the database.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to update the README further if you have more details to add, such as specific configurations or usage instructions for different environments (e.g., deploying on a server). Let me know if you need anything else!
