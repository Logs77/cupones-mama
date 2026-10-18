import random
from datetime import date
import time
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cuponera para Mamá", page_icon="🎁", layout="centered"
)

# Estilo visual CSS para la transición suave de las fotos
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from { opacity: 0.3; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
    }
    .stImage {
        animation: fadeIn 1.2s ease-in-out;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 1. Configuración inicial de la memoria (Stock de cupones)
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

if "foto_index" not in st.session_state:
  st.session_state.foto_index = 0

# Lanzar efectos visuales guardados
if st.session_state.efecto == "globos":
  st.balloons()
  st.session_state.efecto = None
elif st.session_state.efecto == "nieve":
  st.snow()
  st.session_state.efecto = None

# TÍTULO PRINCIPAL BIEN ARRIBA
st.title("🎁 CUPONERA PARA LA MEJOR, LA MAMÁ CON MÁS AGUANTE ♥️")

# SISTEMA DE CUPONES Y LÍMITE DIARIO PRINCIPAL
hoy = date.today()
ya_canjeo_hoy = st.session_state.ultima_fecha_canje == hoy

if ya_canjeo_hoy:
  st.info("⌛ ¡Ya canjeaste tu cupón de hoy! Volvé mañana para usar otro. 😉")
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
        st.session_state.efecto = "globos"
        st.rerun()

    with col2:
      if st.button("↪️ RE-ELEGIR ↪️"):
        st.session_state.cupón_actual = random.choice(st.session_state.cupones)
        st.session_state.efecto = "nieve"
        st.rerun()

else:
  st.balloons()
  st.warning("🥀 ¡Uy, se acabaron todos los cupones! Sos libre por hoy 😔")

st.markdown("---")

# 2. CARTITA (Desplegable abajo)
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

# 3. INFO (Desplegable abajo)
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

# 4. GALERÍA DE FOTOS AUTOMÁTICA AL FINAL (FUERA DE BUCLES QUE BLOQUEEN)
lista_fotos = [
    "https://i.postimg.cc/HkgH0SCw/Screenshot-2026-10-17-22-59-51-113-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/SxhqLZpW/Screenshot-2026-10-17-23-00-03-103-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/FH4mbPQc/Screenshot-2026-10-17-23-00-17-928-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/SxhqLZpM/Screenshot-2026-10-17-23-00-28-019-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/cLSZ7DNK/Screenshot-2026-10-17-23-00-35-923-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/P5jhb6kC/Screenshot-2026-10-17-23-00-41-266-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/vZsM7Pdc/Screenshot-2026-10-17-23-00-49-470-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/NjcY8NwL/Screenshot-2026-10-17-23-02-11-735-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/YCHkNXw0/Screenshot-2026-10-17-23-02-42-527-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/L8pRkyMX/Screenshot-2026-10-17-23-03-10-745-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/DwTFQCKz/Screenshot-2026-10-17-23-03-27-268-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/Z5SZPfh5/Screenshot-2026-10-17-23-08-10-022-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/cLSZ7DNs/Screenshot-2026-10-17-23-08-19-884-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/rwkcGhLM/Screenshot-2026-10-17-23-08-50-007-com-google-android-apps-docs.jpg",
    "https://i.postimg.cc/Bn0s5hGS/Screenshot-2026-10-17-23-09-06-833-com-google-android-apps-docs.png",
    "https://i.postimg.cc/pLHxQ0tV/Screenshot-2026-10-17-23-09-19-540-com-google-android-apps-docs.png",
    "https://i.postimg.cc/RVf4nk2q/Screenshot-2026-10-17-23-09-34-569-com-google-android-apps-docs.png",
]

with st.expander("📸 Nuestros Recuerdos en Movimiento"):
  st.markdown("Un pequeño recorrido por los mejores momentos juntos ❤️")

  foto_actual = lista_fotos[st.session_state.foto_index]

  try:
    st.image(
        foto_actual,
        caption=f"Recuerdo {st.session_state.foto_index + 1} de {len(lista_fotos)}",
        use_container_width=True,
    )
  except:
    st.info("📷 Cargando siguiente recuerdo...")

  # Espera 10 segundos y pasa a la siguiente foto
  time.sleep(10)
  st.session_state.foto_index = (st.session_state.foto_index + 1) % len(
      lista_fotos
  )
  st.rerun()
