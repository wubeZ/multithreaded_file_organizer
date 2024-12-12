import os
import tempfile
import shutil
import pytest
from organizer.file_ops import organize_files

@pytest.fixture
def test_directory():
    test_dir = tempfile.mkdtemp()
    test_files = [
        os.path.join(test_dir, f"file{i}.txt") for i in range(5)
    ]
    for file in test_files:
        with open(file, 'w') as f:
            f.write("Test content")
    yield test_dir, test_files
    # Teardown
    shutil.rmtree(test_dir)

def test_organize_by_type(test_directory):
    test_dir, test_files = test_directory
    organize_files(path=test_dir, by='type', dry_run=False)
    organized_folder = os.path.join(test_dir, 'txt')
    assert os.path.exists(organized_folder)
    for file in test_files:
        assert os.path.exists(os.path.join(organized_folder, os.path.basename(file)))

def test_dry_run(test_directory):
    test_dir, _ = test_directory
    organize_files(path=test_dir, by='type', dry_run=True)
    organized_folder = os.path.join(test_dir, 'txt')
    assert not os.path.exists(organized_folder)