from pathlib import Path
import shutil


class OrganizDir:
    def __init__(self, to_organize_dir):
        self.to_organize_dir = to_organize_dir

    def run(self):
        print('For test')


if __name__ == '__main__':
    Windows_HOME = Path('/mnt/c/Users/Ziba')
    Organizer = OrganizDir(Windows_HOME / 'Downloads')
    Organizer.run()

