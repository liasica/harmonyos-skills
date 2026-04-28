---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugcloudobj
title: 调试云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 调试云对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3da742b25be7a8623a03b43b3553e07dddf407178bcb7924e2f8bec229b5f11f
---

云对象开发完成后，您可以对其进行调试，以验证云对象代码运行是否正常。

目前DevEco Studio云对象调试支持本地调用和远程调用，请根据实际场景选择使用：

* [通过本地调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section248615546567)：在DevEco Studio调试本地开发好的云对象。支持单个调试和批量调试，并支持Run和Debug两种模式，调试功能丰富，常在云对象开发过程或问题定位过程中使用。
* [通过远程调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section123191549587)：先将云对象部署至AGC云端，然后直接在DevEco Studio调用云端云对象。此方式主要用于测试云对象在云端的运行情况、或补充测试因各种因素限制未能在本地调用方式中发现的问题。

## 前提条件

* 请确保您已登录。
* 如果您的工程有代码逻辑涉及云对象调用云数据库，您需在调试前先[将整个云工程部署到AGC云端](agc-harmonyos-clouddev-deploy.md)，否则云端将没有相关数据及环境变量。

## 通过本地调用方式调试云对象

您可在DevEco Studio调试本地开发好的云对象，支持单个调试和批量调试，并支持Run和Debug两种模式。

* 单个调试和批量调试流程相同，区别仅在于：单个调试是一次只为一个云对象启动本地调试，之后只能调用该云对象；批量调试是一次为“cloudfunctions”目录下所有云对象启动本地调试、然后逐个调用各个云对象。
* Run模式和Debug模式的区别在于：Debug模式支持使用断点来追踪云对象的运行情况，Run模式则不支持。

下文以Debug模式下调试单个云对象“my-cloud-object”为例，介绍如何在DevEco Studio调试本地云对象。

1. 右击“my-cloud-object”云对象目录，选择“Debug 'my-cloud-object'”。

   说明

   * 如需批量调试多个云对象，右击“cloudfunctions”目录，选择“Debug Cloud Functions”，即可启动该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，将会启动所有的云函数和云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/QuA3WGOYT8O649A8185phw/zh-cn_image_0000002179338428.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=5DC59EB70D6F45801496535389CE9D3C7F71ACE154CB1E9F1F9BD73D98ED3B1E)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示云对象已成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/CzZZRZonTAqnVAZJ2DPnOg/zh-cn_image_0000002179498092.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=E76553683AD66A3C24D5AE32E36236049FB97F1D8214E720F1192E321EE7F7F6)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行3）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/cOfkBRG6ROyZ-sSzZFQnng/zh-cn_image_0000002179498088.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=BC1D7E61DC1E66BFC487A7ED1631EF6882E9085777711FB28E90051DD059F38A)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发云对象调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/AkQ_ozJAQ-C0MgyxpY7F6w/zh-cn_image_0000002214704325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=8A0B4A21AFC27BDE333153565C048C6BA690C7A3591A24AA90BDCC335CB3A088)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云对象，此处以云对象“my-cloud-object”为例。
   * Environment：选择云对象调用环境。此处选择“Local”，表示本地调用。
   * Method：必填项，输入云对象的方法名称，如“add”。
   * Event：方法参数列表，JSON array格式，依次代表Method的入参。如add方法接收两个number类型的形参，num1与num2，那么填入“[1, 2]”表示构造num1=1，num2=2的请求。

     注意

     如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/L43ySiD6TGq1oXbRGQuEhA/zh-cn_image_0000002214858713.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=5552DEBBE20B9547816380CBF15EFC3E3950D25444803BF262A472B681534EAD)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/f-JyyUzMQ46zL1hECC6faw/zh-cn_image_0000002214704333.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=D45F6E6856FD360597E2206D3591E04830D768234FBFA109F2B2C67295410F48)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/ZtOt6TS4ROSgp_LNfFGYAw/zh-cn_image_0000002179498084.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=C06801F7BB20CA7F6FF9EBF5373F9C6A7276BD8BA5B888261F2AE01A246BD367)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/kMCqdVoMRZGLzlNnztg2mQ/zh-cn_image_0000002179498080.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=2141A6F47864885E49520E184E105054E1BD6CD1E2C4D3A084C7AA3FDA13A7D0)
7. 点击“Trigger”， 将会触发执行云对象的方法，执行结果将展示在“Result”框内。

   说明

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试云对象](agc-harmonyos-clouddev-debugcloudobj.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wo6FxxduQhC9ivddH8YT_A/zh-cn_image_0000002214704357.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=1457ECADF85A5E8BF8DA4CAF3B488209E3AFDF9A4D89577F1E44C7B3CD02C5D5)
8. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/NYMusoHMQv2-26wLtpvQfQ/zh-cn_image_0000002214704361.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=FF4416AD4E3D92CC7CDA5AE18C02E44A6630EFF9304C8057C66B63932F488022)，可停止调试。
9. 根据调试结果修改云对象代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/WcN7z2JNRcCvDxBrqFN06g/zh-cn_image_0000002179338408.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=1178E8E42DB77C10F23F47E4AFF933D9BE7B813EC247C8B014AB534992D909B9)重新以Debug模式启动调试，直至没有问题。
10. 参考步骤5~9，完成云对象其他方法或其他云对象的调试。

## 通过远程调用方式调试云对象

您还可以将云对象部署至AGC云端，然后在DevEco Studio调用云端云对象，以测试云对象在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署云对象](agc-harmonyos-clouddev-deploycloudobj.md)将需要调试的云对象部署至AGC云端。
2. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发云对象调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/brCu1X10RWuKdiVF4IVuPA/zh-cn_image_0000002179338432.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=352105E16EA3462CAECFB2250AF9C9648B361800E7773739669B4F48D8429B05)
3. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云对象，此处依然以“my-cloud-object”为例。
   * Environment：选择云对象调用环境。此处选择“Remote”，表示远程调用。
   * Method：输入云对象的方法名称，如“add”。
   * Event：方法参数列表，JSON array格式，按顺序代表Method的入参，如add方法接收两个number类型的形参，num1与num2，那么填入“[1, 2]”表示构造num1=1，num2=2的请求，如“[1, 2]”。

     注意

     如果Method的入参中的某一个是数组[]类型，那么Event中将至少包含两层方括号，如'[[1, 2], 3]'，外层的方括号表示参数列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/oUYn64l9QYWpmcL9H_hZ2A/zh-cn_image_0000002214704353.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=E8C62BA0704EA17F5308422A43923A5E6A9FA26E9970341668AAD469569F2CA5)
4. 点击“Trigger”， 将会触发执行云对象方法，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/qZaIFcxOSJeVwev8igs8Qg/zh-cn_image_0000002314529249.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=3D069CB452464DB181A57B68E5EB338278B6EBD1FBD00077B121DAB21CC0D0CE)
5. 点击“Logs”页签，还可查看打印的日志定位问题。修改云对象代码、重新部署云对象后再次执行远程调用，直至没有问题。
6. 参考步骤1~5，完成云对象其他方法或其他云对象的调试。
