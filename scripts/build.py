import sys, os, shutil, subprocess, time

# Build tool
hostType = ""
buildType = ""

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


def buildProjectPath(rootPath, host, build):
    global rootDir
    rootDir = rootPath
    global hostType
    hostType = host
    global buildType
    buildType = build

    global scriptDir
    scriptDir = rootDir + os.sep + "scripts"
    global genDir
    genDir = rootDir + os.sep + "_generated"
    global srcDir
    srcDir = rootDir + os.sep + "vue"
    global templateDir
    templateDir = rootDir + os.sep + "templates"

    print("\033[1;34;40mLoad build config\033[0;37;40m")
    print("Host: \033[1;32;40m%s\033[0;37;40m" % hostType)
    print("Build Type: \033[1;32;40m%s\033[0;37;40m" % buildType)
    print("Version: \033[1;32;40m%s\033[0;37;40m\n" % versionName)

    print("\033[1;34;40mLoad project config\033[0;37;40m")
    print("Root dir: 		\033[1;34;40m%s\033[0;37;40m" % rootDir)
    print("Script dir:		\033[1;34;40m%s\033[0;37;40m" % scriptDir)
    print("Genrerated dir: 	\033[1;34;40m%s\033[0;37;40m" % genDir)
    print("Source dir: 	    \033[1;34;40m%s\033[0;37;40m" % srcDir)
    print("Templates dir: 	    \033[1;34;40m%s\033[0;37;40m" % templateDir)
    print("\n")

def buildProgram():
    print("===========================================================")
    print("                      \033[1;32;40mBUILD GO\033[0;37;40m")
    print("===========================================================")

    os.chdir(srcDir)

    cmd = "npm run build"
    print(cmd)
    subprocess.call(cmd, shell=True)

    os.chdir(rootDir)

def buildPackage():
    print("===========================================================")
    print("                      \033[1;32;40mBUILD PACKAGE\033[0;37;40m")
    print("===========================================================")

    specificGenName = "%s-%s_%s" % (
    outputFile, versionName, internalVersionCode)
    src = srcDir + os.sep + "dist"
    des = genDir + os.sep + versionName + os.sep + specificGenName

    print("\033[1;34;40mFrom:\n\033[0;37;40m" + src)
    print("\033[1;34;40mTo\n\033[0;37;40m" + (des + os.sep + "public"))

    if os.path.exists(des):
        shutil.rmtree(des)
    shutil.move(src, (des + os.sep + "public"))

    #src = templateDir + os.sep + "firebase.json"
    #des = genDir + os.sep + versionName + os.sep + "public"
    #shutil.copy(src, des)

    #cmd = "7z a %s.zip %s" % (des, des)
    #subprocess.call(cmd, shell=True)

    print("\n")


def main(argv):
    start = time.time()
    print("===========================================================")
    print("                      \033[1;32;40mBUILD APPLICATION\033[0;37;40m")
    print("===========================================================")

    print(str(argv))
    buildProjectPath(argv[0], argv[1], argv[2])

    buildProgram()

    buildPackage()

    elapsedTime = time.time() - start
    print("Running time: %s s" % str(elapsedTime))


if __name__ == '__main__':
    main(sys.argv[1:])
