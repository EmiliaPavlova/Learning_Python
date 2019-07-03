amount = float(input())
entry_unit = input().lower()
exit_unit = input().lower()

switch_to_meter = {
    'mm': 1000,
    'cm': 100,
    'mi': 0.000621371192,
    'in': 39.3700787,
    'km': 0.001,
    'ft': 3.2808399,
    'yd': 1.0936133
}

units_in_m = 1 * amount
if entry_unit != 'm':
    units_in_m = amount / switch_to_meter.get(entry_unit)

if entry_unit == exit_unit:
    print(amount)
elif exit_unit == 'm':
    print(units_in_m)
else:
    print(units_in_m * switch_to_meter.get(exit_unit))
