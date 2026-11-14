---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-11-14T08:46:47+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:eaaa2e9206250423afefff9e5f5d07639e22f7498693559511fc57f06c151cb1
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/qUjZLfoDQOKdT-_-Peu7ZA/zh-cn_image_0000002788466050.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB4ADBDFDF5C096DFF8E95AA74AA5388F72BF71F3E8178422149AF9D4E244087)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Sy2TmfuYRkGBSX7rXdZ6gQ/zh-cn_image_0000002817505537.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=4481D3271AB808F79353DB451068652812461162EA6A97E60D2A2D155CDF23AC)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/UXEH8fpiSoK-dO_R-B0GgQ/zh-cn_image_0000002788306108.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=32098DF40F2BC3AEF915E8600D01ACE4DEAC298504237962ED84C875ED03D5E9)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/3yW9BVMgTZSBJdsCBzsZYQ/zh-cn_image_0000002817425471.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=F308879D6207B3FCC5702626A0F2B4D82556AF8F822240A709231E343649B2B8)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/HPnvlIi7RJOqy6XK1r0sXg/zh-cn_image_0000002788466050.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B1E6775C67A566DCFA7B5178A76D16C886854EFC983E25591D1EDC0C3530E6F)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
