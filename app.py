import random
import streamlit as st

# Configuración de la página para que se vea como una app
st.set_page_config(
    page_title="Cupones para Mamá", page_icon="🎁", layout="centered"
)

# Lista con más de 50 cupones/favores
cupones = [
    "Lavar los platos",
    "Sacar la basura",
    "Hacer las compras del súper",
    "Dar un masaje de espalda de 15 minutos",
    "Hacer la cama",
    "Lavar la ropa",
    "Barrer toda la casa",
    "Limpiar los vidrios de la ventana",
    "Pasear al perro",
    "Hacer el desayuno y llevártelo a la cama",
    "Preparar el mate o café",
    "Cocinar la cena",
    "Ordenar el living",
    "Lavar el auto o moto",
    "Limpiar el baño",
    "Cargar tu celular",
    "Buscar algo que necesites",
    "Ver una película que vos elijas",
    "Escucharte hablar de lo que quieras sin interrumpir",
    "Hacer un mandado urgente",
    "Planchar la ropa",
    "Limpiar la mesa después de comer",
    "Limpiar la cocina a fondo",
    "Cuidar a tus plantas / regarlas",
    "Hacerte compañía toda la tarde",
    "Dar un abrazo gigante",
    "Un comodín: Me pedís lo que quieras por 1 hora",
    "Organizar la heladera",
    "Cambiar las sábanas de la cama",
    "Limpiar el microondas",
    "Desinfectar la compu o celu",
    "Hacer un postre o algo rico",
    "Sacudir los muebles",
    "Acomodar el placard",
    "Tirar lo que no sirve del cajón de la cocina",
    "Acomodar los zapatos de la entrada",
    "Poner a lavar una tanda de ropa",
    "Doblar la ropa limpia",
    "Guardar la ropa limpia en los roperos",
    "Limpiar la pantalla de la tele",
    "Aspirar la alfombra",
    "Limpiar las telarañas del techo",
    "Hacer los mandados de la verdulería",
    "Comprar el pan fresco",
    "Llevar y traer algo que necesites",
    "Armar un playlist con tus canciones favoritas",
    "Hacerte un té calentito",
    "Dar un paseo juntos",
    "Dejarte descansar sin hacer ruido en casa",
    "Hacerte reír con un chiste malo",
    "Cualquier favor extra que necesites hoy",
]

# Diseño de la app
st.title("🎁 Cuponera Sorpresa para Mamá")
st.write(
    "¡Hola, mamá! Tocá el botón de abajo cada vez que quieras canjear un cupón o"
    " favor del día."
)

st.markdown("---")

# Botón para sortear
if st.button("✨ ¡Sortear Cupón de Hoy! ✨"):
  cupon_elegido = random.choice(cupones)
  st.success("¡Te tocó este cupón! 🎉")
  st.markdown(f"### 👉 **{cupon_elegido}**")
  st.balloons()

st.markdown("---")
st.caption(
    "Hecho con amor y código por tu hijo. (Podés guardar esta página en tu"
    " pantalla de inicio como una app)."
)
