import numpy as np
import pandas as pd
import abce
from abce import Simulation, gui
from supplier import Supplier
from spotbuyer import Spotbuyer
from speculator import Speculator
from coinex import Coinex


# User inputs
parameters = {
#token_supply = int(input())
#seed_price = int(input()) # Initial price at start of trading simulation. Can be inherited from last price of previous simulation for multi-year analysis
#supply_cutoff_price = int(input())
#transaction_fee = int(input())
# Parameters for initial NORI and SOV endowments
#liquidity_premium = int(input()) # Percentage return desired for SOV asset; default = 5%
# Target quantities and prices for spot buyers
# Buy and sell targets for strategic traders
# Proportion of agent types (spot buyer, strategic trader, noise trader), relative to # of suppliers, which is fixed at 100
#speculator_share = int(input(90)) # Share of circulating tokens held by speculators
#supplier_num = int(input(100)) # Default = 100
#spotbuyer_num = int(input()) # Best guess
#trader_num = token_supply / velocity * speculator_share
}


#@gui(parameters)


def main():
	simulation = Simulation(name = "NORI Token Market Simulation v0.1")

#	simulation.declare_round_endowment() IS THIS NECESSARY?

	simulation.build_agents(Supplier, 'supplier', 100) # Put these in parameters.csv and use .build_agents_from_file
	simulation.build_agents(Spotbuyer, 'spotbuyer', 100)
	simulation.build_agents(Speculator, 'speculator', 1000)
	simulation.build_agents(Coinex, 'coinex', 1)

# Create supplier_queue from 'crc_supply_sample.csv' in order returned from the code in lines 70-75, above
# Each supplier has an associated marginal_cost and marginal_qty
# For supplier i, if expected_price >= reserve_price,
#	list_crc and remove from queue
#	else evaluate the next element in list

# LIKE THIS?
# Make 100 suppliers
#for supplier_number in range(100):
#	new_supplier = {'marginal_cost': X, 'marginal_qty': Y, 'expected_price': Z}
#	supplier_queue.append(new_supplier)

	for round in range(360):		# Assume 360 trading days per year
		simulation.advance_round(round)
		Supplier().self.list_crc()	# IS THIS THE RIGHT WAY TO DO THIS? Supplier lists CRC if expected_price > marginal_cost
		spotbuyer.buy_nori()		# Spot Buyer buys NORI from Coinex
		coinex.exch_sell_nori()		# Coinex sells NORI to Spot Buyer
		spotbuyer.buy_crc()		# Spot Buyer purchases CRC
		spotbuyer.retire_crc()		# Spot Buyer (smart contract) retires CRC
		(supplier + spotbuyer()).panel_log(...)	# Log CRC trades
		speculator.trade_nori()		# Speculators trade
		supplier.sell_nori()		# Supplier sells NORI to Coinex
		speculator.sell_nori()		# Speculator sells NORI to Coinex
		coinex.exch_buy_nori()		# Coinex buys
		coinex.panel_log(...)		# Log NORI trades
		# Do we need to clear trades? If so, how?

	simulation.graphs()
	simulation.finalize()

if __name__ == '__main__':
	main()