import pandas as pd
import abce
from abce import NotEnoughGoods

# Create CRC dataframe from CSV, randomly select 100 suppliers, and output as a dictionary - records/tabular format
supply = pd.read_csv('crc_supply.csv') 
crc_sample = supply.sample(n=100) #EVENTUALLY WANT TO TAKE USER INPUT...FROM simulation.py?
crc_list = crc_sample.to_dict('records')

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
		self.expected_price = 'expected_price' # Expected_price over time_horizon. This is set in simulation.py

		#THIS IS WHERE I'M NOT SURE HOW TO PROCEED, BUT HERE GOES:

#		for supplier i in suppliers:
#			crc_qty = crc_list.marginal_qty
#			marginal_cost = crc_list.marginal_cost

#		Does this belong in the simulation code?

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
