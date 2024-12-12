import argparse
from organizer.file_ops import organize_files

def parse_arguments():
    """
    parse command line arguments

    Returns:
    argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(description="Multithreaded File Organizer")
    parser.add_argument('--path', required=True, type=str, help='Path to the directory to organize')
    parser.add_argument('--by', required=True, choices=['type', 'date', 'size'], help='Organize by: type, date, or size')
    parser.add_argument('--dry-run', action='store_true', help='Simulate changes without making them')
    parser.add_argument('--log', type=str, help='Log actions to a file')
    parser.add_argument('--recursive', action='store_true', help='Organize files in subdirectories as well')
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    organize_files(path=args.path, by=args.by, dry_run=args.dry_run, log_file=args.log, recursive=args.recursive)

if __name__ == "__main__":
    main()