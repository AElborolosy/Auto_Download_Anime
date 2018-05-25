"""
Input: Name of Anime
Connects to the xdcc.horriblesubs.info site and queries the packlist for the pack number of the desired Anime.
Return: List of strings containing messages to enter in Horriblesubs channel of Hexchat.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd


# Given the Horrible Subs search result, return a list of messages to send a bot.
def generate_message_list(search_result):

    packlist_df = pd.DataFrame(search_result, columns=['Anime'])
    packlist_df = pd.DataFrame(packlist_df.Anime.str.split(' ', 3).tolist(),
                               columns=['Bot', 'Pack', 'Size', 'Filename'])

    # Minimize selection to just one bot. Defaults to the first bot in the search results.
    first_bot = packlist_df.loc[0, 'Bot']
    one_bot = packlist_df.loc[packlist_df['Bot'] == first_bot]

    msg_list = []
    for row in range(one_bot.shape[0]):
        message = "\n{F}\t/msg {bot} xdcc send #{pack}".format(F=packlist_df.loc[row, 'Filename'],
                                                        bot=packlist_df.loc[row, 'Bot'],
                                                        pack=packlist_df.loc[row, 'Pack'])
        msg_list.append(message)
    return msg_list


# Given the name of an anime (string), searches the pack list for it.
def query_horrible_subs(anime):

    driver = webdriver.Chrome()
    driver.get('http://xdcc.horriblesubs.info')

    # Search the packlist for the desired anime. Wait for results to load.
    search_bar = driver.find_element_by_name('search')
    search_bar.send_keys(anime)
    search_bar.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'anime1')))

    # Store results in a list, remove the header (index 0).
    episodes = driver.find_elements_by_css_selector('tr')
    episode_list = []
    for episode in episodes:
        episode_list.append(episode.text)
    episode_list.pop(0)

    # Quit the driver and return the episode list.
    driver.quit()
    return episode_list


def main(show):

    packlist = query_horrible_subs(anime=show)
    message_list = generate_message_list(packlist)
    return message_list


if __name__ == '__main__':
    main('Toji')
