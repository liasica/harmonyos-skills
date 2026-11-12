---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dd9f781feece56de781d2ea0bdc8e57b488b4a4c5ebd7569a313e4eeb0aec96b
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/mFw_vtgNQ6m79UUI7RE8NQ/zh-cn_image_0000002815557795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC7A8F11C50040D3AF03890679E51733E09A87AC8ACA8C9B4F910DEEEFFB26A0)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/BBMvFKEIRo6VbtchPzZhEA/zh-cn_image_0000002815397879.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D58FBE02A5C28CE767C7216B77C66BDD7FA8C89BBA98915AD79A10491B0DA6E)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/0Wc80jv4SbynsMnGEBnkoA/zh-cn_image_0000002786518304.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=357E95357528675A038016FB920A5EF3C0F826BC0ED6C06CE1999BD0D0EFE430)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/LQFAroOzSu6HdxgPZgfyrw/zh-cn_image_0000002786358376.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB3A89872C0130B8E1CB689651F2083E6A4D4A4935E78FB687A42585ABDF7A64)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/6n2jlTH-SpqlMe5jOsYESw/zh-cn_image_0000002815557795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C790B9AF009BF6041BC3EBF85A64EC97224AF8A3D1700A883DDE83803585B4AD)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
