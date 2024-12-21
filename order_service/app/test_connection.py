# # from app.databases import get_db
# # from app.models import Order

import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app.databases import get_db
# from app.models import Order


# def test_db_connection():
#     db = next(get_db())
#     try:
#         # Test query to fetch all orders
#         orders = db.query(Order).all()
#         print(f"Successfully connected! Found {len(orders)} orders.")
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         db.close()

# if __name__ == "__main__":
#     test_db_connection()
from order_service.app.database import get_db
from app.models import Order

def test_db_operations():
    db = next(get_db())
    try:
        # Insert a test order
        new_order = Order(status="Pending", items=["item1", "item2"], total_price=50.75)
        db.add(new_order)
        db.commit()

        # Query all orders
        orders = db.query(Order).all()
        print(f"Found {len(orders)} orders:")
        for order in orders:
            print(order)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_operations()
