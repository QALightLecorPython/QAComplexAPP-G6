from constants.post_page import PostPageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class PostPage(BasePage):
    """Stores methods describes post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = PostPageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def verify_post_created(self):
        """Verify post creation message"""
        assert self.compare_element_text(xpath=self.const.POST_CREATED_MESSAGE_XPATH,
                                         text=self.const.POST_CREATED_MESSAGE_TEXT)
