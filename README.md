# README

A sample implementation of a conceptual blockchain using Python.

## Contents

- Timestamp: The time that the block was added to the blockchain
- Index: A running number starting from 0 indicating the block number
- Hash of the previous block: The hash result of the previous block.
- Nonce: The number used once.
- Transaction(s): Each block will hold a variable number of transactions

## How to Use

You can use this as a simple blockchain example, the following are commands 
that can be execute on the CLI

`$ curl http://localhost:5000/blockchain` 
- Returns the entire blockchain contents

`$ curl http://localhost:5000/mine`
- Allows you to mine a single block default difficulty is set as `0000`

`$ curl -X POST -H "Content-Type: application/json" -d '{args} http://localhost:5000/transactions/new` 
- Allows you to add a transactions to the blockchain, given that
the arguments are correct.

## TODO

Intergrate into the Ethernet 