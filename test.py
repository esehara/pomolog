import pytest
import pomolog.lib

#Config Fileを呼び出す
def test_configure():
    conf = pomolog.lib.load_configure('sample/config.yaml')
    print(conf)
    assert conf['default']['min'] == 30
    assert conf['default']['rest'] == 5
    assert conf['log'] == 'pomolog.txt'
    assert conf['pre_command']['start'] == 'echo "start"'

#30分たったかどうかを調べる関数を作成する
def test_30min_test():
    import time
    test_class = pomolog.lib.pomotimer(time.mktime((2000,12,29,11,00,00,00,00,00)),30,'test.path')
    assert not test_class.is_done_time(time.mktime((2000,12,29,11,15,00,00,00,00)))
    assert test_class.is_done_time(time.mktime((2000,12,29,11,31,00,00,00,00)))
