import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import InventoryItem
from app.database import get_db

# SQLAlchemy-based GraphQL object type
class InventoryItemType(SQLAlchemyObjectType):
    class Meta:
        model = InventoryItem

class Query(graphene.ObjectType):
    """
    GraphQL queries to fetch inventory data.
    """
    inventory_items = graphene.List(
        InventoryItemType,
        name=graphene.String()  # Add argument to filter by name
    )

    def resolve_inventory_items(root, info, name=None):
        """
        Fetch all inventory items or filter by name.
        """
        db = next(get_db())
        query = db.query(InventoryItem)

        # Apply filter if name is provided
        if name:
            query = query.filter(InventoryItem.name == name)

        return query.all()

schema = graphene.Schema(query=Query)