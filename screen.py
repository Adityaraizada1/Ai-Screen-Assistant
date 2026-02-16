import mss

def take_screenshot(path="screen.png"):
    with mss.mss() as sct:
        sct.shot(output=path)
    return path
