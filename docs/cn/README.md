<div align="center">

<h2>Cities Skylines Radio Manager，CSRM</h2>
<h3>一个GUI化的《都市:天际线Ⅱ》电台制作软件。<br></h3>
简体中文丨<a href="https://github.com/jslxxgyy/CSRM/blob/main/docs/en/Readme.md">English</a>

</div>

## ***重要提醒：***<br>
## ***本软件由易语言编写，大部分杀毒软件都会将其识别为木马病毒。如出现安全提示请自行添加信任区，本人已尽量对编译结果做了打乱处理，源码已开源，介意勿用！***<br>

---

### 软件特点：
本软件完全采用 GUI 界面，可根据用户输入的内容来一键生成电台目录树及对应的json配置文件，无需手动编辑 json 文件，交互友好。自带 ffmpeg，可以将音频文件转换为需要的 .ogg 格式。
### 开发人员提示：
如出现软件自行编译后的结果与发行版本哈希值不同，可能是因为易语言配置中的“编译结果打乱码”与本人设置不同，并不是因为发布的源码编译版本的源码不一致。请更改此设置为303039437后再尝试。<br>
### 用户提示：
在使用此软件前，请确保你已经安装了 cities-skylines-2 模组 [ExtendedRadio](https://www.cslbbs.net/resources/extendedradio.326/)并能被正常加载。本软件可从CSUL的配置中读取游戏相关目录，建议与CSUL安装在同目录下。<br>
视频教程点[这儿](https://www.bilibili.com/video/BV1Hvh1evEuw/)


## 使用方法之新建电台：<br>
- 1.启动主程序点击新建电台打开电台新建窗口<br>
- 2.填写对应信息标*的为必填。
其中：<br>
- 电台名称对应①<br>
- 电台描述对应②<br>
- 频道名称对应③<br>
- 频道描述对应④<br>
- 节目名称对应⑤<br>
- 节目描述对应⑥<br>
- 开始时间和结束时间对应⑦<br>

<div align="center">
  
<img  src="https://raw.githubusercontent.com/jslxxgyy/CSRM/main/docs/network.png" alt="这就是一张图片" >

</div>

### 用户提示：
如果不填写开始时间和结束时间，那么⑦处对应的时间和进度条将不会变化。<br>
在以上信息填写完毕后，点击管理音乐，即可向电台中添加音乐。支持主流的音频格式，非'.ogg'文件会调用ffmpeg自动转换。<br>
点击确定按钮保存音乐配置文件，再点击新建电台按钮即可生成电台。生成的电台位置由在设置中填写的游戏文件或游戏数据目录所决定。
## 使用方法之设置说明：<br>
1.模组类型由用户安装的模组来源自行决定。支持PMOD版和BeplnEx版。不同的版本会要求填写不同的游戏相关路径。如果与CSUL安装在同一目录，可从CSUL的配置文件中依据模组类型自动读取路径。<br>
2.临时文件目录是软件运行时的重要目录，会存储在电台创建过程中的关键中转文件。建议使用“程序目录下的临时目录”使其更易发现，或在自定义时设置一个简明易记的位置。在报告问题时需提供完整的临时文件目录内容，详见问题反馈。<br>
## 功能计划:<br>
- [x] 新建格式为1频道1节目16音乐的电台<br>
- [x] 使用CSUL的配置文件设置游戏相关目录<br>
- [x] 使用ffmpeg转换不为.ogg格式的音乐<br>
- [x] 修改Python代码，能更方便的被其他程序调用<br>
- [x] 导出zip格式的电台包。<br>
- [x] 一键导入zip格式的电台包<br>
- [ ] 修改易代码，能更方便的被其他程序调用<br>
- [ ] 支持自定义电台图标<br>
- [ ] 修改现有电台<br>
- [ ] 新建格式为8频道1节目16音乐的电台<br>
- [ ] 新建格式为8频道4节目16音乐的电台<br>
## 问题反馈：<br>
如程序运行过程中出现任何问题，请先清除临时文件目录后再次尝试。若问题仍然存在，请于[CSLBBS](https://www.cslbbs.net/threads/cities-skylines-radio-manager.1053/)提交反馈。考虑到国内访问GitHub较为困难，我们会优先处理CSLBBS上的问题。<br>
### 在提交问题时：
- 需提供详细的问题说明或提供问题出现的视频或截图<br>
- 需写明程序的版本号及编译时间<br>
- 须上传程序同目录下的load.ini文件<br>
- 临时文件目录中有文件需一并上传<br>