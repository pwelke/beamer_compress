# A Tool to Extract the Last Overlay of Each Latex-Beamer Frame

Extract the last overlay from each frame given a pdf that was created by pdflatex with the latex-beamer package. 


## The Problem

Sometimes, you may like to create a 'handout' version of your slides that don't contain all the fancy overlay animations that you have created.

If you create your slides with latex-beamer, there is the ``overlay`` option, but it just ignores all ``<+->``, ``\pause`` and similar arguments, resulting in suboptimal results if you are overlaying external figures with something like

```
\only<1>{\includegraphics{a.png}}

\only<2>{\includegraphics{b.png}} 
```

In this case, those two images appear both next to each other, with the second figure most likely sticking out of your frame.

## The Solution

The script in this repository takes a pdf and extracts the last page for each page label. Beamer stores overlays with identical labels, i.e. all overlays of frame '42' will have page label '42'.

This may not work for your usecase, e.g. if you have slides with intermediate figures that show completely different things.

If you, on the other hand, just use lazy person animations of hand drawn algorithm progress, then the last slide should contain all information and you may be happy with this script.

## Usage

The script requires ``python>=3.8``, the python package ``python-poppler`` as well as the command line utility ``pdftk`` to be available on your system. The script was tested on Ubuntu 20.04, where these requirements can be fulfilled by running

```
sudo pip install python-poppler
sudo apt install pdftk
```

Calling

```
python beamer_compress.py INFILE OUTFILE
```

will then select the last overlays from each frame in ``INFILE`` and store them in ``OUTFILE``. 

## Known Issues

As I am lazy, the script depends on two pdf libraries. 
It could certainly be improved to work with only one (probably pdftk) which would allow to get rid of the python requirement, as well.
