---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/developer-care
title: 开发者关怀
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 开发者模式 > 开发者关怀
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e92fb8748ef056507dcbff8adb08a90f7f17021700425c2cbff525d2078cd9c5
---

从HarmonyOS 6.1开始，支持开发者关怀功能。开发者关怀致力于为您提供安全友好的开发体验，解决您在设备调试过程中因系统安全保护机制而遇到的不便。例如：当您的设备多次出现系统异常重启后，出于安全考虑，系统将关闭并锁定开发者选项。若您的设备出现开发者选项开启失败的情况，可借助“开发者关怀”功能解决您的问题。

## 运行机制

考虑到您的设备可能处于不同的网络环境，我们提供了在线解锁与离线解锁2种方法，二者最大的区别在于您的设备是否能联网，以及解锁过程中是否需要您的协助。联网情况下，设备将自动上传解锁请求给AGC（AppGallery Connect，华为应用市场），并根据AGC下发的解锁凭据自动解锁设备的开发者选项；未联网情况下，上传解锁请求和下载解锁凭据将需要您的协助，具体如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/N0UbmeS6Q_Sg2HaLmH7apg/zh-cn_image_0000002530912772.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=E04C446223141424D6CB5785E0AFD8FA04719C8C1161173629A6B21FF075CC90 "点击放大")

## 使用流程

本章节介绍解除开发者选项锁定的2种方法及其具体操作流程。

**开发者选项在线解锁**

* 使用在线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“取消”，打开WiFi或数据流量，设备联网后再次尝试打开开发者选项将触发设备进入自动解锁流程，5分钟内设备可自动解锁，届时再尝试打开开发者选项即可成功。

**开发者选项离线解锁**

* 使用离线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“离线解锁设备”，设备将生成离线解锁申请文件 。您将解锁申请文件导出到电脑，并访问AGC网站申请解锁，会拿到AGC网站生成的解锁凭据。最后，您把解锁凭据导入到设备中（与离线解锁申请文件同路径），再次进入“导出成功”弹窗界面，点击“解锁”按钮，即可打开开发者选项。

**图1** 解锁操作流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/w1IgHtrWSqq0lr0EeJFICw/zh-cn_image_0000002561752727.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=E38F66AC353396453555206D85CE257880266A45D114DBF2CC319953FA977915 "点击放大")

### 在线解锁

开启开发者选项失败，且您的设备具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 设备联网。

   点击“取消”按钮，打开设备WiFi或数据流量，确保设备可联网。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/LABSifH7SoG99CLZSL8sFw/zh-cn_image_0000002530752786.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=36F80F55B23ACF55969E429597885D04C0302150FAE12662F36FD11DBD173E52 "点击放大")
2. 触发在线解锁。

   您再次尝试打开开发者选项，触发在线自动解锁，在“开发者模式打开失败”弹窗界面点“取消”退出。
3. 解锁成功。

   由于网络和AGC云处理等原因，在线解锁可能存在一些延迟，您可每分钟尝试打开开发者选项，一般设备在触发在线解锁后5分钟内，可自动解锁。

### 离线解锁

开启开发者选项失败，且您的设备不具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 触发离线解锁，导出解锁申请文件到电脑。

   点击“离线解锁设备”按钮，触发离线解锁，在弹窗“导出成功”后，设备会在Download/SecurityGuardAssistant路径生成解锁申请文件panic.json，导出此文件到电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/fDqb_JGHQbm7W546ABbHmg/zh-cn_image_0000002530752784.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=A2EA360DA9CF2956BD485E133A56D5A1F57F21A488E5F2EBF1DB95B41874A14D "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/LAfx9WXhT12zewYvMaOqaQ/zh-cn_image_0000002561752725.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=AF43B1CC2E7773C7597AFE75ACD684E70E91D219B53A46460318EE4A88F0C620 "点击放大")
2. 访问AGC网站，申请解锁凭据。

   在电脑端访问AGC网站【开发与服务】->【质量】->【开发者关怀】页面，上传解锁申请文件panic.json，获取解锁凭据文件。

   * AGC网址：[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject/461323198430420904/97458334310914890?extrainfo=)，登录您的华为开发者账户，进入后选择或者创建一个项目。
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前没有创建过项目，请点击【添加项目】，输入项目名称后点击【完成】。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Vfb9ptEESN6VLASNS5bcZg/zh-cn_image_0000002530912768.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=F48DD1AD92CC12785183A204451CF86FCBAF0650DC3509B8DE865DD50DC229C3 "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/z6_m-YwVTEyyBl0Iyf7Q8Q/zh-cn_image_0000002561832701.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=2C828E78DA9C6D881D45D751B381ACD6E1477268BC191B101FD290EB235A5606 "点击放大")
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前创建过项目，选择已存在的项目即可。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/HihshKp0RwmSjF7PcRMLvA/zh-cn_image_0000002530752774.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=7359C5B192478CC89C337E9F02FDAF36CB272A464481CAFE31CFB951A28150F0 "点击放大")
     + 在【开发与服务-项目】页面，【质量】栏目下即可看到【开发者关怀】菜单，具体如下图所示。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/xodgtj6tTG6SC-KgGSYWXg/zh-cn_image_0000002561752731.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=C0E1DEB3931902515534569A85C67EBA771B9357EC73E140AC50E31B937DC162 "点击放大")
   * 进入开发者关怀界面，上传解锁申请文件后，页面会生成1个解锁凭据文件panic.unlock，请下载该文件到电脑，具体如下图所示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/QjPGCT_0T0KpZEPFJfYPbA/zh-cn_image_0000002530752790.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=DF61FC26890921B549977755A995BBEEE4F378FC55CF94CC6FF8F0EF026941DD "点击放大")
3. 导入解锁凭据到设备并尝试开启开发者选项。

   把解锁凭据导入到设备中（与离线解锁申请文件同路径Download/SecurityGuardAssistant），再次尝试打开开发者选项。
4. 解锁成功。

   您点击“解锁”按钮后，弹出“解锁成功”提示，即可打开开发者选项。

## 常见问题

### 在线解锁如果一直失败，如何处理

在线解锁依赖设备的网络环境和AGC云的处理响应，可能存在失败的情况，如果多次尝试在线解锁失败，建议您稍后重试或者使用离线解锁的方式进行处理。
