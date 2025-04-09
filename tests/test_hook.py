"""
file: test_hook.py
Author: 城下秋草
Desc: hook demo 测试脚本
"""
import pytest


@pytest.fixture
def stu_data(request):
    return request.param

def test_stu(stu_data):
    print(f"{stu_data[0]}'s age is {stu_data[1]}",end=" ")
    assert True

@pytest.mark.parametrize("param",["小赵",22,("小李", 24)])
def test_user_view(param):
    print(param, end=" ")
    # assert type(param) is not tuple

@pytest.mark.legacy
def test_old_version():
    assert 1