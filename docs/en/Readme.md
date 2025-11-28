> [!NOTE]
> AI Translation: This document has been translated by an AI. Please note that translations may not be perfect.

<div align="center">

<h2>Cities Skylines Radio Manager (CSRM)</h2>
<h3>A radio creation tool for <i>Cities: Skylines II</i>.<br></h3>
简体中文丨<a href="https://github.com/jslxxgyy/CSRM/blob/main/docs/en/Readme.md">English</a>

</div>

> [!CAUTION]
> **This software is written in Easy Language, which may trigger false positives from antivirus software. This project guarantees that the software contains no malicious code. Please add it to your trust/whitelist manually. The compilation results have been obfuscated as much as possible.**

---

This software is designed to work with the *Cities: Skylines II* mod **ExtendedRadio**. It can generate a custom radio station directory tree and corresponding JSON configuration files with one click based on user input, allowing you to create custom radio stations in the game without manually editing JSON files. It also supports importing/exporting radio stations. The software comes with built-in ffmpeg to convert audio files to the .ogg format required by the game.

> [!TIP]
> Before using this software, please ensure you have installed the *cities-skylines-2* mod [ExtendedRadio](https://www.cslbbs.net/resources/extendedradio.326/) and that it loads correctly. This software can read the game data directory from CSUL's configuration. It is recommended to install it in the same directory as CSUL.

## How to Use:
### Create a New Radio Station:
- 1. Upon first launch, set the game data directory and temporary file directory.
- 2. Click "New Radio Station" to open the creation window.
- 3. Fill in the custom radio station information. Fields marked with * are required.
    Among these:
    - **Radio Station Name** will be displayed at position ① in the image below.
    - **Radio Station Description** will be displayed at position ②.
    - **Channel Name** will be displayed at position ③.
    - **Channel Description** will be displayed at position ④.
    - **Program Name** will be displayed at position ⑤.
    - **Program Description** will be displayed at position ⑥.
    - **Start Time** and **End Time** will be displayed at position ⑦.

<div align="center">
  
<img  src="https://gitee.com/jslxxgyy/CSRM/raw/main/docs/network.png" alt="This is an image" >

</div>

> [!TIP]
> If Start Time and End Time are left blank, the corresponding time display and progress bar at position ⑦ will not change.

After filling in the above information, click the "Add / Change" button on the right to add music to the corresponding radio program. This step supports almost all audio formats. Non-.ogg files will be automatically converted using ffmpeg when creating the radio station.
Click the "Create Radio Station" button to generate the station. The location of the generated station is determined by the game data directory specified in the settings. After generation, you can choose to export the station, which creates an `output.zip` file in the output folder.
After seeing the prompt "Radio station creation completed," you can reload the stations in the ExtendedRadio mod settings or restart the game to reload the mod.

You can also visit www.bilibili.com/video/BV1Hvh1evEuw/ for a [video tutorial](https://www.bilibili.com/video/BV1Hvh1evEuw/).

## Settings Explanation:
- **Mod Type** should be selected by the user based on the source of their installed mod. Supports the PMOD version and the BeplnEx version. Different versions require different game-related paths to be filled in. If installed in the same directory as CSUL, the paths can be automatically read from CSUL's configuration file based on the mod type.
> [!WARNING]
> Starting from version 0.3.0, support for the BeplnEx version of the mod will be discontinued.

- **Temporary File Directory** is a crucial directory for the software's operation, storing key files generated during the radio creation process. It is recommended to use the "Temporary directory under the program directory" option or set a simple, memorable location when customizing. The complete contents of the temporary file directory may be required when reporting issues.

## Planned Features:
- [x] Create a radio station with a single channel, single program, and multiple songs.
- [x] Use CSUL's configuration file to set game-related directories.
- [x] Use ffmpeg to convert non-.ogg format music.
- [x] Export radio station packages in zip format.
- [ ] One-click import of zip format radio station packages.
- [ ] Support for custom radio station icons.
- [ ] Modify existing radio stations.
- [ ] Create radio stations with multiple channels, multiple programs, and multiple songs.

## Issue Reporting:
If you encounter any problems while running the program, please try clearing the game's custom radio station file directory (after backing up) and attempt again. If the problem persists, please submit feedback at [CSLBBS](https://www.cslbbs.net/threads/cities-skylines-radio-manager.1053/). Considering the difficulty of accessing GitHub from some regions, issues reported on CSLBBS will be prioritized.
Recently, CSLBBS has experienced access instability. If you cannot access CSLBBS, please go to GitHub to submit issues.

### When reporting an issue:
- Provide a detailed description of the problem, or a video/screenshot showing the issue.
- State the program's version number and compilation time.
- Upload the `load.ini` file from the program's running directory.
- If there are files in the temporary file directory, upload them as well.

### Is this code reliable?
This is my first GitHub project and it's still in its early stages. There are many minor issues in the code, and I cannot guarantee testing for every possible scenario, so oversights are inevitable. If you have suggestions for this project or wish to contribute code, PRs and issues are welcome! (The project will be rewritten in C# later.)