from flask import Flask, request, render_template, redirect
app = Flask(__name__)

# Register the setup page and import create_connection()
from utils import create_connection, setup
app.register_blueprint(setup)


@app.route('/')
def home():
    return "Hello World!"


# TODO: Add a '/register' (add_user) route that uses INSERT
@app.route('/register', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        with create_connection() as connection:
            with connection.cursor() as cursor:
                sql = """INSERT INTO users
                    (first_name, last_name, email, password)
                    VALUES (%s, %s, %s, %s)
                """
                values = (
                    request.form['first_name'],
                    request.form['last_name'],
                    request.form['email'],
                    request.form['password']
                )
                cursor.execute(sql, values)
                connection.commit()
        return redirect('/')
    return render_template('users_add.html')

# TODO: Add a '/dashboard' (list_users) route that uses SELECT

# TODO: Add a '/profile' (view_user) route that uses SELECT

# TODO: Add a '/delete_user' route that uses DELETE

# TODO: Add an '/edit_user' route that uses UPDATE



if __name__ == '__main__':
    import os

    # This is required to allow flashing messages. We will cover this later.
    app.secret_key = os.urandom(32)

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
