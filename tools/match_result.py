import requests
from bs4 import BeautifulSoup

# Declare constants
URL = "https://www.mackolik.com/mac/fenerbah%C3%A7e-vs-us-gilloise/dw542vmlld15tysxsc0r7s74k"
#URL = "https://www.mackolik.com/mac/grom-nowy-staw-vs-lks-lodz/acka1s4menhmohgcy442wo1lg"
# Fenerbahce vs Us Gilloise match score (Fenerbahce Home, Us Gilloise Away)

# Home score <span class="p0c-soccer-match-details-header__score-home">0</span>
# Away score <span class="p0c-soccer-match-details-header__score-away">0</span>

def get_match_result() -> str:
    """
    Get the current match result for Fenerbahce vs Us Gilloise

    Returns:
        str: The current match result or a message if the match hasn't started
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the score elements
        home_score = soup.find('span', class_='p0c-soccer-match-details-header__score-home')
        away_score = soup.find('span', class_='p0c-soccer-match-details-header__score-away')
        
        if home_score and away_score:
            return f"Fenerbahce {home_score.text} - {away_score.text} Us Gilloise"
        else:
            return "The match hasn't started yet or the score is not available."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"
