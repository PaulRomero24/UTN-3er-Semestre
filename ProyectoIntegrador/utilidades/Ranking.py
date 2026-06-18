class Ranking:
    def __init__(self, ranking_dao):
        self.ranking_dao = ranking_dao

    def mostrar_top10(self):
        resultados = self.ranking_dao.obtener_top10()

        print("\n==========================================")
        print("         TOP 10 MEJORES JUGADORES")
        print("==========================================")

        if not resultados:
            print("   Aún no hay partidas registradas.")
            print("==========================================\n")
            return

        print(f"{'Pos.':<6}{'Jugador':<22}{'Puntaje':<10}{'Turnos':<8}{'Resultado'}")
        print(f"{'----':<6}{'-------':<22}{'-------':<10}{'------':<8}{'---------'}")

        for i, fila in enumerate(resultados, 1):
            nombre, puntaje, turnos, resultado, fecha = fila

            # Truncar nombre si es muy largo — igual que en Java
            if len(nombre) > 17:
                nombre = nombre[:17] + "..."
            else:
                nombre = nombre.ljust(20)

            pos = f"{i}."
            print(f"{pos:<6}{nombre:<22}{puntaje:<10}{turnos:<8}{resultado}")

        print("==========================================\n")