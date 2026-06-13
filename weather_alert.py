import requests

API_KEY = "ae54c8ea9a9d7219f5becd718fb6a65f"
CITY = "Thiruvananthapuram"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    data = response.json()

    if response.status_code == 200 and "main" in data:

        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print("\nWeather Alert System")
        print("--------------------")
        print("City:", CITY)
        print("Temperature:", temperature, "°C")
        print("Condition:", condition)

        if temperature > 35:
            print("\nALERT: High Temperature Detected!")
            print("Alert email sent")

        elif "rain" in condition.lower():
            print("\nALERT: Rain Expected!")
            print("Alert email sent")

        else:
            print("\nWeather is normal")

    else:
        print("\nAPI Error:")
        print(data)

except Exception as e:
    print("Error:", e)