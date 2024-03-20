import os
import time

def cıkıs():
    print("""
------------------------------------------------------------------------------------------------------------------------
|                                                    SEE YOU LATER                                                     |        
------------------------------------------------------------------------------------------------------------------------
          """)
    time.sleep(2)
    exit()





def Main():
    os.system("cls")
    os.system("color 6")
    print("""
------------------------------------------------------------------------------------------------------------------------
|                                                    Mirlex - Installer                                                |        
------------------------------------------------------------------------------------------------------------------------
[0]- 7-Zip                                  [17]- Only Office                        [34]- Python 3.11
[1]- Adobe Acrobat Reader                   [18]- LibreOffice                        [35]- Skype
[2]- Adobe Photoshop                        [19]- Krita                              [36]- Slack
[3]- Audacity                               [20]- Malwarebytes                       [37]- Opera
[4]- BCU Uninstaller                        [21]- Microsoft Edge                     [38]- Oracle Virtualbox
[5]- Blender                                [22]- Microsoft Excel                    [39]- ProtonVPN
[6]- BleachBit                              [23]- Microsoft Office                   [40]- TeamSpeak3
[7]- Brave                                  [24]- OBS Studio                         [41]- TeamViewer
[8]- Discord                                [25]- Microsoft Teams                    [42]- VLC Media Player
[9]- Everything (File Search)               [26]- Microsoft Word                     [43]- Visual Studio Code
[10]- Evernote                              [27]- Notepad++                          [44]- WhatsApp
[11]- Firefox                               [28]- Notion                             [45]- Wireshark
[12]- GIMP                                  [29]- Opera GX                           [46]- WinRAR
[13]- Epic Games Launcher                   [30]- Rufus                              [47]- Powertoys
[14]- Google Chrome                         [31]- Revo Uninstaller                   [48]- Anydesk
[15]- Bandicam                              [32]- Spotify                            [49]- Zoom
[16]- HWMonitor                             [33]- Steam                              [50]- Librewolf                           
------------------------------------------------------------------------------------------------------------------------
[99]-EXIT                                                                                                              |                                                
------------------------------------------------------------------------------------------------------------------------
      """)



indirilecekler = {
    "0": "7zip",
    "1": "AdobeReader",
    "2": "Adobe.Photoshop",
    "3": "audacity",
    "4": "-e --id Klocman.BulkCrapUninstaller",
    "5": "Blender",
    "6": "-e --id BleachBit.BleachBit",
    "7": "BraveBrowser",
    "8": "Discord",
    "9": "-e --id voidtools.Everything",
    "10": "Evernote",
    "11": "Mozilla.Firefox",
    "12": "GIMP",
    "13": "-e --id EpicGames.EpicGamesLauncher",
    "14": "Google.Chrome",
    "15": "-e --id BandicamCompany.Bandicam",
    "16": "-e --id CPUID.HWMonitor",
    "17": "-e --id ONLYOFFICE.DesktopEditors",
    "18": "LibreOffice",
    "19": "-e --id KDE.Krita",
    "20": "Malwarebytes",
    "21": "Microsoft.Edge",
    "22": "Microsoft.Excel",
    "23": "Microsoft.Office",
    "24": "OBS.Studio",
    "25": "Microsoft.Teams",
    "26": "Microsoft.Word",
    "27": "Notepad++",
    "28": "Notion",
    "29": "-e --id Opera.OperaGX",
    "30": "-e --id Rufus.Rufus",
    "31": "-e --id RevoUninstaller.RevoUninstaller",
    "32": "spotify",
    "33": "Steam",
    "34": "-e --id Python.Python.3.11",
    "35": "Skype",
    "36": "Slack",
    "37": "-e --id Opera.Opera",
    "38": "-e --id Oracle.VirtualBox",
    "39": "-e --id ProtonTechnologies.ProtonVPN",
    "40": "-e --id TeamSpeakSystems.TeamSpeakClient",
    "41": "TeamViewer",
    "42": "VLC",
    "43": "VisualStudioCode",
    "44": "WhatsApp",
    "45": "Wireshark",
    "46": "WinRAR",
    "47": "-e --id Microsoft.PowerToys",
    "48": "WinSCP",
    "49": "-e --id AnyDeskSoftwareGmbH.AnyDesk",
    "50": "-e --id LibreWolf.LibreWolf"

}

def coklu2 ():
    select = input("Please select the applications you want to download: ")
    selection = select.split(',')
    num_selected = len(selection)
    while True:
        for i in range (num_selected):
            num = selection[i]
            if num in indirilecekler:
                os.system("winget install " + indirilecekler[num])
                print("!!! Downloaded successfully !!!")
            elif select=="99":
                cıkıs()
            else:
                print("!!! You selected an invalid option, please enter again !!!")
                coklu2()
        select2=input("Do You Want to Continue?|Y/N: ").upper()
        if select2=="Y":
            coklu()
        else:
            cıkıs()





def coklu ():
    Main()
    select = input("""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

If you want to download multiple EXAMPLE = 0,1,2,3
If you want to download single, EXAMPLE = 0

↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

Please select the applications you want to download: """)
    selection = select.split(',')
    num_selected = len(selection)
    while True:
        for i in range (num_selected):
            num = selection[i]
            if num in indirilecekler:
                os.system("winget install " + indirilecekler[num])
                print("!!! Downloaded successfully !!!")
            elif select=="99":
                cıkıs()
            else:
                print("!!! You selected an invalid option, please enter again !!!")
                coklu2()
        select2=input("Do You Want to Continue?|Y/N: ").upper()
        if select2=="Y":
            coklu()
        else:
            cıkıs()



coklu()
