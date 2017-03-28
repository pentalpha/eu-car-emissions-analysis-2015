#disable annoying warnings
def disableWarnings():
    import warnings as wn
    wn.filterwarnings('ignore')


#alternative to output_notebook which loads html from file
def displayHTML(file):
    from IPython.core.display import display, HTML
    with open(file, 'r') as myfile:
        data=myfile.read()
        display(HTML(data))
