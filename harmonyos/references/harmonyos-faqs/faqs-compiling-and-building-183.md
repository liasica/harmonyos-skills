---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183
title: "执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ab719be206f59d420d16ee214801981d432e35bf68bc03dcd3d618c4c3989ff8
---

**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/BIsiGW--QiiJaO7G6eUC8A/zh-cn_image_0000002654798019.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E97DEDE5C1B0871E7E3F26FED36A6D273A22D3B0C484F1D0BC269510DD2E10B)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/NteCcvMaSFGVsFvsqEW5Lw/zh-cn_image_0000002624638572.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9CA62E7DBA4BB09606B6838E1C27DE55D13E003E96092E93F8E21C8EA37480B)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```powershell
node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/bPn0GBx9Tb-D7Yo4N2Ky2Q/zh-cn_image_0000002654837991.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0891EF330DDA75D433E4B7FF7D3D949BABA86347D48FB71E54482CC5C2EC48E)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/TWLwepfoRauX_cMfkI9O7g/zh-cn_image_0000002624478680.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED730B27560CE0BCB6DFF7B52CDF8B350C82B4B9CB594EDB9A74E1AAD9E83D9B)

Mac或Linux系统参考[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/ge6jyJr-TMKGzSCW459RaA/zh-cn_image_0000002654798043.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA7A693F01C326DD85456EFE4ACA0FFBF5C7B28431FDF0F2D07B1607FDB788FD)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/B63MaejKRtCf82LJNzLdGg/zh-cn_image_0000002624638594.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=506C440F7DA4C3AF9CA015F674B6FF5B763F89BC39F171FF695F17E5EC3D3A61 "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/TL0niUe9TFCvPEWXqZJ2mw/zh-cn_image_0000002654838001.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=B436C89E61D8B837D8AB098A1DB8CCC113A79D906BCF4E85780EEF5DEC2BD50A)
