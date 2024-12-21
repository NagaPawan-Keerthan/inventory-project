from flask import Flask
from flask_graphql import GraphQLView
from app.schema import schema
from app.models import Base
from app.database import engine

# Initialize the Flask app
app = Flask(__name__)

# Create all database tables
Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
    return "Welcome to the Order Service! Use /graphql to access the API."

# Add GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)