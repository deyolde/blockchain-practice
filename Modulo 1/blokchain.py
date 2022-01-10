# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 20:24:46 2022

@author: david yolde
"""

# Módulo 1 - crear una cadena de bloques
# Flask instalado
# Postman instalado

# Importar las librerías
import datetme
import hashlib
import json
from flask import Flask, jsonify

# Parte 1 - Crear la Cadena de Bloques
class Blockchain:
    
    def __init__(self):
        self.clain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetme.datetme.now()),
                 'proof' : proof,
                 'previous_hash'  : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previos_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previos_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        
# Parte 2 - Minado de Bloque de la cadena