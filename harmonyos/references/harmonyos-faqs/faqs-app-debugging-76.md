---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-76
title: Wearable和Lite Wearable穿戴设备真机调试和调测
breadcrumb: FAQ > DevEco Studio > 应用调试 > Wearable和Lite Wearable穿戴设备真机调试和调测
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:dc69a4ffd5842f2065f62ca155eec5d8721e01615de7cf61a099d8860bd7737a
---

## 问题现象

开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？

## 背景知识

* Wearable设备推荐使用[WiFi无线调试](../harmonyos-guides/ide-run-device.md#section9315596477)。
* 在Lite Wearable中运行应用/服务，依赖HarmonyOS NEXT版本以前的华为手机上的运动健康和应用调测助手APP辅助进行。

## 解决方案

* Wearable设备调试：

  前提条件：需要登录华为开发者账号才有无线调试选项。

  1. 将Wearable设备和PC连接到同一WLAN网络。

     在设置>系统>开发者选项中，打开"无线调试"或"通过WLAN调试"（Wearable设备）开关，并获取设备端的IP地址和端口号。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/LD6ljB6OQnavgLVcVgqQtQ/zh-cn_image_0000002680692122.png "点击放大")
  2. 连接设备，有两种方式。
     1. 在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/BrbUeWCKSuaX-es64IUtdg/zh-cn_image_0000002710371895.png "点击放大")
     2. 执行hdc命令，关于hdc工具的使用指导请参考[hdc](../harmonyos-guides/hdc.md)。

        hdc tconn设备IP地址:端口号。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/NarvSgixTJmGNXGgzBDtMA/zh-cn_image_0000002710212037.png)

        在菜单栏中，单击Run>Run'模块名称'或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。
  3. DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
* Lite wearable设备调试：

  前提条件：

  1. 运动健康app升级最新版本。
  2. 从华为应用市场安装应用调测助手APP。
  3. 提前对应用/服务进行[签名](../harmonyos-guides/ide-signing.md)。

  具体步骤：

  1. 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。
  2. 手机与电脑使用USB连接时，在手机上选择传输文件连接方式。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/q6EdjSXeT9GpsD_CZ98QqA/zh-cn_image_0000002680532244.png "点击放大")
  3. 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的"/sdcard/haps/"目录。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/RMqW0GodTe-3RlQBwEDJeQ/zh-cn_image_0000002710371897.png)
  4. 将Lite Wearable通过蓝牙与华为手机进行连接。
     1. 进入运动健康APP，在设备页签中，单击添加设备按钮。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/WRlHx4OIQBi9B4YkO4kblw/zh-cn_image_0000002710212041.png "点击放大")
     2. 进入手表列表中，选择对应的Lite Wearable型号。
     3. 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。
  5. 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
  6. 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/8Y9a6g41SQOhpRAMmpmuxw/zh-cn_image_0000002710212825.png "点击放大")
  7. 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。

## 常见FAQ

Q：HarmonyOS NEXT系统上能否开发Lite Wearable类型的手表应用？

A：Lite Wearable中运行应用/服务依赖HarmonyOS NEXT版本以前的手机上的运动健康和应用调测助手APP辅助进行，暂不支持在HarmonyOS NEXT系统上直接调试Lite Wearable设备。轻量级智能穿戴与智能穿戴在硬件能力和系统支持上不同，暂时无法仅开发一版实现通用。Wearable是当前更主流的方向，是HarmonyOS NEXT生态重点支持的穿戴设备类型。

Q：通过应用调测助手向Lite Wearable设备安装HAP时提示"安装失败：40.配置文件格式错误"怎么办？

A：该问题通常是由于工程级[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)中[compatibleSdkVersion](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)配置格式不正确导致。compatibleSdkVersion必须写成5.0.0(12)格式，不能写成其他字符串格式。

Q：GT系列手表能否用于穿戴应用测试？

A：可以。GT系列手表属于Lite Wearable（轻量级智能穿戴）设备，应按Lite Wearable方式进行测试，不支持Wearable（智能穿戴）直连方式。当前支持的GT系列手表型号及对应API版本如下：WATCH GT 2（API 5）、WATCH GT 2 Pro（API 6）、WATCH GT 3（API 6）、WATCH GT 4（API 10）、WATCH GT 5（API 12），开发时需按具体型号的API能力做兼容。创建工程时选择"[Lite] Empty Ability"模板，设备类型设为"Lite Wearable"。GT真机不能直接连接DevEco Studio，需手动签名并在调试Profile中注册设备，将HAP拷贝至华为手机，通过运动健康完成配对，再用应用调测助手安装到手表。基础功能也可先用Lite Wearable预览器或仿真器验证。
