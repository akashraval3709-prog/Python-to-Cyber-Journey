from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql://root:@localhost/product"
app.config['SQLALCHEMY_TREACK_MODIFICATION'] =False
db =SQLAlchemy(app)
#
class inventory(db.Model):
    
    id = db.Column(db.Integer , primary_key=True)
    product_code =db.Column(db.String(20),unique=True ,nullable=False)
    name = db.Column(db.String(50) ,nullable=False)
    price=db.Column(db.Float,nullable=False)
    stock=db.Column(db.Integer , nullable=False)
    
with app.app_context():
    try:
        db.create_all() 
        
        inventoryList=[inventory( product_code='LAP101', name='HP Laptop', price=55000, stock=12),
                    inventory( product_code='MOB202', name='Samsung S24', price=75000, stock=8),
                    inventory( product_code='MOU303', name='Wireless Mouse', price=1200, stock=0),
                    inventory( product_code='KEY404', name='Keyboard', price=2000, stock=15),
                   
                    ]   
        productNum = inventory.query.count()
        if productNum ==0:    
            db.session.add_all(inventoryList)
            db.session.commit()
            
        allData = inventory.query.all()
        
        for data in allData:
            print(f"{data.product_code}\t{data.name}\t{data.price}\t{data.stock}")
        highPrice = inventory.query.order_by(inventory.price.desc()).first()
        if highPrice:
            print(f'\nHigh Price Product : {highPrice.name}')
            print(f'Price : {highPrice.price}')
        else:
            print("No products found in database.")
        
        quantity = inventory.query.filter(inventory.stock > 8)
        print("\nProduct stock more thane 8 is ")
        for i in quantity:
            print(i.name)
            
        
        updateData = inventory.query.filter_by(stock=0).update({inventory.stock: inventory.stock+10})
        
        if updateData == 1:
            update = inventory.query.filter_by(product_code ='MOU303').first()
            print(f'{update.name} {update.stock} \n')
         
        allData = inventory.query.all()
        
        for data in allData:
            print(f"{data.product_code}\t{data.name}\t{data.price}\t{data.stock}")
        
        print("\n--- Products Sorted A-Z ---")
        sortedData = inventory.query.order_by(inventory.name.asc()).all()
        for data in sortedData:
            print(f"{data.product_code}\t{data.name}\t{data.price}\t{data.stock}")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("Rollback Done! Products already exist.")
        print(e)