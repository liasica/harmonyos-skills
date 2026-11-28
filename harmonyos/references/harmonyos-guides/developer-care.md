---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/developer-care
title: 开发者关怀
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 开发者模式 > 开发者关怀
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:b1cbbab003085f5226cfccf16ae8699dd57f8475983509082804edfbffa733df
---

从HarmonyOS 6.1开始，支持开发者关怀功能。开发者关怀致力于为您提供安全友好的开发体验，解决您在设备调试过程中因系统安全保护机制而遇到的不便。例如：当您的设备多次出现系统异常重启后，出于安全考虑，系统将关闭并锁定开发者选项。若您的设备出现开发者选项开启失败的情况，可借助“开发者关怀”功能解决您的问题。

## 运行机制

考虑到您的设备可能处于不同的网络环境，我们提供了在线解锁与离线解锁2种方法，二者最大的区别在于您的设备是否能联网，以及解锁过程中是否需要您的协助。联网情况下，设备将自动上传解锁请求给AGC（AppGallery Connect，华为应用市场），并根据AGC下发的解锁凭据自动解锁设备的开发者选项；未联网情况下，上传解锁请求和下载解锁凭据将需要您的协助，具体如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zgLp1Kq-Q2ecMwvb9i8Qtg/zh-cn_image_0000002779566676.jpg?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEDDC42ABA9BA8725DA30D5C8DADB42C59A8CF435D155268E723FE0F0766DB25 "点击放大")

## 使用流程

本章节介绍解除开发者选项锁定的2种方法及其具体操作流程。

**开发者选项在线解锁**

* 使用在线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“取消”，打开WiFi或数据流量，设备联网后再次尝试打开开发者选项将触发设备进入自动解锁流程，5分钟内设备可自动解锁，届时再尝试打开开发者选项即可成功。

**开发者选项离线解锁**

* 使用离线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“离线解锁设备”，设备将生成离线解锁申请文件 。您将解锁申请文件导出到电脑，并访问AGC网站申请解锁，会拿到AGC网站生成的解锁凭据。最后，您把解锁凭据导入到设备中（与离线解锁申请文件同路径），再次进入“导出成功”弹窗界面，点击“解锁”按钮，即可打开开发者选项。

**图1** 解锁操作流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/5LINbHjzSACE20kCtFjKYQ/zh-cn_image_0000002808886345.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=80C33DE26AE70E2E21C8F02834A926F876391A9B26AFB151CD589CC71811C3BC "点击放大")

### 在线解锁

开启开发者选项失败，且您的设备具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 设备联网。

   点击“取消”按钮，打开设备WiFi或数据流量，确保设备可联网。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/j_GbQg5lQSyZy0RDkJAH-A/zh-cn_image_0000002779406704.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B23C7475B9E2657BD56AA705E26C73647930082C5AC9D29F6D9FE2E45B4364F "点击放大")
2. 触发在线解锁。

   您再次尝试打开开发者选项，触发在线自动解锁，在“开发者模式打开失败”弹窗界面点“取消”退出。
3. 解锁成功。

   由于网络和AGC云处理等原因，在线解锁可能存在一些延迟，您可每分钟尝试打开开发者选项，一般设备在触发在线解锁后5分钟内，可自动解锁。

### 离线解锁

开启开发者选项失败，且您的设备不具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 触发离线解锁，导出解锁申请文件到电脑。

   点击“离线解锁设备”按钮，触发离线解锁，在弹窗“导出成功”后，设备会在Download/SecurityGuardAssistant路径生成解锁申请文件panic.json，导出此文件到电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/TIB6Hn-aTxCnvbWikDAuvg/zh-cn_image_0000002808886341.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E68C812EBB47BDBE9EEBC99C0043C0573574E1249AFEEC2CA28B090B0277B2D "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/bNSBN5JKRciKULqwny0DVw/zh-cn_image_0000002808766261.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AE1104FD06A521FBDCD4A3C579AB3F8B5B85F7EF3836D04B933B673239B218F "点击放大")
2. 访问AGC网站，申请解锁凭据。

   在电脑端访问AGC网站【开发与服务】->【质量】->【开发者关怀】页面，上传解锁申请文件panic.json，获取解锁凭据文件。

   * AGC网址：[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject/461323198430420904/97458334310914890?extrainfo=)，登录您的华为开发者账户，进入后选择或者创建一个项目。
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前没有创建过项目，请点击【添加项目】，输入项目名称后点击【完成】。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/DXORvzBLTCiwZi7qifJFkQ/zh-cn_image_0000002779566674.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA4EB994E01A9063406B3CA9F85C486057AD8DFF6C1009D39B6F9C1FB0FBC476 "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/0dy17PE5ThWa8powCVcXkA/zh-cn_image_0000002779406700.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C9F31225DD2E0AEDEE6A3E122EA42E039A649427DD8216C0E65C36AA4F0C484 "点击放大")
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前创建过项目，选择已存在的项目即可。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/mzBq4jiMQX-57sis00fcMg/zh-cn_image_0000002779406698.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=72034A81BC2213249CD519C4877AE1A15B8ADA20C1D2A3593C85BB08A59A67EA "点击放大")
     + 在【开发与服务-项目】页面，【质量】栏目下即可看到【开发者关怀】菜单，具体如下图所示。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/I30LqjXjTfmFyznv4bkrpw/zh-cn_image_0000002808766265.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=E05676E5C757DF3E86CA24FB2F8451106B49898B20296E1ECB3BCC13236CE818 "点击放大")
   * 进入开发者关怀界面，上传解锁申请文件后，页面会生成1个解锁凭据文件panic.unlock，请下载该文件到电脑，具体如下图所示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/TOXEAz0ZS3yg94O61Shmrg/zh-cn_image_0000002779566684.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=175AF4170AC2DD139F238AD5961ADF03E5776A71DA14E7ACF42D3461465AA2E4 "点击放大")
3. 导入解锁凭据到设备并尝试开启开发者选项。

   把解锁凭据导入到设备中（与离线解锁申请文件同路径Download/SecurityGuardAssistant），再次尝试打开开发者选项。
4. 解锁成功。

   您点击“解锁”按钮后，弹出“解锁成功”提示，即可打开开发者选项。

## 常见问题

### 在线解锁如果一直失败，如何处理

在线解锁依赖设备的网络环境和AGC云的处理响应，可能存在失败的情况，如果多次尝试在线解锁失败，建议您稍后重试或者使用离线解锁的方式进行处理。
