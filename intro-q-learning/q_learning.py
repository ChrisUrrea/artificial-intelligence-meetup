import numpy as np

# parametro de aprendizaje (approx 0-1 )
alpha = 0.7
# parametro de descuento (approx. 0-1 )
gamma = 0.9

### Parte 1. Definir el intorno ###

# 1.1 Definir - mapa de ubicaciones a estados
ubicacion_a_estado = {'A': 0,
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8,
                     'J': 9,
                     'K': 10,
                     'L': 11}

# 1.2 Definir - mapa de estados a ubicaciones
estado_a_ubicacion = {estado : ubicacion for ubicacion, estado in ubicacion_a_estado.items()}

# 1.3 - Definir - lista de acciones
acciones =  [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]

# Defining the rewards
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
              [1,0,1,0,0,1,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,1,0,0,0],
              [0,1,0,0,0,0,0,0,0,1,0,0],
              [0,0,1,0,0,0,1,1,0,0,0,0],
              [0,0,0,1,0,0,1,0,0,0,0,1],
              [0,0,0,0,1,0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0,0,1,0,1,0],
              [0,0,0,0,0,0,0,0,0,1,0,1],
              [0,0,0,0,0,0,0,1,0,0,1,0]])

### Parte 2. Construir el Agente con Q-learning ###

# 2.1 - Inicializar Q(s, a) a un matrix de zeros
# con dimenciones matrix de (12 posible acciones x 12 possible estados)

# 2.2 Implentar el processo de aprendizaje para nuestro Q-Learning agente
def ruta_optima(ubicacion_comienzp, ubicacion_final):
    R_nuevo = np.copy(R)
    estado_final = ubicacion_a_estado[ubicacion_final]
    # poner un precio final 
    R_neuvo[estado_final, estado_final] = 1000
    Q = np.array(np.zeros([12,12]))
    for i in range(1000):
        current_state = np.random.randint(0,12)
        playable_actions = []
        for j in range(12):
            if R_new[current_state, j] > 0:
                playable_actions.append(j)
        next_state = np.random.choice(playable_actions)
        TD = R_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD
    route = [starting_location]
    next_location = starting_location
    while (next_location != ending_location):
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        route.append(next_location)
        starting_location = next_location
    return ruta

### Parte 3. Implementar tu inteligencia artificial en el centro de distribucion ###
 
def ruta_optima(ubicacion_comienzo, ubicacion_final):
    # la ruta - lista de ubicaciones comenzando con ubicacion presente
    ruta = [ubicacion_comienzo]
    
    ubicacion_siguiente = ubicacion_comienzo
    while(ubicacion_siguiente != ubicacion_final):
        # consequir el indice de la ubicacion 
        estado_presente = ubicacion_a_estado[ubicacion_comienzo]
        estado_siguiente = np.argmax(Q[estado_presente,])
        ubicacion_siguiente = estado_a_ubicacion[estado_siguiente]
        ruta.append(ubicacion_siguiente)
        ubicacion_comienzo = ubicacion_siguiente
    return ruta

print("Ruta Optima:")
print(ruta_optima("E", "G"))