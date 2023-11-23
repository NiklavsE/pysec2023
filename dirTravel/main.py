import os
import datetime

##########################################################################
# Script that can recursively traverse directories and print the file listing
# in a hierarchical way with additional info about file size, creation date.
# test_case folder is an example directory structure that is used for
# demonstration purposes.
##########################################################################


def recDirLister(passedDir, level=1):
    for entry in os.scandir(passedDir):
        currentEntryFullDir = passedDir + '/' + entry.name

        output = ('---' * level) + entry.name

        if entry.is_file():
            stats = ''' Size: {} Created at: {} Modified At: {}'''.format(
                entry.stat().st_size,
                datetime.datetime.fromtimestamp(
                    os.path.getctime(currentEntryFullDir)),
                datetime.datetime.fromtimestamp(
                    os.path.getmtime(currentEntryFullDir))
            )

            output += stats

        print(output)

        if entry.is_dir():
            recDirLister(currentEntryFullDir, level + 1)


if __name__ == "__main__":
    recDirLister('./test_case')
