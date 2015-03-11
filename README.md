BitSim
======

Development of this project will continue once I have more free time to spare.

A simple Bitcoin trading simulator

<b>Requirements</b>

* Requests library
* Python3

<b>Functions available:</b>

* getCurrentBTCPrice() - Returns the current BTC price
* getLow() - Returns the current 24H low
* getHigh() - Returns the current 24H high
* getCurrentTime() - Returns the current unix timestamp
* runSim(outFile) - Runs the simulation as based off the input file
* processFile(inFile) - Processes an input file
* processLine(line) - Processes a line of an input file
* buy(amount, price, trader) - Buys amount # of BTCs @ price price using the defined trader
* sell(amount, price, trader) - Same as buy only sell
* printCurrentInfo() - Prints the current simulator data
* getFee(amount) - Determines the BitStamp fee for a transaction of amount $'s
* Interactive Mode 

<b>To Do:</b>

* Add EUR currency support

les ending in *.BTCsim are used for saving (logging), and reading in transactions to get the account up to date. File format can be seen in the Test.BTCsim file. Make sure to run using python3!
