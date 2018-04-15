import numpy as np
import abce
from abce import NotEnoughGoods

#class forecasts:
# Adapted from LeBaron (2016). Need to adjust to your needs
    # initialize forecast components
 #   def __init__(self,Lmax,pf,sigmae):
 #       self.fundamental = 0.
 #       # chartist is vector for different lengths
 #       self.chartist    = np.zeros(Lmax)
 #       self.noise       = 0.
 #       self.v = 0.
 #       self.pf = pf
 #       self.sigmae = sigmae
 #       self.Lmax = Lmax
    # update forecasts   
 #   def updateForecasts(self,t,price,ret):
 #       self.fundamental = np.log(self.pf/price)
 #       self.noise = self.sigmae*np.random.randn()
 #       self.v = np.var(ret[0:t])
 #       revrets = ret[t:(t-self.Lmax):-1]
 #       self.chartist = np.cumsum(revrets)/np.arange(1.,float(self.Lmax+1))

class Speculator(abce.Agent, abce.Trade):
	def init(self, simulation_parameters, agent_parameters):
		self.create('NORI', 50000) # From token supply parameters. Equal to proportion held by speculators divided by # of speculators.
		self.create('SOV', 0) # This may need to be greter than one...
		self.target_price = 'target_price'
		# set strategy weights
		# set all positive :  this diverges from the paper a little
#		self.fundWeight =  np.abs(sigmaF*np.random.randn())
#		self.chartWeight = (sigmaM*np.random.randn())
#		self.noiseWeight = (sigmaN*np.random.randn())
		# horizons for momentum rules 
#		self.l = np.random.randint(Lmin,Lmax)
		# random component of spread
#		self.k = kmax*np.random.rand()
#		self.fcast = 0.
#		self.pfcast = 0.
#		self.wealth = 0.
#		self.bid = 0.
#		self.ask = 0.
		# forecast adjustment weight
#		self.fcastAdjust = 1./(self.fundWeight+self.chartWeight+self.noiseWeight)

#	def updateFcast(self,forecast,price,tau):
		# weighted forecast value
#		self.fcast = self.fcastAdjust*(self.fundWeight*forecast.fundamental+self.chartWeight*forecast.chartist[self.l] + \
#			self.noiseWeight*forecast.noise)
		# bound the forecast
#		self.fcast = min(self.fcast,0.5)
#		self.fcast = max(self.fcast,-0.5)
		# exponentiate the forecast to get future price forecast 
		# note:  this could have a variance adjustment, but it doesn't at the moment
#		self.pfcast = price*np.exp(self.fcast+0.0*forecast.v)

	# YOUR CODE RESUMES HERE
	# Agents sell/buy NORI
	def spec_buy_nori(self):
		nori_specs = self.get_offers('NORI')
		for nori_spec in nori_specs:
			if self.target_price < market_price:
				self.accept(offer)
			else:
				self.sell('speculator', k, # Sell token to another speculator
					good='NORI',
					quantity=nori_qty, # Sell some quantity (to be determined) of NORI at market_price 
					price=market_price) # Price at time step t* when market_price > reserve_price