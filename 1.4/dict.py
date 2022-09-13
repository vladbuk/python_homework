dict = { 
    "hdd": "1Tb",
    "cpu": "Intel",
    "ram": "8Gb"
}

print(dict)
print(dict["hdd"])

dict["hdd"] = "4Tb"
print(dict["hdd"])

dict["mb"] = "Asus"
dict.pop("cpu")
print(dict)

for key in dict.keys():
    print(key)

for key in dict.values():
    print(key)