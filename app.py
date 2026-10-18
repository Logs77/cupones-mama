import random
import streamlit as st

#Lavar los platos 12, Sacar la basura 10, Hacer LAS camas 15, Ir a comprar 10, Ver peli 5, pedir LO QUE QUIERAS 25, Tender la ropa 8, Ordenar la ropa 7, Hacer comida/ayudar 15, 

#CARTITA
with st.expander("💌 Ver carta especial para vos 💌"):
  st.markdown(
      """
        ### ¡Feliz día má!
        Este programa (cuponera) lo hice con mucho amor, esfuerzo y programacion exclusivamente para vos♥️.     
        
        Cada vez que necesites un favor o algo, podés usar un cupón apretando el boton. Este año no tuve plata para regalarte nada pero bueno aunque este regalo no sea casi nada se me ocurrio porque se programar, es para ayudarte en lo que necesites y lo que quieras.
        
        Te quiero muchísimo, gracias por aguantarme todos los dias, se que es muy dificil mantener al mejor hijo del mundo😎. Pero bueno, aunque aveces discutimos, yo te quiero un montón y te voy a seguir queriendo mas todavía, se que aveces pido mucho pero bueno ya no te voy a pedir mas cosas (esperemos, na mentira), voy a intentar ayudarte en todo lo que pueda para devolverte un poquitito de lo que me das cada dia🫶.
♥️♥️Te quiero mucho ma♥️♥️
♥️♥️♥️♥️FELÍZ DIA♥️♥️♥️♥️
        """)
with st.expander("ℹ️INFO sobre cuponesℹ️"):
  st.markdown(
      f"""
      ### 🎫Información sobre los cupones🎫:
•Hay en total {len(st.session_state.cupones)} cupones. Cuando apretas el boton de -Sortear Cupón- aleatoriamente se elige uno de los {len(st.session_state.cupones)} cupones, inmediatamente ese cupon se borra, osea puede volver a salir ese pero ya se gasto uno de ese tipo (por ejemplo si habia 12 de lavar los platos y te toca uno, va a haber 11) Pero igual son muchos, te van a durar varios meses.
•‼️IMPORTANTE‼️: Si no te gusta lo que te toco NO se gasta, elegis otro con boton de -REELEGIR-.
•‼️IMPORTANTE‼️: VIERNES Y SABADO NO LABURO😠
• Y son estos (Su nombre y la cantidad que hay):
-Lavar los platos 🍽️🥛 12
-Sacar la basura 🗑️ 10
-Hacer las camas 🛏️ 15
-Ir a comprar 🛒 10
-Ver peli 🎞️ 5
-Tender la ropa 👕 8
-Ordenar la ropa🧦👚🧣 7
-Hacer la comida (o ayudarte) 🍗 15
-Ordenar y limpiar la COCINA 🧹 5
-Ordenar y limpiar la PIEZA 🛏️ 3
-Ordenar y limpiar el BAÑO 🚽 3
-Pedi CUALQUIER favor 🌠 25!
      """)

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
      "Pedirme LO QUE QUIERAS🌠"
  ]

st.title("🎁 CUPONERA PARA LA MEJOR, LA MAMA CON MAS AGUANTE ♥️")


# Verificamos si todavía quedan cupones en la lista
if len(st.session_state.cupones) > 0:
  st.write(f"‼️ Cupones disponibles: 🎫 {len(st.session_state.cupones)}")

  if st.button("✨¡SORTEAR CUPÓN!✨"):
    # Elegimos uno al azar
    elegido = random.choice(st.session_state.cupones)
    st.success("Te tocó este cupón 🎉")
    st.markdown(f"### 👉 **{elegido}**")
  if st.button("✅ELEGIR ESE✅")
    
  if st.button("↪️RE-ELEGIR↪️"):
    elegido = random.choice(st.session_state.cupones)
else:
  st.balloons()
  st.warning("🥀¡uy se acabaron todos los cupones!😔")
