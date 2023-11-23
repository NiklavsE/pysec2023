import urllib.request
import os
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    def updateOnProgress(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

# Example usage:
url         = 'https://http.cat/images/102.jpg'
destination = 'test.png'

with DownloadProgressBar(unit='B', unit_scale=True,
                            miniters=1, desc=url.split('/')[-1]) as downloadProgressBar:
    urllib.request.urlretrieve(url, filename=destination, reporthook=downloadProgressBar.updateOnProgress)
