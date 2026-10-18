import random
import streamlit as st

#Lavar los platos 12, Sacar la basura 10, Hacer LAS camas 10, Ir a comprar 10, Ver peli 5, pedir LO QUE QUIERAS 15, 

# Configuración inicial de la memoria (para que guarde el stock mientras usa la app)
if "cupones" not in st.session_state:
  # Acá ponés tu lista con la cantidad de veces que querés que esté disponible cada uno
  st.session_state.cupones = [
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Lavar los platos🥛🥄",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Sacar la basura🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Hacer las camas🛏️",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ir a comprar🛒",
      "Ver una peli🎬",
      "Ver una peli🎬",
      "Ver una peli🎬",
      "Ver una peli🎬",
      "Ver una peli🎬",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Pedirme LO QUE QUIERAS🌠",
      "Comando de 1 hora",
  ]

st.title("🎁 Cuponera para vos maa ♥️")

# Verificamos si todavía quedan cupones en la lista
if len(st.session_state.cupones) > 0:
  st.write(f"‼️ Cupones disponibles: 🎫 {len(st.session_state.cupones)}")

  if st.button("✨ ¡Sortear Cupón! ✨"):
    # Elegimos uno al azar
    elegido = random.choice(st.session_state.cupones)
    # Lo borramos usando .remove() para que no vuelva a salir hasta que se acaben
    st.session_state.cupones.remove(elegido)

    st.success("Te tocó este cupón 🎉")
    st.markdown(f"### 👉 **{elegido}**")
else:
  st.balloons()
  st.warning("🥀¡uy se acabaron todos los cupones!😔")
