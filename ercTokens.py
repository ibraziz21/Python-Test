
from moralis import evm_api


API_KEY = 'EEkNrAb3BrFrUj0ti6mZqflZ3m2f8Vow705K7e0AiZBuBlynRXaoNPZF6jjohcPC'

w_Address = "0x11ec36418bE9a610904D1409EF0577b645104881"
t_Chains = input("Set an EVM chain: ")
param= {
    "address": w_Address,
    "chain": t_Chains
}

result = evm_api.token.get_wallet_token_balances(
    api_key=API_KEY,
    params= param
    
)
print(len(result))


import pandas as pd
df = pd.DataFrame(result)

print(df)
