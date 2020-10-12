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
        
    def def __init__(self):
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

