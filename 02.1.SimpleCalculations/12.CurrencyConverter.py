amount = float(input('Amount = '))
entry_currency = input('Currency = ').upper()  # I'm too lazy to press the caps lock
exit_currency = input('Converted currency = ').upper()

BGN = 1
USD = 1.79549
EUR = 1.95583
GBR = 2.53405
currency = str(entry_currency + '/' + exit_currency)

currencies = {
  'BGN': {'USD': 1 / USD, 'EUR': 1 / EUR, 'GBR': 1 / GBR},
  'USD': {'BGN': USD, 'EUR': USD / EUR, 'GBR': USD / GBR},
  'EUR': {'BGN': EUR, 'USD': 1 / EUR, 'GBR': EUR / GBR},
  'GBR': {'BGN': GBR, 'USD': GBR / USD, 'EUR': GBR / EUR}
}

result = None
if entry_currency not in currencies or exit_currency not in currencies:
    print('Not supported currency')
elif entry_currency == exit_currency:
    result = 1
    print('Same currency')
else:
    result = amount * currencies.get(entry_currency).get(exit_currency)
    print(f'{(round(result, 2))} {exit_currency}')

