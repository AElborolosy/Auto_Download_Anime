"""
Input: Text file, each line is a string containing the name of an anime
Output: List of messages to send in Horriblesubs to download an update
"""


# Import collect message script.
import collect_message as cm


def main():
    # Collect list of animes.
    file_path = 'data//anime_list.txt'
    file = open(file_path, 'rU')
    anime_list = [x for x in str(file.read()).split('\n')]
    file.close()

    # Print the updates for each anime.
    for anime in anime_list:
        episode_list = cm.main(anime)
        print("\n%s:%s" %(anime, episode_list[-1]))
    return


if __name__ == '__main__':
    main()
