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

        horizontal_or_vertical = input("Voulez vous le placer horizontalement ou verticalement ? (h ou v)\n\n").lower()
        if horizontal_or_vertical == "h":
            for elements in range(name_ship.ship_size):
                position = [row, col+elements,"o"]
                self.ship_coordinates.append(position)
                plateau[name_ship.ship_coordinates[0][0]][name_ship.ship_coordinates[0][1] + elements] = "o"
                print(position)

        elif horizontal_or_vertical == "v":
            for elements in range(name_ship.ship_size):
                position = [row + elements, col,"o"]
                self.ship_coordinates.append(position)
                plateau[name_ship.ship_coordinates[0][0] + elements][name_ship.ship_coordinates[0][1]] = "o"
                print(position)