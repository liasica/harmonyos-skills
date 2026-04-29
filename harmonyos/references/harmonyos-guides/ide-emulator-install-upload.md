---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-install-upload
title: 安装应用程序包和上传文件
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 安装应用程序包和上传文件
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:476f46cd61c5f1eb65a09731ca525fca05782b67c86131a82968700c5fc4c353
---

* 安装应用程序包

  您可以将本地的HAP包安装到模拟器上，只需要将本地的HAP包拖动到屏幕上即可进行安装，支持一次性拖拽安装多个HAP包。模拟器也支持安装包含HSP文件的应用，只需要将HSP和HAP一起拖动到屏幕上即可进行安装。

  您也可以在命令行窗口进入DevEco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc app install命令安装包。安装完成后，可在应用列表里查看已安装的应用。
* 上传文件

  您可以将本地文件上传到模拟器中，只需要将文件拖动至模拟器屏幕上即可。模拟器支持批量上传文件，上传的文件存放在虚拟设备的/storage/media/100/local/files/Docs/Download/目录下。您可以在模拟器上打开**文件管理 > 我的手机 > 下载**查看上传的文件。

  此外，您也可以在命令行窗口进入DevEco Studio安装目录的sdk\default\openharmony\toolchains目录下，使用hdc file send命令上传文件。

  从DevEco Studio 6.1.0 Beta2版本开始，使用API 21及以上的镜像时，上传的图片类文件将保存在图库中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/pLoC6vdgTcqp4CSO9KP4jA/zh-cn_image_0000002530911066.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054636Z&HW-CC-Expire=86400&HW-CC-Sign=5A5282EACAED48D2D4AAB2F3D89DABB34195F709B62721A2F9F994BC819B4929 "点击放大")
