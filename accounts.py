import time
from functions import Functions
from web3 import Web3

# Aurora Testnet:

contraddr = {
    'FAUCET': '0xe8b53eE0443620fB8DcEaEB6DE98ED117971c329',
    'approve_WNEAR': '0x01b2edff9b095dc270beca46e2efb41a3ecee169',
    'deposit_WNEAR': '0x910fb0AE51761ccCDBbD9ced613e6A4dc571594a',
    'collateral_WNEAR': '0x79e62AAfc1675c9F737Ec4Bb949115bfC8D2E2E6',
    'borrow_WNEAR': '0x910fb0AE51761ccCDBbD9ced613e6A4dc571594a',

    'approve_USDC': '0xe1Db3E2f129539b2399d8Cd9e808305c85f0c82f',
    'deposit_USDC': '0x7A9984522bC81B348d66379ed36Be5BD6147820E',
    'collateral_USDC': '0x79e62AAfc1675c9F737Ec4Bb949115bfC8D2E2E6',
    'borrow_USDC': '0x7A9984522bC81B348d66379ed36Be5BD6147820E',

    'approve_USDT': '0x4459ED2dEFFe0569AE748aD5D7cFEFDeeF667E87',
    'deposit_USDT': '0xDACC02a4Ff16Ea3c1515AdbfdCeb7B1F448B79c8',
    'collateral_USDT': '0x79e62AAfc1675c9F737Ec4Bb949115bfC8D2E2E6',
    'borrow_USDT': '0xDACC02a4Ff16Ea3c1515AdbfdCeb7B1F448B79c8',

    'approve_DAI': '0x1c9998C7768517b83136d3b237a31bc69eDc9028',
    'deposit_DAI': '0xC337343d1ac9F77B1305261CCD17e3799F088D4B',
    'collateral_DAI': '0x79e62AAfc1675c9F737Ec4Bb949115bfC8D2E2E6',
    'borrow_DAI': '0xC337343d1ac9F77B1305261CCD17e3799F088D4B',

    'approve_WBTC': '0xA69506eAbdC11BBdAf2259882A02a91B66E6d7E1',
    'deposit_WBTC': '0x981bD5832EAB9C8F607940E0e9faCBf8C09ee20a',
    'collateral_WBTC': '0x79e62AAfc1675c9F737Ec4Bb949115bfC8D2E2E6',
    'borrow_WBTC': '0x981bD5832EAB9C8F607940E0e9faCBf8C09ee20a'
}

number_of_tokens = {
    'WNEAR': 5500 * 10 ** 24,
    'USDC': 27500 * 10 ** 6,
    'USDT': 27500 * 10 ** 6,
    'DAI': 27500 * 10 ** 18,
    'Borrow_DAI1': 95000 * 10 ** 18,
    'Deposit_DAI1': 95000 * 10 ** 18,
    'Borrow_DAI2': 70000 * 10 ** 18,
    'Deposit_DAI2': 70000 * 10 ** 18,
    'Borrow_DAI3': 55000 * 10 ** 18,
    'Deposit_DAI3': 55000 * 10 ** 18,
    'Borrow_DAI4': 40000 * 10 ** 18,
    'Deposit_DAI4': 40000 * 10 ** 18,
    'Borrow_DAI5': 30000 * 10 ** 18,
    'Deposit_DAI5': 30000 * 10 ** 18
}


def osnova(address, privatekey):
    aurora_testnet = Functions()

    print(f"Address: {address} Private: {privatekey}")

    aurora_testnet.httpprovider('https://testnet.aurora.dev/')
    # ('abi', 'contract_address')

    aurora_testnet.contract_address('ABI2.txt', contraddr['FAUCET'])
    for _ in range(11):
        aurora_testnet.faucet(address, privatekey)
        print('faucet_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_WNEAR'])
    aurora_testnet.approve(contraddr['deposit_WNEAR'], number_of_tokens['WNEAR'], address, privatekey)
    print('approve_success_WNEAR')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_WNEAR'])
    aurora_testnet.deposit(number_of_tokens['WNEAR'], address, privatekey)
    print('deposit_success_WNEAR')

    aurora_testnet.contract_address('ABI2.txt', contraddr['collateral_WNEAR'])
    aurora_testnet.collateral(contraddr['deposit_WNEAR'], address, privatekey)
    print('collateral_success_WNEAR')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_USDC'])
    aurora_testnet.approve(contraddr['deposit_USDC'], number_of_tokens['USDC'], address, privatekey)
    print('approve_success_USDC')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_USDC'])
    aurora_testnet.deposit(number_of_tokens['USDC'], address, privatekey)
    print('deposit_success_USDC')

    aurora_testnet.contract_address('ABI2.txt', contraddr['collateral_USDC'])
    aurora_testnet.collateral(contraddr['deposit_USDC'], address, privatekey)
    print('collateral_success_USDC')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_USDT'])
    aurora_testnet.approve(contraddr['deposit_USDT'], number_of_tokens['USDT'], address, privatekey)
    print('approve_success_USDT')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_USDT'])
    aurora_testnet.deposit(number_of_tokens['USDT'], address, privatekey)
    print('deposit_success_USDT')

    aurora_testnet.contract_address('ABI2.txt', contraddr['collateral_USDT'])
    aurora_testnet.collateral(contraddr['deposit_USDT'], address, privatekey)
    print('collateral_success_USDT')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['DAI'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['DAI'], address, privatekey)
    print('deposit_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['collateral_DAI'])
    aurora_testnet.collateral(contraddr['deposit_DAI'], address, privatekey)
    print('collateral_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Borrow_DAI1'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['borrow_DAI'])
    aurora_testnet.borrow(number_of_tokens['Borrow_DAI1'], address, privatekey)
    print('borrow_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Deposit_DAI1'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['Deposit_DAI1'], address, privatekey)
    print('deposit_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Borrow_DAI2'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['borrow_DAI'])
    aurora_testnet.borrow(number_of_tokens['Borrow_DAI2'], address, privatekey)
    print('borrow_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Deposit_DAI2'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['Deposit_DAI2'], address, privatekey)
    print('deposit_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Borrow_DAI3'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['borrow_DAI'])
    aurora_testnet.borrow(number_of_tokens['Borrow_DAI3'], address, privatekey)
    print('borrow_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Deposit_DAI3'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['Deposit_DAI3'], address, privatekey)
    print('deposit_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Borrow_DAI4'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['borrow_DAI'])
    aurora_testnet.borrow(number_of_tokens['Borrow_DAI4'], address, privatekey)
    print('borrow_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Deposit_DAI4'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['Deposit_DAI4'], address, privatekey)
    print('deposit_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Borrow_DAI5'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['borrow_DAI'])
    aurora_testnet.borrow(number_of_tokens['Borrow_DAI5'], address, privatekey)
    print('borrow_success')

    aurora_testnet.contract_address('ABI2.txt', contraddr['approve_DAI'])
    aurora_testnet.approve(contraddr['deposit_DAI'], number_of_tokens['Deposit_DAI5'], address, privatekey)
    print('approve_success_DAI')

    aurora_testnet.contract_address('ABI2.txt', contraddr['deposit_DAI'])
    aurora_testnet.deposit(number_of_tokens['Deposit_DAI5'], address, privatekey)
    print('deposit_success_DAI')
