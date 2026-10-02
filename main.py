from pyscript import display, document


def SKU_generator(e):
    # Clear previous SKU display output
    document.getElementById('sku_output').innerHTML = " "

    # Fetch values from HTML input fields
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value

    # Build SKU: First 3 letters of category + First 4 letters of product + quantity
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    # Display generated SKU inside the 'sku_output' element
    display("SKU: ", sku, target='sku_output')


def create_order(e):
    # Total items in menu: 23 items
    items = [(f"item{i}", f"qty{i}") for i in range(1, 24)]
    
    subtotal = 0.0

    for item_id, qty_id in items:
        item = document.getElementById(item_id)
        qty_elem = document.getElementById(qty_id)
        
        if item and item.checked:
            price = float(item.value)
            try:
                qty = int(qty_elem.value) if qty_elem and int(qty_elem.value) > 0 else 1
            except ValueError:
                qty = 1
                
            subtotal += price * qty

    # Calculate tax (12% VAT) and final total
    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Format receipt output HTML with comma separators for clean numbers
    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:,.2f}</p>
    <p>Tax (12% VAT): ₱{tax:,.2f}</p>
    <p><strong>Total: ₱{total:,.2f}</strong></p>
    """

    # Render formatted receipt into element with ID 'show'
    document.getElementById("show").innerHTML = receipt