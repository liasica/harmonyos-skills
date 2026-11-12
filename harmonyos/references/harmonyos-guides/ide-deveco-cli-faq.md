---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-faq
title: 常见问题
breadcrumb: 指南 > DevEco CLI > 常见问题
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d4dc5a9d46ad6aad8b7d0db08b7a47ef9a6b3d3c5701d0f8f5a670beafc6b4ad
---

## 在鸿蒙电脑执行DevEco CLI命令时，提示"Signal 5（core dumped）"

**问题现象**

DevEco CLI命令执行错误，提示"Signal 5（core dumped）"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/FAZBbNMYQT64L-aBJDK6yA/zh-cn_image_0000002779566638.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=94E0E503F88E96D2878200F1554FCE51B9AB87B9A3041919AB1E67B5B4CC364A "点击放大")

**可能原因**

使用其他来源（如DevNode-OH）的node，未使用DevEco Studio或Command Line Tools中自带的node。

**解决措施**

重新配置环境变量，具体请参考[搭建环境（鸿蒙电脑）](ide-deveco-cli-install.md#section31836342457)。

## 在鸿蒙电脑执行DevEco CLI命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/EfMQXF4lTH2LNVmU9i28pQ/zh-cn_image_0000002808886303.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7B52C19DD192CE86478657DD1F09ABC329F35F2E5D8F8208A123D1D298D3A18)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/qqw-FHbJSEeXqvi0JC7svw/zh-cn_image_0000002808766217.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=09139D538CF29451D6929CCA5A541EFA9430859E33613C20DC2B1D599BE3B291)

**可能原因**

鸿蒙电脑版DevEco CLI只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-cli命令安装尝鲜版。
