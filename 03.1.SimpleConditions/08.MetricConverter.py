amount = float(input())
entry_unit = input().lower()
exit_unit = input().lower()

m_mm = 1000
m_cm = 100
m_mi = 0.000621371192
m_in = 39.3700787
m_km = 0.001
m_ft = 3.2808399
m_yd = 1.0936133

measures = {
    'mm': {'cm': m_cm/m_mm, 'm': 1/m_mm, 'mi': m_mi/m_mm, 'in': m_in/m_mm, 'km': m_km/m_mm, 'ft': m_ft/m_mm, 'yd': m_yd/m_mm},
    'cm': {'mm': m_mm/m_cm, 'm': 1/m_cm, 'mi': m_mi/m_cm, 'in': m_in/m_cm, 'km': m_km/m_cm, 'ft': m_ft/m_cm, 'yd': m_yd/m_cm},
    'm': {'mm': m_mm, 'cm': m_cm, 'mi': m_mi, 'in': m_in, 'km': m_km, 'ft': m_ft, 'yd': m_yd},
    'mi': {'mm': m_mm/m_mi, 'cm': m_cm/m_mi, 'm': 1/m_mi, 'in': m_in/m_mi, 'km': m_km/m_mi, 'ft': m_ft/m_mi, 'yd': m_yd/m_mi},
    'in': {'mm': m_mm/m_in, 'cm': m_cm/m_in, 'm': 1/m_in, 'mi': m_mi/m_in, 'km': m_km/m_in, 'ft': m_ft/m_in, 'yd': m_yd/m_in},
    'km': {'mm': m_mm/m_km, 'cm': m_cm/m_km, 'm': 1/m_km, 'mi': m_mi/m_km, 'in': m_in/m_km, 'ft': m_ft/m_km, 'yd': m_yd/m_km},
    'ft': {'mm': m_mm/m_ft, 'cm': m_cm/m_ft, 'm': 1/m_ft, 'mi': m_mi/m_ft, 'in': m_in/m_ft, 'km': m_km/m_ft, 'yd': m_yd/m_ft},
    'yd': {'mm': m_mm/m_yd, 'cm': m_cm/m_yd, 'm': 1/m_yd, 'mi': m_mi/m_yd, 'in': m_in/m_yd, 'km': m_km/m_yd, 'ft': m_ft/m_yd}
}

if entry_unit == exit_unit:
    print(amount)
else:
    print(amount * measures.get(entry_unit).get(exit_unit))
