from core.entrypoint import process_json_file
# from core.entrypoint import request, get_coordinates, get_available_state_data
from utils.utils import init_tmp_path

if __name__ == "__main__":
    import os
    import glob

    # Get the directory path for JSON files
    data_dir = os.path.join(os.path.dirname(__file__), "data_sample_to_search")
    
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(data_dir, "*.json"))
   
    init_tmp_path()
    # Process each JSON file
    for json_file in json_files:
        process_json_file(json_file)
