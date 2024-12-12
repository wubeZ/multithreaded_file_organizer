import os
import shutil
from organizer.logger import setup_logger
from organizer.config import categorize_by_type, categorize_by_date, categorize_by_size
from organizer.task_management import process_in_threads
from organizer.utils import timing

@timing
def organize_files(path, by, dry_run, log_file=None, recursive=False):
    """
    Organize files in a directory based on the specified method
    
    Args:
    path (str): Path to the directory to organize
    by (str): Organization method: type, date, or size
    dry_run (bool): Simulate changes without making them
    log_file (str): Path to the log file
    recursive (bool): Organize files in subdirectories as well
    """

    if not os.path.exists(path):
        raise ValueError(f"Path {path} does not exist.")

    logger = setup_logger(log_file)

    dict_categorizer = {
        'type': categorize_by_type,
        'date': categorize_by_date,
        'size': categorize_by_size
    }

    if by not in dict_categorizer:
        raise ValueError("Invalid organization method.")

    logger.info(f"Organizing files in {path} by {by} {'(dry run)' if dry_run else ''}")

    file_groups = dict_categorizer[by](path, recursive)
    process_in_threads(dry_run, file_groups=file_groups, logger=logger)