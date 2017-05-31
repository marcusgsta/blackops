#!/usr/bin/python3
"""
Controller class
"""
#from sqlalchemy import Column, Float, String, Integer
#from sqlalchemy.ext.declarative import declarative_base
#
#Base = declarative_base()
from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from product import Product
# import all product categories classes
from car import Car
from clothes import Clothes
from computer import Computer
from diving import Diving
from drone import Drone
from firstaid import Firstaid
from radio import Radio
from shoes import Shoes
from spyware import Spyware
from weapon import Weapon

from stock import Stock
from staff import Staff
from rented_material import RentedMaterial

ENGINE = create_engine("sqlite:///static/db/blackops.sqlite")
Session = sessionmaker(bind=ENGINE)
session = Session()


class Controller():
    """Controller class"""

    list_of_categories = ["Välj kategori",
                          "car",
                          "clothes",
                          "computer",
                          "diving",
                          "drone",
                          "firstaid",
                          "radio",
                          "shoes",
                          "spyware",
                          "weapon"]

    def __init__(self):
        """Constructor"""
        pass

    def fix_products_table(self):
        """
        Fix Products table
        """
        products_table = ""
        all_products = session.query(Product).all()
        
        sorted_table = self.sort_list(all_products)
        for product in sorted_table:
#        for product in all_products:
            products_table += """<tr><td>{id}</td>
            <td>{name}</td>
            <td>{p_type}</td>
            <td>{classification}</td>
            <td>{price}</td>
            <td><a href='?del={id}&p_type={p_type}' class="btn btn-primary btn-sm">Ta bort</a></td></tr>"""\
            .format(id=product.id,
                    name=product.name,
                    p_type=product.p_type,
                    classification=product.classification,
                    price=product.price)
        return products_table

    def print_category_table(self, category_class, title, specific_title):
        """
        Print Category table
        """
        category_table = ""
        category = session.query(category_class).all()
#        message = category
        category_table += """
            <thead>
            <h2>{title}</h2>
            <tr>
            <th>#</th>
            <th>Namn</th>
            <th>Klassifikation</th>
            <th>{specific_title}</th>
            </tr>
            </thead>
            <tbody>"""\
            .format(
                title=title,
                specific_title=specific_title)

        for element in category:
            category_table += """
            <tr><td>{id}</td>
            <td>{name}</td>
            <td>{classification}</td>
            <td>{specific}</td>
            </tr>"""\
            .format(
                id=element.id,
                name=element.name,
                classification=element.classification,
                specific=element.get_specific()[1])

        return category_table

    def fix_category_table(self):
        """
        Fix Category table
        """
        category_table = ""
        if request.method == "POST" and request.form["category"] != "Välj kategori":
            this_category = request.form["category"]

            if this_category == "clothes":
                category_table = self.print_category_table(Clothes, "Kläder", "Storlek")

            elif this_category == "car":
                category_table = self.print_category_table(Car, "Bilar", "Typ av bil")

            elif this_category == "computer":
                category_table = self.print_category_table(Computer, "Datorer", "Operativsystem")

            elif this_category == "diving":
                category_table = self.print_category_table(Diving, "Dykutrustning", "Storlek")

            elif this_category == "drone":
                category_table = self.print_category_table(Drone,
                                                           "Droner och dronutrustning",
                                                           "Typ av dron")

            elif this_category == "firstaid":
                category_table = self.print_category_table(Firstaid, "Första hjälpen", "Typ")

            elif this_category == "radio":
                category_table = self.print_category_table(Radio, "Radioutrustning", "Band")

            elif this_category == "shoes":
                category_table = self.print_category_table(Shoes, "Skor", "Storlek")

            elif this_category == "spyware":
                category_table = self.print_category_table(Spyware, "Spionutrustning", "Typ")

            elif this_category == "weapon":
                category_table = self.print_category_table(Weapon, "Vapen", "Typ av vapen")

            return category_table



    def remove_product(self, p_id, p_type):
        """
        Delete product
        """
        if p_type == "car":
            child = session.query(Car).get(p_id)
            session.delete(child)
        if p_type == "clothes":
            child = session.query(Clothes).get(p_id)
            session.delete(child)
        if p_type == "computer":
            child = session.query(Computer).get(p_id)
            session.delete(child)
        if p_type == "drone":
            child = session.query(Drone).get(p_id)
            session.delete(child)
        if p_type == "diving":
            child = session.query(Diving).get(p_id)
            session.delete(child)
        if p_type == "firstaid":
            child = session.query(Firstaid).get(p_id)
            session.delete(child)
        if p_type == "radio":
            child = session.query(Radio).get(p_id)
            session.delete(child)
        if p_type == "shoes":
            child = session.query(Shoes).get(p_id)
            session.delete(child)
        if p_type == "spyware":
            child = session.query(Spyware).get(p_id)
            session.delete(child)
        if p_type == "weapon":
            child = session.query(Weapon).get(p_id)
            session.delete(child)

        session.commit()
        message = """
        <div class="alert alert-dismissible alert-danger">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        Produkt raderades!
        </div>
        """
        return message

    def add_product(self):
        """
        Add product
        """
        p_type = request.form["p_type"]

        if p_type == "car":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Car(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "clothes":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]
            new_product = Clothes(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "computer":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Computer(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "diving":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Diving(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "drone":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Drone(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "firstaid":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Firstaid(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "radio":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Radio(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "shoes":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Shoes(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        if p_type == "spyware":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Spyware(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()


        if p_type == "weapon":
            arguments_list = [request.form["name"],
                              p_type,
                              request.form["price"],
                              request.form["specific"]]

            new_product = Weapon(
                arguments_list=arguments_list,
                classification=request.form["classification"])
            session.add(new_product)
            session.commit()

        message = """
        <div class='alert alert-dismissible alert-success'>
        <button type='button' class='close' data-dismiss='alert'>&times;</button>
        Produkt lades till!
        </div>
        """
        return message

    def add_products_to_stock(self):
        """
        Add products to stock
        """
        product_id = request.form["p_select"]
        product = session.query(Product).get(product_id)
        p_name = product.name
        p_classification = product.classification
        p_amount = request.form["amount"]

        new_product = Stock(
            name=p_name,
            classification=p_classification,
            amount=p_amount)

        session.add(new_product)
        session.commit()
        message = """
        <div class='alert alert-dismissible alert-success'>
        <button type='button' class='close' data-dismiss='alert'>&times;</button>
        Produkterna lades till i lagret
        </div>
        """
        return message

    def remove_from_stock(self, remove_from_stock):
        """
        Remove products from stock
        """
        session.query(Stock).filter(Stock.id == remove_from_stock).delete()
        session.commit()
        message = """
        <div class="alert alert-dismissible alert-danger">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        Produkt raderades från lagret!
        </div>
        """
        return message

    def get_list_of_stock(self):
        """
        Get list of stock
        """
        list_of_stock = session.query(Stock).all()
        return list_of_stock

    def fix_stock_table(self):
        """
        Fix stock table
        """
        stock_table = ""
        whole_stock = session.query(Stock).all()

        sorted_list = self.sort_list(whole_stock)
        for product in sorted_list:
#        for product in whole_stock:
            stock_table += """<tr><td>{id}</td>
            <td>{name}</td>
            <td>{classification}</td>
            <td>{amount}</td>
            <td><a href='?del={id}' class="btn btn-primary btn-sm">Ta bort</a></td></tr>"""\
            .format(id=product.id, name=product.name,\
            classification=product.classification, amount=product.amount)
        return stock_table

    def rent_product(self):
        """
        Rent product
        """
        employee = request.form["employee"]
        product_id = request.form["p_select"]
        amount = float(request.form["amount"])
        cl_employee = session.query(Staff).get(employee).role
        cl_product = session.query(Stock).get(product_id).classification
        if cl_employee < cl_product:
            message = """
            <div class="alert alert-dismissible alert-danger">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            Personen har inte rätt behörighet!
            </div>
            """
            return message

        amount_of_product = session.query(Stock).get(product_id).amount
        if amount_of_product - amount >= 0:
            session.query(Stock).filter(Stock.id ==\
            product_id).update({"amount": (Stock.amount - amount)})
            employee_name = session.query(Staff).get(employee).name
            product_name = session.query(Stock).get(product_id).name
            product_id = session.query(Stock).get(product_id).id

            new_item = RentedMaterial(
                person_name=employee_name,
                product_name=product_name,
                amount=amount,
                product_id=product_id)
            session.add(new_item)
            session.commit()
            message = """
            <div class="alert alert-dismissible alert-success">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            Uthyrning genomförd!
            </div>
            """
            return message

        else:
            message = """
            <div class="alert alert-dismissible alert-danger">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            Uthyrning misslyckades! Det finns inte tillräckligt av produkten på lager.
            </div>
            """
            return message

    def return_product(self, return_this_product):
        """
        Return product
        """
        amount = session.query(RentedMaterial).get(return_this_product).amount
        product_id = session.query(RentedMaterial).get(return_this_product).product_id

        session.query(Stock).filter(Stock.id == \
        product_id).update({"amount": (Stock.amount + amount)})
        session.commit()

        session.query(RentedMaterial).filter(RentedMaterial.id == return_this_product).delete()
        session.commit()

    def sort_list(self, list_of_items):
        """
        Sort items with 'ordered list' class
        """
        from unorderedlist import OrderedList
        new_list = OrderedList()
        for item in list_of_items:
            new_list.add(item)
        return new_list

    def fix_staff_table(self):
        """
        Fix Staff table
        """
        staff_table = ""
        all_staff = session.query(Staff).all()
        sorted_list = self.sort_list(all_staff)
#        message = sorted_list
#        for staff in all_staff:
        for staff in sorted_list:
            staff_table += """<tr><td>{id}</td>
            <td>{name}</td>
            <td>{role}</td>
            <td><a href='?del={id}' class="btn btn-primary btn-sm">Ta bort</a></td></tr>"""\
            .format(id=staff.id, name=staff.name, role=staff.role)
        return staff_table
#        return message

    def fix_rented_products_table(self):
        """
        Fix Rented Products table
        """
        rented_products_table = ""
        all_rented_products = session.query(RentedMaterial).all()
        for product in all_rented_products:
            rented_products_table += """<tr><td>{person_name}</td>
            <td>{product_name}</td><td>{amount}</td>
            <td><a href='?return={id}' class="btn btn-primary btn-sm">Returnera</a></td></tr>"""\
            .format(person_name=product.person_name,\
            product_name=product.product_name, amount=product.amount, id=product.id)
        return rented_products_table

    def remove_staff(self, del_this_person):
        """
        Delete person
        """
        session.query(Staff).filter(Staff.id == del_this_person).delete()
        session.commit()
        message = """
        <div class="alert alert-dismissible alert-danger">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        Personen raderades!
        </div>
        """
        return message

    def add_staff(self):
        """
        Add person
        """
        new_person = Staff(
            name=request.form["name"],
            role=request.form["role"])

        session.add(new_person)
        session.commit()
        message = """
        <div class='alert alert-dismissible alert-success'>
        <button type='button' class='close' data-dismiss='alert'>&times;</button>
        Person lades till!
        </div>
        """
        return message

    def change_staff(self):
        """
        Change classification of staff
        """
        new_classification = request.form["role"]
        employee = request.form["employee"]
        session.query(Staff).filter(Staff.id == employee).update({"role": new_classification})
        session.commit()
        message = """
        <div class="alert alert-dismissible alert-success">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        Klassificering ändrades!
        </div>
        """
        return message

    def get_list_of_staff(self):
        """Get list of staff"""
        staff_list = session.query(Staff).all()
        return staff_list

    def get_list_of_products(self):
        """Get list of material"""
        product_list = session.query(Product).all()
        return product_list
