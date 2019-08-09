period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, period + 1):
    patients_for_the_day = int(input())
    if (day % 3 == 0) and (untreated_patients > treated_patients):
        doctors += 1
    if patients_for_the_day > doctors:
        treated_patients += doctors
        untreated_patients += patients_for_the_day - doctors
    else:
        treated_patients += patients_for_the_day

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
