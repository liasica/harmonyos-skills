---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/developer-care
title: 开发者关怀
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 开发者模式 > 开发者关怀
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:5f4f632e3aa5243a0ec60fc422e12959fe35e13abbb13728c27c749268bd7491
---

从HarmonyOS 6.1开始，支持开发者关怀功能。开发者关怀致力于为您提供安全友好的开发体验，解决您在设备调试过程中因系统安全保护机制而遇到的不便。例如：当您的设备多次出现系统异常重启后，出于安全考虑，系统将关闭并锁定开发者选项。若您的设备出现开发者选项开启失败的情况，可借助“开发者关怀”功能解决您的问题。

## 运行机制

考虑到您的设备可能处于不同的网络环境，我们提供了在线解锁与离线解锁2种方法，二者最大的区别在于您的设备是否能联网，以及解锁过程中是否需要您的协助。联网情况下，设备将自动上传解锁请求给AGC（AppGallery Connect，华为应用市场），并根据AGC下发的解锁凭据自动解锁设备的开发者选项；未联网情况下，上传解锁请求和下载解锁凭据将需要您的协助，具体如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/CN1d4afdSA-_40v28_v0pw/zh-cn_image_0000002779566676.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4C39284B69334E07C7ED61FAB236FD83AD405D3B0CAA8ADD3F7040D38685FBE "点击放大")

## 使用流程

本章节介绍解除开发者选项锁定的2种方法及其具体操作流程。

**开发者选项在线解锁**

* 使用在线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“取消”，打开WiFi或数据流量，设备联网后再次尝试打开开发者选项将触发设备进入自动解锁流程，5分钟内设备可自动解锁，届时再尝试打开开发者选项即可成功。

**开发者选项离线解锁**

* 使用离线解锁功能，您可以在出现“开发者模式打开失败”弹窗情况时，点击“离线解锁设备”，设备将生成离线解锁申请文件 。您将解锁申请文件导出到电脑，并访问AGC网站申请解锁，会拿到AGC网站生成的解锁凭据。最后，您把解锁凭据导入到设备中（与离线解锁申请文件同路径），再次进入“导出成功”弹窗界面，点击“解锁”按钮，即可打开开发者选项。

**图1** 解锁操作流程示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/uWFe_CjTSN2twnzH1O_pCQ/zh-cn_image_0000002808886345.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=041A09D7DB54502D990E8FECA1207BDE039EECA105E9FA50C9417F5129EA93D1 "点击放大")

### 在线解锁

开启开发者选项失败，且您的设备具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 设备联网。

   点击“取消”按钮，打开设备WiFi或数据流量，确保设备可联网。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/AJ9auP0lTt6QYfrd_ZyFXg/zh-cn_image_0000002779406704.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F32C89BD4D57C0E3646F5D0CB57C1F62F789B1B2825BBB1A469666529AB3F2F "点击放大")
2. 触发在线解锁。

   您再次尝试打开开发者选项，触发在线自动解锁，在“开发者模式打开失败”弹窗界面点“取消”退出。
3. 解锁成功。

   由于网络和AGC云处理等原因，在线解锁可能存在一些延迟，您可每分钟尝试打开开发者选项，一般设备在触发在线解锁后5分钟内，可自动解锁。

### 离线解锁

开启开发者选项失败，且您的设备不具备联网条件。

您尝试打开开发者选项，设备弹窗提示“开发者模式打开失败”。

1. 触发离线解锁，导出解锁申请文件到电脑。

   点击“离线解锁设备”按钮，触发离线解锁，在弹窗“导出成功”后，设备会在Download/SecurityGuardAssistant路径生成解锁申请文件panic.json，导出此文件到电脑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ymLFrs16RhCo8X6xsqjVjg/zh-cn_image_0000002808886341.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=250AAA69C9038EEC105822EA4D083C99C5EC312201B0B747E0A138B52735BD83 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/af3on5XJRUSYl2AK-WAgAQ/zh-cn_image_0000002808766261.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=68F4654281223CAAE2076034AE032ACB4C2FD7E2F71C020F5C0B08E2373B1443 "点击放大")
2. 访问AGC网站，申请解锁凭据。

   在电脑端访问AGC网站【开发与服务】->【质量】->【开发者关怀】页面，上传解锁申请文件panic.json，获取解锁凭据文件。

   * AGC网址：[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject/461323198430420904/97458334310914890?extrainfo=)，登录您的华为开发者账户，进入后选择或者创建一个项目。
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前没有创建过项目，请点击【添加项目】，输入项目名称后点击【完成】。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/cMc5DgQDTlWygjiUBSXoow/zh-cn_image_0000002779566674.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=134CDA5FFFD56B63A10D0310D6EDA3D27C6826FD9F385DF4499EF4B42CF512AF "点击放大")

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/9n40WqrETECryEaJi7jajA/zh-cn_image_0000002779406700.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=989B128A90420AF78AA0A35CFF0F33C4E5A09F75FB805431C2AABEB1E10884DC "点击放大")
     + 登录AGC网站后，选择【开发与服务】页面，如果您之前创建过项目，选择已存在的项目即可。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/gzsHAMf2RzKIlKiwtkzg0Q/zh-cn_image_0000002779406698.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=78E4B41B584C562C69B8C4D191AB0E0A1EB3D5DCDF0F4D7ABD5383064EED8E08 "点击放大")
     + 在【开发与服务-项目】页面，【质量】栏目下即可看到【开发者关怀】菜单，具体如下图所示。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/9EpRqd4tSq266TxruBBF3g/zh-cn_image_0000002808766265.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=936D7C33AD1285FC438353C16A4DEE4927C91EE93772AB5FC08F851A133841ED "点击放大")
   * 进入开发者关怀界面，上传解锁申请文件后，页面会生成1个解锁凭据文件panic.unlock，请下载该文件到电脑，具体如下图所示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/jMpax1s8RGG37T1yagMrwA/zh-cn_image_0000002779566684.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=397516DD71B3E77CFC7B3BB15C37B038991A9F17EFEF69020496F0069B1F8802 "点击放大")
3. 导入解锁凭据到设备并尝试开启开发者选项。

   把解锁凭据导入到设备中（与离线解锁申请文件同路径Download/SecurityGuardAssistant），再次尝试打开开发者选项。
4. 解锁成功。

   您点击“解锁”按钮后，弹出“解锁成功”提示，即可打开开发者选项。

## 常见问题

### 在线解锁如果一直失败，如何处理

在线解锁依赖设备的网络环境和AGC云的处理响应，可能存在失败的情况，如果多次尝试在线解锁失败，建议您稍后重试或者使用离线解锁的方式进行处理。
