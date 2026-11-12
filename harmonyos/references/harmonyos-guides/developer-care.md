---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/developer-care
title: 开发者关怀
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 开发者模式 > 开发者关怀
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:6d92b3c38f599584aa0428c37a9a18c03183d5a10e7c02514077a8bba49f98e0
---

从HarmonyOS 6.1开始，支持开发者关怀功能。开发者关怀致力于为您提供安全友好的开发体验，解决您在设备调试过程中因系统安全保护机制而遇到的不便。例如：当您的设备多次出现系统异常重启后，出于安全考虑，系统将关闭并锁定开发者选项。若您的设备出现开发者选项开启失败的情况，可借助“开发者关怀”功能解决您的问题。

## 运行机制

考虑到您的设备可能处于不同的网络环境，我们提供了在线解锁与离线解锁2种方法，二者最大的区别在于您的设备是否能联网，以及解锁过程中是否需要您的协助。联网情况下，设备将自动上传解锁请求给AGC（AppGallery Connect，华为应用市场），并根据AGC下发的解锁凭据自动解锁设备的开发者选项；未联网情况下，上传解锁请求和下载解锁凭据将需要您的协助，具体如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/zAyXnoxqR8iLKRYhEh8t7Q/zh-cn_image_0000002779566676.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=01A7194EA6121BFDB445B1F06E9F06A61A8718FAD3A63550E7AA521B75A460B0 "点击放大")

## 使用流程

本章节介绍解除开发者选项锁定的2种方法及其具体操作流程。

**开发者选项在线解锁**

* 使用在线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“取消”，打开WiFi或数据流量，设备联网后再次尝试打开开发者选项将触发设备进入自动解锁流程，5分钟内设备可自动解锁，届时再尝试打开开发者选项即可成功。

**开发者选项离线解锁**

* 使用离线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“离线解锁设备”，设备将生成离线解锁申请文件 。您将解锁申请文件导出到电脑，并访问AGC网站申请解锁，会拿到AGC网站生成的解锁凭据。最后，您把解锁凭据导入到设备中（与离线解锁申请文件同路径），再次进入“导出成功”弹窗界面，点击“解锁”按钮，即可打开开发者选项。

**图1** 解锁操作流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/y13IyNB3RnuqQ2cJa5ofSQ/zh-cn_image_0000002808886345.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=51F8E36B7744685FADA7228B54F5A7EEFD09162054421BBD6B7EB17723AEEAE3 "点击放大")

### 在线解锁

开启开发者选项失败，且您的设备具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 设备联网。

   点击“取消”按钮，打开设备WiFi或数据流量，确保设备可联网。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/XWMxFdNyQl2_9iDrdKUv_Q/zh-cn_image_0000002779406704.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D26AED90C9DCF16F827EE489073988E33924A3233065066A9FE91AAA553D272 "点击放大")
2. 触发在线解锁。

   您再次尝试打开开发者选项，触发在线自动解锁，在“开发者模式打开失败”弹窗界面点“取消”退出。
3. 解锁成功。

   由于网络和AGC云处理等原因，在线解锁可能存在一些延迟，您可每分钟尝试打开开发者选项，一般设备在触发在线解锁后5分钟内，可自动解锁。

### 离线解锁

开启开发者选项失败，且您的设备不具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 触发离线解锁，导出解锁申请文件到电脑。

   点击“离线解锁设备”按钮，触发离线解锁，在弹窗“导出成功”后，设备会在Download/SecurityGuardAssistant路径生成解锁申请文件panic.json，导出此文件到电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/-A6ImqcJSjSt8fHQ5iI1tg/zh-cn_image_0000002808886341.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E20C58A581EAEC01A8AF7A28A0696A6698791BDAD1AAE56EFF1130FDA898353 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/N2TlwSbGTjmEMIfFDQLd6A/zh-cn_image_0000002808766261.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=756A47520E64B786C5E47BDDA036D64BD6EEF6CFB3A78CD8E6FB6F6410CBBFE3 "点击放大")
2. 访问AGC网站，申请解锁凭据。

   在电脑端访问AGC网站【开发与服务】->【质量】->【开发者关怀】页面，上传解锁申请文件panic.json，获取解锁凭据文件。

   * AGC网址：[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject/461323198430420904/97458334310914890?extrainfo=)，登录您的华为开发者账户，进入后选择或者创建一个项目。
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前没有创建过项目，请点击【添加项目】，输入项目名称后点击【完成】。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/3-JT85XZSyeLPvHdHit2ag/zh-cn_image_0000002779566674.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD4BE7987BC7C71E9D4494928342268CC863EE7BB0E3476EE21DEB7D649B7EDF "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/B3Uym7PtRkuU-Oppx3JiFA/zh-cn_image_0000002779406700.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=941D52B3967AE68265EB30403AEB91E78ECDDE29223FE4DB82DADB176890A943 "点击放大")
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前创建过项目，选择已存在的项目即可。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/m6592jXQSzuOy7iuSb6sOQ/zh-cn_image_0000002779406698.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCE4DF46FF1092BD7B7E98C84E6381AE308ED750F3D78F636F55FB0DD9D41765 "点击放大")
     + 在【开发与服务-项目】页面，【质量】栏目下即可看到【开发者关怀】菜单，具体如下图所示。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/yHZlK-qXSlCYDjWrPxtkbg/zh-cn_image_0000002808766265.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=83CB1B5779870058764B3742AB992D5695FF7DAE1DE6BC6FF8B6E1A6DC26B1DA "点击放大")
   * 进入开发者关怀界面，上传解锁申请文件后，页面会生成1个解锁凭据文件panic.unlock，请下载该文件到电脑，具体如下图所示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/s-jX4va6QWq1GytFz8sHhw/zh-cn_image_0000002779566684.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=73203228E822EA619F8250BF582E854964CDC0B3A2D2C773291A8C4E8B6BDDA3 "点击放大")
3. 导入解锁凭据到设备并尝试开启开发者选项。

   把解锁凭据导入到设备中（与离线解锁申请文件同路径Download/SecurityGuardAssistant），再次尝试打开开发者选项。
4. 解锁成功。

   您点击“解锁”按钮后，弹出“解锁成功”提示，即可打开开发者选项。

## 常见问题

### 在线解锁如果一直失败，如何处理

在线解锁依赖设备的网络环境和AGC云的处理响应，可能存在失败的情况，如果多次尝试在线解锁失败，建议您稍后重试或者使用离线解锁的方式进行处理。
