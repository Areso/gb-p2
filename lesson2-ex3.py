import yaml


def write_savegame_to_yaml(mychar):
    with open('data.yaml', 'w') as f_n:
        yaml.dump(mychar, f_n, default_flow_style=True, allow_unicode=True)
    return 0

def load_savegame_from_yaml():
    with open("data.yaml", 'r') as stream:
        print(yaml.safe_load(stream))
    return 0

mycharname = {}
mycharname["0"] = ord("€")
mycharname["1"] = ord("₮")
mychar = {}
mychar["inventory"] = ['sword, shield']
mychar["level"] = 85  # 85 level!
mychar["name"] = mycharname
write_savegame_to_yaml(mychar)
load_savegame_from_yaml()

