tareas = []

# Pedimos 3 tareas al usuario
for i in range(3):
    tarea = input(f"Escribe tu tarea {i+1}: ")
    tareas.append(tarea)

#Se muestran las tareas
print("\n--- Tu Agenda de Hoy ---")
for i, tarea in enumerate(tareas, 1):
    print(f"{i}.{tarea}")
    
# Marcar una tarea como hecha
num = int(input("\n ¿Cual tarea ya completaste? (Poner numero): "))

if 1 <= num <= 3:
    tareas[num-1] = tareas[num-1] + " Hecho"
    print("\n --- Agenda Actualizada ---")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}.{tarea}")
else:
    print("Numero no valido.")