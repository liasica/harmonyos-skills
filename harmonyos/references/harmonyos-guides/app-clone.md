---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-11-21T09:10:50+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:922a2412a5f6a86637fa472d39c576b2edaf0fd2905d8669f9b75283bcdc4755
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/gau0pNdgQlmuavdwyO1p9w/zh-cn_image_0000002821755989.png?HW-CC-KV=V1&HW-CC-Date=20261121T010926Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DD33CE1A4968916B5129BF5FBE537D4A6B12ADF4FAADA69FEF3A7D45A8EBE23)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/hGCBsHHIQwmHsbQcjC3PSA/zh-cn_image_0000002793036054.png?HW-CC-KV=V1&HW-CC-Date=20261121T010926Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FB4DAC0A4712CBD659F20CAD582B015CB2FD4BBDF3E586CF13E99B9A69AC79C)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/jhnVEZRpTLGZuRAdDQegtA/zh-cn_image_0000002792876086.png?HW-CC-KV=V1&HW-CC-Date=20261121T010926Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E69D91F796076A38A054903B3CA5D3FBAA207EFF6E59EAAF356BA1F3E969A7D)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Sb_bUIVFQmqCEXHGiTza2Q/zh-cn_image_0000002821835991.png?HW-CC-KV=V1&HW-CC-Date=20261121T010926Z&HW-CC-Expire=31536000000&HW-CC-Sign=68AE5DFBABA88898F6F8512824227B3444A77FF920C25C4DCEB69CAA641571BA)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/zoxyX_7ZTkmsx8llHm9R3w/zh-cn_image_0000002821755989.png?HW-CC-KV=V1&HW-CC-Date=20261121T010926Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CE3FDD23470E66FEDC6D57B2BAB3C13DEB37C5F441E16F5C79BC25FA88E6DC2)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
