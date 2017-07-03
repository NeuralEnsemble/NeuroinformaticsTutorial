import os
from subprocess import call

from pdfrw import PdfReader, PdfWriter
          
sections = ['Introduction','1_Experimental_datasets', '2_Structured_data_from_literature', '3_Analysis_tools', '4_Simulation_environments', '5_Model_sharing', '6_Computing_infrastructure', '7_Open_source_initiatives', '8_Web_portals']
#sections = ['Introduction','1_Experimental_datasets', '2_Structured_data_from_literature']


for section in sections:

    big_file = PdfWriter()
    
    for f in os.listdir(section):
        fpath = section+'/'+f
        if os.path.isfile(fpath) and fpath.endswith('pptx') and not f=='Template.pptx':
            print("Incorporating: %s"%fpath)
            call(["libreoffice", "--headless", "--invisible", "--convert-to", "pdf", fpath])
            pdf_file_name = f.replace('pptx','pdf')
            
            pdf_file = PdfReader(pdf_file_name)
            print("  Adding pages from %s"%pdf_file_name)
            big_file.addpages(pdf_file.pages)
            call(["mv", pdf_file_name, "temp"])
        

    big_file.write('Part1_%s.pdf'%section)


print("Done.")



