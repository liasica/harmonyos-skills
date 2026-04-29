---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183
title: 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e09606ff8919a4db57ef3dfdbd37398696a55fc10b54bf6f9c5196ea0a183b89
---

**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/S-qrOuMzR--DhXOI_oreIA/zh-cn_image_0000002345811941.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=0044EE940F09AB45300564CCB1E215333B6A334F47D1BA5F2DF723CF3A5C1270)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/yuH2408aRcOVJ58zn8yJyQ/zh-cn_image_0000002312015854.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=A9A85CB9DAA47A7E7530528471BD9645611BB40F0969569044B2A650ECF81D28)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```
1. node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/2iHjZT1VRM2meJzaE_2BNg/zh-cn_image_0000002284561689.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=18456B45C7A0DA93B00CAC8161BD1A1F3744C815D74DEA8FDDB2E8A4DB9B323A)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/WiD3_Pd0QTGViAKwaSlrqQ/zh-cn_image_0000002284693797.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=F19AA8C765E4B478EE7CD8D4C05CB404BE53C121942B284FE91181E003714CF6)

Mac或Linux系统参考[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/qf6RIWj_RpOpa0UtxNfmPg/zh-cn_image_0000002284546061.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=0880A99424BE0F269A15BEEB8B69D4F979FE75EADFBA18B12CD635E9056021AC)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/VUbmLvLFS9aB0s1WpE4aAg/zh-cn_image_0000002284672673.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=BF41B236AA027A500425A9627E6313635F51C3BC8366D6B0A442B56050F4106C "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/2BEkT6eFRamWk_0htcVgZQ/zh-cn_image_0000002277140989.png?HW-CC-KV=V1&HW-CC-Date=20260429T062101Z&HW-CC-Expire=86400&HW-CC-Sign=03904FF804ADF53028E2EA941F82618152EC2BFCF36B47AA935F30363B535016)
