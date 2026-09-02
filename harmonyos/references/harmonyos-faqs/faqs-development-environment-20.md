---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-20
title: Mac安装DevEco-Studio后启动报错“NSInternalInconsistencyException”如何解决
breadcrumb: FAQ > DevEco Studio > 环境准备 > Mac安装DevEco-Studio后启动报错“NSInternalInconsistencyException”如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f8ec5bfa2fc18b93096da109fc79ad3c8db348c8f12f3268cf1cc53c759a8bcd
---

## 问题现象

Mac环境下，安装DevEco Studio后启动报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/2HAhbImGTiGzB5M3lns8GA/zh-cn_image_0000002658924269.png "点击放大")

报错信息如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fk4DniyJS3q2BBh2KoY_ug/zh-cn_image_0000002658804323.png "点击放大")

## 背景知识

Mac环境下安装DevEco Studio[操作指导](../harmonyos-guides/ide-software-install.md#section102166218352)。

## 解决方案

对于启动报错可以按照如下步骤处理：

1. 找到DevEco Studio安装目录，用命令行sh bin/inspect.sh启动DevEco Studio，分析终端打印的错误日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/GJ4Tm2PmTMuRuW0NkjxZXA/zh-cn_image_0000002628564966.png "点击放大")
2. 根据报错内容DEVECOSTUDIO\_VM\_OPTIONS = /Users/{USER\_NAME}/Downloads/jihuo.live/jihuo-tool/vmoptions/devecostudio.vmoptions，可以判断启动脚本被修改了。
3. 删除启动脚本，启动脚本默认路径为“/Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist”，删除后重启Mac即可。

## 总结

* 由于DevEco Studio和Jetbrains用的是相同的启动脚本，且脚本会一直沿用，如果脚本被修改，会导致不可知的问题。
* 如果运行过Jetbrains的破解软件，修改了Jetbrains启动脚本中的环境变量，会导致Java虚拟机无法启动，DevEco Studio无法打开。
