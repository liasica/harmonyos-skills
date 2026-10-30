---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-10-31T07:31:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:92d292abd457751a1eaa7a29441f37332b8d7be63e1a86d70a75f4261c278c4f
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/e9yu3DKHTfm3X6mbLeyflA/zh-cn_image_0000002806027685.png)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/j57hPx2nR5eKk5Mopn7FNg/zh-cn_image_0000002806107575.png)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/IfujUvuXTDqPjEXoiN4Grw/zh-cn_image_0000002776907956.png)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Gv0qEizNStaCgjySKPtJEw/zh-cn_image_0000002776747970.png)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/F94kWyJxTJKh467-hlRNYQ/zh-cn_image_0000002806027685.png)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
