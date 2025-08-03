"""START

IMPORT wikipedia module
IMPORT DisambiguationError, PageError exceptions from wikipedia.exceptions

DEFINE FUNCTION main():
    PRINT "Enter page title (blank to quit):"

    LOOP infinitely:
        PROMPT user to input "Enter page title: "
        SET query = user input trimmed of whitespace

        IF query IS empty THEN
            PRINT "Thank you."
            EXIT LOOP

        TRY:
            CALL wikipedia.page with parameters:
                title = query
                auto_suggest = True  # enables suggestions but may alter results

            SET page to returned Wikipedia page object

        EXCEPT DisambiguationError AS e:
            PRINT "We need a more specific title. Try one of the following, or a new search:"
            PRINT first 10 elements of e.options list  # show up to 10 possible titles

        EXCEPT PageError:
            PRINT "Page id \"" + query + "\" does not match any pages. Try another id!"

        EXCEPT Any Other Exception AS e:
            PRINT "An unexpected error occurred: " + string representation of e

        ELSE:  # If no exceptions occurred
            PRINT a newline and "Title: " concatenated with page.title

            SET summary_excerpt = page.summary

            IF length of summary_excerpt > 500 THEN
                SET summary_excerpt = first 500 characters of summary_excerpt plus "..."

            PRINT "Summary:\n" concatenated with summary_excerpt
            PRINT "URL: " concatenated with page.url and a newline

IF the program is executed as main:
    CALL main()

END
"""

"""
wiki.py
Use the wikipedia Python library to query Wikipedia pages interactively.

- Prompts user for page titles/search queries.
- Handles disambiguation and page not found exceptions.
- Prints page title, summary, and URL.
- Loop continues until blank input is given.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    print("Enter page title (blank to quit):")
    while True:
        query = input("Enter page title: ").strip()

        if not query:
            print("Thank you.")
            break

        try:
            # By default autosuggest helps but can cause unexpected suggestions
            # Using autosuggest=True here; adjust if needed.
            page = wikipedia.page(query, auto_suggest=True)

        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            # Show up to 10 options to avoid overwhelming output
            print(e.options[:10])

        except PageError:
            print(f'Page id "{query}" does not match any pages. Try another id!')

        except Exception as e:
            # Catch any other unexpected exceptions gracefully
            print(f"An unexpected error occurred: {e}")

        else:
            # Successfully retrieved a page; print details.
            print(f"\nTitle: {page.title}")
            # Print only first 500 characters of the summary for readability
            summary_excerpt = page.summary
            if len(summary_excerpt) > 500:
                summary_excerpt = summary_excerpt[:500].rstrip() + "..."
            print(f"Summary:\n{summary_excerpt}")
            print(f"URL: {page.url}\n")

if __name__ == "__main__":
    main()
