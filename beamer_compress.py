import poppler as pop
import os
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.stderr.write(f'This script takes exactly two arguments: an input pdf file and an output pdf file\nUsage:\n./{sys.argv[0]} INFILE OUTFILE\n')
        sys.exit(1)

    filename = sys.argv[1]
    outfile = sys.argv[2]

    doc = pop.load_from_file(filename)

    print(doc.pages)

    currentframe = doc.create_page(0)
    currentframelabel = 1
    framelist = list()
    pagelist = list()

    for i in range(1, doc.pages):
        page = doc.create_page(i)
        if page.label == currentframelabel:
            currentframe = page
        else:
            framelist.append(currentframe)
            pagelist.append(str(i))
            currentframe = page
            currentframelabel = page.label

    framelist.append(currentframe)
    pagelist.append(str(doc.pages))


    print('Extracted frame->page mapping:')
    print([f'{a.label}->{b}' for a,b in zip(framelist, pagelist)])

    os.system(f'pdftk \"{filename}\" cat {" ".join(pagelist)} output \"{outfile}\"')