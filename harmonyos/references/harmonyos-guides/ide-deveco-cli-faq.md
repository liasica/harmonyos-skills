---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-faq
title: 常见问题
breadcrumb: 指南 > DevEco CLI > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f8830d54d4169461ca3341458bf8fb52298db7b471f7807f79f0c754074c47fc
---

## 在鸿蒙电脑执行DevEco CLI命令时，提示"Signal 5（core dumped）"

**问题现象**

DevEco CLI命令执行错误，提示"Signal 5（core dumped）"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/hEgflCLKSHawRpDj2PVwng/zh-cn_image_0000002778756703.png "点击放大")

**可能原因**

使用其他来源（如DevNode-OH）的node，未使用DevEco Studio或Command Line Tools中自带的node。

**解决措施**

重新配置环境变量，具体请参考[搭建环境（鸿蒙电脑）](ide-deveco-cli-install.md#section31836342457)。

## 在鸿蒙电脑执行DevEco CLI命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/lJY-uiy1QaKjFqjF1-oYTg/zh-cn_image_0000002749157634.png)

**可能原因**

配置环境变量时，未使用命令行解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，直接鼠标右键解压，导致压缩包中的文件执行权限和软链接丢失。

**解决措施**

在终端中执行以下命令，对命令行工具解压。更多请参考[搭建环境（鸿蒙电脑）](ide-deveco-cli-install.md#section31836342457)。

```shell
tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
```

## 在鸿蒙电脑执行npm install -g @deveco/deveco-cli@stable命令报错

**问题现象**

在鸿蒙电脑上执行npm install -g @deveco/deveco-cli@stable命令安装DevEco CLI时，有报错提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/pJoqLBG8TOWdOwBZJ1wfCA/zh-cn_image_0000002778648371.png)

**可能原因**

鸿蒙电脑版DevEco CLI只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-cli命令安装尝鲜版。
