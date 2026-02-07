import requests

def get_ip_info(ip: str) -> dict:
    """
    Fetches IP information from ip-api.com.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"status": "fail", "message": str(e)}
