def conditioner(troom, tcond, mode):
    if mode == 'freeze':
        return min(troom, tcond)
    elif mode == 'heat':
        return max(troom, tcond)
    elif mode == 'auto':
        return tcond if troom != tcond else troom
    elif mode == 'fan':
        return troom


troom, tcond = map(int, input().split())
mode = input().strip()
result_temperature = conditioner(troom, tcond, mode)
print(result_temperature)
