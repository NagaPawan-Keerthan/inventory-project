from flask import Flask
from flask_graphql import GraphQLView
from app.schema import schema
from app.models import Base
from app.database import engine
import sys
import os

# Add the project root directory to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.schema import schema
from app.models import Base
from app.database import engine

# Initialize the Flask app
app = Flask(__name__)

# Create all database tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
    return "Welcome to the Inventory Service! Use /graphql to access the API."

# Add GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Inventory Service runs on port 5001