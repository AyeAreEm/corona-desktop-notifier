from win10toast import ToastNotifier
import time
import requests

toaster = ToastNotifier()

try:
    data = requests.get("https://api.covid19api.com/summary")

except:
    toaster.show_toast("No Internet", "You do not have internet, please connect to the internet and try again.")

if data is not None:
    getData = data.json()
    covid = getData["Global"]
    title = "Covid-19 Globally"
    message = "There are {} confirmed, {} deaths and {} recovered.".format(covid["TotalConfirmed"], covid["TotalDeaths"], covid["TotalRecovered"])

    toaster.show_toast(title, message, icon_path="covid_fVi_icon.ico", duration=20)
