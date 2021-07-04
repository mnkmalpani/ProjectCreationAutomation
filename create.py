import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
access_token = os.getenv("ACCESS_TOKEN")

print("path to create the project is: ", path)

if path is None:
	print("please give the right path name")
	sys.exit(1)

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    if os.path.exists(path + str(folderName)):
        os.makedirs(path + str(folderName) + "/src")
        os.makedirs(path + str(folderName) + "/bin")
        os.makedirs(path + str(folderName) + "/test")
        with open("requirements.txt", "w") as fp:
            pass
        with open("MakeFile", "w") as fp:
            pass
    user = Github(access_token).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
