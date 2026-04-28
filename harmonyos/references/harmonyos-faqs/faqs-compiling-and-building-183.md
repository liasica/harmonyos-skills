---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-183
title: 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 执行命令卡在起daemon的日志上或编译报错“ReferenceError, TransformStream is not defined in hvigorfile: XXX”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3bbf9eec0af616eb4774ed4a7a5fcd4754b12ff3c13ae0b0737815703f860410
---

**问题现象**

流水线或命令行中执行命令后在起daemon的日志上：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/S-qrOuMzR--DhXOI_oreIA/zh-cn_image_0000002345811941.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=6BA88492090B1F34050FDB7565C3CFABD207ED09071B6B858C8AB232F1619D13)

或者是流水线或命令行中编译报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/yuH2408aRcOVJ58zn8yJyQ/zh-cn_image_0000002312015854.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=AB88F38DDCFCBA84B582DA7B122C584B75A77DC55DDBE4D0F5BE62EE61F43D44)

**问题原因**

编译不支持低于v18.0.0的Node.js版本。相关配置查看[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

**解决措施**

1.确认流水线或计算机配置的Node.js的版本。

Windows通过cmd或Powershell运行， Mac或Linux系统通过终端（Terminal）运行：

```
1. node -v
```

查看输出：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/2iHjZT1VRM2meJzaE_2BNg/zh-cn_image_0000002284561689.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=305969C393E19D40ED67E5A66838170EE7C44A997EC7881B52D99758816A88B8)

2.如果流水线或计算机配置的Node.js的版本低于v18.0.0，推荐使用DevEco Studio或Command Line Tools自带的Node.js包来配置系统变量。

Windows系统打开环境变量的配置，将DevEco或Command Line Tool自带的Node.js包的路径添加进系统变量的Path中。如果是通过NODE\_HOME配置的，可以直接修改NODE\_HOME配置的路径。若系统中已存在其他Node.js版本，需将工具自带的Node.js路径添加至Path变量的最前端，确保优先使用该版本；通过NODE\_HOME配置时，需检查Path中是否包含%NODE\_HOME%/bin（Windows）或$NODE\_HOME/bin（Mac/Linux）以确保生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/WiD3_Pd0QTGViAKwaSlrqQ/zh-cn_image_0000002284693797.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=21E280E722BD07E7E569540E1C456DFAA67B8C346DD31CCBDB805534D22C8640)

Mac或Linux系统参考[配置Node.js环境变量](../harmonyos-guides/ide-command-line-building-app.md#section159168531288)。

DevEco Studio的自带的Node.js的路径为DevEco Studio安装目录/DevEco Studio/tools/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/qf6RIWj_RpOpa0UtxNfmPg/zh-cn_image_0000002284546061.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=2DED961B15ACD36551EB1E5916D585CB925F6A84024188333E9129E067E62E5A)

Command Line Tools自带的Node.js的路径为Command Line Tools安装路径/command-line-tools/tool/node。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/VUbmLvLFS9aB0s1WpE4aAg/zh-cn_image_0000002284672673.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=A741EB5566E0805D240562F7F86BDF9D7348DC723BA0598159EE9BE6A3D2C286 "点击放大")

3.将自定义的Node.js版本升级为与DevEco Studio或Command Line Tools自带的Node.js版本一致。通过上述路径运行node -v查看版本，然后在Node.js官方网站中下载对应版本。下载地址为：https://nodejs.org/dist/v18.20.1/。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/2BEkT6eFRamWk_0htcVgZQ/zh-cn_image_0000002277140989.png?HW-CC-KV=V1&HW-CC-Date=20260428T002945Z&HW-CC-Expire=86400&HW-CC-Sign=B23B8F7ED5DFE5D5EDB798592BF9F898173675621087E03F4380326224C66980)
