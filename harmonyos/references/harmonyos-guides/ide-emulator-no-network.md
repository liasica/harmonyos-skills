---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-no-network
title: 离线部署模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 离线部署模拟器
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60d89dffb39939648a8759c3753060ff03b6e7cc6c6e5d5e76db5a03e1582add
---

如果开发者所使用的电脑处于完全无网络的离线环境中，需要先在一台可访问网络的电脑上准备好DevEco Studio并下载模拟器镜像，将DevEco Studio和模拟器镜像文件拷贝到无网络电脑中。

**有网络电脑：**

在可访问网络的电脑上下载安装DevEco Studio，并下载所需的模拟器镜像，具体可参考[创建模拟器](ide-emulator-create.md)。

例如在Windows电脑下载手机镜像，并指定镜像下载路径为D:\Sdk，实际完整的镜像路径是D:\Sdk\system-image\HarmonyOS-xxx\phone\_all\_x86。

说明

如未指定镜像下载路径，默认路径请参考[创建模拟器](ide-emulator-create.md)。

**无网络电脑：**

1. 将DevEco Studio和模拟器镜像文件拷贝到无网络电脑中，需要注意有网络和无网络电脑的镜像子文件夹路径（如system-image\HarmonyOS-xxx\phone\_all\_x86）要保持一致。

   拷贝镜像时，在无网络电脑新建存放镜像的目录，如D:\No-network\Sdk，在此目录下新建镜像子文件夹路径system-image\HarmonyOS-xxx\phone\_all\_x86，将有网络电脑phone\_all\_x86下的所有文件拷贝到该路径下。
2. 在无网络电脑上创建模拟器，注意创建时将镜像路径更改为上个步骤的路径，如D:\No-network\Sdk，具体可参考[创建模拟器](ide-emulator-create.md)，创建成功后即可使用模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/h_vcOf4iQsKDNaoKV3nILg/zh-cn_image_0000002530751070.png?HW-CC-KV=V1&HW-CC-Date=20260427T235643Z&HW-CC-Expire=86400&HW-CC-Sign=BEA7F3A044CB1F8DF3C44655251292100422CFC034DE5DA6537749EDA97CDD14)
