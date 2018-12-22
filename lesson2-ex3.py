import pyyaml

def write_order_to_yaml(mychar):
    with open('data.yaml', 'w') as f_n:
        pyyaml.dump(mychar, f_n)
    return 0

mycharname = {}
mycharname["0"]=ord("€")
mycharname["1"]=ord("₮")
mychar = {}
mychar["inventory"] = ['sword, shield']
mychar["level"] = 85  # 85 level!
mychar["name"] = mycharname
write_order_to_yaml(mychar)


