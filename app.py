import datetime
import json
import hashlib
from flask import Flask, jsonify
from dataclasses import dataclass, asdict
from typing import List, Dict

@dataclass
class Block:
    index: int
    timestamp: str
    proof: int
    previous_hash: str

class Blockchain:
   def __init__(self):
       self.chain: List[Block] = []
       self.create_block(proof=1, prev_hash='0')

   def create_block(self, proof: int, prev_hash: str) -> Block:
       block = Block(
           index=len(self.chain) + 1,
           timestamp=str(datetime.datetime.now()),
           proof=proof,
           previous_hash=prev_hash
       )
       self.chain.append(block)
       return block

   def get_previous_block(self) -> Block:
       last_block = self.chain[-1]
       return last_block

   def proof_of_work(self, prev_proof: int) -> int:
       new_proof = 1
       check_proof = False

       while check_proof is False:
           hash_operation = hashlib.sha256(str(new_proof ** 2 - prev_proof ** 2).encode()).hexdigest()
           
           if hash_operation[:4] == '0000':
               check_proof = True
           else:
               new_proof += 1

       return new_proof

   def hash(self, block: Block) -> str:
       encoded_block = json.dumps(asdict(block), sort_keys=True).encode()
       return hashlib.sha256(encoded_block).hexdigest()

   def is_chain_valid(self, chain: List[Block]) -> bool:
       prev_block = chain[0]

       block_index = 1
       while block_index < len(chain):
           block = chain[block_index]

           if block.previous_hash != self.hash(prev_block):
               return False
           prev_proof = prev_block.proof

           current_proof = block.proof

           hash_operation = hashlib.sha256(str(current_proof ** 2 - prev_proof ** 2).encode()).hexdigest()

           if hash_operation[:4] != '0000':
               return False

           prev_block = block
           block_index += 1
       return True


app = Flask(__name__)

blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
   prev_block = blockchain.get_previous_block()
   prev_proof = prev_block.proof
   proof = blockchain.proof_of_work(prev_proof)
   prev_hash = blockchain.hash(prev_block)

   block = blockchain.create_block(proof, prev_hash)
   response = {
       'message': 'Block mined!',
       **asdict(block)
   }
   return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
   response = {
       'chain': [asdict(block) for block in blockchain.chain],
       'length': len(blockchain.chain),
       'valid': blockchain.is_chain_valid(blockchain.chain)
   }
   return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)