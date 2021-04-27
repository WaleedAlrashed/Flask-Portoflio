import requests
import json


if __name__ == '__main__':
    url = 'https://www.unisita.com/api/v1/register'
    data = {
	"name": "postman1",
	"phone_number": "949980284",
    "email" : "test12454545@gmail.com",
    "gender": "f",
    "birth_date":"2013/04/01",
	"password": "123456",
	"password_confirmation": "123456",
	"fcm_token": "cY4ODc3dWSQ:APA91bGwqKD2Nsi63zttB7HomHDXyPRuId0CMcCx0UZR0ciYBfiE1LCj3v3eTCIdqzsVWu_iGvBmvnsqXDN-NB4F4jZwEZGooZ4fVlP3sYecYD-R4mNm1wt6I7yZ1sqaCHUpCK-0y3PH"}
    
    headers = {
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest"
  }
    response = requests.post(url,data=data,headers = headers)
    print(response.content)