---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugcloudobj
title: 调试云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 调试云对象
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:e4a38648e97960fe4b2f5db6e30a98b499ba90bd4c88e39dfdaaaa5483925357
---

云对象开发完成后，您可以对其进行调试，以验证云对象代码运行是否正常。

目前DevEco Studio云对象调试支持本地调用和远程调用，请根据实际场景选择使用：

* [通过本地调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section248615546567)：在DevEco Studio调试本地开发好的云对象。支持单个调试和批量调试，并支持Run和Debug两种模式，调试功能丰富，常在云对象开发过程或问题定位过程中使用。
* [通过远程调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section123191549587)：先将云对象部署至HarmonyOS 开发者中心，然后直接在DevEco Studio调用云端云对象。此方式主要用于测试云对象在云端的运行情况、或补充测试因各种因素限制未能在本地调用方式中发现的问题。

## 前提条件

* 请确保您已登录。
* 如果您的工程有代码逻辑涉及云对象调用云数据库，您需在调试前先[将整个云工程部署到HarmonyOS 开发者中心](agc-harmonyos-clouddev-deploy.md)，否则云端将没有相关数据及环境变量。

## 通过本地调用方式调试云对象

您可在DevEco Studio调试本地开发好的云对象，支持单个调试和批量调试，并支持Run和Debug两种模式。

* 单个调试和批量调试流程相同，区别仅在于：单个调试是一次只为一个云对象启动本地调试，之后只能调用该云对象；批量调试是一次为“cloudfunctions”目录下所有云对象启动本地调试、然后逐个调用各个云对象。
* Run模式和Debug模式的区别在于：Debug模式支持使用断点来追踪云对象的运行情况，Run模式则不支持。

下文以Debug模式下调试单个云对象“my-cloud-object”为例，介绍如何在DevEco Studio调试本地云对象。

1. 右击“my-cloud-object”云对象目录，选择“Debug 'my-cloud-object'”。

   **说明** 

   * 如需批量调试多个云对象，右击“cloudfunctions”目录，选择“Debug Cloud Functions”，即可启动该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，将会启动所有的云函数和云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/RDTNB1YYQy-zxt1edh5yxw/zh-cn_image_0000002179338428.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CB15FB3B480F63E9C9E92980DF6835F54F5361D18D07374974E1D3F62C7B058)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示云对象已成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/qh6yy9ceT4uzsnKnfc-Nrw/zh-cn_image_0000002179498092.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=55B05B901930AE4E42C05C3184A038DB24F81C917459375185DD71E834477A6E)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行3）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EP16ZdPXSjG4B48O0mY1WA/zh-cn_image_0000002179498088.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A93BF2E73126E781B2C6178E593DCD3BE6B97E8739D4322B8BD7BA9A137D14F)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发云对象调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/j1X3JLAyQOOTH86qyH_a-g/zh-cn_image_0000002214704325.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=F450FBA7E70F83507AD9357B7B5D1F3E88CF69BD7DC41CCD81121992499CD25D)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云对象，此处以云对象“my-cloud-object”为例。
   * Environment：选择云对象调用环境。此处选择“Local”，表示本地调用。
   * Method：必填项，输入云对象的方法名称，如“add”。
   * Event：方法参数列表，JSON array格式，依次代表Method的入参。如add方法接收两个number类型的形参，num1与num2，那么填入“[1, 2]”表示构造num1=1，num2=2的请求。

     **注意** 

     如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/syHlOC1aQXKN65hw6olMCA/zh-cn_image_0000002214858713.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DF725F81EE46C2259B8A5A974C7104F7F655B1A74FF9922284D65B672D553E9)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/aHPGBu99TLCGHAhpm4JOZw/zh-cn_image_0000002214704333.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=853B0AD4FB7C4B00C1B24FBC745C31250700957EF59EE66B86F39F61A9BD41D8)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/fGogYJMzSEu8mMV1ILngBg/zh-cn_image_0000002179498084.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7B9EA5BB650AC80E7A10AB25C227F1724165E17CAB421BE0F626AF540DF0A60)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/47hxkh2mRDqjGSXTDg_YkQ/zh-cn_image_0000002179498080.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=C63BBF5C9C3F068316CAA8C46EDCBE9324E594555CC5350FDE8258295EC17205)
7. 点击“Trigger”， 将会触发执行云对象的方法，执行结果将展示在“Result”框内。

   **说明** 

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/C8G5-GztTrCr8LpcFFqfZg/zh-cn_image_0000002214704357.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=235B76EEFE0CCA8D5BF839386D22210273162DD5FC7D744D25D1D6343B20EDF5)
8. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Orwae4mOQbyYLnPFNzaiaw/zh-cn_image_0000002214704361.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B12BEEBCD95C3B53AFE1F5FF0D385A21824E66A027FEC49C14FB2873D2B19AE)，可停止调试。
9. 根据调试结果修改云对象代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/aIHd528YS_iQMFF5famtdw/zh-cn_image_0000002179338408.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA94DB95823D384E4A0F01F1E2FE9FF614D10168A8AC77721E417CBC1123AC25)重新以Debug模式启动调试，直至没有问题。
10. 参考步骤5~9，完成云对象其他方法或其他云对象的调试。

## 通过远程调用方式调试云对象

您还可以将云对象部署至HarmonyOS 开发者中心，然后在DevEco Studio调用云端云对象，以测试云对象在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署云对象](agc-harmonyos-clouddev-deploycloudobj.md)将需要调试的云对象部署至HarmonyOS 开发者中心。
2. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发云对象调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/20nTh742SoGtF_POLjaG2w/zh-cn_image_0000002179338432.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BAA677DE393842740DA108C640046369CD5F47F8491889ECB7749F6CDBE88EB)
3. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云对象，此处依然以“my-cloud-object”为例。
   * Environment：选择云对象调用环境。此处选择“Remote”，表示远程调用。
   * Method：输入云对象的方法名称，如“add”。
   * Event：方法参数列表，JSON array格式，按顺序代表Method的入参，如add方法接收两个number类型的形参，num1与num2，那么填入“[1, 2]”表示构造num1=1，num2=2的请求，如“[1, 2]”。

     **注意** 

     如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/3OGg2n2sTx-YdRp6jqnotA/zh-cn_image_0000002214704353.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDF9AF023A5B08B1D108EC88E728E39060566DD3E9E98F74CE236784C4B05893)
4. 点击“Trigger”， 将会触发执行云对象方法，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/CMQGZjh2RXyJ3g9c-Yhoxw/zh-cn_image_0000002314529249.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=38122655FFF4E97B2DD942231FB57809D1E9A01E167D9FFC52B5DD39CA18A3DA)
5. 点击“Logs”页签，还可查看打印的日志定位问题。修改云对象代码、重新部署云对象后再次执行远程调用，直至没有问题。
6. 参考步骤1~5，完成云对象其他方法或其他云对象的调试。
