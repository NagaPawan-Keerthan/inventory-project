import graphene
import requests
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Order
from app.database import get_db

class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order

class Query(graphene.ObjectType):
    """
    GraphQL queries to fetch orders.
    """
    orders = graphene.List(OrderType)

    def resolve_orders(root, info):
        db = next(get_db())
        return db.query(Order).all()

class Mutation(graphene.ObjectType):
    """
    GraphQL mutations to create orders.
    """
    create_order = graphene.Field(OrderType, items=graphene.List(graphene.String))

    def resolve_create_order(root, info, items):
        db = next(get_db())
        total_price = 0.0
        inventory_service_url = "http://localhost:5001/graphql"

        # Fetch prices from Inventory Service
        for item in items:
            query = {
    "query": f"""
    query {{
        inventoryItems(name: "{item}") {{
            name
            price
        }}
    }}
    """
}

            response = requests.post(inventory_service_url, json=query)
            if response.status_code == 200:
                data = response.json()
                price = float(data['data']['inventoryItems'][0]['price'])
                total_price += price
            else:
                raise Exception(f"Failed to fetch price for item: {item}")

        # Insert the order into the database
        new_order = Order(status="Pending", items=items, total_price=total_price)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        return new_order

schema = graphene.Schema(query=Query, mutation=Mutation)