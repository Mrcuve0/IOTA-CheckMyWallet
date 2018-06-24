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
					res = str('%.2f' % (balance[0])) + " iota"
				else:
					res = str('%.2f' % (balance[0]/1000)) + " [K]iota"
			else:
				res = str('%.2f' % (balance[0]/1000000)) + " [M]iota"
		else:
			res = str('%.2f' % (balance[0]/1000000000)) + " [G]iota"
	else:
		res = str('%.2f' % (balance[0]/1000000000000)) + " [T]iota"
	return (res)

print("Actual Balance: " + str(checkBalance()))
