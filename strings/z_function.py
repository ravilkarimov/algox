def z_function_trivial(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z


def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        # если мы уже видели этот символ
        if i <= right:
            # то мы можем попробовать его инициализировать z[i - l],
            # но не дальше правой границы: там мы уже ничего не знаем
            z[i] = min(right - i + 1, z[i - left])
        # дальше каждое успешное увеличение z[i] сдвинет z-блок на единицу
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        # проверим, правее ли мы текущего z-блока
        if i + z[i] - 1 > right:
            right = i + z[i] - 1
            left = i
    return z
