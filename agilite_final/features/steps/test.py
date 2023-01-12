from behave import given, when, then
import importlib.util
import sys
spec_mairie = importlib.util.spec_from_file_location("Mairie", "/home/alexis/Documents/Dauphine/agilite_final/agilite_mairie/features/steps/test.py")
foo_mairie = importlib.util.module_from_spec(spec_mairie)
sys.modules["Mairie"] = foo_mairie
spec_mairie.loader.exec_module(foo_mairie)

spec_etudiant = importlib.util.spec_from_file_location("Etudiant", "/home/alexis/Documents/Dauphine/agilite_final/agilite_etudiant/features/steps/test.py")
foo_etudiant = importlib.util.module_from_spec(spec_etudiant)
sys.modules["Etudiant"] = foo_etudiant
spec_etudiant.loader.exec_module(foo_etudiant)
