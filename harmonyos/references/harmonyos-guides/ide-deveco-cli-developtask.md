---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-developtask
title: 常用开发任务
breadcrumb: 指南 > DevEco CLI > 常用开发任务
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ace8ddd76647085ff8537a00bf038ab22e89b40664f62ea84c767c07d271ec55
---

以开发一个音乐类型的HarmonyOS应用为例，介绍DevEco CLI常用命令。

## 开发准备

### 初始化CLI环境

输入自然语言“将devecocli的skills或mcp服务配置到opencode中”，让Agent调用鸿蒙开发相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/izRWkwP6RH2F2W9-DSGM0A/zh-cn_image_0000002808886619.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECF2D9C6CB5B32DD6E05C0B966EA22F09013FC274887889D7523708543EAADDE "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ZHz5l7EVRQ-16u5OJ-LuxA/zh-cn_image_0000002779566942.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BD7CF3B6E41888DA9E097AD721030B713B1CEA1BA6226DFE5E394BDDB8DA14A "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/CiknXatXRSiCpF1TinUV-A/zh-cn_image_0000002779406986.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9AFC0B0B14974A0B69E61F605A3A413DED7409679A0859CE6578F9FA965B249)

### 登录华为账号

登录华为账号，以便进行签名配置、构建或发布等需要账号权限的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ppwghidTSImQZW50XkawhQ/zh-cn_image_0000002779566956.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=018E83B7FAE936F4E0D6B1889A4783FAD4A2FE4489FE4B1EB1DEA3ABE51570CD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hHor9J35T2qOyx04GyPmhw/zh-cn_image_0000002808886597.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6B194A32A212E336D4D3421CF38F7AD65CDB3F912C36E0C0BE7B952685E72DF)

### 查询文档

搜索并查看鸿蒙开发文档，了解指定组件或API的用法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/yg3asPhbSM2FRmzcffeVoQ/zh-cn_image_0000002779566962.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BB7AE357E29D0544A29E193C386EC7706027AC1CAC1DB07BBA10A1FB6515DF4)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jFHXZnXnQyqzmZq8kASUFA/zh-cn_image_0000002808886631.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EC004D3ED6C0CA867B7F9D8E2791F10D7347C44FEBF718C936DE126D8D747DE)

## 创建项目

### 创建音乐应用工程

创建一个音乐类型的应用工程，自动生成基础目录结构和示例代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/5qyRoDBIRTCbaf-vluNpnw/zh-cn_image_0000002808886611.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=423B97A2FD56632463C6E11109009ED9445CB4D266F8E1C97F2368A6247D8316)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/w1gKEnz_QQG62vfOgiq_qA/zh-cn_image_0000002779566964.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F478025CD0C987BD5F5F88D25C9CE72ABE7C17D90BFB4942AA74E8E9841B542)

### 配置签名

配置调试签名，使应用可以安装到真机或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/VLnUViEhT6uEGKqF8JRKRg/zh-cn_image_0000002808766517.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=88680951D8FCCF4114126995C33A89C57372999AD6B808BC629761C7A0090546)

## 生成代码

### 编写播放器核心功能

编写音乐播放器的核心功能代码，并在编写代码过程中自动查看相关API的用法，对生成的功能代码进行检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/mqpgVbmCQDWsmSzLNp6BvA/zh-cn_image_0000002779566950.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=888464395490D11CACA45ABD8AE9FAD9BD6C502B5E84080E148A9927B1BCA106)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/tWUu3ru-RhGRZYU-fQe2pQ/zh-cn_image_0000002808886599.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=A95F2EF2F621D9EC741CE00EC04B13E69999B172DAB8A27E10B02A2F6BFA54DE)

### 检查代码规范

检查代码是否符合ArkTS编码规范，并给出改进建议。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/u26Z5JdjQ4et52H6E35zJg/zh-cn_image_0000002808766535.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA340A61062598DEC29BD64C729FED07FFA994E9D5A51986DF6628C01D1574F8)

### 检查兼容性

检查项目在目标设备上的兼容性，排查潜在的兼容问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/AogyLaM9SYKGH0s2Fp8rNg/zh-cn_image_0000002779406984.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=98DDD8F1BB1C1D664A78A2D36FDA8BEE27EA025D0AB98031CC25AEFBE471B31F)

## 构建与运行

### 调试构建

执行调试构建，将应用安装到设备或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/fMkVhF-iSWaAZKsOFNcIiA/zh-cn_image_0000002808886603.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=40691EB90ED982C70409981C704E5092C4ED1416996E55C260BC89DDCD558CD4)

### 清理构建产物

清理构建产生的中间文件和产物，释放磁盘空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/oIw57PKLSFyo88wgbmQBWw/zh-cn_image_0000002808766539.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=0333C751083288DEBE878308FD135643F26FA8534779140D783EF239810660E2)

## 热重载开发

将主题色改为亮色，通过热重载在不重启应用的情况下验证UI改动生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/vA8j0-JgRjmqCwxioq2xXA/zh-cn_image_0000002808766523.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC406691990FD7A26ED9B5DFB1AE2FB162DFBBBF8982F4C0704A65BC2141D769)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Vtqo1hS6QMqR0CmRNEaM-g/zh-cn_image_0000002779406974.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=8018F9EE5D92364CDD44D6DAD83E3BCACB3CC22F3B774202D52D639FC9048ADC)

## 模拟器测试

### 镜像管理

查询适用于当前工程的模拟器镜像。Agent读取工程的API配置，调用DevEco CLI的镜像查询能力，检查手机镜像的系统版本和下载状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/8Mu_iX5VSX-jpvz4CogD4g/zh-cn_image_0000002808886621.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=69A65AB521931E2E5D45082ADB4EB6CB898DE11AD01734367E013CE03C9D2BB8)

Agent选择本地已下载的HarmonyOS 7.0手机镜像，供后续创建测试实例使用。需要其他版本时，可以继续获取所需镜像。

### 创建专用测试模拟器

为音乐应用创建专用测试模拟器。确定名称后，Agent调用 DevEco CLI的实例创建能力，再查询实例列表，确认MusicApp\_Phone已创建成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/FDXSu3MsQHijyi3GBaT32Q/zh-cn_image_0000002808766537.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ACB89BF19EC96084EEF54452AC7710A18BA3D8856585CB5483DA2332A500FEA)

### 启动模拟器

启动测试实例。Agent调用 DevEco CLI启动模拟器，并查询运行状态和连接信息，为后续部署应用确定目标设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/6sXAym-FThK12guorK2QXw/zh-cn_image_0000002779566952.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=D60246EF87A865B04B9073CBB6F8059F2A822F892E46DB9682C560F2130B5DE0)

启动完成后，模拟器显示系统界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/4npuVkgRSjubdLFN7t5HDw/zh-cn_image_0000002808766531.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=486485CD8D6E25D0F3EDF4D54628D3360E9255B67E731085A31E3C555F8264D4 "点击放大")

### 在模拟器上调试运行应用

将音乐应用运行到已启动的模拟器。Agent结合工程模块和目标设备，调用DevEco CLI完成调试构建、安装和启动，并根据返回结果反馈部署状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jqIQDplHQgy0XPPiWnR91g/zh-cn_image_0000002779566968.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9D0498EAB12A410CBADE78C44EED7E8489123F00245B1018CC9E347A915B931 "点击放大")

应用启动后，可在模拟器上查看首页的推荐歌单和歌曲列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/NaiNSyznQ_eJbBrQHfshiw/zh-cn_image_0000002779566954.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FE8E049A07A4F6C3F043EAF7041DBA1BDF752F34957CC7505DEEAFFF495594A "点击放大")

### 调整模拟器音量

在测试过程中，调整模拟器音量。Agent调用DevEco CLI的模拟器控制能力，将音量操作应用到当前测试实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/dGs8Dlc9TDOeYxplvbfalw/zh-cn_image_0000002779406982.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF7412C14AE3AAA39C6EFE477B0633ECCD6E176763EACFAF4640151C20D6C8D0 "点击放大")

结合系统音量面板，观察播放器页面和应用首页的显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/4tb5w-2zSUmOX-cks4_ZcQ/zh-cn_image_0000002808766529.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDF0B6F0DC8192B2B49C1350EA99C29D5134AC354B33FCCE518E122AD872AD23 "点击放大")

## 调试与日志

### 查看设备日志

获取测试设备最近的日志。Agent调用DevEco CLI的日志采集能力，读取最近100行内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/i67TauKyS-a7ETpBSRslVg/zh-cn_image_0000002779406960.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=16B2FD0E6AAD84121A2C54DA335745271EDA006B39711F9CE4D0E6D25D2CE9CE)

当返回内容主要为系统应用日志时，可以进一步限定应用范围，继续筛选。

### 音乐应用专项日志

只查看当前音乐应用的日志。Agent根据工程包名调用DevEco CLI的应用日志筛选能力，提取应用启动和页面加载等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/zjLPg8hYRYmhFuxeYw2B5Q/zh-cn_image_0000002808766547.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=50644AA3094466CEF0DB0A5045A319D33B0020F01AD435603512222F3555E734)

Agent将生命周期日志解释为应用创建、窗口创建、进入前台和页面加载完成，帮助判断启动过程。需要进一步分析播放行为时，可以按播放器的业务标记筛选相关事件。

### 实时日志跟踪

持续跟踪应用日志，同时操作播放、暂停和切歌。Agent使用DevEco CLI的实时日志能力采集运行信息，将新产生的日志与界面操作对应起来。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/2g7FoMFfTLmmfr2BYRbTYQ/zh-cn_image_0000002779406976.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=387D2002AD90F587D57307364C10C59FA7548DB7DD71B092F7CBBACAFC93C0E9)

### 查看历史日志

查询指定时间段内的应用日志，例如当前时刻10分钟前至5分钟前这段时间。Agent 将时间范围转换为日志查询条件，调用DevEco CLI获取对应记录，并解释该时段发生的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/d-F9-4hqQduzu93QUNYkUA/zh-cn_image_0000002779406964.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=410AEB527E2DF9A64C75434019DE181E3F6B134F0D7407841F7789A814A6FF7E)

查询结果包含应用创建、进入前台和页面加载记录，可用于回溯启动过程，或与异常发生的时间进行对照。

### 分析崩溃日志

在测试代码中加入越界访问，点击“下一首”触发崩溃，用于演示故障定位流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/mXAUz-MBT2Wkav9XN8ms8w/zh-cn_image_0000002808886617.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=087E334087EF37925F654F62E248616863F974796D04346465129688E3EDF1AD)

应用崩溃后，分析原因。Agent调用DevEco CLI获取崩溃日志，提取异常类型和调用栈，再读取对应源码进行定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Mk3a2UN5R1CiJm4bxcAvWQ/zh-cn_image_0000002779566940.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0CA3050150F9EB03CA90C28831297303A4A4E741CE4A3381438AC15C93427D1)

Agent定位到“下一首”逻辑中的歌单越界访问：读取不存在的歌曲后继续访问其名称，引发异常。根据这一结果，可以继续移除演示故障代码、检查歌单边界，并通过DevEco CLI重新构建运行，按相同操作复验。

## Skills（可选）

### 列举可用Skills

查询HarmonyOS应用开发可用的技能。Agent调用DevEco CLI的技能查询能力，获取skill列表，并按ArkUI开发、崩溃分析、多设备适配等用途进行整理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/G-bpxOOCSnW7bCEHzdLUQg/zh-cn_image_0000002779566944.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC8BA843155DFC12CEEBFC2A0DE5850C93C306794F785AF8FCD1CA351BAB956A)

### 查找所需Skills

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/CbnAhxYmTJGOTMF2PsVOXg/zh-cn_image_0000002779406966.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=C24CDCFB91022007ED9AE6C0242DB97D8D600C1C93E27D7418BDC40A4EA83B6E)

Agent结合各项技能的描述，选择多设备适配入口，以及折叠状态、窗口尺寸、屏幕方向和交互方式相关技能，并说明选择理由。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ChWBZZv8RYmeORzW26eQEA/zh-cn_image_0000002808766525.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1DFE73FA240B3D2D183251E0D18C1FE1845AD056EC3590757DE11D5D53DDF84)

### 安装Skills

将选定skill安装到当前工程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/80gONZgfR7a7y59iEab-Aw/zh-cn_image_0000002779406962.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=A561003158FC34D4E5F4E6B19E66266A81771BBCEBBA6C3EADEB98860C9B4293)Agent调用DevEco CLI的skill安装能力，完成五项技能的安装，并反馈安装结果。Agent可加载对应技能，依据其中的指导开展适配开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Xu2AolX6Qb29CfUUW8gkYw/zh-cn_image_0000002808886605.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EC8F463AF0ADE5245F53EF10A588FCC2E19CE47A6245737F22A4E2C02029A4C)

## 应用发布前检查

### 兼容性检查

检查当前代码的系统版本兼容性。Agent先调用 DevEco CLI查询可用的检查版本，再结合工程配置确定源版本和目标版本，执行工程扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/GmU3VWNHQR69e6h6jX5AlA/zh-cn_image_0000002779406972.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B54869DB77DE012C6711835288D19C070E21331D0BCBCB0CF234B34FA59F931)

DevEco CLI返回API变更及代码位置，Agent据此整理接口定义、视觉布局和接口行为等方面的影响，指出需要关注的调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/KDenC0HKTka0vIuEgneSpw/zh-cn_image_0000002808886609.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8460E862695AC430C415E4C563B2FE00255E744034E71C80188CECCCAB67BC)

### 签名检查

检查工程签名配置和材料，确认是否满足构建及发布要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ydKzHv-nQOqpl-8kANF2Fg/zh-cn_image_0000002779566946.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=241B6B908BB6862047230C1084B19C8E799CE86146B8ABE6DFFC48F8368FBA5E)

Agent读取工程配置，检查构建产品与签名配置的关联，再核对证书、密钥库、profile、应用包名和有效期，汇总检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/1FBpMLsXSf2HaAbigpDx5g/zh-cn_image_0000002808766533.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=A70B2853B1DB420FF8B13FFF15E4E6CD5AA5EE851BA82D9DEBC068A109C4748A)

### 发布构建

执行发布构建。Agent根据工程配置调用DevEco CLI的release构建能力，检查构建结果，并查找生成的应用包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/l-L8OW0mTjOV218Qrhp4jg/zh-cn_image_0000002808766541.png?HW-CC-KV=V1&HW-CC-Date=20261128T023501Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DCECBE2B7C735670B77482014BEE506AFDC7497255378C3203E051EE2976335)

构建完成后，Agent汇总已签名和未签名产物的位置，便于继续测试或准备交付。
