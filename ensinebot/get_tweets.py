import twitter
from pathlib import Path

def get_search_terms():
    path = Path("keywords.txt")
    if not path.exists():
        return false

    with open(path) as f:
        method = None
        words = "q="
        for l in f.readlines():
            l = l.strip()
            if method is None:
                method = l
                continue
            elif l == "---":
                if method == "ALL":
                    words += "("
                elif method == "ANY":
                    words = words.rstrip("%20OR%20")
                    words += ")"
                method = None
                continue

            if method == "ALL":
                words += l + "%20"
            elif method == "ANY":
                words += l + "%20OR%20"
            elif method == "NONE":
                words += "-" + l + "%20"

    words = words.rstrip("%20")
    print(words)
    return words

def get_tweets(api):
    rq = get_search_terms()
    rq += "&f=live"
    search = api.GetSearch(raw_query=rq)
    print(search)
