---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-11
title: 跨端分享文件接收策略
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 跨端分享文件接收策略
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:26+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:b6bfe9e844b7a3a0161a7afd6d8e63b81dd155d6dc782259fff256fb16e5f068
---

## 问题现象

手机碰一碰或者隔空投送分享文件到PC，PC端是如何接收分享文件的。

## 背景知识

[碰一碰](../harmonyos-guides/knock-share.md)：双端设备需要在亮屏、且解锁的状态下并且都已开启华为分享服务（系统默认开启）的情况下。手机与手机间碰一碰，通过手机顶部的相碰触发、手机与PC/2in1设备碰一碰，通过手机顶部与PC窗口的相碰触发。

[隔空传送](../harmonyos-guides/gestures-share-overview.md)：支持用户通过“一抓一放”手势实现跨设备文件分享（图片、视频、文档等）以及跨设备链接分享。

## 解决方案

### 场景一：碰一碰

文件分享时按设备的不同类型，文件接收的策略存在差异。

* 手机接收文件

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1y-bsUMYRu-Mh9WAQCD9pQ/zh-cn_image_0000002658793795.png "点击放大")

  接收端将媒体文件存储到图库中，图库大图预览；非媒体文件存储到文件管理器中，单文件使用文件预览，多文件在文件管理器中高亮显示。
* PC/2in1设备接收文件：
  1. 手机碰一碰PC/2in1设备桌面时，可以默认碰一碰将媒体以及非媒体文件保存到文件管理中，文件管理中文件高亮显示。
  2. 手机PC/2in1设备应用窗口碰一碰时，应用可注册监听文件接收接口[on('dataReceive')](../harmonyos-references/share-harmony-share.md#ondatareceive)方法，将手机分享的文件存储于应用沙箱目录下，应用可自行处理预览方式。具体可参考：[分享内容直达应用界面](../harmonyos-guides/knock-share-pc-phones-sandbox.md)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/SavFzWDzQ0OuGHjwtCy33w/zh-cn_image_0000002628394528.png "点击放大")

碰一碰分享支持[指定应用直达](../harmonyos-guides/share-access-one-step.md#指定应用直达)能力，可实现同开发者账号下应用跨端指定应用直达。

**说明** 

手机与手机碰一碰对华为账号无要求，而手机与PC/2in1碰一碰则需登录同一华为账号方可进行分享。

### 场景二：隔空传送

当用户做出手势进行隔空传送分享时，系统触发回调，应用可以在回调中实现数据分享。

* 手机、平板接收文件：媒体文件存储至图库，在图库大图预览；非媒体文件存储至文件管理器，文件管理中文件高亮显示。
* PC/2in1设备接收文件：媒体以及非媒体文件存储至文件管理器，文件管理中文件高亮显示。

分享内容为App Linking链接时，将自动打开目标应用，并由应用处理链接传递的参数，实现内容的快速访问，详情参考[分享App Linking直达应用](../harmonyos-guides/gestures-share-scenes.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/BkgEI4AyRsu748rZ7gIfaQ/zh-cn_image_0000002628554420.png "点击放大")

[应用自定义数据类型](../harmonyos-guides/uniform-data-type-descriptors.md#应用自定义数据类型)文件分享接收端接收数据时遵循统一规则，文件接收端存储在文件管理“华为分享”目录，有可打开应用直接打开，无可打开应用弹出提示。更多详情请参考[目标设备接收分享数据一步直达体验](../harmonyos-guides/share-access-one-step.md)。
