from concurrent.futures import ThreadPoolExecutor
import os
import shutil
from organizer.utils import timing
from organizer.utils import with_progress_and_logs

@timing
def move_file(src, dest, dry_run, logger):
    """
    Move a file from source to destination

    Args:
    src (str): Source file path
    dest (str): Destination file path
    dry_run (bool): Simulate changes without making them
    logger (logging.Logger): Logger object
    """
    if dry_run:
        logger.info(f"Dry run: Would move {src} to {dest}")
    else:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)
        logger.info(f"Moved {src} to {dest}")

@timing
@with_progress_and_logs(desc="Processing Files")
def process_in_threads(dry_run, file_groups=None, logger=None, progress_bar=None):
    """
    Process file groups in threads

    Args:
    file_groups (dict): Dictionary containing destination folders as keys and files as values
    dry_run (bool): Simulate changes without making them
    logger (logging.Logger): Logger object
    progress_bar (tqdm.tqdm): Progress bar object
    """
    total_files = sum(len(files) for files in file_groups.values())
    with ThreadPoolExecutor() as executor:
        job_list = []
        for dest_folder, files in file_groups.items():
            for file in files:
                src = file
                dest = os.path.join(dest_folder, os.path.basename(file))
                job_list.append(executor.submit(move_file, src, dest, dry_run, logger))
                
        
        # Wait for all threads to finish
        for job in job_list:
            job.result()
            progress_bar.update(1)