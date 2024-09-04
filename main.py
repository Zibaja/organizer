from pathlib import Path
import shutil
from Data import Data_DIR
from utils import read_json


class OrganizDir:
    """Class to organize all files in a given directoty 
    Example:
    >>>    Organizer = OrganizDir()
    >>>    Organizer.run(to_organize_directory)
    """
    suffix_dir = read_json(Data_DIR / 'suffix_dir.json')

    def run(self, to_organize_dir: str):
        """Run to move files to the specified desitination in suffix_dir
        :type to_organize_dir: str
        """
        self.to_organize_dir = Path(to_organize_dir)
        print('For test')
        assert self.to_organize_dir.exists(), \
            f"Diretory  '{self.to_organize_dir.resolve()} ' not found!"

        for path in self.to_organize_dir.iterdir():
            if path.is_dir():
                if path.name in self.suffix_dir.values():
                    continue
                dest = 'dirs'
                DEST_DIR = path.parent / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(path, DEST_DIR)

            elif path.is_file():
                suffix = path.suffix
                dest = self.suffix_dir.get(suffix)

                if not dest:  # it prevents creating nested if and if there is no destination it goes to next iteration
                    continue

                DEST_DIR = path.parent / dest   # this is only the path but it doesnt exist
                DEST_DIR.mkdir(exist_ok=True)  # to generate the directory
                shutil.move(path, DEST_DIR)  # move a file from origin to destination


if __name__ == '__main__':
    Windows_HOME = Path('/mnt/c/Users/Ziba')
    Organizer = OrganizDir()
    Organizer.run(Windows_HOME / 'Downloads')

