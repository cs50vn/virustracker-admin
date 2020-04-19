import sys, os, shutil, subprocess, time, json

# Build tool
hostType = ""
projectId = ""
firebaseToken = ""
siteName = ""

# Project config
rootDir = ""
scriptDir = ""
genDir = ""
srcDir = ""
templateDir = ""

# App config
outputFile = "virustracker-admin"
versionCode = "1.0.0"
internalVersionCode = "1.0.0"
versionName = "v" + versionCode


def buildProjectPath(rootPath, id, token, name):
    global rootDir
    rootDir = rootPath
    global projectId
    projectId = id
    global firebaseToken
    firebaseToken = token
    global siteName
    siteName = name

    global scriptDir
    scriptDir = rootDir + os.sep + "scripts"
    global genDir
    genDir = rootDir + os.sep + "_generated"
    global srcDir
    srcDir = rootDir + os.sep + "vue"
    global templateDir
    templateDir = rootDir + os.sep + "templates"    

    print("\033[1;34;40mLoad project config\033[0;37;40m")
    print("Root dir: 		\033[1;34;40m%s\033[0;37;40m" % rootDir)
    print("Script dir:		\033[1;34;40m%s\033[0;37;40m" % scriptDir)
    print("Genrerated dir: 	\033[1;34;40m%s\033[0;37;40m" % genDir)
    print("Source dir: 	    \033[1;34;40m%s\033[0;37;40m" % srcDir)
    print("Templates dir: 	    \033[1;34;40m%s\033[0;37;40m" % templateDir)
    print("\n")

def deployProgram():
    print("===========================================================")
    print("                      \033[1;32;40mDEPLOY ADMIN TO FIREBASE HOSTING\033[0;37;40m")
    print("===========================================================")

    specificGenName = "%s-%s_%s" % (outputFile, versionName, internalVersionCode)

    #Generate firebase.json
    f = open(templateDir + os.sep + "firebase.json", "r")
    s = f.read()
    s = s % dict(target_site=siteName)

    data = json.loads(s)
    #Write to gen data dir
    desFile = genDir + os.sep + versionName + os.sep + specificGenName + os.sep + "firebase.json"
    #f = open(desFile, "w+")
    #f.write(s + "\n")

    
    with open(desFile, 'w') as json_file:
        json.dump(data, json_file)

    print(s)
    #Deploy

    os.chdir(genDir + os.sep + versionName + os.sep + specificGenName)

    cmd = "firebase --project %s target:apply hosting %s %s" % (projectId, siteName, siteName)
    subprocess.call(cmd, shell=True)
    print(cmd)

    cmd = "firebase --project %s --token %s deploy" % (projectId, firebaseToken)
    print(cmd)
    subprocess.call(cmd, shell=True)

    os.chdir(rootDir)


def main(argv):
    start = time.time()
    print("===========================================================")
    print("                      \033[1;32;40mBUILD APPLICATION\033[0;37;40m")
    print("===========================================================")

    print(str(argv))
    buildProjectPath(argv[0], argv[1], argv[2], argv[3])

    deployProgram()

    elapsedTime = time.time() - start
    print("Running time: %s s" % str(elapsedTime))


if __name__ == '__main__':
    main(sys.argv[1:])
