import requests



API_KEY="788bba7e8d47a6dcbe49013b00042632"

"""Data is 3 hourly for 5 days to calculate forecast for 2 days it means we need to search 8 data points
 for a day and for two days it will be 16"""


def get_data(place,forcast_days=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forcast_days
    filtered_data=filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Pune",forcast_days=3))
