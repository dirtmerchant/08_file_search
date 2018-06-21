import glob
import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print_header("We can't search for nothing!")
        return

    search_folders(folder, text)


def print_header():
    print('------------------')
    print('  File Search App')
    print('------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search?')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for? [Single phrases only]?")
    return text


def search_folders(folder, text):
    # items = os.listdir(folder)
    items = glob.glob(os.path.join(folder, '*'))
    for item in items:
        if os.path.isdir(item):
            continue


if __name__ == '__main__':
    main()
