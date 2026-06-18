class Login:
    def __init__(self, jugador_dao):
        self.jugador_dao = jugador_dao

    def iniciar_sesion(self):
        """
        Maneja el flujo completo de login/registro.
        Devuelve un objeto Jugador si tuvo éxito, o None si el usuario cancela.
        """
        print("\n" + "=" * 40)
        print("         BATALLA NAVAL — LOGIN")
        print("=" * 40)

        while True:
            print("\n1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Volver al menú")

            opcion = input("\nElegí una opción: ").strip()

            if opcion == "1":
                jugador = self.__login()
                if jugador:
                    return jugador

            elif opcion == "2":
                jugador = self.__registro()
                if jugador:
                    return jugador

            elif opcion == "3":
                return None

            else:
                print("Opción no válida.")

    def __login(self):
        """Busca el jugador en la BD con nombre y password"""
        print("\n--- Iniciar sesión ---")
        nombre = input("Nombre de usuario: ").strip()
        password = input("Contraseña: ").strip()

        jugador = self.jugador_dao.buscar_jugador(nombre, password)
        if jugador:
            print(f"\n¡Bienvenido de vuelta, {jugador.nombre}! 👋")
            return jugador
        else:
            print("\n❌ Usuario o contraseña incorrectos.")
            return None

    def __registro(self):
        """Registra un jugador nuevo en la BD"""
        print("\n--- Registrarse ---")
        nombre = input("Elegí un nombre de usuario: ").strip()

        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            return None

        password = input("Elegí una contraseña: ").strip()
        if not password:
            print("❌ La contraseña no puede estar vacía.")
            return None

        confirmar = input("Confirmá la contraseña: ").strip()
        if password != confirmar:
            print("❌ Las contraseñas no coinciden.")
            return None

        return self.jugador_dao.registrar_jugador(nombre, password)