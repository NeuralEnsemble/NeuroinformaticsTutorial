import os
import sys
from subprocess import call
import platform

from pdfrw import PdfReader, PdfWriter
          
sections = ['Introduction','1_Experimental_datasets', '2_Structured_data_from_literature', '3_Analysis_tools', '4_Simulation_environments', '5_Model_sharing', '6_Computing_infrastructure', '7_Open_source_initiatives', '8_Web_portals']
#sections = ['Introduction','1_Experimental_datasets', '2_Structured_data_from_literature']

only_sec = None

if len(sys.argv) == 2:
    only_sec = sys.argv[1]
    print("Only doing sections starting with %s"%only_sec)

for section in sections:

    if only_sec==None or section.startswith(only_sec):
        print("++++++++++++++++++++++++++++++++++\n+  Adding section: %s\n+"%section)
        big_file = PdfWriter()

        files = os.listdir(section)

        files = sorted(files)

        for f in files:
            fpath = section+'/'+f
            if os.path.isfile(fpath) and fpath.endswith('pptx') and not f=='Template.pptx':
                print("+   Incorporating: %s"%fpath)
                cmd = "libreoffice"
                if platform.system()=='Darwin':
                    cmd = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
                call([cmd, "--headless", "--invisible", "--convert-to", "pdf", fpath])
                pdf_file_name = f.replace('pptx','pdf')

                pdf_file = PdfReader(pdf_file_name)
                print("+     Adding pages from %s\n+"%pdf_file_name)
                big_file.addpages(pdf_file.pages)
                if not 'ICG' in pdf_file_name:
                    call(["mv", pdf_file_name, "temp"])


        big_file.write('Part1_%s.pdf'%section)


print("Done.")



