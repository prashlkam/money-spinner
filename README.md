# noney-spinner
a utility that could be used for Margin / Options Trading........

MoneySpinner - Trading Bot (overview)
======================================

 * to trade in Index / Stock Options
 * will be fully automated (very little human interaction required)
 * Simple logic (no Technical Analysis involved). Core Logic flow is as follows...
  - trade on single option contract from 9:15am to 3:25pm
  - Dynamic SLTP logic can be used to switch the position (from call to put OR vice-versa)
  - from 3:25 to 3:30pm - the existing position will be squared off and an In-the-money Straddle will be purchased at the Nearest Strike price possible.
  - on the next day - the position that has a loss will be sold within the first 2 minutes and the profit making position will be continued with a Dynamic SLTP.
  - at the end of weekly expiry - positions will be taken for the following week.
  
Limitations:-
---------------
 * Burn Down in the value of options - is the Only real risk
 * Flat / Sideways Market - is the worst Scenario.
 
Work already done:-
---------------------
 * Dynamic SLTP Logic already implemented
 
What needs to be done:-
-------------------------
 * Time trigger based Start / Switch / Stop
 * Select option based on current price of Underlying -> nearest In-the-money strike price
 * Reverse positions based on SLTP getting Triggered
 * Front End UI 
 * connection and security (Zerodha API)
 * Get Ticks (at like 5 Sec intervals) 
 * Data flow Pipeline
 * db Integration
 * add Payment gateway (deposit / withdrawal)
 * Abstraction of Usage
 * Any Extras that may be required
