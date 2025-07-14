from graphviz import Digraph

def create_erd():
    er = Digraph('ERD', filename='banking_erd', format='png')
    
    # Entities
    er.node('Customer', shape='ellipse')
    er.node('Account', shape='ellipse')
    er.node('Transaction', shape='ellipse')
    
    # Attributes
    er.node('Cust_ID', shape='oval')
    er.node('Last_Name', shape='oval')
    er.node('First_Name', shape='oval')
    er.node('Address', shape='oval')
    er.node('Customer_Type', shape='oval')
    
    er.node('Acc_ID', shape='oval')
    er.node('Balance', shape='oval')
    er.node('Interest_Rate', shape='oval')
    er.node('Date_Opened', shape='oval')
    er.node('Account_Type', shape='oval')
    
    er.node('Trans_ID', shape='oval')
    er.node('Amount', shape='oval')
    er.node('Type', shape='oval')
    er.node('Date', shape='oval')
    er.node('Location', shape='oval')
    er.node('Comments', shape='oval')
    
    # Relationships
    er.node('Owns', shape='diamond')
    er.node('Has', shape='diamond')
    er.node('Involves', shape='diamond')
    
    # Connections
    er.edge('Cust_ID', 'Customer')
    er.edge('Last_Name', 'Customer')
    er.edge('First_Name', 'Customer')
    er.edge('Address', 'Customer')
    er.edge('Customer_Type', 'Customer')
    
    er.edge('Acc_ID', 'Account')
    er.edge('Balance', 'Account')
    er.edge('Interest_Rate', 'Account')
    er.edge('Date_Opened', 'Account')
    er.edge('Account_Type', 'Account')
    
    er.edge('Trans_ID', 'Transaction')
    er.edge('Amount', 'Transaction')
    er.edge('Type', 'Transaction')
    er.edge('Date', 'Transaction')
    er.edge('Location', 'Transaction')
    er.edge('Comments', 'Transaction')
    
    # Relationships connections
    er.edge('Customer', 'Owns')
    er.edge('Owns', 'Account')
    
    er.edge('Account', 'Has')
    er.edge('Has', 'Transaction')
    
    er.edge('Transaction', 'Involves')
    er.edge('Involves', 'Account')
    
    return er

# Generate and render the ER diagram
erd_diagram = create_erd()
erd_diagram.render(view=True)