import pandas as pd
import abce
from abce import NotEnoughGoods

# DO YOU NEED TO PUT THE SUPPLIER IMPORT STUFF HERE, IN THE SIMULATION FILE, OR SOMEWHERE ELSE?
# IMPORT SUPPLIERS 
# For some reason, the following code adds another ID column with a blank heading...
# Create CRC dataframe
supply = pd.read_csv('crc_supply.csv') 
maxprice = 35 # NEEDS TO BE USER ENTERED, DEFAULT = $35
filter_price = supply[supply.marginal_cost <= maxprice]
# Randomly select 100 suppliers
crc_sample = filter_price.sample(n=100)
crc_sample.to_csv('crc_supply_sample.csv') # Output as a CSV? List? What's the best approach here?

class Supplier(abce.Agent, abce.Firm, abce.Trade):
	def init(self, simulation_parameters, agent_parameters):
		""" 1. Create accounts with initial balance of zero, 2. Set up marginal cost and qty import from CSV"""
		self.create('CRC', 0) #INHERITED FROM crc_supply_sample.csv
		self.crc_qty = 'crc_qty'
		self.marginal_cost = 'marginal_cost' # Marginal cost from crc_supply_sample.csv
		self.create('NORI', 0)
		self.nori_qty = 'nori_qty'
		self.create('SOV', 0)
		self.sov_qty = 'sov_qty'
		self.expected_price = 'expected_price' # Expected_price over time_horizon

	def list_crc(self):
		""" List available CRCs for sale if expected_price is greater than marginal_cost """
		self.sell('spotbuyer', j, # j = whoever the spot buyer is
					good='CRC',
					quantity=crc_qty, # m = list full amount of CRCs in account
					price=market_price) # Price at time step t when buy order comes in  

	def sell_nori(self):
		""" Sell NORI to Coinex when market_price > reserve_price """
		self.sell('coinex', 0, # Sell token to Exchange 0 for market price of NORI, less transaction fee
					good='NORI',
					quantity=nori_qty, # Sell entire quantity of NORI at market_price 
					price=market_price) # Market_price > reserve_price