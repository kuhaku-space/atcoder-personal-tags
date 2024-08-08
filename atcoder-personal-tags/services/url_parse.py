import urllib.parse


def get_contest_id_from_problem_url(problem_url: str | None) -> str | None:
    if not problem_url:
        return None
    parsed_url = urllib.parse.urlparse(problem_url)
    if not parsed_url:
        return None
    if parsed_url.scheme != "https" or parsed_url.netloc != "atcoder.jp":
        return None
    li = parsed_url.path.split("/")
    if len(li) != 5:
        return None
    if li[0] != "" or li[1] != "contests" or li[3] != "tasks":
        return None
    return li[2]


def get_problem_id_from_problem_url(problem_url: str | None) -> str | None:
    if not problem_url:
        return None
    parsed_url = urllib.parse.urlparse(problem_url)
    if not parsed_url:
        return None
    if parsed_url.scheme != "https" or parsed_url.netloc != "atcoder.jp":
        return None
    li = parsed_url.path.split("/")
    if len(li) != 5:
        return None
    if li[0] != "" or li[1] != "contests" or li[3] != "tasks":
        return None
    return li[4]
