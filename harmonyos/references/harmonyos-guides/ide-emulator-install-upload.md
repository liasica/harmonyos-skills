---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-install-upload
title: 安装应用程序包和上传文件
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 安装应用程序包和上传文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48d45a8d2cc5cca48e64590ca684a58d5dd0913276d54ceb2fde7bc057a8fea0
---

* 安装应用程序包

  您可以将本地的HAP包安装到模拟器上，只需要将本地的HAP包拖动到屏幕上即可进行安装，支持一次性拖拽安装多个HAP包。模拟器也支持安装包含HSP文件的应用，只需要将HSP和HAP一起拖动到屏幕上即可进行安装。

  您也可以在命令行窗口进入DevEco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc app install命令安装包。安装完成后，可在应用列表里查看已安装的应用。
* 上传文件

  您可以将本地文件上传到模拟器中，只需要将文件拖动至模拟器屏幕上即可。模拟器支持批量上传文件，上传的文件存放在虚拟设备的/storage/media/100/local/files/Docs/Download/目录下。您可以在模拟器上打开**文件管理 > 我的手机 > 下载**查看上传的文件。

  此外，您也可以在命令行窗口进入DevEco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc file send命令上传文件。

  从DevEco Studio 6.1.0 Beta2版本开始，使用API 21及以上的镜像时，上传的图片类文件将保存在图库中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/AXFzDTFfRF6gQXgzIy6n9g/zh-cn_image_0000002530911066.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235641Z&HW-CC-Expire=86400&HW-CC-Sign=9A5A50DEEADBC5EAB2C3A02DDD0E8F5E4AC90D90F68EC802B9248FB30B5E02F0 "点击放大")
