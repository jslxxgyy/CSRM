<div align="center">

<h2>Cities Skylines Radio Manager, CSRM</h2>
<h3>A GUI-based radio creation software for Cities: Skylines II.<br></h3>
Simplified Chinese | <a href="https://github.com/jslxxgyy/CSRM/blob/main/docs/en/Readme.md">English</a>

</div>

## ***Important Reminder:***<br>
## ***This software is written in EasyLanguage, and most antivirus software will recognize it as a Trojan virus. If you receive a security alert, please add it to your trust zone. I have tried my best to obfuscate the compilation results. The source code is open-source; if concerned, do not use!***<br>

---

### Software Features:
This software is fully GUI-based, allowing users to automatically generate a radio directory tree and the corresponding JSON configuration files based on the entered content, eliminating the need for manual editing of JSON files. It is user-friendly and comes with ffmpeg for converting audio files into the required .ogg format.
### Developer Tips:
If the results of self-compilation differ from the hash value of the release version, it may be due to different settings in the "Compiling result scramble code" in the EasyLanguage configuration, not because the source code of the release version is inconsistent. Please change this setting to 303039437 before trying again.<br>
### User Tips:
Before using this software, ensure you have installed the cities-skylines-2 mod [ExtendedRadio](https://www.cslbbs.net/resources/extendedradio.326/) and it loads properly. This software can read game-related directories from the CSUL configuration and is recommended to be installed in the same directory as CSUL.<br>
Video tutorial available [here](https://www.bilibili.com/video/BV1Hvh1evEuw/)


## Instructions for Creating a New Radio Station:<br>
- 1. Start the main program and click on 'Create New Station' to open the new station window<br>
- 2. Fill in the required information. Mandatory fields are marked with an asterisk.
These include:<br>
- Radio station name corresponds to ①<br>
- Radio station description corresponds to ②<br>
- Channel name corresponds to ③<br>
- Channel description corresponds to ④<br>
- Program name corresponds to ⑤<br>
- Program description corresponds to ⑥<br>
- Start and end times correspond to ⑦<br>

<div align="center">
  
<img  src="https://raw.githubusercontent.com/jslxxgyy/CSRM/main/docs/network.png" alt="This is just an image" >

</div>

### User Tips:
#### If you do not fill in the start and end times, then the time and progress bar at ⑦ will not change.<br>
#### After filling in the information above, click 'Manage Music' to add music to the station. Now supports mainstream audio formats; non-.ogg files will be automatically converted using ffmpeg.<br>
Click the confirm button to save the music configuration file, then click 'Create New Station' to generate the station. The location of the generated station is determined by the game file or game data directory specified in the settings. For a video tutorial, please visit:<br>
### User Tips:
#### If the generated station cannot be used in the game or errors occur, please delete the temporary files directory and try generating again with the same content. If the issue persists, please report it on cslbbs. See issue feedback for details.<br>
## Instructions on Settings:<br>
1. The type of mod is determined by the source of the mods installed by the user. Supports PMOD version and BeplnEx version. Different versions will require different game-related paths. If installed in the same directory as CSUL, the paths can be automatically read from CSUL’s configuration file based on the type of mod.<br>
2. The temporary files directory is an important directory during the operation of the software, storing key intermediate files during radio creation. When setting this directory, it is recommended to use "temporary directory under the program directory" to make it easier for users to locate, or set a clear and memorable location when customizing. When reporting issues, a complete content of the temporary files directory is required. See issue feedback for details.<br>
## Feature Plan<br>
- [x] Can create a station with 1 channel, 1 program, and 16 pieces of music<br>
- [x] Can use CSUL’s configuration files to set game-related directories<br>
- [x] Can use ffmpeg to convert non-.ogg format music<br>
- [x] Modify Python code to make it more easily callable by other programs<br>
- [ ] Modify EasyLanguage code to make it more easily callable by other programs<br>
- [ ] Support custom radio station icons
- [ ] Able to export the radio station package in zip format for easy redistribution<br>
- [ ] Able to import zip format radio station packages with one click<br>
- [ ] Able to modify existing stations<br>
- [ ] Able to create a station with 8 channels, 1 program, and 16 pieces of music<br>
- [ ] Able to create a station with 8 channels, 4 programs, and 16 pieces of music<br>
## Issue Feedback:<br>
If any issues occur during the operation of the p
