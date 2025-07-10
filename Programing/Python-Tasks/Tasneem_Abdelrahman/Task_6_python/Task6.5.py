languages={
    "one":{
    "name":"Html","progress":"90%"}, 
    "two":{ 
"name":"Css","progress":"80%"}, 
"three":{
"name":"python","progress":"30%"}, 
"four":{
"name":"AI","progress":"20%"
}
} 
print(f"{languages["one"]["name"]} progress is {languages["one"]["progress"]}")
print(f"{languages["two"]["name"]} progress is {languages["two"]["progress"]}")
print(f"{languages["three"]["name"]} progress is {languages["three"]["progress"]}")
print(f"{languages["four"]["name"]} progress is {languages["four"]["progress"]}")
languages.update({"five":{"name": "c++","progress": "50%"}}) 
print(f"{languages["five"]["name"]} progress is {languages["five"]["progress"]}")