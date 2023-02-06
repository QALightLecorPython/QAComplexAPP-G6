from time import sleep

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestChat:
    """Stores tests for chat base functionality"""

    def test_self_messages(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Open chat
            - Send message
            - Verify that message appears
            - Send one more message
            - Verify that both message displayed
        """
        # Open chat
        hello_page.header.open_chat()

        expected_messages = []

        # Send message
        for index in range(20):
            message = f"Hello{index}"

            # Send message
            expected_messages.append(message)
            hello_page.chat.send_message(text=message)

            # Verify that message appears
            hello_page.chat.verify_messages(expected_messages)

        sleep(5)
