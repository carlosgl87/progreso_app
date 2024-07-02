import streamlit as st
import pandas as pd
import pickle

lista_actividades_economicas = ['Agricultura y ganaderia excepto fruticultura', 'Bienes inmuebles y servicios prestados a empresas', 'Comercio al por mayor', 'Comercio al por menor, restaurantes y hoteles', 'Comunicaciones', 'Construccion de viviendas', 'Electricidad, gas y agua', 'Establecimientos financieros y de seguros', 'Explotacion de minas y canteras', 'Fabricacion de productos minerales metalicos y no metalicos', 'Fabricaci¢n de productos minerales met\xa0licos y no met\xa0licos, maquinarias y equipos', 'Fruticultura', 'Industria de la madera y muebles', 'Industria de productos alimenticios, bebidas y tabaco', 'Industria de productos quimicos y derivados del petroleo, carbon, caucho y plastico', 'Industria del papel, imprentas y editoriales', 'Industria textil y de cuero', 'Leasing de consumo', 'Otras industrias manufactureras', 'Otras obras y construcciones', 'Pesca', 'Servicios comunales, sociales y personales', 'Silvicultura y extraccion de madera', 'Sin Información', 'Transporte y almacenamiento']
lista_ejecutivos = ['Adolfo Gutierrez', 'Barbara Montemayor', 'Blanca Valeria Jara', 'Camila Ordenes', 'Carla Barria', 'Carlos Andrade', 'Carlos Robles', 'Carolina Alvarez', 'Carolina Morales Hott', 'Carolina Paz Inostroza', 'Charline Vidal', 'Claudia Moraga', 'Cristian Aros', 'Daniela Leon', 'Diana Gonzalez', 'Edison Vicencio', 'Edson Sepulveda', 'Eduardo Miranda', 'Elena Herrera', 'Eliseo Lara', 'Evelyn Retamal', 'Fabian Leiva', 'Fabiola Bueno', 'Felipe Robles', 'Francisco Pinto', 'Gabriela Plaza Michea', 'Gerson Valenzuela Veloso', 'Gustavo Saldías', 'Hector Otarola Sanchez', 'Javier Lara', 'Jennifer Filun', 'Jessica Solis Medina', 'Jesus Pinzon', 'Jonathan Carrizo', 'Jorge Rojas', 'Jose Manuel Valdes', 'Juan Antonio Ramos', 'Juan Arancibia', 'Juan Claudio Saavedra', 'Juan Pablo Quintero', 'Juan Pablo Rosello', 'Karol Aguilar', 'Katherine Zapata', 'Leandro Quilodran', 'Luis Ocaranza', 'Luisa Abarca Navarro', 'Marcel Hernandez', 'Marcela Aliaga', 'Marcelo Sanhueza', 'Marco Andres Gacitua Santibañez', 'Marco Avendaño', 'Marcos Araya', 'Maria Constanza', 'Maria José Gonzalez', 'Maria Riquelme', 'Marlyns Caro', 'Matias Jaramillo', 'Matias Poblete', 'Mauricio Obando', 'Mauricio Rubilar Aguilar', 'Miriam Ruiz', 'Natalia Avendaño', 'PRB1', 'Pablo Condori', 'Pablo Gómez M.', 'Pamela Araya', 'Pamela Bravo Arevalo', 'Priscila Espinoza', 'Roberto Calderon', 'Roberto Mejias', 'Roberto Vega', 'Rodrigo Valdivia Tello', 'Ronald Carrie', 'Rossana Vaccaro', 'Roxana Olivares', 'Sergio Venegas', 'Valeria Murgas', 'Victor Manuel Concha Ramos', 'Viviana Barrientos', 'Zulay Albarran']
lista_sucursales = ['Antofagasta', 'Calama', 'Casa Matriz', 'Concepcion', 'Copiapo', 'Iquique', 'La Serena', 'Los Angeles', 'No Definido', 'Puerto Montt', 'Rancagua', 'Talca', 'Viña del Mar']
lista_columnas = ['numero_cuotas_gracia', 'monto_inicial_uf', 'prov_seguros_uf', 'tasa', 'total_cuotas', 'valor_financiar_uf', 'valor_cuota_uf', 'tipo_producto_Leasing', 'tipo_producto_Microleasing', 'tipo_producto_others', 'actividad_economica_Agricultura y ganaderia excepto fruticultura', 'actividad_economica_Bienes inmuebles y servicios prestados a empresas', 'actividad_economica_Construccion de viviendas', 'actividad_economica_Explotacion de minas y canteras', 'actividad_economica_Leasing de consumo', 'actividad_economica_Otras obras y construcciones', 'actividad_economica_Servicios comunales, sociales y personales', 'actividad_economica_Transporte y almacenamiento', 'actividad_economica_others', 'tipo_persona_Jurídica', 'tipo_persona_Natural', 'moneda_$', 'moneda_UF']

#st.image("progresojpeg.jpeg")
st.text("")
st.markdown("<h2 style='text-align: center; color: grey;'>Modelo Predictivo Riesgo</h2>", unsafe_allow_html=True)
st.text("")
#col1, col2, col3 = st.columns(3)
col1, col2 = st.columns(2)

with col1:
    st.write("**Datos Producto**")
    tipo_producto = st.selectbox("Tipo Producto", ["Leasing", "Leasing Retail",'MicroLeasing'])
    monto_total = st.number_input("Monto Leasing (UF)")
    monto_inicial = st.number_input("Monto Inicial (UF)")
    seguro = st.number_input("Seguro (UF)")
    tasa = st.number_input("Tasa Leasing")
    cuotas = st.number_input("Total Cuotas")
    cuotas_gracia = st.number_input("Cuotas de Gracia")
    valor_cuota = st.number_input("Valor de la Cuota (UF)")
    moneda = st.selectbox("Moneda", ["Pesos", "UF"])

with col2:
    st.write("**Datos del Cliente**")
    actividad_economica = st.selectbox("Actividad Economica", lista_actividades_economicas)
    tipo_persona = st.selectbox("Tipo Persona", ["Natural", "Juridica"])

# with col3:
#     st.write("**Datos del Ejecutivo**")
#     ejecutivo = st.selectbox("Ejecutivo", lista_ejecutivos)
#     sucursal = st.selectbox("Sucursal", lista_sucursales)

customized_button = st.markdown("""
    <style >
    .stDownloadButton, div.stButton {text-align:center}

        }
    </style>""", unsafe_allow_html=True)

if st.button('Perfil Riesgo'):
    
    df = pd.DataFrame(columns = lista_columnas)
    
    if tipo_producto == 'Leasing':
        output_lista_tipo_producto = [1,0,0]
    elif tipo_producto == 'MicroLeasing':
        output_lista_tipo_producto = [0,1,0]
    else:
        output_lista_tipo_producto = [0,0,1]

    if actividad_economica == 'Agricultura y ganaderia excepto fruticultura':
        output_lista_actividad_economica = [1,0,0,0,0,0,0,0,0]
    elif actividad_economica == 'Bienes inmuebles y servicios prestados a empresas':
        output_lista_actividad_economica = [0,1,0,0,0,0,0,0,0]
    elif actividad_economica == 'Construccion de viviendas':
        output_lista_actividad_economica = [0,0,1,0,0,0,0,0,0]
    elif actividad_economica == 'Explotacion de minas y canteras':
        output_lista_actividad_economica = [0,0,0,1,0,0,0,0,0]
    elif actividad_economica == 'Leasing de consumo':
        output_lista_actividad_economica = [0,0,0,0,1,0,0,0,0]
    elif actividad_economica == 'Otras obras y construcciones':
        output_lista_actividad_economica = [0,0,0,0,0,1,0,0,0]
    elif actividad_economica == 'Servicios comunales, sociales y personales':
        output_lista_actividad_economica = [0,0,0,0,0,0,1,0,0]
    elif actividad_economica == 'Transporte y almacenamiento':
        output_lista_actividad_economica = [0,0,0,0,0,0,0,1,0]
    else:
        output_lista_actividad_economica = [0,0,0,0,0,0,0,0,1]

    if tipo_persona == 'Juridica':
        output_lista_tipo_persona = [1,0]
    else:
        output_lista_tipo_persona = [0,1]

    if moneda == 'Pesos':
        output_lista_moneda = [1,0]
    else:
        output_lista_moneda = [0,1]

    # if ejecutivo == 'Edson Sepulveda':
    #     output_lista_ejecutivo = [1,0,0,0,0]
    # elif ejecutivo == 'Juan Antonio Ramos':
    #     output_lista_ejecutivo = [0,1,0,0,0]
    # elif ejecutivo == 'Maria José Gonzalez':
    #     output_lista_ejecutivo = [0,0,1,0,0]
    # elif ejecutivo == 'Roberto Mejias':
    #     output_lista_ejecutivo = [0,0,0,1,0]
    # else:
    #     output_lista_ejecutivo = [0,0,0,0,1]

    # if sucursal == 'Antofagasta':
    #     output_lista_sucursal = [1,0,0,0,0,0]
    # elif sucursal == 'Casa Matriz':
    #     output_lista_sucursal = [0,1,0,0,0,0]
    # elif sucursal == 'Concepcion':
    #     output_lista_sucursal = [0,0,1,0,0,0]
    # elif sucursal == 'La Serena':
    #     output_lista_sucursal = [0,0,0,1,0,0]
    # elif sucursal == 'Viña del Mar':
    #     output_lista_sucursal = [0,0,0,0,1,0]
    # else:
    #     output_lista_sucursal = [0,0,0,0,0,1]
    #['numero_cuotas_gracia', 'monto_inicial_uf', 'prov_seguros_uf', 'tasa', 'total_cuotas', 'valor_financiar_uf', 'valor_cuota_uf', 'tipo_producto_Leasing', 'tipo_producto_Microleasing', 'tipo_producto_others', 'actividad_economica_Otras obras y construcciones', 'actividad_economica_Transporte y almacenamiento', 'actividad_economica_others', 'tipo_persona_Jurídica', 'tipo_persona_Natural', 'moneda_$', 'moneda_UF', 'ejecutivo_cartera_Edson Sepulveda', 'ejecutivo_cartera_Juan Antonio Ramos', 'ejecutivo_cartera_Maria José Gonzalez', 'ejecutivo_cartera_Roberto Mejias', 'ejecutivo_cartera_others', 'sucursal_ejec_cartera_Antofagasta', 'sucursal_ejec_cartera_Casa Matriz', 'sucursal_ejec_cartera_Concepcion', 'sucursal_ejec_cartera_La Serena', 'sucursal_ejec_cartera_Viña del Mar', 'sucursal_ejec_cartera_others']
    # print([cuotas_gracia,monto_inicial,seguro,tasa,cuotas,monto_total,valor_cuota] + output_lista_tipo_producto + output_lista_actividad_economica + output_lista_tipo_persona + output_lista_moneda + output_lista_ejecutivo + output_lista_sucursal)
    df.loc[0] = [cuotas_gracia,monto_inicial,seguro,tasa,cuotas,monto_total,valor_cuota] + output_lista_tipo_producto + output_lista_actividad_economica + output_lista_tipo_persona + output_lista_moneda
    print(df)


    xgb_modelo_dejar_pagar = pickle.load(open('modelo_no_pago.pkl', "rb"))
    xgb_modelo_mora = pickle.load(open('modelo_demora.pkl', "rb"))
    xgb_modelo_mora_temprana = pickle.load(open('modelo_demora_temprana.pkl', "rb"))

    riesgo_dejar_pagar = xgb_modelo_dejar_pagar.predict_proba(df)[0][1]
    riesgo_mora = xgb_modelo_mora.predict_proba(df)[0][1]
    riesgo_mora_temprana = xgb_modelo_mora_temprana.predict_proba(df)[0][1]
    #print(xgb_modelo_dejar_pagar.predict_proba(df)[0][1])
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.write("**Riesgo No Pago**")
        st.write("**Probabilidad:** " + str(riesgo_dejar_pagar) )
        if riesgo_dejar_pagar > 0.67:
            st.write("🟠 **Riesgo Alto**")
        elif riesgo_dejar_pagar < 0.33:
            st.write("🟢 **Riesgo Bajo**")
        else:
            st.write("🟡 **Riesgo Medio**")

    with col_2:
        st.write("**Riesgo Demora**")
        st.write("**Probabilidad:** " + str(riesgo_mora) )
        if riesgo_mora > 0.67:
            st.write("🟠 **Riesgo Alto**")
        elif riesgo_mora < 0.33:
            st.write("🟢 **Riesgo Bajo**")
        else:
            st.write("🟡 **Riesgo Medio**")


    with col_3:
        st.write("**Riesgo Demora Temprana**")
        st.write("**Probabilidad:** " + str(riesgo_mora_temprana) )
        if riesgo_mora_temprana > 0.67:
            st.write("🟠 **Riesgo Alto**")
        elif riesgo_mora_temprana < 0.33:
            st.write("🟢 **Riesgo Bajo**")
        else:
            st.write("🟡 **Riesgo Medio**")

