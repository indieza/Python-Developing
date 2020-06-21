number = float(input())
source = input()
dest = input()

metrics = {
    "m-mm": number * 1000,
    "m-cm": number * 100,
    "m-mi": number * 0.000621371192,
    "m-in": number * 39.3700787,
    "m-km": number * 0.001,
    "m-ft": number * 3.2808399,
    "m-yd": number * 1.0936133,
    "mm-m": number / 1000,
    "mm-cm": number / 1000 * 100,
    "mm-mi": number / 1000 * 0.000621371192,
    "mm-in": number / 1000 * 39.3700787,
    "mm-km": number / 1000 * 0.001,
    "mm-ft": number / 1000 * 3.2808399,
    "mm-yd": number / 1000 * 1.0936133,
    "cm-m": number / 100,
    "cm-mm": number / 100 * 1000,
    "cm-mi": number / 100 * 0.000621371192,
    "cm-in": number / 100 * 39.3700787,
    "cm-km": number / 100 * 0.001,
    "cm-ft": number / 100 * 3.2808399,
    "cm-yd": number / 100 * 1.0936133,
    "mi-m": number / 0.000621371192,
    "mi-mm": number / 0.000621371192 * 1000,
    "mi-cm": number / 0.000621371192 * 100,
    "mi-in": number / 0.000621371192 * 39.3700787,
    "mi-km": number / 0.000621371192 * 0.001,
    "mi-ft": number / 0.000621371192 * 3.2808399,
    "mi-yd": number / 0.000621371192 * 1.0936133,
}

print(metrics['{0}-{1}'.format(source, dest)])
