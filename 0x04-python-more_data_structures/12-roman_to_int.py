#!/usr/bin/python3
def roman_to_int(roman_string):
    romandic = {'I': 1 , 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    if roman_string:
        sumo = 0
        if len(roman_string) == 1:
                if roman_string[0] in romandic:
                    sumo += romandic[roman_string[0]]
                    return (sumo)
                else:
                    return None
        for i in range(1, len(roman_string)):
            if roman_string[i] in romandic  and roman_string[i - 1] in romandic:
                if romandic[roman_string[i]] <= romandic[roman_string[i - 1]]:
                    sumo = sumo - romandic[roman_string[i]]
                    sumo += romandic[roman_string[i - 1]] + romandic[roman_string[i]]
                    if i == len(roman_string) - 1:
                        sumo += romandic[roman_string[i]]
                else:
                    sumo += romandic[roman_string[i]] - romandic[roman_string[i - 1]]
            else:
                return None
        return (sumo)
    else:
        return None
