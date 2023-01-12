from behave import given, when, then
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("Mairie", "/home/alexis/Documents/Dauphine/agilite_final/agilite_mairie/classes.py")
foo = importlib.util.module_from_spec(spec)
sys.modules["Mairie"] = foo
spec.loader.exec_module(foo)

# foo.MyClass()


@given(u'le nombre d employes d une mairie "{mairie1}" "{mairie2}" "{mairie3}" "{mairie4}"')
def step_impl(context, mairie1, mairie2, mairie3, mairie4):
    mairie = foo.Mairie('Creteil', '94000')
    employe = foo.Employe("Dupont",mairie)
    employe.ajouter_total(mairie1)
    employe.ajouter_total(mairie2)
    employe.ajouter_total(mairie3)
    employe.ajouter_total(mairie4)
    context.employe = employe
    context.mairie1 = mairie1
    context.mairie2 = mairie2
    context.mairie3 = mairie3
    context.mairie4 = mairie4


@when(u'le nombre d employes est positif')
def step_impl(context):
    assert int(context.mairie1) >= 0 and int(context.mairie2) >= 0 and int(context.mairie3) >= 0 and int(context.mairie4) >= 0


@then(u'le "{total}" des employes d une mairie doivent etre automatiquement calcules')
def step_impl(context, total):
    assert int(total) == int(context.employe.total_mairie)
