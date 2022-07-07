from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  text         = request.values.get("text", "default")

  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON What would you want to check about Muchira Junior  \n"
      response += "1. My Profile \n"
      response += "2. My phone number"

  elif text    == '1':
      # Business logic for first level response
      response  = "CON Choose profile information you want to view \n"
      response += "1. Web profile \n"
      response += "2. Github profile"

  elif text   == '2':
      # This is a terminal request. Note how we start the response with END
      response = "END My phone number is " + "+254 771 571087.  \n Thank You."
  elif text          == '1*1':
      # This is a second level response where the user selected 1 in the first instance
      webprofile  = "http://muchirajunior.netlify.app/"
      # This is a terminal request. Note how we start the response with END
      response       = "END Visit " + webprofile + " to get my web portifolio. \n Thank You."
  elif text  == "1*2":
      githubProfile="https://github.com/muchirajunior"
      response  = "END Visit " + githubProfile + " to get my GitHub profile. \n Thank You."


  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response
