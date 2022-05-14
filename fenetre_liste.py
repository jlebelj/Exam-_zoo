# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import interface_liste_animaux
# importation classe
from liste_globale import lst_animal_globale
# definition

class Fenetre_liste(QtWidgets.QDialog, interface_liste_animaux.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_liste, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("enclos")
        for e in lst_animal_globale:
            self.TB_liste_animaux.append(e.__str__())
            self.TB_liste_animaux.append("")

    @pyqtSlot()
    def on_BT_quitter_clicked(self):
        self.close()