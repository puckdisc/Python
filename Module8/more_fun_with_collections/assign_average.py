def switch_average(letter):
    min = {
        'A': 90,
        'B': 80
    }

    switch = min.get(letter, lambda: "Invalid Entry. ")
    return switch

if __name__ == '__main__':
    switch_average('A')

