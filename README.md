# iCloud Photo Sharing Downloader (on non Apple Ecosystem)


## Tested on

Windows with python 3.12, with firefox latest


## Prereq

This application uses Firefox as their webdriver. Make sure to install firefox first.
And also Python 3.12.X


## How to run

```
pip install requirements.txt
```

Please open the `main.py` file, then edit the line:
```python
driver.get("INSERT LINK DIRECT TO PHOTOS HERE")
```

insert link that will direct to the first image in the gallery (because this scripts run automatically to the next picture by invoking `send.keys()`)

After save, close the file and run
```
python main.py
```

Now, the quirks of iCloud Photo Sharing on Browser is that it will auto hide the header that have button "Download". This can cause element stale error. So what to do?

Solution: During the lenghty process of the download, you have to manually hover and shake the mouse in the browser window, just to keep the header Download button visible.


## Improvement

Several improvement can be made that can use Selenium `actionchains` to simulate movement of the cursor. But frankly, this code only runs once on my lifetime, and I'm open for contribution to add such functionality, or other functionality deems improvement.

Thank you.


## Donate on Ko-Fi: https://ko-fi.com/haiziizzudin

Thank you from the bottom of my heart 💓