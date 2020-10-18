import sys

import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

import requests
from urllib.parse import urlparse

class Blockchain(object):

    difficulty_target = "0000"

# Creates a class named blockchain with two methods
# hash_block() method encodes a block into array of bytes and then hashes it; you need to ensure that the dictionary is sorted, or you'll have inconsistent hashes later on
# __init__() function is the constructor for the class. Here, you store the entire blockchain as a list. 
# Because every blockchain as genesis block, you need to initialise the genesis block with the hash of the previous block, and in this example, 
# we simply used a fixed string called "genesis_block" to obtain the hash.
# Once the hash of the previous block is found, we need to find the nonce for the block using the method named proof_of_work()

    def hash_block(self, block):
        block_encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
        
    def __init__(self):
        # stores all the blocks in the entire blockchain
        self.chain = [] 
        # temporarily stores the transcations for the current block
        self.current_transcations = []
        # create the genesis block with a specific fixed hash of previous block genesis block starts with index 0
        genesis_hash = self.hash_block("genesis_block")
        self.append(
            hash_of_previous_block = genesis_block,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )

    # Use PoW to find the nonce for the current block
    def proof_of_work (self, index, hash_of_previous_block, transcations):
        # try with nonce = 0
        nonce = 0
        
        # try hashing the nonce together with the hash of the previous block until its valid
        while self.valid_proof(index, hash_of_previous_block, transcations, nonce) is False:
            nonce += 1
            
        return nonce

    def valid_proof(self, index, hash_of_previous_block, transcations, nonce):
        # Create a string containing the hash of the previous block and block content, including the nonce
        content = f"{index}{hash_of_previous_block}{transaction}{nonce}".encode()
        # Hash using sha256
        content_hash = hashlib.sha256(content).hexdigest()
        
        # Check if the hash meets the difficulty target
        return content_hash[:len(self.difficulty_target)] == self.difficulty_target

    # Creates a new block and adds it to the blockchain
    def append_block(self, nonce, hash_of_previous_block):
        
        # When the block is added to the blockchain, the current timestamp is also added to the block

        block = {
            'index' : len(self.chain),
            'timestamp': time(),
            'transactions': self.current_transcations,
            'nonce' : nonce,
            'hash_of_previous_block' : hash_of_previous_block
        }
        # Reset current list of transcations
        self.current_transcations = []
        
        # add the new block to the blockchain
        self.chain.append(block)
        return block 

    def add_transaction(self, sender, recipient, amount):
        
        # Adds a new transaction to the current list of transactions.
        # Gets the index of the last block in the blockchain and adds one to it
        # New index will be the block that the current transcation will be added to
        
        self.current_transcations.apped({
            'amount' : amount,
            'recipient' : recipient,
            'sender' : sender
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        # returns the last block in the blockchain
        return self.chain[-1]

    

    

    

