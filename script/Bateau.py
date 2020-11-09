class Bateau:
    bateau = {}

    def __init__(self, name, size, state = "actif"):
        self.ship_name = name
        self.ship_coordinates = []
        self.ship_state = state
        self.ship_size = size


    def modifier_tableau(self):
        pass

    def position_bateau(self, col, row, name_ship, plateau):
        coordonnees_plateau = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6
        }
        col = coordonnees_plateau[col]
        row = row + 2
        self.ship_coordinates = [row, col]
        horizontal_or_vertical = input("Voulez vous le placer horizontalement ou verticalement ? (h ou v)").lower()
        if horizontal_or_vertical == "h":
            left_or_right = input("Voulez-vous le placer à droite ou à gauche? (d ou g)").lower()
            if left_or_right == "d":
                for elements in range(name_ship.ship_size):
                    plateau[name_ship.ship_coordinates[0]][name_ship.ship_coordinates[1] + elements] = "o"
            elif left_or_right == "g":
                for elements in range(name_ship.ship_size):
                    plateau[name_ship.ship_coordinates[0]][name_ship.ship_coordinates[1]- elements] = "o"
        elif horizontal_or_vertical == "v":
            up_or_down = input("Voulez-vous le placer en haut ou en bas?").lower()
            if up_or_down == "h":
                for elements in range(name_ship.ship_size):
                    plateau[name_ship.ship_coordinates[0] - elements][name_ship.ship_coordinates[1]] = "o"
            elif up_or_down == "b":
                for elements in range(name_ship.ship_size):
                    plateau[name_ship.ship_coordinates[0] + elements][name_ship.ship_coordinates[1]] = "o"