from functions import Functions
from accounts import osnova
import threading
from threading import *
import time


def accounts():
    with open('Wallets.txt', 'r') as file:
        wallets = [row.strip() for row in file]
    threads = 50
    i = 1
    provider = Functions()
    web3 = provider.httpprovider('https://testnet.aurora.dev/')
    provider.contract_address('ABI2.txt', '0xe8b53eE0443620fB8DcEaEB6DE98ED117971c329')
    while wallets:
        if threading.active_count() <= threads:
            for _ in range(threads):
                privatekey = wallets.pop(0)
                address = web3.eth.account.privateKeyToAccount(privatekey).address
                Thread(target=osnova, args=(address, privatekey,), name=f"HUY-{i}").start()
                i += 1

if __name__ == '__main__':
    accounts()
