import unittest
import app


def add_2_5():
    assert app.TestBase.add(2,5)==7


if __name__=='__main__':
    add_2_5()

