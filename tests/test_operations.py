### importing from src folder 
from src.math_operations import add,sub 


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(-1,2)==1
    assert add(100,1000 )==1100

def test_sub():
    assert sub(5,3)==2
    assert sub(-10,10)==-20
    assert sub(5,2)==3
    assert sub(100,200)==-100