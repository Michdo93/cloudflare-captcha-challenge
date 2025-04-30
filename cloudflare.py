import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

# Konfiguration der Chrome-Optionen
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Falls du den Browser ohne GUI nutzen möchtest
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Verstecke Webdriver-Erkennung

# Initialisiere den undetected-chromedriver
driver = uc.Chrome(options=chrome_options)

# Navigiere zur Seite mit der Cloudflare Challenge
driver.get("https://www.scrapingcourse.com/cloudflare-challenge")

# Warte, bis die Seite vollständig geladen ist
time.sleep(5)

# Definition des Pfades zum Screenshot der Captcha-Checkbox
captcha_image_path = 'captcha_checkbox.png'  # Pfad zu deinem Screenshot
ACCURACY = 0.8  # Die Genauigkeit für das Finden des Bildes (zwischen 0 und 1)

# Start der While-Schleife zur Bildsuche und Klicken auf die Captcha-Checkbox
toPressButton = None
timeout = time.time()  # Speichere die Startzeit

while toPressButton is None:
    if time.time() > timeout + 30:  # Timeout nach 30 Sekunden
        print("Timeout erreicht, Captcha nicht gefunden.")
        break

    try:
        # Suche nach dem Captcha-Bild auf dem Bildschirm
        toPressButton = pyautogui.locateOnScreen(captcha_image_path, confidence=ACCURACY)

        if toPressButton is not None:
            print(f"Captcha gefunden an Position: {toPressButton}")
            # Klicke auf die gefundene Position
            pyautogui.click(toPressButton)
            print("Captcha-Checkbox wurde angeklickt!")
            break
    except Exception as e:
        print(f"Fehler beim Suchen des Captchas: {e}")
        time.sleep(1)  # Warte 1 Sekunde, bevor erneut gesucht wird

# Warte, damit Cloudflare das Captcha verarbeitet
time.sleep(20)

# Optional: Überprüfe, ob die Seite weitergeladen wurde (indem du den Seitentitel prüfst)
print(f"Seitentitel nach dem Laden: {driver.title}")

# Nimm einen Screenshot der Seite
driver.save_screenshot("cloudflare-challenge.png")

# Schließe den Browser
driver.quit()
