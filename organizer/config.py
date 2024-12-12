import os
from collections import defaultdict
from datetime import datetime

def categorize_by_type(path, recursive):
    """
    Categorize files by their extension
    Args:
    path (str): Path to the directory to organize
    recursive (bool): Organize files in subdirectories as well
    Returns:
    dict: Dictionary with keys as destination folders and values as list of files
    """
    
    file_groups = defaultdict(list)
    for root, _, files in os.walk(path):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            dest_folder = os.path.join(path, file_ext.lstrip('.'))
            file_groups[dest_folder].append(os.path.join(root, file))
        if not recursive:
            break
    return file_groups

def categorize_by_date(path, recursive):
    file_groups = defaultdict(list)
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m')
            dest_folder = os.path.join(path, file_date)
            file_groups[dest_folder].append(file_path)
        if not recursive:
            break
    return file_groups

def categorize_by_size(path, recursive):
    file_groups = defaultdict(list)
    size_categories = {"small": 10**6, "medium": 10**7, "large": 10**9}

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size <= size_categories['small']:
                dest_folder = os.path.join(path, 'small')
            elif file_size <= size_categories['medium']:
                dest_folder = os.path.join(path, 'medium')
            else:
                dest_folder = os.path.join(path, 'large')

            file_groups[dest_folder].append(file_path)
        if not recursive:
            break
    return file_groups