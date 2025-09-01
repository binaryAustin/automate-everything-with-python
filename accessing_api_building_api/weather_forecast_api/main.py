import os
import csv
from datetime import datetime, timezone
from dotenv import load_dotenv
import requests

load_dotenv(".env")

api_key = os.getenv("OPENWEATHER_API_KEY")


def main():
    city_name = "Hanoi"
    country_code = "VN"

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&units=metric&appid={api_key}"

    res = requests.get(url, timeout=10.0)
    body = res.json()

    forecasts = body["list"]

    with open("weather_forecast_api/hanoi.csv", mode="w", encoding="utf-8") as fw:
        csv_writer = csv.writer(fw)
        csv_writer.writerow(["time", "temperature", "condition"])

        for forecast in forecasts:
            dt_str = (
                datetime.fromtimestamp(float(forecast["dt"]), tz=timezone.utc)
                .isoformat(timespec="seconds")
                .replace("+00:00", "Z")
            )
            csv_writer.writerow(
                [
                    dt_str,
                    forecast["main"]["temp"],
                    forecast["weather"][0]["description"],
                ]
            )


if __name__ == "__main__":
    main()
