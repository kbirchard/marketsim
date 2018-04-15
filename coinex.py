import abce
from abce import NotEnoughGoods

#Coinex is simply a market maker that converts between SOV and NORI at the prevailing rate
class Coinex(abce.Agent, abce.Trade) :
	def init(self, simulation_parameters, agent_parameters) :
		self.create('NORI', 50000000) # From token supply parameters. Equal to proportion of tokens not held by speculators
		self.nori_qty = 'nori_qty'
		self.create('SOV', 500000000) # To provide liquidity
		self.nori_sov = 'nori_sov' # Exchange rate: USD:NORI
	def exch_sell_nori(self) :
		""" Sell NORI to Spot Buyers and Speculators """
		self.sell('spotbuyer', l, # Many spot buyers
			good='NORI',
			quantity=q,	# Quantity required by Spot Buyer
			price=market_price)
	def exch_buy_nori(self):
		""" Purchase NORI at market_price from Suppliers, Spot Buyers, and Speculators """
		nori_exchgs = self.get_offers('NORI')
		for nori_exchg in nori_exchgs:
			self.accept(offer)
		if NotEnoughGoods:
				self.accept(nori_exchg, self.possession('SOV') / nori_exchg.price)