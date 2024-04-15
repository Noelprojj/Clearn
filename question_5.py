import combate_pokemon
nombre_pokemon1, vida1, ataque1, defensa1 = input(), int(input()), int(input()), int(input())
nombre_pokemon2, vida2, ataque2, defensa2 = input(), int(input()), int(input()), int(input())
print(f"Comienza el combate entre {nombre_pokemon1} de tipo {combate_pokemon.obtener_tipo_pokemon(nombre_pokemon1)} y {nombre_pokemon2} de tipo {combate_pokemon.obtener_tipo_pokemon(nombre_pokemon2)}")
turno = combate_pokemon.quien_parte(nombre_pokemon1, nombre_pokemon2)
while vida1 > 0 and vida2 > 0:
    atacante, defensor = (nombre_pokemon1, nombre_pokemon2) if turno == nombre_pokemon1 else (nombre_pokemon2, nombre_pokemon1)
    ataque, defensa = (ataque1, defensa2) if atacante == nombre_pokemon1 else (ataque2, defensa1)
    dano = combate_pokemon.calcular_dmg(ataque, combate_pokemon.obtener_tipo_pokemon(atacante), defensa, combate_pokemon.obtener_tipo_pokemon(defensor))
    dano = min(dano, vida2 if atacante == nombre_pokemon1 else vida1)
    if atacante == nombre_pokemon1:
        vida2 -= dano
    else:
        vida1 -= dano
    print(f"{atacante} ha atacado a {defensor} provocando {dano} puntos de damage")
    turno = nombre_pokemon2 if turno == nombre_pokemon1 else nombre_pokemon1
perdedor, ganador = (nombre_pokemon1, nombre_pokemon2) if vida1 <= 0 else (nombre_pokemon2, nombre_pokemon1)
print(f"{perdedor} no puede continuar...")
combate_pokemon.mostrar_ganador(ganador)
