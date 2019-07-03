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

if entry_unit == 'mm':
    amount /= m_mm
elif entry_unit == 'cm':
    amount /= m_cm
elif entry_unit == 'mi':
    amount /= m_mi
elif entry_unit == 'in':
    amount /= m_in
elif entry_unit == 'km':
    amount /= m_km
elif entry_unit == 'ft':
    amount /= m_ft
elif entry_unit == 'yd':
    amount /= m_yd

result = amount

if exit_unit == 'mm':
    result *= m_mm
elif exit_unit == 'cm':
    result *= m_cm
elif exit_unit == 'mi':
    result *= m_mi
elif exit_unit == 'in':
    result *= m_in
elif exit_unit == 'km':
    result *= m_km
elif exit_unit == 'ft':
    result *= m_ft
elif exit_unit == 'yd':
    result *= m_yd

print(result)
