import requests


def get_wikipedia_page(title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts|info",
        "exintro": True,
        "inprop": "url",
        "redirects": 1
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'error' in data:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    else:
        pages = data['query']['pages']
        for page_id, page in pages.items():
            if 'extract' in page:
                print(f'{page["title"]}\n{page["extract"]}\n{page["fullurl"]}')
            elif 'missing' in page:
                print(f'Page id "{title}" does not match any pages. Try another id!')
            else:
                print(
                    f'We need a more specific title. Try one of the following, or a new search:\n{list(pages.keys())}')


def main():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        get_wikipedia_page(title)


if __name__ == "__main__":
    main()