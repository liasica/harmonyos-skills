---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3ed20122024ffecfe0b27cdaf8e2d7b95d2384652916990b2d3e09e398c60500
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/gYVvZI7xQS2k3yKYEFxXSA/zh-cn_image_0000002791564434.png?HW-CC-KV=V1&HW-CC-Date=20261119T014723Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDB074C20BB919951BAD0A539BE76EC21095E48B17D6532A6FB4F667209A2DD5)

## 约束与限制

输入法应用配置分身无效，无法创建应用分身。

## 应用分身的开发步骤

1. 配置应用分身的方法。

   在工程项目中对AppScope/app.json5配置文件配置[multiAppMode](app-configuration-file.md#multiappmode标签)字段。具体配置如下：

   ```json5
   {
     "app": {
       // ...
       "multiAppMode": {
         "multiAppModeType": "appClone",
         "maxCount": 2
       }
     }
   }
   ```
2. 创建分身应用。

   * 首先将已配置好的工程编译打包安装到设备上。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/BBy_aguqQeOSkb4UrYt5kw/zh-cn_image_0000002820524385.png?HW-CC-KV=V1&HW-CC-Date=20261119T014723Z&HW-CC-Expire=31536000000&HW-CC-Sign=92928EA0841DBB162B3FB40380314DEFAA5C1DA4C65CAB28FD5B4EDB94F9BADB)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/0P-UFHq4SfGnk93Moa5F1Q/zh-cn_image_0000002820404385.png?HW-CC-KV=V1&HW-CC-Date=20261119T014723Z&HW-CC-Expire=31536000000&HW-CC-Sign=12A3E16DDE4CA711609CF024659782972B1D2AD5953C6043D5BD62404CD33DED)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/vGbMD3OYTlGXax2Cg6WXCw/zh-cn_image_0000002791724408.png?HW-CC-KV=V1&HW-CC-Date=20261119T014723Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7EAC998FB252E092B57460F3988F1AD67C7B3223F074137C730F41BAAEA469A)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/8orOxFLMRYKE-nq_IK6IBw/zh-cn_image_0000002791564434.png?HW-CC-KV=V1&HW-CC-Date=20261119T014723Z&HW-CC-Expire=31536000000&HW-CC-Sign=801BF0A2E0F72F4851FAC7BE492CF541B848C6FBD2852F037EAD1B77A19E4980)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
