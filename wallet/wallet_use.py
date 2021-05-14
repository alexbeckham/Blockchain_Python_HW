#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import dependencies
import subprocess
import json
from dotenv import load_dotenv


# In[ ]:


# Load and set environment variables
#import mnemonic

load_dotenv()
mnemonic=os.getenv("mnemonic")


# In[ ]:


# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
from constants import *
w3= Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrtegy(medium_gas_price_strategy)


# In[ ]:


# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f'php derive -g --mnemonic= "{mnemonic}" --coin "{coin}" --numderive "{numderive}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)


# In[ ]:


# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {'eth', 'btc-test', 'btc'}
numderive = 3 


# In[ ]:


# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE


# In[ ]:


# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE


# In[ ]:


# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE


# In[ ]:





# In[ ]:




