import main
import time

def test_main():
    x = main.main()
    time.sleep(5)
    assert x == 'hello world'
