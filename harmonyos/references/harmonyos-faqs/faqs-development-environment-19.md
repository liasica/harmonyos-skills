---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-19
title: DevEco Studio未识别到真机设备如何处理
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio未识别到真机设备如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8e724c051bc7e68554f7907663fbe558a4fc31cdb61468daf22bdf9d0c5fb5af
---

## 问题现象

真机通过USB连接电脑，DevEco Studio开发工具未识别到真机设备，无法调试运行。

## 背景知识

当前使用真机调试，可以采用USB连接方式或者无线调试的连接方式。两种连接方式是互斥的，只能使用一种。

**一、使用USB连接方式**：

1. 使用USB方式，将Phone或Tablet与PC进行连接。
2. 在设置>系统>开发者选项中，打开“USB调试”开关（确保设备已连接USB）。
3. 在Phone或Tablet中会弹出“允许USB调试”的弹框如下图，单击允许。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/_SFdtMcpTNmQPwrcEKwG2w/zh-cn_image_0000002628564958.png "点击放大")

**二、使用无线调试连接方式**：

1. 将Phone/Tablet和PC连接到同一WLAN网络。
2. 在设置>系统>开发者选项中，打开“无线调试”开关，并获取Phone/Tablet端的IP地址和端口号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/JM8hoVC2SA2qqBqPdh4rbA/zh-cn_image_0000002628405052.png "点击放大")
3. 在PC中执行hdc tconn设备IP地址:端口号命令连接设备。

## 解决方案

由于存在软件/系统或者硬件原因，可以参考按如下步骤，从软件/系统到硬件按步骤逐一排查下。

**一、软件/系统原因**：

1. 检查设备是否开启“开发者模式”，若没有开启，在设备上打开“开发者选项”，并且打开“USB调试”开关。
2. 连接数据线后，USB连接方式选择“仅充电”。
3. 检查DevEco Studio版本，工具里点击Help -> About DevEco Studio。
4. 检查设备系统与DevEco Studio版本、SDK版本是否配套，请参考[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)。
5. 根据电脑的操作系统，点击[下载地址](https://developer.huawei.com/consumer/cn/download/deveco-studio)选择对应的DevEco Studio版本。
6. 判断hdc与设备的连接情况，判断命令：hdc list targets、hdc shell。
7. 如果上述两个命令不正常，可参考[常见问题](../harmonyos-guides/hdc.md#常见问题)处理解决。
8. 若操作后还是不能连接，请重启设备，然后尝试重新连接。
9. 卸载Windows设备上的VPN软件，再次连接真机。

**二、硬件原因**：

1. 请检查使用的USB连接线是否为充电线而非数据线，请更换为满足USB2.0标准的数据线。
2. 如果使用了拓展坞识别不到，建议使用直连方式再试下，排除拓展坞的问题。
3. 当前的USB数据口可能损坏，请检查端口驱动是否正常，或更换另一个USB数据口后重新尝试。

## 常见FAQ

Q：打开DevEco Testing工具尝试连接手机设备，在设备列表里面无法显示设备，请问如何排查？

A：请参考如下步骤进行排查：

1. 请在cmd中执行hdc list targets命令查询能否识别到设备。
2. 如提示“不是内部或外部命令”，请前往DevEco Testing安装路径，找到hdc.exe（Program Files\DevEco Testing\app\resources\bin），拖入cmd中再次执行hdc list targets命令。
3. 若能识别到，请在任务管理器中，将hdc线程kill后，重新进入DevEco Testing创建任务页，查看设备列表是否显示。
4. 检查当前DevEco Testing版本是否为最新，可以前往[下载中心](https://developer.huawei.com/consumer/cn/download/)更新到最新版本，重新尝试连接设备。

Q：真机调试时连接USB之后，点击传输文件，在DevEco Studio中的真机列表就找不到此设备了？

A：可以根据[使用设备连接助手排查问题](../harmonyos-guides/ide-run-device.md#section155318499334)来排查下。

Q：使用Mac电脑安装DevEco Studio后，通过USB连接到HarmonyOS PC设备进行真机调试无反应，无法找到设备。

A：PC真机调试需要将USB插入正确接口，可以将USB调试选项关闭、重新开启时系统给出提示：USB需要插在右侧的口上才能调试，按提示操作重新连接即可。

Q：hdc工具无法识别不同系统版本的设备？已知5.0及以上下载最新版DevEco Studio开发工具，使用SDK中的hdc即可，历史版本如4.2/3.0版本如何识别设备？

A：目前DevEco Studio 5.0.0及以上版本仅适用于HarmonyOS 5以及以上版本设备开发调试使用，低系统版本设备如HarmonyOS 4.x的设备可以使用DevEco Studio 3.1.1 Release版本的IDE，下载地址：[DevEco Studio历史版本下载](https://developer.huawei.com/consumer/cn/deveco-studio/archive/)。
