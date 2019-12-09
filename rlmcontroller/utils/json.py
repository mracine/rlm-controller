import os, json

# Helper function for reading a JSON file and
# returning a dictionary
def read_from_file(config_file):
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except ValueError:
            # TODO Something here?
            pass

    return {}

# Helper function for writing a dict to
# a JSON file
def write_to_file(config_file, config={}):
    try:
        with open(config_file, 'w') as f:
            json.dump(config, config_file)
            return 0
    except ValueError:
        # TODO Something here?
        pass
    except TypeError:
        # TODO Something here?
        pass

    return -1
