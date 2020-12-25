from responses import success_response_pdf
from generate import generate
from io import StringIO, BytesIO
from xhtml2pdf import pisa   


def convert_html_to_pdf(source_html):
    result_file = BytesIO();
    pisa_status = pisa.CreatePDF(
            source_html, 
            dest=result_file)

    result = result_file.getvalue()   

    if pisa_status.err:
        return pisa_status.err
    else:
        return result

def handler(event, context):
    content = generate()
    parsed_content = ""

    for category in content:
        category_string = f"<h1>{category['name']}</h1>"
        category_string += '''
        <table>
            <thead>
                <tr>
                    <td>Nombre</td>
                    <td>Unidad</td>
                    <td>Precio</td>
                </tr>
            </thead>
            <tbody>
        '''
        for item in category['items']:
            category_string+= f"<tr><td>{item['name']}</td><td>{item['unit']}</td><td>{item['price']}</td></tr>"
        category_string += "</tbody></table>"
        parsed_content+=category_string
    
    response = convert_html_to_pdf(parsed_content)

    return success_response_pdf(response)
        