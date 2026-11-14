---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-faq
title: 常见问题
breadcrumb: 指南 > DevEco CLI > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a864006ba05397aa6df91238fc0e51ae1b00abe39ea0a018e7da0203b9729542
---

## 在鸿蒙电脑执行DevEco CLI命令时，提示"Signal 5（core dumped）"

**问题现象**

DevEco CLI命令执行错误，提示"Signal 5（core dumped）"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/7PGd8TevTFC3fF_H2W4QiQ/zh-cn_image_0000002779566638.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=93D58C59DB7C18B2DD318A65877A06D5B22CCE283D4C73BC6EA5CB38E3877365 "点击放大")

**可能原因**

使用其他来源（如DevNode-OH）的node，未使用DevEco Studio或Command Line Tools中自带的node。

**解决措施**

重新配置环境变量，具体请参考[搭建环境（鸿蒙电脑）](ide-deveco-cli-install.md#section31836342457)。

## 在鸿蒙电脑执行DevEco CLI命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/xwVS3u-RT5ST7m_bitGf7w/zh-cn_image_0000002808886303.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=996581D3A8752F9A01886191791084BEEE89537CB0B917D345353B24C6FEE0F2)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/lY9N1zNYSASUXfuZztdtEQ/zh-cn_image_0000002808766217.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=A52F3CF0AE9EA33E2844058B7F2686546674B76986AA4E9A44D874FCE9865E04)

**可能原因**

鸿蒙电脑版DevEco CLI只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-cli命令安装尝鲜版。
