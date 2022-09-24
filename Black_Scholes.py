import math

from scipy.stats import norm


# first input sto
def black_scholes(spot_price, volatility, interest_rate, strike_price, time_period, choice):
    price = 0
    d1_num = math.log(spot_price / strike_price) + time_period * (interest_rate + 0.5 * (volatility ** 2))
    d1_denom = (volatility * math.sqrt(time_period))
    d1 = d1_num / d1_denom
    d2 = d1 - d1_denom
    if choice.lower() == 'call':
        price = spot_price * norm.cdf(d1, loc=0, scale=1) - (strike_price * norm.cdf(d2, loc=0, scale=1) /
                                                             math.exp(interest_rate * time_period))
    elif choice.lower() == 'put':
        price = (strike_price * norm.cdf(-d2, loc=0, scale=1) / math.exp(interest_rate * time_period)) - \
                spot_price * norm.cdf(-d1, loc=0, scale=1)
    return price


choice = input('please enter the type of option(call, put):')
spot_Price = float(input('Enter the Spot Price:'))
strike_Price = float(input('Enter the Strike Price:'))
time_Period = float(input('Enter the time period:'))
volatility = float(input('Enter the volatility value(as a decimal not percentage):'))
interest_Rate = float(input('Enter the interest rate value(as a decimal not percentage):'))
a = black_scholes(spot_Price, volatility, interest_Rate, strike_Price, time_Period, choice)

print(f'The price of the {choice} option is: {a.round(2)}')
