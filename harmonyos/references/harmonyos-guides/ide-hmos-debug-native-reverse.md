---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b12136b4356daca65d72a56e5f288034f21ea403796d162eec11a13ab6ec2cc6
---

针对C/C++开发场景，鸿蒙电脑DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式。
* 反向Step Over回退到历史行。
* 反向Resume执行到历史断点。
* 在程序执行历史的记录点上查看全局、静态、局部变量值。

## 前提条件

在**文件 > 设置 > 扩展 > C++调试**界面，勾选**开启反向调试**后点击**应用**，开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/T-X30ow0TdSVWJX-6RvlCA/zh-cn_image_0000002820680965.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6B5805F88B31A444A76DE45696EC93A2350FA9D7F202AD9A24AE6F551777BEB)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在调试器中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/IYYKeIFnStuw6laJjVcUrg/zh-cn_image_0000002820720977.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=11D606CE1E2DD803EBC470B87DFC2633E5903FF9B30D931CAF1F91718A1F6B24 "点击放大")

   需要查看历史调试信息时，点击“Open Reverse Mode”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/23F9Fd_hTZuJwNJSPQH6gQ/zh-cn_image_0000002792001014.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=07C6D89EE0F4188EA36C373990431E6D22A383C88ADCEC017D1803D47849BD85 "点击放大")进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/f5qgt-lXRkKZTIYQJIEX9Q/zh-cn_image_0000002791841030.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC1F1CCD042BB7216DEA316843930ED8C8912D6ED5B2385FB36CA00AC2A175D3)

   其中，操作按钮说明如下：
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/bU2h2z6BRUGTaybV5Ui1dA/zh-cn_image_0000002791841038.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=54C136BE76B28C6C29F299DEF8E9F83349CC01122B3025FBEAC2B5C3D1D87131)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/CuWEykyoTGCGZw5aa7d0UQ/zh-cn_image_0000002820680967.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D16936DB54C7AF37903E40813CD5B92979477F69B04BAAF7F6C81C1DBA895C1E "点击放大")：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/p3wkF_-UQMqYab6VPaB3ag/zh-cn_image_0000002791841034.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8B436BE7656F1D7E4FAA50396FF642CF4464FAD00E8E42020AC9660B9C16754 "点击放大")：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ancCC8fHR2OKFrhApIQUMw/zh-cn_image_0000002820680971.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DDFD4060F307FB4CEA42446AEF8DD1F4AE0EBFAF5EB271863EC4E9C9D399840 "点击放大")：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/D507AAZxRoeqEUU8iQKfUA/zh-cn_image_0000002791841036.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FB4D3B70B0A925EF47F1718C61DD8B2600895A99EF263B224CE2C825B995CA9)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

## 时间线视图

进入反向调试模式后，支持C++调试流程中停留过的历史断点和历史行之间的跳转和调试信息查看。

图中的红点表示历史停留过的断点或行，点击跳转到对应断点或行，并显示相关栈帧信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/2MTWBYdzSDKpt6uHDdF8Qw/zh-cn_image_0000002792001012.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=67C872F18162B3B3AF2F01E8A30EF2E0191A4B3080662C8AEEA357D1444C7D2F)
