---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-reverse
title: 反向调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 反向调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8768ecccb48a7e39ccc3f70b2d1804a881c89aae203f03089baf39c9aae3911b
---

针对C/C++开发场景，鸿蒙电脑DevEco Studio在提供基础调试能力的基础上，同时提供反向调试能力，帮助开发者更好地理解代码和更迅速定位问题。

反向调试是指在调试过程中可以回退到历史行和历史断点，查看历史调试信息，包括线程、堆栈和变量信息。支持的调试操作为：

* 进入/退出反向调试模式。
* 反向Step Over回退到历史行。
* 反向Resume执行到历史断点。
* 在程序执行历史的记录点上查看全局、静态、局部变量值。

## 前提条件

在**文件 > 设置 > 扩展 > C++调试**界面，勾选**开启反向调试**后点击**应用**，开启C++反向调试开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/MOuFXvuASRGRvTQjigREpw/zh-cn_image_0000002810750811.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5371414FA17816177CEF4285742961C24254CE249D415D6266C52D435332B473)

## 操作步骤

1. 设置断点，进入调试模式。
2. 开启反向调试开关后，在调试器中会出现反向调试相关按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/R3WZvz_PT-GD3xHQpjLLQQ/zh-cn_image_0000002810750805.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=483929E47FF33DBDC6F06CC2E32FA22CFDECB85753522E9113528CA0507F3280 "点击放大")

   需要查看历史调试信息时，点击“Open Reverse Mode”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/dvfLWW5lT5a-OFNDn0xXVg/zh-cn_image_0000002810630701.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE227CB7D27EA5FDBB198196633CF910B11B571F06A571365751787F03136114 "点击放大")进入反向调试模式，您可以在此模式下进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/zP7CeDjrRqu17ldVf4k8wQ/zh-cn_image_0000002781471156.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D99D47DCBD7D3220EA058A185863231093D3FBBFA36CDF129B27701B1D6B42D5)

   其中，操作按钮说明如下：
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/NqEfTZdsQFC99qAXeK-MgQ/zh-cn_image_0000002810750817.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D724478237726E4F7779202BDDD89F64D64BBC708E2B56EDDD1DD8B6A344816)：退出反向调试模式。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/e9nJM9wJSgeksJzzOj4K6w/zh-cn_image_0000002810750813.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=05ECFDFC3A1F662610EA05D19B0D09CBFC0554FF2EFA2FC45884F37F5A00E692 "点击放大")：切换当前高亮行到下一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/dEfmcLBaQhOlwz-lIO346g/zh-cn_image_0000002781311226.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4784D400E75872B54A26F9C686ECCBF224CDE67D0928DC8667BBE191D50A5278 "点击放大")：切换当前高亮行到上一个历史断点，并显示断点相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/p9Z4XDxRSpiOn1_hUE0AQg/zh-cn_image_0000002810630705.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E1D8D30CC964F493C56D71AD616AC82752E8DD17AB39B97B83A85645A34BA7D "点击放大")：切换当前高亮行到下一个历史行，并显示历史行相关信息。
   * ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/9G89Do26TgisxKqe2NBvTA/zh-cn_image_0000002781471148.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A43FDC4F4F4159FEA6E1AAB2D9F784F13366597D69E4E744F7A52252F523F902)：切换当前高亮行到上一个历史行，并显示历史行相关信息。

## 时间线视图

进入反向调试模式后，支持C++调试流程中停留过的历史断点和历史行之间的跳转和调试信息查看。

图中的红点表示历史停留过的断点或行，点击跳转到对应断点或行，并显示相关栈帧信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/OD6Uckm2S3-IS2CgADtQ-w/zh-cn_image_0000002810630707.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FE820AAFC8875B3B5BF73BC4DDD6B880F238E1E96A8CE35360116521A354459)
