
import streamlit as st
import pandas as pd
import mysql.connector

def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1141",
        database="dbms"
    )
    return conn

# Function to execute a query
def execute_query(query, params=None):
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Function to fetch data
def fetch_data(query, params=None):
    conn = create_conn()
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

# Function to add data
def add_data(table, values):
    query = f"INSERT INTO {table} VALUES ({', '.join(['%s'] * len(values))})"
    execute_query(query, values)

# Function to view data
def view_data(table):
    query = f"SELECT * FROM {table}"
    return fetch_data(query)

# Function to remove data
def remove_data(table, condition):
    query = f"DELETE FROM {table} WHERE {condition}"
    execute_query(query)

# Function to sort data
def sort_values(table, sortby):
    query = f"SELECT * FROM {table} ORDER BY {sortby}"
    return fetch_data(query)
# Function to sort data in reverse
def sort_values_rev(table, sortby):
    query = f"SELECT * FROM {table} ORDER BY {sortby} DESC"
    return fetch_data(query)

# Streamlit app
def main():
    st.title("Ecommerce database management system")

    st.markdown("<h2 style='text-align: center; color: white; padding: 0px'>Select an Operation</h3>", unsafe_allow_html=True)    
    operation = st.selectbox("", ("",'Update', 'View',"Find","Join"))

    if operation == 'Update':
        operation2=st.selectbox( "Select operations under {}".format(operation), ("",'Add','Remove'))

        if operation2 == 'Add':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))

            if table == 'Customer_Address':
                Address_id = st.number_input("Address ID")
                House_no = st.text_input("House Number")
                Area = st.text_input("Area")
                City = st.text_input("City")
                State = st.text_input("State")
                Pincode = st.text_input("Pincode")
                Customer_Id = st.number_input("Customer ID")
                if st.button("Add Address"):
                    add_data('Customer_Address', (Address_id, House_no, Area, City, State, Pincode, Customer_Id))
                    st.success("Data added successfully to Address")
            elif table == 'Employee_Address':
                Address_id = st.number_input("Address ID")
                House_no = st.text_input("House Number")
                Area = st.text_input("Area")
                City = st.text_input("City")
                State = st.text_input("State")
                Pincode = st.text_input("Pincode")
                Customer_Id = st.number_input("Customer ID")
                if st.button("Add Address"):
                    add_data('Employee_Address', (Address_id, House_no, Area, City, State, Pincode, Customer_Id))
                    st.success("Data added successfully to Address")

            elif table == 'Customers':
                Customer_Id = st.number_input("Customer ID")
                User_Name = st.text_input("User Name")
                Name = st.text_input("Name")
                DOB = st.date_input("Date of Birth")
                Age = st.number_input("Age")
                Gender = st.text_input("Gender")
                if st.button("Add Customers"):
                    add_data('Customers', (Customer_Id, User_Name, Name, DOB, Age, Gender))
                    st.success("Data added successfully to Customers")

            elif table == 'Phone_Customer':
                Customer_Id = st.number_input("Customer ID")
                Phone_No = st.number_input("Phone Number")
                if st.button("Add Phone_Customer"):
                    add_data('Phone_Customer', (Customer_Id, Phone_No))
                    st.success("Data added successfully to Phone_Customer")

            elif table == 'Employees':
                Employee_Id = st.number_input("Employee ID")
                Name = st.text_input("Name")
                DOB = st.date_input("Date of Birth")
                Age = st.number_input("Age")
                Gender = st.text_input("Gender")
                Manager_Id = st.number_input("Manager ID")
                if st.button("Add Employees"):
                    add_data('Employees', (Employee_Id, Name, DOB, Age, Gender, Manager_Id))
                    st.success("Data added successfully to Employees")

            elif table == 'Phone_Employee':
                Employee_Id = st.text_input("Employee ID")
                Phone_No = st.text_input("Phone Number")
                if st.button("Add Phone_Employee"):
                    add_data('Phone_Employee', (Employee_Id, Phone_No))
                    st.success("Data added successfully to Phone_Employee")

            elif table == 'Branch':
                Branch_Id = st.number_input("Branch ID")
                Employee_Id = st.number_input("Employee ID")
                Salary = st.number_input("Salary")
                if st.button("Add Branch"):
                    add_data('Branch', (Branch_Id, Employee_Id, Salary))
                    st.success("Data added successfully to Branch")

            elif table == 'Product_Category':
                Category_Id = st.number_input("Category ID")
                Category_Name = st.text_input("Category Name")
                Category_description = st.text_input("Category Description")
                if st.button("Add Product_Category"):
                    add_data('Product_Category', (Category_Id, Category_Name, Category_description))
                    st.success("Data added successfully to Product_Category")

            elif table == 'Product':
                Product_Id = st.number_input("Product ID")
                Product_Name = st.text_input("Product Name")
                Product_Price = st.text_input("Product Price")
                Product_Category_Id = st.number_input("Product Category ID")
                if st.button("Add Product"):
                    add_data('Product', (Product_Id, Product_Name, Product_Price, Product_Category_Id))
                    st.success("Data added successfully to Product")

            elif table == 'Reviews':
                Customer_Id = st.number_input("Customer ID")
                Product_Id = st.number_input("Product ID")
                Rating = st.text_input("Rating")
                if st.button("Add Reviews"):
                    add_data('Reviews', (Customer_Id, Product_Id, Rating))
                    st.success("Data added successfully to Reviews")

            elif table == 'Orders':
                Order_Id = st.number_input("Order ID")
                Customer_Id = st.number_input("Customer ID")
                Number_Of_Products = st.number_input("Number of Products")
                Order_Date = st.date_input("Order Date")
                Total_Amount = st.number_input("Total Amount")
                if st.button("Add Orders"):
                    add_data('Orders', (Order_Id, Customer_Id, Number_Of_Products, Order_Date, Total_Amount))
                    st.success("Data added successfully to Orders")

            elif table == 'Agency':
                Agency_id = st.number_input("Agency ID")
                Order_Id = st.number_input("Order ID")
                Agency_Name = st.text_input("Agency Name")
                Pickup_date = st.date_input("Pickup Date")
                Drop_Date = st.date_input("Drop Date")
                if st.button("Add Agency"):
                    add_data('Agency', (Agency_id, Order_Id, Agency_Name, Pickup_date, Drop_Date))
                    st.success("Data added successfully to Agency")

            elif table == 'Offers':
                Product_Id = st.number_input("Product ID")
                Offer_Id = st.number_input("Offer ID")
                Total_Discount = st.number_input("Total Discount")
                if st.button("Add Offers"):
                    add_data('Offers', (Product_Id, Offer_Id, Total_Discount))
                    st.success("Data added successfully to Offers")

            elif table == 'Payment':
                Payment_Id = st.number_input("Payment ID")
                Order_id = st.number_input("Order ID")
                Payment_Method = st.text_input("Payment Method")
                if st.button("Add Payment"):
                    add_data('Payment', (Payment_Id, Order_id, Payment_Method))
                    st.success("Data added successfully to Payment")

            elif table == 'Variation':
                Variation_Id = st.number_input("Variation ID")
                Product_Id = st.number_input("Product ID")
                Size = st.number_input("Size")
                Color = st.text_input("Color")
                Stock = st.number_input("Stock")
                if st.button("Add Variation"):
                    add_data('Variation', (Variation_Id, Product_Id, Size, Color, Stock))
                    st.success("Data added successfully to Variation")
        elif operation2 == 'Remove':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            condition = st.text_input("Enter condition ")
            if st.button("Remove"):
                remove_data(table, condition)
                st.success("Data removed successfully")
    
    

    

    elif operation == 'View':
        operation2=st.selectbox( "Select operations under {}".format(operation), ("",'View','Sort','Sort_Reverse','View with condition'))
        if operation2 == 'View':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            if st.button("View"):
                data = view_data(table)
                st.table(data)
        elif operation2 == 'View with condition':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            condition = st.text_input("Enter condition")
            if st.button("View with condition"):
                query = f"SELECT * FROM {table} WHERE {condition}"
                data = fetch_data(query)
                st.table(data)
        elif operation2 == 'Sort':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            sortby=st.text_input("Enter column name to sort by")
            if st.button("Sort"):
                data=sort_values(table,sortby)
                st.table(data)
        elif operation2 == 'Sort_Reverse':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            sortby=st.text_input("Enter column name to sort by")
            if st.button("Sort_Reverse"):
                data=sort_values_rev(table,sortby)
                st.table(data)
    
    elif operation == 'Find':
        finding = st.selectbox("To Find", ("",'Max', 'Min', 'Sum', 'Average'))
        if finding == 'Max':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column = st.text_input("Enter column name to find max")
            if st.button("Find Max"):
                st.session_state['find_max_clicked'] = True
                query = f"SELECT MAX({column}) FROM {table}"
                data = fetch_data(query)
                st.session_state['max_data'] = data
                st.session_state['max_value'] = data.iloc[0,0]  # assuming the max value is in the first row and column of the returned DataFrame
            if st.session_state.get('find_max_clicked', False):
                st.table(st.session_state['max_data'])

            viewing = st.selectbox("View data", ("",'Row', 'Row with condition'))
            if viewing == 'Row':
                query1 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['max_value']}"
                data1 = fetch_data(query1)
                st.table(data1)
            elif viewing == 'Row with condition':
                condition = st.selectbox("Select Condition", ("",'Equal', 'Greater', 'Less'))
                if condition == 'Equal':
                    query2 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['max_value']}"
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Greater':
                    query2 = f"SELECT * FROM {table} WHERE {column} > {st.session_state['max_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Less':
                    query2 = f"SELECT * FROM {table} WHERE {column} < {st.session_state['max_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)
        elif finding == 'Min':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column = st.text_input("Enter column name to find min")
            if st.button("Find Min"):
                st.session_state['find_min_clicked'] = True
                query = f"SELECT MIN({column}) FROM {table}"
                data = fetch_data(query)
                st.session_state['min_data'] = data
                st.session_state['min_value'] = data.iloc[0,0]
            if st.session_state.get('find_min_clicked', False):
                st.table(st.session_state['min_data'])
            viewing = st.selectbox("View data", ("",'Row', 'Row with condition'))
            if viewing == 'Row':
                query1 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['min_value']}"
                data1 = fetch_data(query1)
                st.table(data1)
            elif viewing == 'Row with condition':
                condition = st.selectbox("Select Condition", ("",'Equal', 'Greater', 'Less'))
                if condition == 'Equal':
                    query2 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['min_value']}"
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Greater':
                    query2 = f"SELECT * FROM {table} WHERE {column} > {st.session_state['min_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Less':
                    query2 = f"SELECT * FROM {table} WHERE {column} < {st.session_state['min_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)
        elif finding == 'Sum':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column = st.text_input("Enter column name to find sum")
            if st.button("Find Sum"):
                query = f"SELECT SUM({column}) FROM {table}"
                data = fetch_data(query)
                st.table(data)
        elif finding == 'Average':
            table = st.selectbox("Select table", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column = st.text_input("Enter column name to find average")
            if st.button("Find Average"):
                query = f"SELECT AVG({column}) FROM {table}"
                data = fetch_data(query)
                st.table(data)
                st.session_state['average_value'] = data.iloc[0,0]
            viewing = st.selectbox("View data", ("",'Row', 'Row with condition'))
            if viewing == 'Row':
                query1 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['average_value']}"
                data1 = fetch_data(query1)
                st.table(data1)
            elif viewing == 'Row with condition':
                condition = st.selectbox("Select Condition", ("",'Equal', 'Greater', 'Less'))
                if condition == 'Equal':
                    query2 = f"SELECT * FROM {table} WHERE {column} = {st.session_state['average_value']}"
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Greater':
                    query2 = f"SELECT * FROM {table} WHERE {column} > {st.session_state['average_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)
                elif condition == 'Less':
                    query2 = f"SELECT * FROM {table} WHERE {column} < {st.session_state['average_value']} "
                    data2 = fetch_data(query2)
                    st.table(data2)

    elif operation == 'Join':
        typeofjoin=st.selectbox("Select type of join", ("","Cross",'Inner Join','Left Join','Right Join'))
        if typeofjoin == 'Cross':
            table1 = st.selectbox("Select table1", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            table2 = st.selectbox("Select table2", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            if st.button("Cross Join"):
                query = f"SELECT * FROM {table1} CROSS JOIN {table2}"
                data = fetch_data(query)
                st.table(data)
        elif typeofjoin == 'Inner Join':
            table1 = st.selectbox("Select table1", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            table2 = st.selectbox("Select table2", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column1 = st.text_input("Enter column name to join on table1")
            column2 = st.text_input("Enter column name to join on table2")
           
            if st.button("Inner Join"):
                query = f"SELECT * FROM {table1} INNER JOIN {table2} ON {table1}.{column1} = {table2}.{column2}"
                data = fetch_data(query)
                st.table(data)
        elif typeofjoin == 'Left Join':
            table1 = st.selectbox("Select table1", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            table2 = st.selectbox("Select table2", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column1 = st.text_input("Enter column name to join on table1")
            column2 = st.text_input("Enter column name to join on table2")
           
            if st.button("Left Join"):
                query = f"SELECT * FROM {table1} LEFT JOIN {table2} ON {table1}.{column1} = {table2}.{column2}"
                data = fetch_data(query)
                st.table(data)
        elif typeofjoin == 'Right Join':
            table1 = st.selectbox("Select table1", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            table2 = st.selectbox("Select table2", ("",'Customers','Customer_Address','Employee_Address',  'Phone_Customer', 'Employees', 'Phone_Employee', 'Branch', 'Product_Category', 'Product', 'Reviews', 'Orders', 'Agency', 'Offers', 'Payment', 'Variation'))
            column1 = st.text_input("Enter column name to join on table1")
            column2 = st.text_input("Enter column name to join on table2")
           
            if st.button("Right Join"):
                query = f"SELECT * FROM {table1} RIGHT JOIN {table2} ON {table1}.{column1} = {table2}.{column2}"
                data = fetch_data(query)
                st.table(data)
       

    
if __name__ == "__main__":
    main()
