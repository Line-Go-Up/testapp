import main
import time

def test_main():
    x = main.main()
    time.sleep(600)
    assert x == 'hello world'
