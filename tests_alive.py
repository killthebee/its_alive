from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com') == {'status': 'up'}


def test_down():
    assert not is_alive_host('invalid.domain.son') == {'status': 'down'}


def test_connection():
    assert not is_alive_host('semrush55555555555555555555.com') == {'status': 'down'}
