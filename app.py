from flask import Flask, render_template, session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'secret-key'

# Sample products
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Headphones', 'price': 100},
    {'id': 3, 'name': 'Keyboard', 'price': 50},
    {'id': 4, 'name': 'Mouse', 'price': 30},
    {'id': 5, 'name': 'Smartphone', 'price': 800},
    {'id': 6, 'name': 'Monitor', 'price': 200},
    {'id': 7, 'name': 'Webcam', 'price': 60},
    {'id': 8, 'name': 'Speaker', 'price': 120},
    {'id': 9, 'name': 'Tablet', 'price': 400},
    {'id': 10, 'name': 'Charger', 'price': 25},
    {'id': 10, 'name': 'cellphone', 'price': 25},
    {'id': 10, 'name': 'PowerBank', 'price': 25},
]


@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/remove/<int:index>')
def remove_from_cart(index):
    cart = session.get('cart', [])
    if 0 <= index < len(cart):
        cart.pop(index)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    if not cart:
        return redirect(url_for('index'))
    
    total = sum(item['price'] for item in cart)

    if request.method == 'POST':
        # Simulate payment processing
        session.pop('cart', None)
        flash('Payment successful! Thank you for your purchase.')
        return redirect(url_for('payment_success'))

    return render_template('checkout.html', total=total)

@app.route('/success')
def payment_success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
