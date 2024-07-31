import sys
import os
from behave import given, when, then

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main import tasks, completedTasks, addActivity, markActivity, eraseList

@given('la lista de tareas está vacía')
def step_impl(context):
    tasks.clear()
    completedTasks.clear()

@when('el usuario agrega una actividad "{actividad}"')
def step_impl(context, actividad):
    addActivity(actividad)

@then('la lista de tareas debería contener "{actividad}"')
def step_impl(context, actividad):
    assert actividad in tasks, f'Actividad "{actividad}" no encontrada en la lista de tareas'

@given('la lista de tareas contiene actividades:')
def step_impl(context):
    tasks.clear()
    completedTasks.clear()
    for row in context.table:
        addActivity(row['Actividad'])

@when('el usuario marca la actividad "{actividad}" como completada')
def step_impl(context, actividad):
    markActivity(actividad)

@then('la lista de tareas completadas debería contener "{actividad}"')
def step_impl(context, actividad):
    assert actividad in completedTasks, f'Actividad "{actividad}" no encontrada en la lista de tareas completadas'

@when('el usuario ve todas las actividades')
def step_impl(context):
    context.output = tasks

@then('la salida debería contener:')
def step_impl(context):
    expected_output = context.text.strip().split('\n')[1:]
    expected_output = [line.strip() for line in expected_output]
    assert all(activity in tasks for activity in expected_output), f'La salida no contiene todas las actividades esperadas'

@when('el usuario borra toda la lista de tareas')
def step_impl(context):
    eraseList()

@then('la lista de tareas debería estar vacía')
def step_impl(context):
    assert not tasks, 'La lista de tareas no está vacía'

@when('el usuario muestra las actividades pendientes')
def step_impl(context):
    context.pending_output = [actividad for actividad in tasks if actividad not in completedTasks]

@then('la salida debería contener:')
def step_impl(context):
    expected_output = context.text.strip().split('\n')[1:]
    expected_output = [line.strip().split('- ')[1] for line in expected_output]
    assert context.pending_output == expected_output, 'La salida no coincide con las actividades pendientes esperadas'
