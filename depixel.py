import os
import sys

for i in sys.argv[1:]:
     os.system("potrace -b svg -b pdf {0} -o {1}.pdf".format(i,i[:-4]))
os.system(' echo completed successfully')
