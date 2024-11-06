#!/bin/env python

import os
import sys
import tempfile

if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.stderr.write(f'This script takes exactly two arguments: an input pdf file and an output pdf file\nUsage:\n./{sys.argv[0]} INFILE OUTFILE\n')
        sys.exit(1)

    filename = sys.argv[1]
    outfile = sys.argv[2]

    _, tmpn = tempfile.mkstemp()
    os.system(f'pdftk "{filename}" dump_data > {tmpn}')

    framelist = list()
    pagelist = list()  
    with open(tmpn, 'r') as f:
        for line in f:
            tokens = line.split()
            if tokens[0] == 'PageLabelNewIndex:':
                pagelist.append(str(int(tokens[1]) - 1))
            if tokens[0] == 'PageLabelPrefix:':
                framelist.append(tokens[1])
            if tokens[0] == 'NumberOfPages:':
                nop = tokens[1]
    
    os.remove(tmpn)

    pagelist.pop(0)
    pagelist.append(nop)    

    print('Extracted frame->page mapping:')
    print([f'{a}->{b}' for a,b in zip(framelist, pagelist)])

    os.system(f'pdftk "{filename}" cat {" ".join(pagelist)} output "{outfile}"')