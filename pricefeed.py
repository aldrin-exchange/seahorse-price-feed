# pricefeed
# Built with Seahorse v0.2.4
#
# A simple Seahorse program that retrieves prices from the Pyth oracle.

from seahorse.prelude import *
from seahorse.pyth import *

declare_id('Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS')

@instruction
def get_sol_usd_price(price_account: PriceAccount):
  # Retrieves the current price of SOL and logs it.
  print('Fetching SOL/USD price.')
  price_feed = price_account.validate_price_feed('devnet-SOL/USD')
  price = price_feed.get_price()
  # Retrieves the price as a floating-point number
  x: f64 = price.num()
  print(f'The current price of SOL/USD is {x}.')

@instruction
def get_eth_usd_price(price_account: PriceAccount):
  # Retrieves the current price of ETH and logs it.
  print('Fetching ETH/USD price.')
  price_feed = price_account.validate_price_feed('devnet-ETH/USD')
  price = price_feed.get_price()
  x: f64 = price.num()
  print(f'The current price of ETH/USD is {x}.')

@instruction
def sol_net_worth(balance: f64, price_account: PriceAccount):
  # Computes the value of the given amount {balance} of SOL in terms of USD.
  price_feed = price_account.validate_price_feed('devnet-SOL/USD')
  price = price_feed.get_price()
  x: f64 = price.num()
  value = x*balance
  print(f'Your current balance of {balance} SOL is worth {value} USD.')
