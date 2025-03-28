import time
from win10toast import ToastNotifier
toast=ToastNotifier()
while True:
 time.sleep(10)
 toast.show_toast(
     "PANI PILO",
     "Sale 1 hour hogay hai pani tera baap piye ga",
     duration=10,
     icon_path="icon.ico",
     threaded=True
 )