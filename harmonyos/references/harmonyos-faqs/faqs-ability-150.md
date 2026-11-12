---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-150
title: 如何隐藏应用启动时展示的应用图标
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何隐藏应用启动时展示的应用图标
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b0d16abe08f81e5fb5dc7cce4ba3d18bf75fe175c4f7217027948948ee6da303
---

## 问题现象

应用启动时会先展示应用图标，然后再跳转至首页（如下效果图所示）。如何隐藏该应用图标呢？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/VnIk0Q4NTDSxGbak1qgkbw/zh-cn_image_0000002628789248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B5B76AF0CBEBAB8290C21B3F1F7DEA9330287542AA8CE733AD59C3F3E7C8425 "点击放大")

## 背景知识

[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。其中startWindowIcon指定当前UIAbility组件启动页面图标资源文件，startWindowBackground指定当前UIAbility组件启动页面背景颜色资源文件。

## 解决方案

1. 将entry模块的module.json5配置文件中abilities标签下的startWindowIcon字段设置为透明的空图片。

   ```json
   "startWindowIcon": "$media:startIcon1", // 将启动页面图标设置成透明的空图片
   "startWindowBackground": "$color:start_window_background", // 背景颜色
   ```
2. 对于浅色模式和深色模式下，可以分别在entry模块的两个color.json配置文件中配置两套color资源，startWindowBackground配置白色和黑色即可。其中浅色模式的color.json文件路径为“src/main/resources/base/element/color.json”；深色模式的color.json文件路径为“src/main/resources/dark/element/color.json”。

   浅色模式：

   ```json
   {
     "color": [
       {
         "name": "start_window_background",
         "value": "#FFFFFF"
       }
     ]
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/-OS808MkRey8QFm1PZQ6pg/zh-cn_image_0000002628629350.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=946B2CB81C04A4719DF2FDFC9FA685BDE3233EF94438B270C58F596C805D2D4F "点击放大")

   深色模式：

   ```json
   {
     "color": [
       {
         "name": "start_window_background",
         "value": "#000000"
       }
     ]
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/raKVtu_ARGqVWAHftk4-PQ/zh-cn_image_0000002658988571.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=227414E48D9D3D82E70AB7E6CC72DBF80C2EA27500EE47E38E7AE29C696ED4D9 "点击放大")
