import yaml

def load_vars():
    with open("config.yaml", "r") as config_file:
        vars = yaml.load(config_file, Loader = yaml.FullLoader)

    return vars

if __name__ == "__main__":
    vars = load_vars()
    print(vars)