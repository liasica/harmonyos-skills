---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00a3335b5f796ce855eb4edf9f5e7ff63f95153d3052d9974c6d68a5c5ed252c
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/fs566DKCTsq68tDcl_3Cow/zh-cn_image_0000002552957478.png?HW-CC-KV=V1&HW-CC-Date=20260427T233730Z&HW-CC-Expire=86400&HW-CC-Sign=9770B5A5D485C1A1F6F04550C48E96221C0F709A98B5B2003D1278DCA039D056)

## 约束与限制

输入法应用配置分身无效，无法创建应用分身。

## 应用分身的开发步骤

1. 配置应用分身的方法。

   在工程项目中对AppScope/app.json5配置文件配置[multiAppMode](app-configuration-file.md#multiappmode标签)字段。具体配置如下：

   ```
   1. {
   2. "app": {
   3. // ...
   4. "multiAppMode": {
   5. "multiAppModeType": "appClone",
   6. "maxCount": 2
   7. }
   8. }
   9. }
   ```

   [app.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/AppClone/AppScope/app.json5#L16-L33)
2. 创建分身应用。

   * 首先将已配置好的工程编译打包安装到设备上。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/MD82tuixQ36U2tyGWx8g6Q/zh-cn_image_0000002583477479.png?HW-CC-KV=V1&HW-CC-Date=20260427T233730Z&HW-CC-Expire=86400&HW-CC-Sign=70BC379A7FB65702AB999486B5A43FB0508F71A1A2A74BCE17B64B8277F98476)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/QRpb_9xvRAW53lB2QYdT3Q/zh-cn_image_0000002552797830.png?HW-CC-KV=V1&HW-CC-Date=20260427T233730Z&HW-CC-Expire=86400&HW-CC-Sign=CC8B03CA18BD468E450BCE15FD81B4BF39C34E78810B65BD6B467D3AEDCB446E)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/WcFhP0wVSYCDobfsDXv9gQ/zh-cn_image_0000002583437525.png?HW-CC-KV=V1&HW-CC-Date=20260427T233730Z&HW-CC-Expire=86400&HW-CC-Sign=FD025C8C5E755EB4A8AD46DFEFF31FF49250CF4C5DDCCC38D81693A95FD473DF)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/JbmudRzzQrSFZxtNoqNclQ/zh-cn_image_0000002552957478.png?HW-CC-KV=V1&HW-CC-Date=20260427T233730Z&HW-CC-Expire=86400&HW-CC-Sign=DFF1BCD86C9DAD0ABE066184DE8B92A776C942C941A44890611EF62FEFBAA904)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
