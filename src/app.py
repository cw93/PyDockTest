from turtle import update
from flask import Flask, jsonify, request

products = [
            {'id' : 1, 'name': 'Product 1'},
            {'id' : 2, 'name': 'product 2'}            
           ]

app = Flask(__name__) #Main


#new test
# curl -v http://localhost:5000/products
@app.route('/products') #Decorator that is added to any function that handles web request.
def get_products():
    return jsonify(products) #convert python list to json string

# curl -v http://localhost:5000/products/1
@app.route('/product/<int:id>')
def get_product(id):
    #Running through all of the products that have the specified id
    product_list = [product for product in products if product['id'] == id]
    if(len(product_list) == 0):
        return f'Product with id {id} not found', 404 #error string tuple
    return jsonify(product_list[0]) #If list is not empty return the first element in the list.
        
# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}'
# -v http://localhost:5000/products/   ------ Handles a post http method to /products/
@app.route('/product/', methods=['POST'])
def post_product():
    #Retrieves the product from the request body
    request_product = request.json
    
    #Generate an ID for the post (add one to the amount of matching id's)
    new_id = max([product['id'] for product in products]) + 1
    
    #Create a new product
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }
    
    #Append the new product to our product list
    products.append(new_product)
    
    #Return the new product back to the client
    return jsonify(new_product), 201

# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 2"}'
# -v http://localhost:5000/products/   ------ Handles a put http method to /products/?
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    updated_product = request.json
    
    #Find the product with the specified ID
    for product in products:
        if product['id'] == id:
            #Update the product name
            product['name'] = updated_product['name']
            return jsonify(product), 200
        
    return f'Product with id {id} not found', 404

#curl --request DELETE -v http://localhost:5000/product/2
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    #find the product with the specified ID
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'product with id {id} deleted', 200
    
    return f'Product with id {id} not found', 404

if __name__ == '__main__':
    #debug = true - make flask reload application on code changes
    #host = '0.0.0.0'
    app.run(debug=True, host='0.0.0.0')
    