import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)


from mock import patch
from core.notify import Notify


def test_doNotify():

    with patch.object(Notify, 'doNotify', return_value=None) as mock_doNotify:
        Notify().doNotify("test_title", "test_message", "test_appname", "test_icon")

    mock_doNotify.assert_called_once_with("test_title", "test_message", "test_appname", "test_icon")


