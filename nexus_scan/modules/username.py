import requests
from typing import Dict, Optional

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Twitch": "https://m.twitch.tv/{}",
    "Pinterest": "https://pinterest.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
}

def check_single_site(username: str, site_name: str, url_template: str) -> Optional[str]:
    """
    Checks if a username exists on a specific site.
    Returns the profile URL if found, None if not found, or an error message.
    """
    url = url_template.format(username)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return url
        elif response.status_code == 404:
            return None
        else:
            return f"Error: {response.status_code}"
    except requests.RequestException:
        return "Error: Connection failed"

def check_username(username: str) -> Dict[str, Optional[str]]:
    """
    Checks for the existence of a username across all configured platforms.
    """
    results = {}
    for site, url_template in SITES.items():
        results[site] = check_single_site(username, site, url_template)
    return results
