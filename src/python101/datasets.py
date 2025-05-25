import importlib.resources

def get_flatland():
    with importlib.resources.path("python101.data", "flatland.txt") as f:
        data_file_path = f
    return data_file_path

