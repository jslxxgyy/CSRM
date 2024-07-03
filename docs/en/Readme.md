
<div align="center">

# Cities Skylines Radio Manager, CSRM
### A GUI software for creating radio stations in "Cities: Skylines II."

</div>

# **Important Notice:**
# **This software is written in EasyLanguage and most antivirus programs will recognize it as a Trojan virus. If security warnings appear, please add the program to the trust zone yourself. I have tried to scramble the compiled results as much as possible, and the source code is open source. If this concerns you, please refrain from using it!**

### Software Features:
#### This software is fully GUI-based and can generate a radio directory tree and corresponding JSON configuration files based on user input without the need for manual JSON editing, offering user-friendly interaction. It includes ffmpeg to convert audio files to the required .ogg format.
### Developer Note:
#### If the hash value of the software differs from the released version after self-compilation, it might be due to different "Compile Result Scrambling" settings in EasyLanguage configuration. Please change this setting to 303039437 and try again.
### User Note:
#### Before using this software, ensure that you have installed the Cities Skylines 2 mod [ExtendedRadio](https://www.cslbbs.net/resources/extendedradio.326/) and that it loads properly. This software can read game-related directories from CSUL's configuration, and it is recommended to install it in the same directory as CSUL.
## Instructions for Creating a New Radio Station:
- 1. Start the main program and click "Create New Radio Station" to open the new station window.
- 2. Fill in the required information. Fields marked with * are mandatory.
  - Radio station name corresponds to ①
  - Radio station description corresponds to ②
  - Channel name corresponds to ③
  - Channel description corresponds to ④
  - Program name corresponds to ⑤
  - Program description corresponds to ⑥
  - Start and end times correspond to ⑦

<div align="center">
  
<img src="https://raw.githubusercontent.com/jslxxgyy/CSRM/main/docs/network.png" alt="This is an image">

</div>

### User Note:
#### If you do not specify start and end times, the time and progress bar for item ⑦ will not change.
#### After filling in the above information, click "Manage Music" to add music to the station. Now supports mainstream audio formats, and non-.ogg files will be automatically converted using ffmpeg.
Click the confirm button to save the music configuration file, then click the new radio station button to create the station. The location of the created station is determined by the game file or game data directory specified in the settings. For a video tutorial, please visit:
### User Note:
#### If the generated radio station cannot be used in the game or prompts an error, please delete the temporary files directory and try generating it again with the same content. If the problem still cannot be resolved, please report it on cslbbs. See problem feedback for more details.
## Instructions for Settings:
1. The type of mod is determined by the source of the mod installed by the user. Supports PMOD and BeplnEx versions. Different versions will require filling out different game-related paths. If installed in the same directory as CSUL, paths can be automatically read from CSUL's configuration file based on mod type.
2. The temporary files directory is an important directory during the operation of the software, storing key transitional files during the creation of a radio station. When setting this directory, it is recommended to use "temporary directory under the program directory" to make it more easily discoverable by users, or set a straightforward and memorable location when customizing. When reporting issues, provide the complete contents of the temporary files directory. See problem feedback for more details.
## Feature Plan:
- [x] Can create radio stations with the format of 1 channel, 1 program, 16 music tracks
- [x] Can use CSUL's configuration file to set game-related directories
- [x] Can convert non-.ogg format music using ffmpeg
- [x] Modify Python code to make it more conveniently callable by other programs
- [ ] Modify EasyLanguage code to make it more conveniently callable by other programs
- [ ] Support custom radio station icons
- [ ] Can export radio stations as zip packages for easy redistribution
- [ ] Can import zip format radio packages with one click
- [ ] Can modify existing radio stations
- [ ] Can create radio stations with the format of 8 channels, 1 program, 16 music tracks
- [ ] Can create radio stations with the format of 8 channels, 4 programs, 16 music tracks
## Problem Feedback:
If you encounter any issues during the operation of the program, please clear the temporary files directory and try again. If the problem persists, submit feedback on the cslbbs page. Given the difficulty of accessing GitHub in China, I will prioritize issues reported on cslbbs.
### When Submitting a Problem:
① Provide a detailed description of the issue or provide videos or screenshots where the issue occurs.  
② State the program's version number and compilation time.  
③ Upload the load.ini file from the same directory as the program.  
④ If there are files in the temporary files directory, upload them together.  
