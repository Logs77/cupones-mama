import random
from datetime import date
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cuponera para Mamá", page_icon="🎁", layout="centered"
)

# 1. Configuración inicial de la memoria
if "cupones" not in st.session_state:
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
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
      "Sacar la basura🗑️",
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
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Tender la ropa👕",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Ordenar la ropa🧦👚🧣",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Hacer la comida (O ayudarte)🍗",
      "Ordenar y limpiar la COCINA 🧹",
      "Ordenar y limpiar la COCINA 🧹",
      "Ordenar y limpiar la COCINA 🧹",
      "Ordenar y limpiar la COCINA 🧹",
      "Ordenar y limpiar la COCINA 🧹",
      "Ordenar y limpiar la PIEZA 🛏️",
      "Ordenar y limpiar la PIEZA 🛏️",
      "Ordenar y limpiar la PIEZA 🛏️",
      "Ordenar y limpiar el BAÑO 🚽",
      "Ordenar y limpiar el BAÑO 🚽",
      "Ordenar y limpiar el BAÑO 🚽",
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
  ]

if "cupón_actual" not in st.session_state:
  st.session_state.cupón_actual = None

if "ultima_fecha_canje" not in st.session_state:
  st.session_state.ultima_fecha_canje = None

if "cupon_hoy_canjeado" not in st.session_state:
  st.session_state.cupon_hoy_canjeado = None

if "efecto" not in st.session_state:
  st.session_state.efecto = None

# Lanzar efectos visuales guardados
if st.session_state.efecto == "globos":
  st.balloons()
  st.session_state.efecto = None
elif st.session_state.efecto == "nieve":
  st.snow()
  st.session_state.efecto = None

# 2. CARTITA
with st.expander("💌 Ver carta especial para vos 💌"):
  st.markdown(
      """
        ### ¡Feliz día má!
        Este programa (cuponera) lo hice con mucho amor, esfuerzo y programación exclusivamente para vos♥️.     
        
        Cada vez que necesites un favor o algo, podés usar un cupón apretando el botón. Este año no tuve plata para regalarte nada pero bueno aunque este regalo no sea casi nada se me ocurrió porque sé programar, es para ayudarte en lo que necesites y lo que quieras.
        
        Te quiero muchísimo, gracias por aguantarme todos los días, sé que es muy difícil mantener al mejor hijo del mundo😎. Pero bueno, aunque a veces discutimos, yo te quiero un montón y te voy a seguir queriendo más todavía, sé que a veces pido mucho pero bueno ya no te voy a pedir más cosas (esperemos, na mentira), voy a intentar ayudarte en todo lo que pueda para devolverte un poquitito de lo que me das cada día🫶.
♥️♥️Te quiero mucho ma♥️♥️
♥️♥️♥️♥️FELÍZ DÍA♥️♥️♥️♥️
        """
  )

# 3. INFO
with st.expander("ℹ️ INFO sobre cupones ℹ️"):
  st.markdown(
      f"""
      ### 🎫 Información sobre los cupones 🎫:
• Hay en total {len(st.session_state.cupones)} cupones disponibles en el stock. Cuando apretás el botón de -Sortear Cupón- aleatoriamente se elige uno, pero **no se gasta** hasta que aprietes "ELEGIR ESE". Si no te gusta, podés reelegir las veces que quieras sin gastar stock.
• ‼️ **LÍMITE:** Podés canjear **1 cupón por día**.
• ‼️ **IMPORTANTE:** VIERNES Y SÁBADO NO LABURO😠
• Y son estos (Su nombre y la cantidad inicial):
- Lavar los platos 🍽️🥛 12
- Sacar la basura 🗑️ 10
- Hacer las camas 🛏️ 15
- Ir a comprar 🛒 10
- Ver peli 🎞️ 5
- Tender la ropa 👕 8
- Ordenar la ropa 🧦👚🧣 7
- Hacer la comida (o ayudarte) 🍗 15
- Ordenar y limpiar la COCINA 🧹 5
- Ordenar y limpiar la PIEZA 🛏️ 3
- Ordenar y limpiar el BAÑO 🚽 3
- Pedí CUALQUIER favor 🌠 25!
      """
  )

# 4. GALERÍA DE FOTOS (RECUERDOS)
with st.expander("📸 Nuestros Recuerdos"):
  st.markdown("Un pequeño recorrido por algunos momentos juntos ❤️")

  # Acá podés subir tus fotos a GitHub con nombres como "foto1.jpg", "foto2.jpg"
  # y pasarlas acá adentro de st.image(). Por ahora te dejo un ejemplo listo:
  try:
    st.image(
        "foto1.jpg",
        caption="¡Los mejores momentos con la mejor mamá!",
        use_container_width=True,
    )
    # st.image("foto2.jpg", caption="Otro lindo recuerdo", use_container_width=True)
  except:
    st.info(
        "💡 *Consejo:* Subí tus fotos (ej: foto1.jpg) a tu repositorio de GitHub"
        " en la misma carpeta que el archivo app.py para que aparezcan acá"
        " mágicamente."
    )

st.title("🎁 CUPONERA PARA LA MEJOR, LA MAMÁ CON MÁS AGUANTE ♥️")

hoy = date.today()
ya_canjeo_hoy = st.session_state.ultima_fecha_canje == hoy

if ya_canjeo_hoy:
  st.info("⌛ ¡Ya canjeaste tu cupón de hoy! Vuelve mañana para usar otro. 😉")
  st.markdown(
      f"### 🎫 Cupón activo de hoy:\n👉 **{st.session_state.cupon_hoy_canjeado}**"
  )

elif len(st.session_state.cupones) > 0:
  st.write(f"‼️ Cupones disponibles en stock: 🎫 {len(st.session_state.cupones)}")

  # Botón para sortear
  if st.button("✨ ¡SORTEAR CUPÓN! ✨"):
    st.session_state.cupón_actual = random.choice(st.session_state.cupones)

  # Si hay un cupón sorteado en pantalla
  if st.session_state.cupón_actual:
    st.success("Te tocó este cupón 🎉")
    st.markdown(f"### 👉 **{st.session_state.cupón_actual}**")

    col1, col2 = st.columns(2)
    with col1:
      if st.button("✅ ELEGIR ESE ✅"):
        st.session_state.cupones.remove(st.session_state.cupón_actual)
        st.session_state.ultima_fecha_canje = hoy
        st.session_state.cupon_hoy_canjeado = st.session_state.cupón_actual
        st.session_state.cupón_actual = None
        st.session_state.efecto = "globos"  # Activa GLOBOS
        st.rerun()

    with col2:
      if st.button("↪️ RE-ELEGIR ↪️"):
        st.session_state.cupón_actual = random.choice(st.session_state.cupones)
        st.session_state.efecto = "nieve"  # Activa NIEVE
        st.rerun()

else:
  st.balloons()
  st.warning("🥀 ¡Uy, se acabaron todos los cupones! Sos libre por hoy 😔")
