import logging

def setup_logger(log_file=None):
    """
    Setup logger with a console and file handler

    Args:
    log_file (str): Path to the log file

    Returns:
    logging.Logger: Logger object
    """

    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger