from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# Movie table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year_of_release = db.Column(db.Integer, nullable=False)
    user_ratings = db.Column(db.Float)

# Actor table
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Technician table
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Genre table
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/movie', methods=['POST'])
def add_movie():
    data = request.get_json()  # Get JSON data from the request body
    movie = Movie(
        name=data['name'],
        year_of_release=data['year_of_release'],
        user_ratings=data['user_ratings']
    )
    db.session.add(movie)  # Add movie to the database
    db.session.commit()  # Commit the changes to the database
    return jsonify({'message': 'Movie added successfully'}), 201

@app.route('/movie/<int:id>', methods=['GET', 'PUT'])
def movie_details(id):
    movie = Movie.query.get_or_404(id)  # Get movie by ID, or return 404 if not found
    if request.method == 'GET':
        # Return movie details in the response
        return jsonify({
            'name': movie.name,
            'year_of_release': movie.year_of_release,
            'user_ratings': movie.user_ratings
        })
    elif request.method == 'PUT':
        data = request.get_json()  # Get updated data from the request body
        movie.name = data['name']
        movie.year_of_release = data['year_of_release']
        movie.user_ratings = data['user_ratings']
        db.session.commit()  # Commit the changes to the database
        return jsonify({'message': 'Movie updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
