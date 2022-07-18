from requests import get,post
res=post("http://localhost:5000",data="1")
print(res.text)
