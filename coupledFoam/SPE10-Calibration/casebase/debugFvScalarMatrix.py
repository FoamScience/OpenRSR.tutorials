import gdb
import gdb.printing

class FvScalarMatrixPrinter(object):
    "Print an OpenFOAM fvScalarMatrix as Octave/Matlab sparse matrix."

    def __init__(self, val):
        self.val = val

    def to_string(self):
        sr = ""
        print(self.val['source'])
        return sr

# Add printer and register it to (const) fvScalarMatrix objects
pp = gdb.printing.RegexpCollectionPrettyPrinter('Foam::fvMatrix<double>')
pp.add_printer('Foam::fvMatrix<double>','^Foam::fvMatrix<double>$', FvScalarMatrixPrinter)
gdb.printing.register_pretty_printer(gdb.current_objfile(), pp, True)
