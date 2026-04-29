---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone
title: 创建应用分身
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 创建应用分身
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5aa9e3da8f4ce855c4dd58df10c1052bb5a9d5b1e9a73b7e1734f3516c471b59
---

应用分身能在一个设备上安装多个相同的应用，实现多个账号同时登录并独立运行。主要应用场景有社交账号双开、游戏大小号双开等，无需账号切换，从而省去频繁登录的繁琐。

创建应用分身之后，桌面上会出现多个相同图标的应用，其中带有下角标的应用图标表示分身应用。

主应用与分身应用之间的关系如下：

* 主应用和分身应用共享同一个应用。例如，当主应用更新/升级时，主应用与分身应用都会同步更新，包括应用的图标（icon）和名称（label）、应用的新特性等。
* 主应用和分身应用，其对应的使能和相关配置都是独立的，数据也是彼此隔离。
* 主应用被卸载时，所有分身应用也会同步卸载。卸载分身应用时，不会影响主应用。

以下图片展示了应用分身的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/fQUm5yW3REi7ufFTRO9ObA/zh-cn_image_0000002589243775.png?HW-CC-KV=V1&HW-CC-Date=20260429T052532Z&HW-CC-Expire=86400&HW-CC-Sign=DAEB9254F90E4293F9EAEDF78A766D0483A2B0DB85C81488A43B3C27C43BB9FB)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/cNe0IoF0RzqHv9QQLujdFw/zh-cn_image_0000002558763970.png?HW-CC-KV=V1&HW-CC-Date=20260429T052532Z&HW-CC-Expire=86400&HW-CC-Sign=F8030D9862CDDE0C4F015F828645F92DEB0BAA950A5FA5A3B6AAF96BA0C9BA49)
   * 然后打开设置>系统>应用分身，点击“创建分身”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/RA6XDMJyQTqMhW03V-Yx2g/zh-cn_image_0000002558604314.png?HW-CC-KV=V1&HW-CC-Date=20260429T052532Z&HW-CC-Expire=86400&HW-CC-Sign=ECD21E5CF80B6E709BA1CF94A67B37338D4763E2736D1485F5CB695F02298A6B)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-LLjwgT8RnCYqgJc4V9mmw/zh-cn_image_0000002589323839.png?HW-CC-KV=V1&HW-CC-Date=20260429T052532Z&HW-CC-Expire=86400&HW-CC-Sign=BF56A6822E06B2FFE4D9EA332E8F8B86E66AD6131E9312B401166127F7940C69)
   * 返回桌面，检查创建是否成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/3mGLXHsvQPqq68yqLxZOsQ/zh-cn_image_0000002589243775.png?HW-CC-KV=V1&HW-CC-Date=20260429T052532Z&HW-CC-Expire=86400&HW-CC-Sign=884FCE895CE7CFF1F008AD9FF0748976E252422C8587BFD9AA0BACB27DB9C913)

     图中的三个应用的进程、运行、数据、通知等，都是彼此独立的。
