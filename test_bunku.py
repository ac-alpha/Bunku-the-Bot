from zulip_bots.test_lib import BotTestCase, DefaultTests

from zulip_bots.bots.bunku import utils

class TestBunkuBot(BotTestCase, DefaultTests):
    bot_name = "bunku"

    def test_bot(self) -> None:
        dialog = [
        ]
        self.verify_dialog(dialog)
