import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["example1"]
mycol = mydb["product"]
    
    
def insert_product():
    for i in range(100):
         
        mylist = [
          { "name": "phone"+str(i), "price": 10+i,
           "type":"normal", "category":"Mobile"}
        ]
        
        x = mycol.insert_many(mylist)
 
    
    for i in range(100,200):
         
        mylist = [
          { "name": "phone"+str(i), "monthly_price": 10+i,
           "type":"month", "category":"laptop" }
        ]
        
        x = mycol.insert_many(mylist)
    
    
    for i in range(200,400):
        
        mylist = [
          { "name": "food"+str(i),"monthly_price":40+i,
           "type":"month", "category":"Food"}
        ]
        
        x = mycol.insert_many(mylist)
        
        
    for i in range(400,500):
    
        mylist = [
          { "name": "book"+str(i), "price": 30+i,
           "type":"normal", "category":"Books"},
        ]
        
        x = mycol.insert_many(mylist)
        

# print(x.inserted_ids)

# Menu
print("1- Insert 500 random products into a collection with predefined fields(name, price, type, category)\n")
print("2- Create an unique index on product name.\n")
print("3- Find all the products with price in range (100, 200).\n")
print("4- Calculate sum of prices of all the products in each category.\n")
print("5- See the number of products in each category.\n")
print("0- Exit\n")

print("Attention!!!\ndon't enter 1, two times in a row or you get an error because you're wanting the program to overwrite database with duplicated keys")


while(True):
    command = input("Choose a number : ")
    if command == "0":
        mycol.drop()
        print("collection was dropped successfully.")
            
        # x = mycol.delete_many({})
        # print(x.deleted_count, "documents deleted\nThe program has ended.")
        
        break
        
    elif command == "1":
        insert_product()
        print("operation has been done successfully.")
    
    elif command == "2":
        mycol.create_index('name', unique = True)
        print("operation has been done successfully.")
        
    
    elif command == "3":
        normal_products = mycol.find({"price": {"$lte": 200, "$gte": 100}})
        monthly_products = mycol.find({"monthly_price": {"$lte": 200, "$gte": 100}})
        # monthly_products = mycol.find({"price": {"$lte": 200, "$gte": 100} })
        for p in normal_products:
            print("\n" + str(p))
            
        for p in monthly_products:
            print("\n" + str(p))
    
    elif command == "4":
        normal_price = mycol.aggregate([ { 
            "$group": { 
            "_id": "$category", 
            "total price": { "$sum": "$price" }
    } 
} ] )
        for p in normal_price:
            print(p)
          
        print("")
        monthly_price = mycol.aggregate([ { 
            "$group": { 
            "_id": "$category", 
            "total price": { "$sum": "$monthly_price" }
    } 
} ] )
        for p in monthly_price:
            print(p)

    
    elif command == "5":
        Mobile = mycol.count_documents({
    "category": "Mobile"
})
        
        Laptop = mycol.count_documents({
    "category": "laptop"
    })
        Food = mycol.count_documents({
    "category": "Food"
})
        Books = mycol.count_documents({
    "category": "Books"
})
        print("number of mobiles:", Mobile)
        print("number of laptops:", Laptop)
        print("number of foods:", Food)
        print("number of books:", Books)
    
    
    
