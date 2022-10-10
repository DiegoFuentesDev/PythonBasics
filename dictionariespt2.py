from distutils.file_util import move_file

action = {
    "name" : "The Godfather",
    "released" : 1972
}

kids = {
    "name" : "Finding Nemo",
    "released" : 2003
}
movies = {
    "Kids" : kids,
    "Action" : action
}

series = dict(name="Big Bang Theory", bestCharacter="Shedon Cooper")

print("Movies:",movies)
print("Series:",series)