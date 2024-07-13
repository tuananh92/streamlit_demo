import os

def get_data_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    return os.path.join(data_dir, filename)


def get_model_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "model")
    return os.path.join(data_dir, filename)