from docxtpl import DocxTemplate

testinfo = {
    "customer": "FBI",
    "ucm": True,
    "ucm_cloud": False,
    "ucm_cloud_g": False,
    "cuc": True,
    "imp": True,
    "cer": True,
    "expressways": True,
    "endpoints": True,
    "on_premise": True,
    "efax": True,
    "efax_partner": "Imagicle", # Imagicle or StoneFax
    "call_recording": True,


}


def generate_doc(template, doc_type, data):
    template = DocxTemplate(template)
    context = data

    template.render(context)
 
    template.save(f"{doc_type}.docx")
    return True

#generate_doc("RFP Technical Responses.docx")