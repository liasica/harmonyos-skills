---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-developtask
title: 常用开发任务
breadcrumb: 指南 > DevEco CLI > 常用开发任务
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3b9fabc17e2d2b61abea9771768973a5ec40f57f589ce12bf48fd71ff65d51b7
---

以开发一个音乐类型的HarmonyOS应用为例，介绍DevEco CLI常用命令。

## 开发准备

### 初始化CLI环境

输入自然语言“将devecocli的skills或mcp服务配置到opencode中”，让Agent调用鸿蒙开发相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/aivlcircQFqSDxVlveJkIw/zh-cn_image_0000002808886619.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=F574776C06E0C38CE2160AC16E19C856A63ADCFD4814DF66F85A7B229D4CEF4D "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QMKPuHFjRN6KHTIf9u4Nrg/zh-cn_image_0000002779566942.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=8827CBB32BDB12F15B2A58624413BBC18191722690DDF28C679A2C01BAD87DC1 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/bk5HfAVCQAylLru1-1aA2Q/zh-cn_image_0000002779406986.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=70824723664192877F68E15F1372498121F31839BF567F17855A2DD72D62C5DD)

### 登录华为账号

登录华为账号，以便进行签名配置、构建或发布等需要账号权限的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/pb7508bPQjuI_1MV-u4V8Q/zh-cn_image_0000002779566956.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1FF64054E720A786207ED1476CD257F71EB8DD3B3F8A2CFCBCC0BA1F6C5FBF3)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/IybzV25YQKaHLS5HRUc8xA/zh-cn_image_0000002808886597.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=759846661E7ECBF2C4F7B54A4B9144057FB2880879D99148757605D9D4F2642F)

### 查询文档

搜索并查看鸿蒙开发文档，了解指定组件或API的用法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/EM7UrhunTxC9rvqP1o4LcA/zh-cn_image_0000002779566962.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4D363348698864790943D460557E453A85E3AD04D9EE0BE9CDBCA7B95F9CFA6)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/br1rbIxfSQWEvJLWLODryw/zh-cn_image_0000002808886631.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=A091F82765C5897A374F8A9699005E7F645610ED65753DD53F23549AE865E344)

## 创建项目

### 创建音乐应用工程

创建一个音乐类型的应用工程，自动生成基础目录结构和示例代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/AwKzJvY5Qz6wL0CsxnVkCQ/zh-cn_image_0000002808886611.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CD51B3A44B1D5427223566B6A92AB0772F339A2237F1BEA8BA2D2C3DF52C7C6)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/4ffLbZljT0qM6pccTd3GDQ/zh-cn_image_0000002779566964.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C38A731CE278494AF1A36898845CFB5445A20E338F06EB878E339079197EFEB5)

### 配置签名

配置调试签名，使应用可以安装到真机或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/BdPE0ahzQz6-n8PKsa1Z1g/zh-cn_image_0000002808766517.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=15570C1C59B72C3B3B5196684A29710951EB27D1CC21C2B8845AECC944B5A61E)

## 生成代码

### 编写播放器核心功能

编写音乐播放器的核心功能代码，并在编写代码过程中自动查看相关API的用法，对生成的功能代码进行检查。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/PHiCHCKUS46zuL11XYRTrg/zh-cn_image_0000002779566950.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C414990BBFC221176233CD6CE1BE124C42BD61A04D68681B657FA8D2619772F2)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/0zApVUz1QTOmDgEYSc1GoA/zh-cn_image_0000002808886599.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=06D75E97D5DF5B880AD9526F582690E189572482666EEC98C85CEEA881E9A3DC)

### 检查代码规范

检查代码是否符合ArkTS编码规范，并给出改进建议。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/b7GGUKcUSCub_sFD1WWEzw/zh-cn_image_0000002808766535.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EE783671C2060223BC148B2870120E06E86255704814008666EF08C88B25C4A)

### 检查兼容性

检查项目在目标设备上的兼容性，排查潜在的兼容问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/P5oir7WCT4K53NpWVLRb6w/zh-cn_image_0000002779406984.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D886BF6D344CB50CCF7F638B4EC54FC1D3326E6436557DB639F695D4F15BEE55)

## 构建与运行

### 调试构建

执行调试构建，将应用安装到设备或模拟器上进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/_TuKVS0YQLOux3uLWyZrGw/zh-cn_image_0000002808886603.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=591B5E9A420222700E15495A1B14081C862CA302BC0B10E74976BEFDDB5705DA)

### 清理构建产物

清理构建产生的中间文件和产物，释放磁盘空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/BmP81w1MRZ2q3bPY5OaurQ/zh-cn_image_0000002808766539.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3C915DFA41EE563B14DAC5350D121A95723FD05B59EB68A9C5607B78FA8FCB9)

## 热重载开发

将主题色改为亮色，通过热重载在不重启应用的情况下验证UI改动生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/paalRO3LT_e_tEXT2Pr79g/zh-cn_image_0000002808766523.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D768DDD78EBE74309F21BF5AC69A03F5FE4EF0BFA6C62AA80D9FE5AC4E6209C9)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/pmA50x0tRs6Nzc7QvFD_dQ/zh-cn_image_0000002779406974.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=8719651FA411EF41DF8BFCA924F69BDD8AA375CBA45DDCC29BC3468C740A2366)

## 模拟器测试

### 镜像管理

查询适用于当前工程的模拟器镜像。Agent读取工程的API配置，调用DevEco CLI的镜像查询能力，检查手机镜像的系统版本和下载状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/J2hMlEJ7Rw2FyLCgiCuadw/zh-cn_image_0000002808886621.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BE37549B05CF3825D3010E7A129BB29AF9E26117F2D4BEA65E763BA1D0A07BE)

Agent选择本地已下载的HarmonyOS 7.0手机镜像，供后续创建测试实例使用。需要其他版本时，可以继续获取所需镜像。

### 创建专用测试模拟器

为音乐应用创建专用测试模拟器。确定名称后，Agent调用 DevEco CLI的实例创建能力，再查询实例列表，确认MusicApp\_Phone已创建成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/_ezMLs11TCqV_43o1qemOw/zh-cn_image_0000002808766537.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=02F7E0EC8D18EB70D65181ECFDB0AF61E5307D35D563B90876F03201E4C254DD)

### 启动模拟器

启动测试实例。Agent调用 DevEco CLI启动模拟器，并查询运行状态和连接信息，为后续部署应用确定目标设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/wRsr2eN0Q9GZXwR97mdm2A/zh-cn_image_0000002779566952.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=A58D7A74306A79D262E4967C1E4F942BF850BB190497C6DC2BD7D175DAFF4B40)

启动完成后，模拟器显示系统界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/N4Ov9CS-ROyH-yri7cWQYQ/zh-cn_image_0000002808766531.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=A99806FBACC2132A6D2BEE15DC942EBE4D7DA6CC1A7F677696106AC19F140B61 "点击放大")

### 在模拟器上调试运行应用

将音乐应用运行到已启动的模拟器。Agent结合工程模块和目标设备，调用DevEco CLI完成调试构建、安装和启动，并根据返回结果反馈部署状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/29yR5G0-S_ubCaIApGGkIQ/zh-cn_image_0000002779566968.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EEE2E8E1B10CBAD860F2961DD9176032AF1A18E26E05F7356B7BEBF8EA3525D "点击放大")

应用启动后，可在模拟器上查看首页的推荐歌单和歌曲列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/na4cJegOTaWqQrS_WPDouQ/zh-cn_image_0000002779566954.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFD5C57BAF83DAD61A39E73CA27BFF55F63A5EA78BA7496D41AF740567E59D16 "点击放大")

### 调整模拟器音量

在测试过程中，调整模拟器音量。Agent调用DevEco CLI的模拟器控制能力，将音量操作应用到当前测试实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/WVGtEkcVR7mONgSsNPsQoQ/zh-cn_image_0000002779406982.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=6327B3818FE477C9EB8D3435FAB52486099BBA56125E74D87A58A57334054249 "点击放大")

结合系统音量面板，观察播放器页面和应用首页的显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/_yWHirJbQ7aa7dD6rpVxNQ/zh-cn_image_0000002808766529.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C9717D3DB2983CAB5FF445B71AAA26AE5C327251E9547C266564BE07FD2F832 "点击放大")

## 调试与日志

### 查看设备日志

获取测试设备最近的日志。Agent调用DevEco CLI的日志采集能力，读取最近100行内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/PiK7e-9wTCedyvmPDrB-Dg/zh-cn_image_0000002779406960.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8D6AD15E27D8EE3185AACCF21F3617FCF21B3F77D62F4D73C6D23628685AD79)

当返回内容主要为系统应用日志时，可以进一步限定应用范围，继续筛选。

### 音乐应用专项日志

只查看当前音乐应用的日志。Agent根据工程包名调用DevEco CLI的应用日志筛选能力，提取应用启动和页面加载等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/WazgVnVATsOk_CTez5bGVA/zh-cn_image_0000002808766547.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B73C9908E3FFCA58D19E38F12ACFB98EA69447D29B7EEDE6D07F06EC387F294)

Agent将生命周期日志解释为应用创建、窗口创建、进入前台和页面加载完成，帮助判断启动过程。需要进一步分析播放行为时，可以按播放器的业务标记筛选相关事件。

### 实时日志跟踪

持续跟踪应用日志，同时操作播放、暂停和切歌。Agent使用DevEco CLI的实时日志能力采集运行信息，将新产生的日志与界面操作对应起来。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/9XwpCsRNRBG79C0P3ToJkw/zh-cn_image_0000002779406976.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FE68B07E8F6003E3C5EBE327F3D447635C38D69F1755B37F66030003445F8F0)

### 查看历史日志

查询指定时间段内的应用日志，例如当前时刻10分钟前至5分钟前这段时间。Agent 将时间范围转换为日志查询条件，调用DevEco CLI获取对应记录，并解释该时段发生的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/AwpkHRUWRSuoWpPPuH0NcQ/zh-cn_image_0000002779406964.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F69D670105ACC69BB392EBE7E0E1D3EB757ED55B25885DAA031412764A2D25C)

查询结果包含应用创建、进入前台和页面加载记录，可用于回溯启动过程，或与异常发生的时间进行对照。

### 分析崩溃日志

在测试代码中加入越界访问，点击“下一首”触发崩溃，用于演示故障定位流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/r9e1eK9wTGO9igj7MJOygQ/zh-cn_image_0000002808886617.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E94824B1E12368978CD595344D08F2F8F36FE830CE5F7F894662E4910812B2E)

应用崩溃后，分析原因。Agent调用DevEco CLI获取崩溃日志，提取异常类型和调用栈，再读取对应源码进行定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/R9DqqJU9Q7CtNhFIZRbPfQ/zh-cn_image_0000002779566940.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EF0018EABA9D0AD9270095438CB3FF879E5B0001A5FBEEBDAE6FBFEB4F182DF)

Agent定位到“下一首”逻辑中的歌单越界访问：读取不存在的歌曲后继续访问其名称，引发异常。根据这一结果，可以继续移除演示故障代码、检查歌单边界，并通过DevEco CLI重新构建运行，按相同操作复验。

## Skills（可选）

### 列举可用Skills

查询HarmonyOS应用开发可用的技能。Agent调用DevEco CLI的技能查询能力，获取skill列表，并按ArkUI开发、崩溃分析、多设备适配等用途进行整理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/qEpGvfn4TKyQ6VZSQfA87Q/zh-cn_image_0000002779566944.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1CC37CE546516D9B85F81801A5829BBC2145B45DFFA726D680FF162459EC76E)

### 查找所需Skills

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/XjH33mFsSsekiVU_ZfAAIA/zh-cn_image_0000002779406966.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD875B9DAC5501CF2AB5940376D7158BDC5630E84EAD5AC1B0FE1F3D37138616)

Agent结合各项技能的描述，选择多设备适配入口，以及折叠状态、窗口尺寸、屏幕方向和交互方式相关技能，并说明选择理由。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Te1N1HITSte__6mw0H4PTg/zh-cn_image_0000002808766525.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=0226A726F2C1DC0C0812FC8485A7479FD95B3A2BDD9769C3BC5E2229A83788C1)

### 安装Skills

将选定skill安装到当前工程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/RApsckppSZWCXTlwjLTwdA/zh-cn_image_0000002779406962.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=309A514E5A583903C0D65FA85011C3A5540F3536FCC4E2E2492DD1246F53E913)Agent调用DevEco CLI的skill安装能力，完成五项技能的安装，并反馈安装结果。Agent可加载对应技能，依据其中的指导开展适配开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/j9uhyB_4QEy7G8CWFFGuKg/zh-cn_image_0000002808886605.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D0FBD6E54A07145A8CD7877DF37EBB901191338C1D13F214C1307ACEBAE37B7)

## 应用发布前检查

### 兼容性检查

检查当前代码的系统版本兼容性。Agent先调用 DevEco CLI查询可用的检查版本，再结合工程配置确定源版本和目标版本，执行工程扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/_YUwMPxmQVK4Uc3lH5HOaQ/zh-cn_image_0000002779406972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=545970E1E0B7F5CDE1D16D462360E5494D45C98E2FD480C298E55150294E87CE)

DevEco CLI返回API变更及代码位置，Agent据此整理接口定义、视觉布局和接口行为等方面的影响，指出需要关注的调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/gHon9lB8QAqkGAulb7QEvw/zh-cn_image_0000002808886609.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=9640C55C0192AD9EF6E867DBB8C5CB3D627D94FAE1AE0A016AE3E763AAE610EC)

### 签名检查

检查工程签名配置和材料，确认是否满足构建及发布要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/RtRQn2yURq2j4J1crmDiaQ/zh-cn_image_0000002779566946.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BA930668A4AA6CDB32C13358EB2D57F2DE187734B157BB95977A6D4758F1021)

Agent读取工程配置，检查构建产品与签名配置的关联，再核对证书、密钥库、profile、应用包名和有效期，汇总检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/AwCqTB8gTKmr5kggTTkKZw/zh-cn_image_0000002808766533.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=B38F6BF635FE478B6055A735B30207C540A0840C899A947FA096F96CA210571B)

### 发布构建

执行发布构建。Agent根据工程配置调用DevEco CLI的release构建能力，检查构建结果，并查找生成的应用包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/r0TZQExBTDqASUY5pjrsAA/zh-cn_image_0000002808766541.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F714BBACBE16152F9EFCCD8C2640522012E44C6FEE613844C6F45F0CB347611)

构建完成后，Agent汇总已签名和未签名产物的位置，便于继续测试或准备交付。
