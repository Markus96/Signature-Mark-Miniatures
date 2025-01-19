import os
import pymongo
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm  # Ensure these forms are defined in forms.py

# Load environment variables if available
if os.path.exists("env.py"):
    import env

# MongoDB URI and Database setup
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "resin_3d_printing"
USERS_COLLECTION = "Users"
PRODUCTS_COLLECTION = "Products"

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MongoDB connection function
def mongo_connect(URL):
    try:
        conn = pymongo.MongoClient(URL)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")

# Connect to MongoDB
conn = mongo_connect(MONGO_URI)
db = conn[DATABASE]
users_collection = db[USERS_COLLECTION]
products_collection = db[PRODUCTS_COLLECTION]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        users_collection.insert_one({
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_password
        })
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users_collection.find_one({'email': form.email.data})
        if user and check_password_hash(user['password'], form.password.data):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)