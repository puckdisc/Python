def switch_average(letter):
    min = {
        'A': 90,
        'B': 80
        'C': 70
        'D': 60
        'F': 0
    }

    switch = min.get(letter, lambda: "Invalid Entry. ")
    return switch

if __name__ == '__main__':
    switch_average('A')

