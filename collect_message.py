"""
Connects to the xdcc.horriblesubs.info site and queries the packlist for the pack number of the desired Anime.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Given the name of an anime (string), searches the pack list for it.
def query_horrible_subs(anime):

    driver = webdriver.Chrome()
    driver.get('http://xdcc.horriblesubs.info')

    search_bar = driver.find_element_by_name('search')
    search_bar.send_keys(anime)
    search_bar.send_keys(Keys.ENTER)

    # episodes = driver.find_elements_by_tag_name('tr')
    episodes = driver.find_elements_by_id('name')
    for episode in episodes:
        print(episode.text)

    driver.close()
    driver.quit()
    return


def main():

    query_horrible_subs('Toji')

    return


if __name__ == '__main__':
    main()
