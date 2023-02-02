class ProfilePageConsts:
    USERNAME_XPATH = ".//h2"
    FOLLOW_BUTTON_XPATH = ".//button[contains(text(), 'Follow')]"
    FOLLOWING_TAB_XPATH = ".//a[@href='/profile/{user}/following']"
    FOLLOWING_TAB_TEXT = "Following: {count}"
