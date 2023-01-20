from behave import given, when, then
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("Etudiant", "/home/alexis/Documents/Dauphine/agilite_final/agilite_etudiant/classes.py")
foo = importlib.util.module_from_spec(spec)
sys.modules["Etudiant"] = foo
spec.loader.exec_module(foo)

# foo.MyClass()

# from home.alexis.Documents.Dauphine.agilite import Etudiant, Cahier


@given(u'des points attribues par differents professeurs "{point1}" "{point2}" "{point3}" "{point4}"')
def step_impl(context, point1, point2, point3, point4):
    etudiant = foo.Etudiant('Harry', 'Potter')
    cahier = foo.Cahier(etudiant)
    cahier.ajouter_points(point1)
    cahier.ajouter_points(point2)
    cahier.ajouter_points(point3)
    cahier.ajouter_points(point4)
    context.cahier = cahier
    context.point1 = point1
    context.point2 = point2
    context.point3 = point3
    context.point4 = point4


@when(u'le nombre de points est positif')
def step_impl(context):
    assert int(context.point1) >= 0 and int(context.point2) >= 0 and int(context.point3) >= 0 and int(context.point4) >= 0


@then(u'le "{total}" des points de un etudiant doivent etre automatiquement calcules')
def step_impl(context, total):
    assert int(total) == int(context.cahier.page_points)
