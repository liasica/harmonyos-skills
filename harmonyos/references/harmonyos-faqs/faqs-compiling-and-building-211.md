---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-211
title: 一键编译打包所有product
breadcrumb: FAQ > DevEco Studio > 编译构建 > 一键编译打包所有product
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:971cd969f983d46fff3b64cc6d16936fde6a7a20b015ef8a681ce2b0d938bca6
---

## 问题现象

当项目包含多个product时，如何实现一键批量编译打包？目前只能逐个product进行编译打包，效率较低。

## 背景知识

[hvigorw](../harmonyos-guides/ide-hvigor-commandline.md#section16300629103)作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。

编译构建参数详情见[编译构建](../harmonyos-guides/ide-hvigor-commandline.md#section9580122622012)。

## 解决方案

通过hvigorw命令实现一键编译打包所有product。对应的命令行如下（这里的default、default1、default2替换为对应的product，如有更多product，可按相同格式追加命令）：

```screen
hvigorw -p product=default -p buildMode=release assembleApp; hvigorw -p product=default1 -p buildMode=release assembleApp; hvigorw -p product=default2 -p buildMode=release assembleApp;
```

DevEco Studio配置的详细步骤如下：

1. 编辑配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/XTD2U-AmQMSWazui9V4-Tw/zh-cn_image_0000002658928501.png "点击放大")
2. 点击加号创建Shell Script。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cRUx22M9RM-F44feRQ918w/zh-cn_image_0000002628409282.png "点击放大")
3. 选择Script text，将命令写入，多个命令用分号隔开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_KEspRFpSZCJpw8TwHOenw/zh-cn_image_0000002658808553.png "点击放大")
4. 切换创建的脚本，执行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gZQ8thPHSGSdkIaXMky7VQ/zh-cn_image_0000002628569178.png "点击放大")
