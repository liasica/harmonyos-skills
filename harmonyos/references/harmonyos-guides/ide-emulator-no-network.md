---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-no-network
title: 离线部署模拟器
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 离线部署模拟器
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cb1714082f19f324b10eaaaa7d158a583bd03774f001d7c5cc8cb068f4ed12e9
---

如果开发者所使用的电脑处于完全无网络的离线环境中，需要先在一台可访问网络的电脑上准备好DevEco Studio并下载模拟器镜像，将DevEco Studio和模拟器镜像文件拷贝到无网络电脑中。

**有网络电脑：**

在可访问网络的电脑上下载安装DevEco Studio，并下载所需的模拟器镜像，具体可参考[创建模拟器](ide-emulator-create.md)。

例如在Windows电脑下载手机镜像，并指定镜像下载路径为D:\Sdk，实际完整的镜像路径是D:\Sdk\system-image\HarmonyOS-xxx\phone\_all\_x86。

**说明** 

如未指定镜像下载路径，默认路径请参考[创建模拟器](ide-emulator-create.md)。

**无网络电脑：**

1. 将DevEco Studio和模拟器镜像文件拷贝到无网络电脑中，需要注意有网络和无网络电脑的镜像子文件夹路径（如system-image\HarmonyOS-xxx\phone\_all\_x86）要保持一致。

   拷贝镜像时，在无网络电脑新建存放镜像的目录，如D:\No-network\Sdk，在此目录下新建镜像子文件夹路径system-image\HarmonyOS-xxx\phone\_all\_x86，将有网络电脑phone\_all\_x86下的所有文件拷贝到该路径下。
2. 在无网络电脑上创建模拟器，注意创建时将镜像路径更改为上一步骤的路径，如D:\No-network\Sdk，具体可参考[创建模拟器](ide-emulator-create.md)，创建成功后即可使用模拟器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/pdzTf45DTr-c8LIV0lLWGA/zh-cn_image_0000002701821808.png)
