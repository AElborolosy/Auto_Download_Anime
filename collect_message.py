"""
Connects to the xddc.horriblesubs.info site and queries the packlist for the pack number of the desired Anime.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():

    driver = webdriver.Chrome()
    driver.get('http://xdcc.horriblesubs.info')
    search_bar = driver.find_element_by_name('search')
    search_bar.send_keys('Toji')
    search_bar.send_keys(Keys.ENTER)

    episodes = driver.find_elements_by_class_name('anime0')
    print(episodes)

    driver.quit()
    return


if __name__ == '__main__':
    main()