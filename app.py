from datetime import date
import os
import random
import time
import pandas as pd
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

# Archivo local en la nube para persistencias
ARCHIVO_CANJES = "canjes.csv"


def cargar_canjes():
  if os.path.exists(ARCHIVO_CANJES):
    try:
      return pd.read_csv(ARCHIVO_CANJES)
    except:
      pass
  return pd.DataFrame(columns=["Fecha", "Cupon"])


def guardar_canje(fecha, cupon):
  df = cargar_canjes()
  nuevo_df = pd.DataFrame([{"Fecha": str(fecha), "Cupon": cupon}])
  df = pd.concat([df, nuevo_df], ignore_index=True)
  df.to_csv(ARCHIVO_CANJES, index=False)


df_canjes = cargar_canjes()

# Lista completa inicial de cuponess
stock_inicial = [
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

# Calcular cupones disponibles restando los ya canjeados
cupones_disponibles = list(stock_inicial)
if not df_canjes.empty and "Cupon" in df_canjes.columns:
  for cupon_usado in df_canjes["Cupon"].dropna():
    if cupon_usado in cupones_disponibles:
      cupones_disponibles.remove(cupon_usado)

# Validar si ya canjeó hoy
hoy = date.today()
ya_canjeo_hoy = False
cupon_de_hoy = None

if not df_canjes.empty and "Fecha" in df_canjes.columns:
  df_canjes["Fecha"] = pd.to_datetime(df_canjes["Fecha"]).dt.date
  canjes_hoy = df_canjes[df_canjes["Fecha"] == hoy]
  if not canjes_hoy.empty:
    ya_canjeo_hoy = True
    cupon_de_hoy = canjes_hoy.iloc[-1]["Cupon"]

if "cupón_actual" not in st.session_state:
  st.session_state.cupón_actual = None
if "efecto" not in st.session_state:
  st.session_state.efecto = None
if "foto_index" not in st.session_state:
  st.session_state.foto_index = 0

# Lanzar efectos visuales
if st.session_state.efecto == "globos":
  st.balloons()
  st.session_state.efecto = None
elif st.session_state.efecto == "nieve":
  st.snow()
  st.session_state.efecto = None

# TÍTULO PRINCIPAL
st.title("🎁 CUPONERA PARA LA MEJOR, LA MAMÁ CON MÁS AGUANTE ♥️")

if ya_canjeo_hoy:
  st.info("⌛ ¡Ya canjeaste tu cupón de hoy! Volvé mañana para usar otro. 😉")
  st.markdown(f"### 🎫 Cupón activo de hoy:\n👉 **{cupon_de_hoy}**")

elif len(cupones_disponibles) > 0:
  st.write(
      f"‼️ Cupones disponibles en stock: 🎫 {len(cupones_disponibles)}"
  )

  if st.button("✨ ¡SORTEAR CUPÓN! ✨"):
    st.session_state.cupón_actual = random.choice(cupones_disponibles)

  if st.session_state.cupón_actual:
    st.success("Te tocó este cupón 🎉")
    st.markdown(f"### 👉 **{st.session_state.cupón_actual}**")

    col1, col2 = st.columns(2)
    with col1:
      if st.button("✅ ELEGIR ESE ✅"):
        guardar_canje(hoy, st.session_state.cupón_actual)
        st.session_state.cupón_actual = None
        st.session_state.efecto = "globos"
        st.rerun()

    with col2:
      if st.button("↪️ RE-ELEGIR ↪️"):
        st.session_state.cupón_actual = random.choice(cupones_disponibles)
        st.session_state.efecto = "nieve"
        st.rerun()

else:
  st.balloons()
  st.warning("🥀 ¡Uy, se acabaron todos los cupones! Sos libre por hoy 😔")

st.markdown("---")

# MÚSICA DE FONDO
with st.expander("🎵 Elegí la música de fondo 🎵"):
  st.markdown(
      "Poné play en la canción que más te guste para acompañar el momento:"
  )

  st.caption("Opción 1: Cama y Mesa (Roberto Carlos)")
  try:
    st.audio(
        "Roberto_Carlos_-_Cama_y_Mesa_Cama_e_Mesa_Cama_e_Mesa_(mp3.pm).mp3",
        format="audio/mp3",
    )
  except:
    pass

  st.caption("Opción 2: Libertango Instrumental (Astor Piazzolla)")
  try:
    st.audio(
        "Astor_Piazzolla_-_Libertango_Instrumental_(mp3.pm).mp3",
        format="audio/mp3",
    )
  except:
    pass

  st.caption("Opción 3: Sin principio ni final (Abel Pintos)")
  try:
    st.audio(
        "Abel_Pintos_-_Sin_principio_ni_Final_(mp3.pm).mp3", format="audio/mp3"
    )
  except:
    pass

# CARTITA
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

# INFO
with st.expander("ℹ️ INFO sobre cupones ℹ️"):
  st.markdown(
      f"""
      ### 🎫 Información sobre los cupones 🎫:
• Hay en total {len(cupones_disponibles)} cupones disponibles en el stock actual. Cuando apretás el botón de -Sortear Cupón- aleatoriamente se elige uno, pero **no se gasta** hasta que aprietes "ELEGIR ESE".
• ‼️ **LÍMITE:** Podés canjear **1 cupón por día**.
• ‼️ **IMPORTANTE:** VIERNES Y SÁBADO NO LABURO😠
      """
  )

# GALERÍA DE FOTOS AUTOMÁTICA
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
  st.markdown("Unas fotos por los mejores momentos ❤️")

  foto_actual = lista_fotos[st.session_state.foto_index]

  try:
    st.image(
        foto_actual,
        caption=f"Recuerdo {st.session_state.foto_index + 1} de {len(lista_fotos)}",
        use_container_width=True,
    )
  except:
    st.info("📷 Cargando siguiente recuerdo...")

  time.sleep(10)
  st.session_state.foto_index = (st.session_state.foto_index + 1) % len(
      lista_fotos
  )
  st.rerun()
