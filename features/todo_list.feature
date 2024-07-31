Feature: Gestión de Lista de Tareas

  Scenario: Agregar una actividad a la lista de tareas
    Given la lista de tareas está vacía
    When el usuario agrega una actividad "Estudiar para el examen"
    Then la lista de tareas debería contener "Estudiar para el examen"

  Scenario: Marcar una actividad como completada
    Given la lista de tareas contiene actividades:
      | Actividad              |
      | Estudiar para el examen|
    When el usuario marca la actividad "Estudiar para el examen" como completada
    Then la lista de tareas completadas debería contener "Estudiar para el examen"

  Scenario: Ver todas las actividades en la lista de tareas
    Given la lista de tareas contiene actividades:
      | Actividad              |
      | Estudiar para el examen|
      | Comprar víveres        |
    When el usuario ve todas las actividades
    Then la salida debería contener:
      """
      Actividades:
      - Estudiar para el examen
      - Comprar víveres
      """

  Scenario: Borrar toda la lista de tareas
    Given la lista de tareas contiene actividades:
      | Actividad              |
      | Estudiar para el examen|
      | Comprar víveres        |
    When el usuario borra toda la lista de tareas
    Then la lista de tareas debería estar vacía

  Scenario: Mostrar actividades pendientes
    Given la lista de tareas contiene actividades:
      | Actividad              |
      | Estudiar para el examen|
      | Comprar víveres        |
    And el usuario marca la actividad "Estudiar para el examen" como completada
    When el usuario muestra las actividades pendientes
    Then la salida debería contener:
      """
      Actividades pendientes:
      - Comprar víveres
      """
