import time
from web3 import Web3
from loguru import logger
from sys import stderr


logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")


class Functions:
    def __init__(self, web3='', contract='', transaction='', nonce=1, tx_hash=''):
        self.web3 = web3
        self.contract = contract
        self.transaction = transaction
        self.nonce = nonce
        self.tx_hash = tx_hash

    def httpprovider(self, httpprovider):
        self.web3 = Web3(Web3.HTTPProvider(httpprovider))
        return self.web3

    def contract_address(self, abi_file, contract_address):
        abi = open(abi_file, 'r').read().replace('\n', '')
        self.contract = self.web3.eth.contract(Web3.toChecksumAddress(contract_address), abi=abi)

    def build_params(self, address):
        address = address

        self.nonce = self.web3.eth.getTransactionCount(address)
        params = ({
            'gas': 6721975,
            'gasPrice': self.web3.toWei('0', 'gwei'),
            'from': address,
            'nonce': self.nonce
        })
        return params

    def build_transaction(self, privatekey):
        try:
            signed_tx = self.web3.eth.account.signTransaction(self.transaction, private_key=privatekey)
            self.tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            #txstatus = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            txstatus = self.web3.eth.waitForTransactionReceipt(self.tx_hash.hex()).status
            if txstatus == 1:
                logger.success(f'TX status: {txstatus}')
            else:
                logger.error(f'TX status: {txstatus}')
        except Exception as error:
            if 'ERR_INCORRECT_NONCE' in str(error):
                zhopa = "pisya"
            else:
                self.build_transaction(privatekey)

        else:
            return True

    def approve(self, approve_contract, number_of_token, address, privatekey):

        # (address spender, uint256)
        self.transaction = self.contract.functions.approve(approve_contract, number_of_token).buildTransaction(self.build_params(address))
        self.build_transaction(privatekey)

    def deposit(self, number_of_token, address, privatekey):
        self.transaction = self.contract.functions.mint(number_of_token).buildTransaction(self.build_params(address))
        self.build_transaction(privatekey)

    def collateral(self, collat_contract, address, privatekey):
        self.transaction = self.contract.functions.enterMarkets([self.web3.toChecksumAddress(collat_contract)]).buildTransaction(self.build_params(address))
        self.build_transaction(privatekey)

    def borrow(self, number_of_token, address, privatekey):
        # (uint256)
        self.transaction = self.contract.functions.borrow(number_of_token).buildTransaction(self.build_params(address))
        self.build_transaction(privatekey)

    def faucet(self, address, privatekey):
        self.transaction = self.contract.functions.drip().buildTransaction(self.build_params(address))
        self.build_transaction(privatekey)