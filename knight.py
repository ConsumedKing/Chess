pos_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]


class Knight:
    def __init__(self, color, position):
        self.color = str(color)
        self.position = position

    def __repr__(self) -> str:
        if self.color == "b":
            return "n"
        else:
            return "N"

    def move(self, current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        if pos_letters.index(ch) + 2 > 7 or nm + 1 > 8:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)+2]}{nm+1}")
        if pos_letters.index(ch) + 2 > 7 or nm - 1 < 1:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)+2]}{nm-1}")

        if pos_letters.index(ch) - 2 < 0 or nm + 1 > 8:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)-2]}{nm+1}")

        if pos_letters.index(ch) - 2 < 0 or nm - 1 > 1:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)-2]}{nm-1}")

        if pos_letters.index(ch) + 1 > 7 or nm + 2 > 8:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm+2}")

        if pos_letters.index(ch) - 1 < 0 or nm + 2 > 8:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm+2}")

        if pos_letters.index(ch) + 1 > 7 or nm - 2 < 1:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)+1]}{nm-2}")

        if pos_letters.index(ch) - 1 < 0 or nm - 2 < 1:
            pass
        else:
            moves.append(f"{pos_letters[pos_letters.index(ch)-1]}{nm-2}")

        return moves

    def draw(self):
        if self.color == "w":
            return "white_knight"
        return "black_knight"
