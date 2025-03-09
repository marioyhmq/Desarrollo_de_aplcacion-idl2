import streamlit as st

def validate_product(name, price, categories, on_sale, image):
    errors = []
    
    if len(name) > 20:
        errors.append("El nombre del producto no debe superar los 20 caracteres.")
    
    try:
        price = float(price)
        if price <= 0 or price > 999:
            errors.append("El precio del producto debe ser mayor a 0 y menor a 999 soles.")
    except ValueError:
        errors.append("El precio debe ser un número decimal válido.")
    
    valid_categories = ["Chocolates", "Caramelos", "Mashmelo", "Galletas", "Salados", "Gomas de mascar"]
    if not set(categories).issubset(set(valid_categories)):
        errors.append("Las categorías seleccionadas no son válidas.")
    
    if len(categories) == 0 or len(categories) > 4:
        errors.append("Debe seleccionar entre 1 y 4 categorías.")
    
    if not on_sale:
        errors.append("El usuario debe definir si el producto está en venta o no.")
    
    if image is None:
        errors.append("Debe subir una imagen del producto.")
    
    return errors

st.title("Registro de Productos - Confitería Dulcino")

with st.form("product_form"):
    name = st.text_input("Nombre del Producto (máximo 20 caracteres)")
    price = st.text_input("Precio del Producto (entre 0 y 999 soles)")
    categories = st.multiselect("Categorías del Producto", ["Chocolates", "Caramelos", "Mashmelo", "Galletas", "Salados", "Gomas de mascar"])
    on_sale = st.radio("¿El producto está en venta?", ["Sí", "No"])
    image = st.file_uploader("Suba una imagen del producto", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button("Registrar Producto")

    if submit:
        errors = validate_product(name, price, categories, on_sale, image)
        
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("¡Felicidades! Su producto se agregó correctamente.")
            if image:
                st.image(image, caption="Imagen del Producto", use_column_width=True)
