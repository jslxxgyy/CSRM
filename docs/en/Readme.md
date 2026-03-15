> [!NOTE]
> AI Translation: This document has been translated by an AI. Please note that translations may not be perfect.

<div align="center">

<h2>Cities Skylines Radio Manager, CSRM</h2>
<h3>A radio creation software for "Cities: Skylines 2".<br></h3>
<a href="https://github.com/jslxxgyy/CSRM/blob/main/Readme.md">简体中文</a>丨English

</div>

> [!CAUTION]
> **This software is written in Easy Language and may trigger false positives in antivirus software. This project guarantees that no malicious code is present in the software. Please manually add the software to your antivirus software’s trusted zone. The compilation results have been obfuscated.**

---

This software works with the "Cities Skylines 2" mod [ExtendedRadio](https://mods.paradoxplaza.com/mods/75862/Windows) and allows you to easily generate custom radio station directory trees and corresponding JSON configuration files based on the entered content. You can create custom radio stations in the game without manually editing JSON files, and the software supports importing/exporting radio stations. The software comes with FFmpeg, which can convert audio files into the required .ogg format for the game.

> [!TIP]
> Before using this software, please ensure that the "Cities Skylines 2" mod ExtendedRadio is installed and properly loaded.

## How to create a radio station:
- 1. On first launch, the settings window will open automatically. After configuring the options, click OK to restart the program.
- 2. Click "Create New Radio" to open the new radio station window.
- 3. Fill in the custom radio information, fields marked with * are required.
   - The radio station name will be displayed at position ① in the image.
   - The radio station description will be displayed at position ② in the image.
   - The channel name will be displayed at position ③ in the image.
   - The channel description will be displayed at position ④ in the image.
   - The program name will be displayed at position ⑤ in the image.
   - The program description will be displayed at position ⑥ in the image.
   - The start time and end time will be displayed at position ⑦ in the image.

<div align="center">
  
<img  src="https://gitee.com/jslxxgyy/CSRM/raw/main/docs/network.png" alt="">

</div>

> [!TIP]
> If you do not enter start and end times, the time and progress bar corresponding to ⑦ will not change.

Once the information is filled in, click the "Add" button in the music management group box to add music to the corresponding radio program. This step supports almost all audio formats. Non-`.ogg` files will be automatically converted using FFmpeg when creating the radio station. Click "Create New Radio" to generate the radio station. The location of the generated radio station is determined by the game data directory set in the settings. After the station is created, you can choose to export the radio station, specifying the export location and file name. Once done, a prompt saying "Radio station creation completed" will appear, and you can reload the radio station in the ExtendedRadio mod settings. It is recommended to restart the game to reload the mod.

You can also visit Bilibili for the [video tutorial](https://www.bilibili.com/video/BV1Hvh1evEuw/).

## Importing Radio Stations
The CSRM import feature allows you to import radio station packages in zip format that were exported when creating the radio stations. Simply click on "Import Radio" on the main interface, select the radio station package to import, and click OK. No additional information is required.

### Forward Compatibility
CSRM's import feature has some forward compatibility (yes, even such a small project has forward compatibility). The compatibility between various releases and the current version of CSRM (0.2.2 - Eula) is as follows:

| Version  | Compatibility | Notes |
|----------|---------------|-------|
| 0.0.3 - Aether  | ❌ | This version lacks the radio export feature |
| 0.1.0 - Bennett | ❌ | Due to a major overhaul in version 0.2.0, the radio package format is completely different and not compatible with later versions. Only 0.1.0 can import 0.1.0 radio packages. |
| 0.2.0 - Citlali | ⚠ | Import is possible, but with some issues: ① The directory for imported radio stations is decided by the configuration in the imported radio package, not by the game data directory in settings. If the directory in the imported package does not exist, the import will fail. ② If "Do not use FFmpeg to convert audio formats" is selected during radio creation, the import will fail. ③ Regardless of whether "Write additional data for the program" is selected during station creation, additional program data will not be retained during import. |
| 0.2.1 - Dehya | ⚠ | Same as 0.2.0 - Citlali |
| 0.2.2 - Eula | ✔ | Fully compatible |

❌: Incompatible, attempting import will prompt "Invalid radio station file!"  
⚠: Partially compatible, with potential risks and issues when attempting import.  
✔: Fully compatible.  

## Settings Description:  
### Radio Station Generation Settings  
The game data directory should be filled with the directory where the game stores saves, custom assets, logs, and mods obtained from Paradox Mods. It is typically located at `C:/Users/<your username>/AppData/LocalLow/Colossal Order/Cities Skylines II/`. If you are using CSUL (Cities: Skylines II Universal Launcher), you can also retrieve the directory from CSUL’s configuration file `CSUL.config`.

> [!WARNING]
> Support for BeplnEx version mods has been removed from version 0.2.2 - Eula.

> [!WARNING]
> Some users may move the game data directory by creating a symbolic link. The program's support for symbolic link directories is uncertain. It is recommended to fill in the actual directory instead of the symbolic link.

### Temporary File Directory
The temporary file directory is an important directory for the software's operation, where key files are stored during the radio station creation process. It is recommended to use the "Temporary directory under the program directory" option, or set a custom location that is simple and easy to remember. When reporting an issue, please provide the complete contents of the temporary file directory.

### FFmpeg Options  
The encoding quality level in the FFmpeg options is used to control the bitrate of the .ogg file generated when converting audio files using FFmpeg. There are 12 levels to choose from, and the corresponding bitrate for each level is approximately as follows:

| Quality Level | Bitrate                     |
|---------------|-----------------------------|
| -1            | 32-48kbps                   |
| 0             | 48-64kbps                   |
| 1             | 64-80kbps                   |
| 2             | 80-96kbps                   |
| 3             | 96-112kbps (default)        |
| 4             | 112-128kbps                 |
| 5             | 128-160kbps                 |
| 6             | 160-192kbps                 |
| 7             | 192-224kbps                 |
| 8             | 224-256kbps                 |
| 9             | 256-320kbps                 |
| 10            | Maximum possible bitrate    |

If you need more precise control over the file's quality, you can check the "Use Constant Bitrate" option and input a bitrate value. The bitrate is not limited, but it is recommended to choose a value between 32 and 500 Kbps. Extremely high or low bitrates may cause encoder initialization failure. The Vorbis encoder uses VBR (Variable Bitrate) encoding, so the actual bitrate may vary slightly from the set bitrate.  
Enabling "Parallel Multi-Audio Transcoding" allows multiple FFmpeg processes to transcode all audio files simultaneously, potentially faster than transcoding each audio file sequentially.

## Planned Features:
- [x] Create single-channel, single-program, multi-music radio stations
- [x] Automatically convert audio using FFmpeg
- [x] Customize audio conversion quality
- [x] Read game data directory from CSUL
- [x] Export radio stations
- [x] Import radio stations
- [x] Online program updates
- [ ] Use custom FFmpeg program
- [ ] Customize radio station icons
- [ ] Modify existing radio stations
- [ ] Tabbed layout for new radio station window
- [ ] Multi-language support
- [ ] Create multi-channel, multi-program, multi-music radio stations

## Issue Feedback & Q&A

### Issue Feedback:
If you encounter any issues while using the software, please back up your files and clear the game’s custom radio station directory, then try the operation again. If the issue persists, please submit feedback at [CSLBBS](https://www.cslbbs.net/threads/cities-skylines-radio-manager.1053/). Due to limited access to GitHub in China, issues on CSLBBS will be given priority.  
Recently, CSLBBS has been experiencing instability. If you cannot access CSLBBS, please move to GitHub to submit issues.  
When submitting an issue:
- Provide a detailed description of the problem or video/screenshot of the issue
- Specify the program version number and compile time
- Upload the `load.ini` file from the program's running directory
- Include any relevant files from the temporary file directory

### Q&A

Q: Why can’t I run the program after downloading it, and it says "Contains a virus or potential junk software"?   
A: This program is written in Easy Language and may trigger false positives in antivirus software. If you encounter such warnings, simply add the program directory to the antivirus software’s exclusion list, trusted zone, or whitelist.

---
Q: Why do I always enter the settings when starting the program?  
A: This is most likely due to a missing or corrupted configuration file. When the program detects an invalid configuration file, it will prompt you to reconfigure. You can delete the `load.ini` file in the program directory, then restart the program and re-enter the settings.

---
Q: Why are the program descriptions and start/end times by default not editable? What happens if "Write additional data" is checked?  
A: In the current version of the ExtendedRadio mod (1.4.6), if a radio station's directory contains a `program.json` file with descriptions and start/end times, the radio station will freeze in the game after all music has played once. Whether you switch to another station and back or manually change the track, the station will not play the next track until the station is reloaded in the ExtendedRadio settings or the game is restarted.

---
Q: What operations were performed on my audio files during FFmpeg transcoding?  
A: During transcoding, the program removes audio cover information from video streams using the `-vn` parameter. The game cannot play `.ogg` audio files with video cover streams. Additionally, if you input a FLAC file with a sample rate higher than 48 kHz and 24-bit depth, using the libvorbis encoder may result in "Encoder initialization failed." To avoid potential compatibility issues with high sample rate audio in the game and mod, the sample rate is forced to 48 KHz using the `-ar 48000` parameter during transcoding.

---
Q: Why can’t I play the newly created radio station after reloading it in the game?  
A: This issue is not related to the radio station itself, but rather to the station not being correctly loaded. Restart the game to reload the mod, and the issue will be resolved.

## Repository Structure and Development Process

The CSRM project follows a dual-branch parallel development model. The `main` branch is the primary branch, and the other branch is the testing branch, named after the development codename for the next version. All features and performance improvements are pushed to this branch first. When the testing branch matures, it will be merged into the `main` branch and released later. When a release contains defects, patches are pushed directly to the `main` branch, with a fix release being issued and later merged back into the testing branch.

### Self-compilation

To experience features not yet available in the release from the testing branch, install the latest release first, then pull the files from the testing branch into the folder containing the official release. Replace the original main program during self-compilation to avoid dependency issues. CSRM depends on the Jingyi module, so ensure it's prepared for self-compiling. Once you have these ready, you’ll have your own CSRM development environment. Why not submit a PR?

### Does your code remain stable?
This is my first GitHub project, and it’s still in the early stages. There are many issues with the code, and I can't ensure that every situation is tested. If you have any feedback or would like to contribute code, feel free to submit a PR/issue! (The project will be rewritten in C# later)

## Acknowledgements
Thanks to the [Snap.Hutao](https://github.com/DGP-Studio/Snap.Hutao)[^1] project for providing guidance and reference for the CSRM documentation and Changelog standardization.  
Thanks to the [Snap.Hutao.Deployment](https://github.com/Masterain98/Snap.Hutao.Deployment) project for providing design inspiration for CSRM's updater.  
Thanks to the [FFmpeg](https://github.com/FFmpeg/FFmpeg) project for providing the audio transcoding functionality to CSRM under the GPL open source license. You can check the source code used by CSRM in this [repository](https://github.com/jslxxgyy/FFmpeg).  
Thanks to the [ExtendedRadio](https://github.com/AlphaGaming7780/ExtendedRadio) project, which is a dependency for CSRM; without it, there would be no CSRM.

[^1]: The original Snap.Hutao project has ceased development due to a legal notice from miHoYo. The original Snap.Hutao repository is no longer public. Please refer to [this repository](https://github.com/jslxxgyy/Snap.Hutao.backup) for source code, and [this repository](https://github.com/wangdage12/Snap.Hutao) for the successor project.  
We hope miHoYo can embrace the open-source community!  
Lastly, the highest respect goes to the Snap.Hutao development organization — [DGP-Studio](https://github.com/DGP-Studio) and every developer, contributor, and supporter, including [@wangdage12](https://github.com/wangdage12), as well as every player striving for the best gaming experience on the desktop version of Genshin Impact!