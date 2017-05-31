#!/usr/bin/env python3

""" SQLAlchemy """
#
#from product import Product
#from car import Car
#from spyware import Spyware
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#
#engine = create_engine("sqlite:///static/db/blackops.sqlite")
#
#Session = sessionmaker(bind=engine)
#session = Session()
#
#new_product = Spyware(
#    name="Penna",
#    spyware_name="Penna",
#    classification=2,
#    p_type="spyware",
#    amount=50,
#    price=600)
#session.add(new_product)
#session.commit()
#
#products_table = ""
#all_products = session.query(Product).all()
#for product in all_products:
#    products_table += """<tr><td>{id}</td>
#    <td>{name}</td>
#    <td>{p_type}</td>
#    <td>{amount}</td>
#    <td>{price}</td>
#    <td><a href='?del={id}'>Ta bort</a></td></tr>"""\
#    .format(id=product.id, name=product.name,\
#    p_type=product.p_type, amount=product.amount, price=product.price)
#
#print(products_table)

#new_product = Car(
#name=request.form["name"],
#p_type=request.form["p_type"],
#amount=request.form["amount"],
#price=request.form["price"])


#agent = Agent("Marcus")
#
#print(agent.classification)
#
#print(agent.name)

#from flask import request
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from stock import Stock
#
#engine = create_engine("sqlite:///static/db/blackops.sqlite")
#
#Session = sessionmaker(bind=engine)
#session = Session()

#for name, m_type in session.query(Stock.name, Stock.m_type):
#    print("Namn: {n}, Typ: {t}".format(n=name, t=m_type))

#for row in session.query(Stock).filter(Stock.name.like("%Ja%")):
#    print(row)

#for row in session.query(Stock).filter(Stock.name.in_(["a", "Luger", "c", "d"])):
#    print(row)

# get result as a list
#print(session.query(Stock).filter(Stock.amount > 5).all())
