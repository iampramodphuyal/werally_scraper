from core.entrypoint import process_json_file
# from core.entrypoint import request, get_coordinates, get_available_state_data
from utils.utils import init_tmp_path
from logger.logger import get_logger


if __name__ == "__main__":
    import os
    import glob
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # Number of concurrent tasks to run
    MAX_WORKERS = 5  # adjust as needed
    logger = get_logger("mainFile")
    # Get the directory path for JSON files
    data_dir = os.path.join(os.path.dirname(__file__), "data_sample_to_search")

    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(data_dir, "*.json"))

    init_tmp_path()

    if not json_files:
        logger.info(f"No JSON files found in {data_dir}")
    else:
        # Use a thread pool to process files in parallel with a fixed concurrency limit
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_json_file, jf): jf for jf in json_files}
            for fut in as_completed(futures):
                jf = futures[fut]
                try:
                    fut.result()
                except Exception as e:
                    logger.critical(f"Error processing {jf}: {e}")
