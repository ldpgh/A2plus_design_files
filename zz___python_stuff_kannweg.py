


try: App.closeDocument(doc.Name)
except: pass

try: App.closeDocument("hier_level_2")
except: pass

mydebug=1
from PySide import QtGui
mw=Gui.getMainWindow()
mw.findChild(QtGui.QPlainTextEdit, "Python console").clear()
mw.findChild(QtGui.QTextEdit, "Report view").clear()

import a2p_importpart as a2p
import FreeCAD

from importlib import reload
reload(a2p)
import a2p_importedPart_class
reload(a2p_importedPart_class)
from a2p_importedPart_class import Proxy_importPart, ImportedPartViewProviderProxy

App.newDocument()
doc=FreeCAD.activeDocument()

dirName='%APPDATA%/FreeCAD/A2plus_design_files/'
a2p.importPartFromFile( doc, dirName+'hier_level_2.FCStd', instanceParameters={"ww":55} )








a2p_importedPart_class








a2p.importPartFromFile(
  doc,
  dirName+"hier_level_2.FCStd',
  instanceParameters={"ww":11, "ll":11, "hh":11}
)

a2p.importPartFromFile(
  doc,
  dirName+"hier_level_2.FCStd',
  instanceParameters={"ww":11, "ll":22, "hh":33}
)



FreeCADGui.removeWorkbench("A2plus")
FreeCADGui.reloadWorkbench("src/Mod/MyWorkbench/InitGui.py")




### lutz_dd, 2025_12_12 ... start
    #-------------------------------------------
    # Instanz-Parameter dauerhaft speichern
    #-------------------------------------------
    FreeCAD.Console.PrintMessage("mydebug = %r" % mydebug)
    mydebug=newObj
    FreeCAD.Console.PrintMessage("mydebug = %r" % mydebug)
    FreeCAD.Console.PrintMessage(
                            f"[A2plus] instanceParameters = %r\n" % instanceParameters
                        )
    if instanceParameters:
        newObj.instanceParameters = instanceParameters
### lutz_dd, 2025_12_12 ... end






import FreeCAD

class ProxyDemo:
    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "CubeSize", "TestGroup", "Größe des Würfels")
        obj.CubeSize = 10.0

    def onChanged(self, fp, prop):
        if prop == "CubeSize":
            FreeCAD.Console.PrintMessage(f"[Demo] CubeSize geändert: {fp.CubeSize}\n")

doc = FreeCAD.activeDocument() or FreeCAD.newDocument()
obj = doc.addObject("Part::FeaturePython", "MyPart")
ProxyDemo(obj)
doc.recompute()


