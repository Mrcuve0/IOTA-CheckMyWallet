from iota import Iota
from iota import Address

iotaNode = "https://field.carriota.com:443"

api = Iota(iotaNode, "")
input_address = input("Insert address: ")
address = [Address(input_address)]

def checkBalance():
	result = api.get_balances(address)
	balance = result['balances']
	if (balance[0]/1000000000000 < 1):
		if(balance[0]/1000000000 < 1):
			if(balance[0]/1000000 < 1):
				if(balance[0]/1000 < 1):
					res = str(balance[0]) + " iota"
				else:
					res = str(balance[0]/1000) + " Kiota"
			else:
				res = str(balance[0]/1000000) + " Miota"
		else:
			res = str(balance[0]/1000000000) + " Giota"
	else:
		res = str(balance[0]/1000000000000) + " Tiota"
	return (res)

print("Actual Balance: " + str(checkBalance()))
