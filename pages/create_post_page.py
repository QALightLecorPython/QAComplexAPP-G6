from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class CreatePostPage(BasePage):
    """Stores methods describes create post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CreatePostPageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.const.TITLE_INPUT_XPATH, value=post.title)
        self.fill_field(xpath=self.const.BODY_AREA_XPATH, value=post.body)

        self.click(xpath=self.const.SAVE_POST_BUTTON_XPATH)

        from pages.post_page import PostPage
        return PostPage(self.driver)
