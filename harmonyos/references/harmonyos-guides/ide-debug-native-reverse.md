---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:48e539ce41172311038d57adf4afa8afe54d26d8dc1d2ba309f702a2f7494c93
---

针对C/C++开发场景，DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式
* 反向Step Over回退到历史行
* 反向Resume执行到历史断点
* 在程序执行历史的记录点上查看全局、静态、局部变量值

## 前提条件

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build,Execution,Deployment > Debugger > C++ Debugger**设置界面，勾选**Enable time travel debug**开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/TxH90GpCTfKGV_1GZL9LbQ/zh-cn_image_0000002808886189.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=1405C8640AB1E35D34A0323964680A9B1FE28E280FA75D37E09358208ACB1B3B)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在Debugger中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/m8nDXZxzTgerbhwmaMKUfQ/zh-cn_image_0000002808766105.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2B750E98EC64A511F68B2F41F9EBAD010E236B97B01445168D9416E78A7C3C9)

   需要查看历史调试信息时，点击“Open Time Travel Debug”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/2tTl3h9PTSOc8iHuJWOwjw/zh-cn_image_0000002808766109.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=5958822B20DA9AEC1AE970D23818A68A0A0DE65F34EC902A9979486A1671F9A0)进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/QX_YucM9SzaSC3Uboe-VaQ/zh-cn_image_0000002779406548.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AC7F07257E1D25D5DF9E480511626A39ACF156D716957101D16ECFAC17C2AFC)

   其中，操作按钮说明如下：

   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/q4pym4izRvKNBZ7JaBGN7g/zh-cn_image_0000002779406552.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BD52748A109EE3142CA1D9E42529C5D106D30974763F62552FA1715A9B27F86)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/qnislT_KQIywl_95lMaAjg/zh-cn_image_0000002808886193.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=E04F9BA451316FD54DA7FD12029795BE77619F996A3B2900B479271191A873F4)：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/WCjVSizASkSb9jB6jiEvBQ/zh-cn_image_0000002779566532.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE5EAFD825553C1DD200E0914D329AEDC86ABEB68B195079379BA40BCCEC1145)：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/S7SgHAnsTCWtsT_9VEUpGQ/zh-cn_image_0000002808886185.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=44336CD13C8E52719B30A3D2489152285AA8815CE95A58A716E083FDEFC29946)：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/xDtJdDy-TLuJo3nm-88boA/zh-cn_image_0000002779566528.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CB55F83D58125C49497A61D5A5A94CA61CD8FCDFE36F48AE77F0106A225EA60)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

**说明** 

某些功能在反向调试模式下无法使用，此时会根据您的行为进行对应提示。
