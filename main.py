import gc
import os
import psutil
from core.entrypoint import process_json_file, get_available_state_data
from utils.utils import init_tmp_path
from logger.logger import get_logger

def log_memory_usage():
    """Log current memory usage"""
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 / 1024  # Convert to MB
    logger.debug(f"Current memory usage: {mem:.2f} MB")


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
    get_available_state_data()

    if not json_files:
        logger.info(f"No JSON files found in {data_dir}")
    else:
        processed_count = 0
        batch_size = 5  # Adjust based on your memory usage patterns
        
        # Log initial memory usage
        try:
            log_memory_usage()
        except ImportError:
            logger.warning("psutil not installed - memory monitoring disabled")
            
        # Use a thread pool to process files in parallel with a fixed concurrency limit
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_json_file, jf): jf for jf in json_files}
            for fut in as_completed(futures):
                jf = futures[fut]
                try:
                    fut.result()
                    processed_count += 1
                    
                    # Run garbage collection after each batch
                    if processed_count % batch_size == 0:
                        # Clear memory after processing a batch of files
                        gc.collect()
                        logger.debug(f"Garbage collection run after processing {processed_count} files")
                        try:
                            log_memory_usage()
                        except ImportError:
                            pass
                        
                except Exception as e:
                    logger.critical(f"Error processing {jf}: {e}")
            
        # Final garbage collection after all files are processed
        gc.collect()
        logger.debug("Final garbage collection run")
        try:
            log_memory_usage()
        except ImportError:
            pass
