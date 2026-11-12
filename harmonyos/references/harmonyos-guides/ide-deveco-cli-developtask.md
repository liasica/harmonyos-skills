---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-developtask
title: 常用开发任务
breadcrumb: 指南 > DevEco CLI > 常用开发任务
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9fa26605231ea5d70262e6400d24944d5ddd0eec0e76715e9c1a94ffecb89046
---

以开发一个音乐类型的HarmonyOS应用为例，介绍DevEco CLI常用命令。

## 开发准备

### 初始化CLI环境

输入自然语言“将devecocli的skills或mcp服务配置到opencode中”，让Agent调用鸿蒙开发相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/gsCEdHJSSCyXgwI0SFyrrg/zh-cn_image_0000002808886619.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=49106D4DE6E770C4263B3CC4CE3C845D16A1F7B05AC1786CD514E8D2BB1EA14B "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/YAbgPr0mSQCUKeGU0uN8mw/zh-cn_image_0000002779566942.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9494749201115F400A203756C049342E4D8600FC7E665861B73C0E897B50DF46 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/LTyVm4hzROW2Y9XxGLARxg/zh-cn_image_0000002779406986.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAA531581AB7331303DEBD112BDDD0F211F50C8F8759B4838F8D9C9B386550C5)

### 登录华为账号

登录华为账号，以便进行签名配置、构建或发布等需要账号权限的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/qr8BOoUsTjC_zWSiikHKLg/zh-cn_image_0000002779566956.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DF19DEAADBFB8C7C460E091A29A644F7870886200933100B3E28742FFF83963)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/lTTPaahdSEWrhYWGJkzGxQ/zh-cn_image_0000002808886597.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=486C684541F8018F9225686E0E812DB23C828AFF93C5CEE70AD38130DC2CBEF1)

### 查询文档

搜索并查看鸿蒙开发文档，了解指定组件或API的用法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/bpuVPLUcS26c9JBvRLIZAw/zh-cn_image_0000002779566962.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A13054F360E4C67FA2F609A36FBF43F22FF4FF6D0679FACBF673910D8CDBA478)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iAZwJ82eS_CfukdKQXAYIA/zh-cn_image_0000002808886631.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D9A7DF6834AF7CFB4E36FBA55012D3E7BB31E1976B1F9A1D72E8938F911FAD4)

## 创建项目

### 创建音乐应用工程

创建一个音乐类型的应用工程，自动生成基础目录结构和示例代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/G5a9sj8iTGGMhCOJQCyotQ/zh-cn_image_0000002808886611.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=942B7300A32A552E1CE1E2373CA5BC8E557F86235E876519057365E8FB9BD380)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/GiRUHN_6QzyX3eylIsz-lg/zh-cn_image_0000002779566964.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=73DDAC14860614D1037501F7F20D7A551FBAA82702E207875A845D8D0F2E5598)

### 配置签名

配置调试签名，使应用可以安装到真机或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/yzW1pLFMQvysG7uCZdkj3Q/zh-cn_image_0000002808766517.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB008144966E9848FD9FFD8E3CF56CB8B72DEA79692C81F8BD3E1799F51B4C12)

## 生成代码

### 编写播放器核心功能

编写音乐播放器的核心功能代码，并在编写代码过程中自动查看相关API的用法，对生成的功能代码进行检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/y1Zg43W_SSeOzkTilVFFug/zh-cn_image_0000002779566950.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CAD3795BF6E261D97308801EF9E417D168C5FC95FB2E24161B8D8F614E7526A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/5DqSXomLSlO_yEQXl9ofMA/zh-cn_image_0000002808886599.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2D82AA212A8EDD4E267990970066D271987C54EEC4A77B3CE3DB633629BD6F9)

### 检查代码规范

检查代码是否符合ArkTS编码规范，并给出改进建议。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/4gO5eHz-QFibt5hrJscWOQ/zh-cn_image_0000002808766535.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=35F0779580B24FFEEAB6AC930865AA7DC1EE6718BC4CE482629FDB5038C7A2C6)

### 检查兼容性

检查项目在目标设备上的兼容性，排查潜在的兼容问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/uQbzwlFiQOWEJeoD3wPmWw/zh-cn_image_0000002779406984.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=75FB8F2CD5FD828AA802D40A76309C5CBE47B42275542372CE0B5947FBADD03D)

## 构建与运行

### 调试构建

执行调试构建，将应用安装到设备或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/J82HUjM8SRmDgX3JmM68rQ/zh-cn_image_0000002808886603.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=60F324B472F185792336A1721161988B3F790D55A9386080D23245EE7A7E2338)

### 清理构建产物

清理构建产生的中间文件和产物，释放磁盘空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/2_tX0X_iT8mFh3KFvOoC5Q/zh-cn_image_0000002808766539.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=490C797A31B497941C4E35E1BAB6D41BB65A3D3AC13B85A1C14F32FE4ADACD80)

## 热重载开发

将主题色改为亮色，通过热重载在不重启应用的情况下验证UI改动生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/2BVmg9_vSg61DuABTP10uQ/zh-cn_image_0000002808766523.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0097C72A29789F8B1F6B678E97F70F9878AC41E5C5812DBF0FD5C88F01E22FDC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HIPd4Dw4RaW9kkaZ0IbJVA/zh-cn_image_0000002779406974.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD5325B93A26D74D7C2871C497031DAE52009274D4B0BBAB7AF868F342900F0C)

## 模拟器测试

### 镜像管理

查询适用于当前工程的模拟器镜像。Agent读取工程的API配置，调用DevEco CLI的镜像查询能力，检查手机镜像的系统版本和下载状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/VGoDHme7RaawBDJoV2iwiA/zh-cn_image_0000002808886621.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCA2242272C761295823099EB470E3D295644AA2DA8CD35F06B1B2D9E46A937E)

Agent选择本地已下载的HarmonyOS 7.0手机镜像，供后续创建测试实例使用。需要其他版本时，可以继续获取所需镜像。

### 创建专用测试模拟器

为音乐应用创建专用测试模拟器。确定名称后，Agent调用 DevEco CLI的实例创建能力，再查询实例列表，确认MusicApp\_Phone已创建成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/MR83ezwbSGqWhx4b4c1VKg/zh-cn_image_0000002808766537.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D165D5425FA93DF6527311F7A31C6E3DCA9E8EB002D9923F33934B4C50AE01B)

### 启动模拟器

启动测试实例。Agent调用 DevEco CLI启动模拟器，并查询运行状态和连接信息，为后续部署应用确定目标设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/oLgqJ0FvQwi7IPH9hpdSMg/zh-cn_image_0000002779566952.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4499A930C9EE01AD32E8D6201502A4C3EA90AC6CD642934F241ED3162DCF3F8F)

启动完成后，模拟器显示系统界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/eg6XBwOTQ3mgx4ILLJy-1g/zh-cn_image_0000002808766531.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C43BEE207BDBC5962E278BEA6DC6277226449CCEED9883EB1149E3C0A12A3571 "点击放大")

### 在模拟器上调试运行应用

将音乐应用运行到已启动的模拟器。Agent结合工程模块和目标设备，调用DevEco CLI完成调试构建、安装和启动，并根据返回结果反馈部署状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/u5cbPg88TpG1IarogP8Vrg/zh-cn_image_0000002779566968.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=31B639D3C79F3ED5DE5257DA07134331DD4B5489071D8D9DE82B90F27534A615 "点击放大")

应用启动后，可在模拟器上查看首页的推荐歌单和歌曲列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Cm9BNaIXRaeipCvA_1QxYg/zh-cn_image_0000002779566954.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C865B7DB8849E532118A0F03D889BB9AB5225AB56149918956079F7659783FB "点击放大")

### 调整模拟器音量

在测试过程中，调整模拟器音量。Agent调用DevEco CLI的模拟器控制能力，将音量操作应用到当前测试实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/a7ApqL3oQG6PbqR-yjzxtg/zh-cn_image_0000002779406982.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B568F12EDFF3B6D1374FDC0C1D65BF8BC2CF6DFFDE40BE2FF614DABE2600E1C "点击放大")

结合系统音量面板，观察播放器页面和应用首页的显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/0prmDti4Qe-6V_aFJ2IwQQ/zh-cn_image_0000002808766529.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8041FE5EF3ABFCF5054F6A9CB2404B7F04B7DFC05306FF7925E55427456D1A87 "点击放大")

## 调试与日志

### 查看设备日志

获取测试设备最近的日志。Agent调用DevEco CLI的日志采集能力，读取最近100行内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/-MwjcaWfQa6yayF3ergXAQ/zh-cn_image_0000002779406960.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C2875884C6A8D3F821A8816AA388AFDF123D7B125C793997B0DAB0B28700ABA)

当返回内容主要为系统应用日志时，可以进一步限定应用范围，继续筛选。

### 音乐应用专项日志

只查看当前音乐应用的日志。Agent根据工程包名调用DevEco CLI的应用日志筛选能力，提取应用启动和页面加载等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/tzErvGxMR1ilqwRvAEM_mw/zh-cn_image_0000002808766547.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BC050E0AE0E096333E87C703832EE4A3576E07016ED0C7CD2659C987597C528)

Agent将生命周期日志解释为应用创建、窗口创建、进入前台和页面加载完成，帮助判断启动过程。需要进一步分析播放行为时，可以按播放器的业务标记筛选相关事件。

### 实时日志跟踪

持续跟踪应用日志，同时操作播放、暂停和切歌。Agent使用DevEco CLI的实时日志能力采集运行信息，将新产生的日志与界面操作对应起来。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/UqSX4vb_RcKtc-Ld0_mMKw/zh-cn_image_0000002779406976.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6EDF061D5141903492932653AB2A3D9FA6F915B36C75672A7ADFB0799A8A4E6)

### 查看历史日志

查询指定时间段内的应用日志，例如当前时刻10分钟前至5分钟前这段时间。Agent 将时间范围转换为日志查询条件，调用DevEco CLI获取对应记录，并解释该时段发生的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/67pTznK1RmKQEowTycTYeQ/zh-cn_image_0000002779406964.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3BD51F5482A223437DB8C59814325C4DBEDE5781655B8BDF729902C8BEF9D0E)

查询结果包含应用创建、进入前台和页面加载记录，可用于回溯启动过程，或与异常发生的时间进行对照。

### 分析崩溃日志

在测试代码中加入越界访问，点击“下一首”触发崩溃，用于演示故障定位流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/6rX05wotSGiHjBowWL8c0A/zh-cn_image_0000002808886617.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FA45300C6506D6CF10EEE83E1F38F4CBE9DC51DD8DB8481EA113AC01D00D042)

应用崩溃后，分析原因。Agent调用DevEco CLI获取崩溃日志，提取异常类型和调用栈，再读取对应源码进行定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/73ESoCw_TP2Q6LEGG7NYgg/zh-cn_image_0000002779566940.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5A39E7E1F4659A03A798E925726BBA8B5B25405C76E7ADFA2B4C7CBCFA6FD7E)

Agent定位到“下一首”逻辑中的歌单越界访问：读取不存在的歌曲后继续访问其名称，引发异常。根据这一结果，可以继续移除演示故障代码、检查歌单边界，并通过DevEco CLI重新构建运行，按相同操作复验。

## Skills（可选）

### 列举可用Skills

查询HarmonyOS应用开发可用的技能。Agent调用DevEco CLI的技能查询能力，获取skill列表，并按ArkUI开发、崩溃分析、多设备适配等用途进行整理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/YNoJIxHkRHSfescqKYGENQ/zh-cn_image_0000002779566944.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=44AD6B02139BF1C68C89E7BEB7CC7220ED5DDF879177CA809A8BB64B80C29AFD)

### 查找所需Skills

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/OsM26lCcSbC4mUXR7npotQ/zh-cn_image_0000002779406966.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DA7CCD7247D4DCE88E1F9A065E3F4DAF7A5340EE2A2EBB767B4AB42828EF58E)

Agent结合各项技能的描述，选择多设备适配入口，以及折叠状态、窗口尺寸、屏幕方向和交互方式相关技能，并说明选择理由。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/_5Z8WI0uTYuB9jZrvmx3xw/zh-cn_image_0000002808766525.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2533449C8AF70B292ADEAF61FB401E344755CA0A9F090442DB1ABD075E3F7B5)

### 安装Skills

将选定skill安装到当前工程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/VnPaAGg0QIa5uHbuSbUXgQ/zh-cn_image_0000002779406962.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=93B306822B69A283F8C50EBF14EE3C6163DBF3C6DE7E9D1518F013478CC93B8F)Agent调用DevEco CLI的skill安装能力，完成五项技能的安装，并反馈安装结果。Agent可加载对应技能，依据其中的指导开展适配开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/yFLG6I-IT7W_Jl5TzlavjQ/zh-cn_image_0000002808886605.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C17215833BAE2AA001FD67B5E00D1C0D858305C8E02ED9D37DDF3A724F9AD4A)

## 应用发布前检查

### 兼容性检查

检查当前代码的系统版本兼容性。Agent先调用 DevEco CLI查询可用的检查版本，再结合工程配置确定源版本和目标版本，执行工程扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/8yrmxgwWQd-MP_vUD36KIw/zh-cn_image_0000002779406972.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=70B3DCA9BA36D7A7E93D69CC0E80A124DCAC2477D8F004DDFCAF69C1F228E64C)

DevEco CLI返回API变更及代码位置，Agent据此整理接口定义、视觉布局和接口行为等方面的影响，指出需要关注的调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/a-lPA2gFQWKdatMpgnQPaw/zh-cn_image_0000002808886609.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=90908087D5BB5F588BA17D9F037151AA44DF33C4D9425598C4B05278EF90BE7E)

### 签名检查

检查工程签名配置和材料，确认是否满足构建及发布要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/9peM7AFXQParF14x1pzfVw/zh-cn_image_0000002779566946.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0987BB4F9C98B3CD26521D217D368163132B2E93E8BD2EA1B61C6CE70B1503E4)

Agent读取工程配置，检查构建产品与签名配置的关联，再核对证书、密钥库、profile、应用包名和有效期，汇总检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/3G7E88uoQFKNwIqjpLxRhA/zh-cn_image_0000002808766533.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D74F3DC22F028A1E03C4BF30F46E7391246B5CD13E9556E6DE3D460FE95334BC)

### 发布构建

执行发布构建。Agent根据工程配置调用DevEco CLI的release构建能力，检查构建结果，并查找生成的应用包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/nuHU5k0uS-aWo6wFqUl2WQ/zh-cn_image_0000002808766541.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8F63B78E49636C1EDF997B7CA9D04602A1AE3645A9885C50F6A8A5573213567)

构建完成后，Agent汇总已签名和未签名产物的位置，便于继续测试或准备交付。
