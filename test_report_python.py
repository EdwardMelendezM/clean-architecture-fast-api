from xhtml2pdf import pisa
from io import BytesIO

def generar_reporte_pdf_con_estilos(datos, nombre_pdf):
    # Crear un objeto BytesIO para almacenar el PDF generado
    pdf_output = BytesIO()

    # Crear el contenido del template HTML con estilos
    template_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #333;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h1>Informe de Datos</h1>
        <table>
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Edad</th>
                    <th>Ciudad</th>
                </tr>
            </thead>
            <tbody>
                """

    # Agregar datos al template HTML
    for item in datos:
        template_html += f"""
                    <tr>
                        <td>{item['Nombre']}</td>
                        <td>{item['Edad']}</td>
                        <td>{item['Ciudad']}</td>
                    </tr>
                """

    # Cerrar el template HTML
    template_html += """
            </tbody>
        </table>
    </body>
    </html>
    """

    # Renderizar el HTML a PDF
    pisa.CreatePDF(template_html, dest=pdf_output)

    # Guardar el PDF en un archivo
    with open(nombre_pdf, 'wb') as pdf_file:
        pdf_file.write(pdf_output.getvalue())

# Datos de ejemplo
datos_ejemplo = [
    {"Nombre": "Juan", "Edad": 30, "Ciudad": "Ciudad A"},
    {"Nombre": "María", "Edad": 25, "Ciudad": "Ciudad B"},
    {"Nombre": "Carlos", "Edad": 35, "Ciudad": "Ciudad A"},
]

# Generar y guardar el informe en formato PDF con estilos
generar_reporte_pdf_con_estilos(datos_ejemplo, "informe_con_estilos.pdf")