# Plain English Description of Simulation Model
April 14, 2018

There are 4 classes of agents:

## Supplier: 
Supplies carbon storage services, represented by units called CRCs (Carbon Removal Credits). 

Create 3 accounts, all initialized with a value of zero:
- CRC = quantity of CRCs possessed by Supplier 
- NORI = quantity of NORI tokens
- SOV = quantity of a Store-of-value asset, such as US dollars

The objective of each supplier is to sell its CRCs for NORI and cash out its NORI at a price greater than its marginal cost of providing carbon storage services.

Each supplier has an expected_price, which is normally distributed with a mean equal to the current market_price and a standard deviation of ???

Supplier lists all its available CRCs when its expected_price > market_price
>	This "listing" is added to the supplier_queue, which is an ordered list of CRCs available for sale in first-in, first-out fashion

CRCs are sold when a spot buyer purchases them. Spot buyers may purchase some or all of a particular supplier's CRCs.

If supplier has a positive balance of NORI, then it sells to Coin Exchange when market_price > marginal_cost


## Spot Buyer: 
Purchases CRCs and retires them

Create 2 accounts, initialized w/ value of zero:
- NORI = same definition as supplier
- SOV = same definition as supplier 

The objective of the spot buyer is to purchase and retire CRCs.

A spot buyer has a target_price and quantity, which are based on a table to be developed

Spot buyer purchases NORI with SOV when market_price < target_price

Spot buyer purchases all available CRCs with NORI, up to its target_qty, when its turn in the queue arrives. 
>	If CRC inventory is less than target_qty, spot buyer purchases available quantity

Spot buyer "consumes" CRCs (in the parlance of ABCE), logs consumption of CRCs and price

If spot buyer has a positive NORI balance, then it sells to Coin Exchange when market_price > target_price 


## Trader: 
Composite of three types of traders we might expect to see in the market: a fundamental trader with long-term price expectation _u_, a momentum trader, and a noise trader

Create 2 accounts, initialized w/ value of zero:
- NORI = same definition as suppliers & spot buyers
- SOV = same definition as suppliers & spot buyers 

The objective of a trader is to maximize its returns (represented by SOV) by buying and selling NORI and converting NORI to SOV when market_price exceeds its target price.


## Coin Exchange:
This is simply an exchange that converts NORI to SOV and vice versa. It is assumed that all markets are liquid, and accepts offers and bids at any price.
