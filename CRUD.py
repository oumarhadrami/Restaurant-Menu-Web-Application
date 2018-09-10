from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Creating or inserting in database:

MyFirstRestaurant = Restaurant(name='Vitamin Palace')
session.add(MyFirstRestaurant)
session.commit()

fruitbowl = MenuItem(name='Fruit Bowl', description='Best fruits combined',
                     course='Entree', price='$1.5', restaurant=MyFirstRestaurant)
session.add(fruitbowl)
session.commit()


# Read from databse:

print("The restaurants:\n ")
for item in session.query(Restaurant).all():
    print(item.name)

print()

print("Menu Items:\n ")
for item in session.query(MenuItem).all():
    print(item.name)


# Update database:

veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()


# Deleting from database:

spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
