import abce
from abce import NotEnoughGoods


class Spotbuyer(abce.Agent, abce.Household, abce.Trade):
	def init(self, simulation_parameters, agent_parameters):
		""" 1. Create accounts with initial balances 2. Set target prices & quantities """
		self.create('CRC', 0)
		self.crc_qty = 'crc_qty'
		self.create('NORI', 0)
		self.nori_qty = 'nori_qty'
		self.create('SOV', 0)
		self.sov_qty = 'sov_qty'
		self.target_price = 'target_price' 
		self.target_qty = 'target_qty'
		self.set_cobb_douglas_utility_function({'CRC': 0.5, 'SOV': 0.5})
		self.current_utility = 0

	def buy_nori(self):
		""" Purchase NORI if market_price is less than target price """
		nori_offers = self.get_offers('NORI')
		for nori_offer in nori_offers:
			if offer.price <= target_price: 
				try:
					self.accept(offer)
				except NotEnoughGoods:
					self.accept(offer, self.possession('SOV') / offer.price)

	def buy_crc(self):
		""" Purchase CRC at market_price """
		crc_offers = self.get_offers('CRC')
		for crc_offer in crc_offers:
			if offer.price <= market_price:
				try:
					self.accept(offer)
				except NotEnoughGoods:
					self.accept(offer, self.possession('NORI') / offer.price)

	def retire_crc(self):
		""" Retire (consume) CRC """
		self.crcs_retired = self.consume_everything()
		self.log('Spot buyers', self.current_utility) # We want to log crc_qty, market_price, and nori_qty, not utility