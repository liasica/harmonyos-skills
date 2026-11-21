---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183
title: "执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”"
category: harmonyos-faqs
scraped_at: 2026-11-21T09:19:27+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:fe53d015dd40b6e6a1de7c171b7dfa941bbfc053df1d3c5e56be25419bce0748
---

**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/6-u43z6xSk2ZhKvHYR5_Bg/zh-cn_image_0000002654798019.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A1F84884CCC3569E0D1D47F3DBE568220E4BAC78D1E25864ABC77F38F96B09C)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/OyCfjscsT0etxynGxOTdSg/zh-cn_image_0000002624638572.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBC4348F6BE7B145053D8B6F0F5A0CCC6ED739D5A68A5B5379C95489D6C900A4)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](../doccenter-deveco-studio/ide-command-line-building-app.md)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```powershell
node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/zaKvZckHRRmhXRbRDMVKqw/zh-cn_image_0000002654837991.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=C59DC692AB83625EF40DE3C62D471EF2A4826A4BD44466C9C45AE129DF13C604)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/wfp-sXlsSsCEB-rjT_MdaQ/zh-cn_image_0000002624478680.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=921FD17A09E3CF44F0CC18D4D1AD8AB8D1E9A87504E3BD19E769FFC2FD086010)

Mac或Linux系统参考[配置Node.js环境变量](../doccenter-deveco-studio/ide-command-line-building-app.md)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/irTbKT_SRx-rPe3udGreAQ/zh-cn_image_0000002654798043.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD19E22C46E05B8EB8007E359E364AF7C48AC07DFB9A76AA0DD2871778D5F9E6)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2nmQTZBbRgiC7Ghjsk1jfw/zh-cn_image_0000002624638594.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=07C4726AFD1DB8C0813445C2CE3C05C0801FD10F14479C6AA5878D7515087311 "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/BCaYC2ZkRvibmh0RjoAOpg/zh-cn_image_0000002654838001.png?HW-CC-KV=V1&HW-CC-Date=20261121T011927Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AE8724447A08023BFA1132106CBED2DC5E8426918EAC6D25201291C7A21EBD4)
