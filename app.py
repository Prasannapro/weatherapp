from flask import Flask,render_template,request
import requests
import json

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        print("hii")
        location=request.form['location']
        print(location)
        api="6f5f05a0291976543db63f26234bd0a8"
        # api_key: 6f5f05a0291976543db63f26234bd0a8
        weather_url=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}&units=metric')

    #     weather_data=weather_url.json()
    #     print(weather_data)

    #     temp=weather_data['main']['temp']
    #     # weather=weather_data['weather']['description']

    #     return render_template("result.html",temp=temp,location=location)
    # return render_template("index.html")
      if(weather_data["cod"] == "404"):
            return render_template("error.html")
        else:
            temp=weather_data['main']['temp']
            weather=weather_data['weather'][0]['description']

            return render_template("result.html",temp=temp,location=location,weather=weather)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
           
