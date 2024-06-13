import pytest
from xontrib_chatgpt.chatmanager import ChatManager

from xontrib_chatgpt.events import (
    add_events,
    rm_events,
)


def test_add_and_rm_events(xession):
    cm = ChatManager()
    add_events(xession, cm)
    events = xession.builtins.events

    assert events.exists("on_chat_create")
    assert events.exists("on_chat_destroy")
    assert events.exists("on_chat_used")

    rm_events(xession)

    assert not events.exists("on_chat_create")
    assert not events.exists("on_chat_destroy")
    assert not events.exists("on_chat_used")
