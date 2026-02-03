from flask import Flask, request, jsonify
from data import movies, shows, bookings

app = Flask(__name__)

# ---------------- MOVIE APIs ----------------

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    movies.append(data)
    return jsonify({"message": "Movie added"}), 201


@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify({"message": "Movie updated"}), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


# ---------------- SHOW TIMING APIs ----------------

@app.route("/api/movies/<int:movie_id>/shows", methods=["GET"])
def get_shows(movie_id):
    movie_shows = [s for s in shows if s["movie_id"] == movie_id]
    if not movie_shows:
        return jsonify({"error": "No shows available"}), 404
    return jsonify(movie_shows), 200


# ---------------- BOOKING API ----------------

@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json

    movie_id = data.get("movie_id")
    show_id = data.get("show_id")
    seats = data.get("seats")

    if not movie_id or not show_id or not seats:
        return jsonify({"error": "Missing booking details"}), 400

    for show in shows:
        if show["show_id"] == show_id and show["movie_id"] == movie_id:

            if show["available_seats"] < seats:
                return jsonify({"error": "Not enough seats"}), 400

            show["available_seats"] -= seats

            movie_price = next(
                (m["price"] for m in movies if m["id"] == movie_id), 0
            )

            booking = {
                "movie_id": movie_id,
                "show_id": show_id,
                "show_time": show["time"],
                "seats": seats,
                "total_price": seats * movie_price
            }

            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Show not found"}), 404


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)
