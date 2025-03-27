from seleniumbase import SB
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class GoogleMeetConnector:

    def join_google_meet(self, meet_url: str, user_name: str, callback=None):
        logging.info(f"Joining Google Meet with url: {meet_url}, user: {user_name}")
        try:
            with SB(uc=True, locale="tr-TR", headless=True) as sb:
                logging.info("SeleniumBase SB instance created")
                sb.open(meet_url)
                logging.info(f"Opened meet url: {meet_url}")
                sb.click("//span[contains(text(),'Mikrofon ve kamera olmadan devam et')]")
                logging.info("Clicked 'Continue without microphone and camera'")
                sb.type("//input[@placeholder='Adınız']", user_name)
                logging.info(f"Typed username: {user_name}")
                sb.click("//span[contains(text(),'Katılma isteği')]")
                logging.info("Clicked 'Request to join'")
                sb.wait_for_element("//div[contains(text(),'Bu toplantıda kimse yok')]", timeout=5000)
                logging.info("Successfully joined Google Meet")
                if callback:
                    callback()
        except Exception as e:
            logging.error(f"Google connection error: {type(e).__name__} - {e}")
