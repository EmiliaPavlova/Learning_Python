bitcoin = int(input())
yuan = float(input())
commission_rate = float(input()) / 100

bitcoin_lev_rate = 1168
yuan_dollar_rate = 0.15
dollar_lev_rate = 1.76
euro_lev_rate = 1.95

amount_leva = bitcoin * bitcoin_lev_rate + yuan * yuan_dollar_rate * dollar_lev_rate
amount_euro = amount_leva / euro_lev_rate
result = amount_euro - amount_euro * commission_rate
print('%.2f' % result)
