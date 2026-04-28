---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugfunc
title: 调试函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 调试函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:deb43f71abc071d6bcd3579830ba9be7e6cfedd04fc66f42de5223850c812b23
---

函数开发完成后，您可以对函数进行调试，以验证函数代码运行是否正常。

目前DevEco Studio函数调试支持本地调用和远程调用，请根据实际场景选择使用：

* [通过本地调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section248615546567)：在DevEco Studio调试本地开发好的函数。支持单个调试和批量调试，并支持Run和Debug两种模式，调试功能丰富，常在函数开发过程或问题定位过程中使用。
* [通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)：先将函数部署至AGC云端，然后直接在DevEco Studio调用云端函数。此方式主要用于测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调用方式中发现的问题。

## 前提条件

* 请确保您已登录。
* 如果您的工程有代码逻辑涉及云函数调用云数据库，您需在调试前先[将整个云工程部署到AGC云端](agc-harmonyos-clouddev-deploy.md)，否则云端将没有相关数据及环境变量。

## 通过本地调用方式调试函数

您可在DevEco Studio调试本地开发好的函数，支持单个调试和批量调试，并支持Run和Debug两种模式。

* 单个调试和批量调试流程相同，区别仅在于：单个调试是一次只为一个函数启动本地调试，之后只能调用该函数；批量调试是一次为“cloudfunctions”目录下所有函数启动本地调试、然后逐个调用各个函数。
* Run模式和Debug模式的区别在于：Debug模式支持使用断点来追踪函数的运行情况，Run模式则不支持。

下文以Debug模式下调试单个函数“my-cloud-function”为例，介绍如何在DevEco Studio调试本地函数。

1. 右击“my-cloud-function”函数目录，选择“Debug 'my-cloud-function'”。

   说明

   * 直接从当前路径下Debug，使用的是默认的Debug配置，您也可[自定义Debug配置](agc-harmonyos-clouddev-debugfunc.md#section65830284215)。自定义Debug配置后再从此路径下Debug，将优先采用自定义Debug配置。
   * 如需批量调试多个函数，右击“cloudfunctions”目录，选择“Debug Cloud Functions”，即可启动该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，将会启动所有的云函数和云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/OojVH9QeR-iLesd_QgqEag/zh-cn_image_0000002214858717.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=15F9CDAB96344ECBB19E4F7220BAF14A40D981A05E1CD6876A6A9344EA39F23E)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示函数成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/sggstFMvQIueHVhbR4jicQ/zh-cn_image_0000002214704369.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=B6E996FE5B89B8002828F52CC8D900C524436D269CCDBF23409F30F10F174FFB)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行15）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/CgBFM6AwSUakyP57IVwXWA/zh-cn_image_0000002533684069.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=7AF31AACEC74A1154EFB10090CBDD7B4709E653524785BCA9179B92CBA192785)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/A60CT7FRSammu4LjFj0H4Q/zh-cn_image_0000002179338456.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=3C8FD7AC53AB664A424F159D7EBAC7138B5B9635A60F57027D697CD8EE85EF53)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Local”，表示本地调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/BZfr_yl8TCa1Ml9HdNM6-g/zh-cn_image_0000002179338412.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=BADA8814BCADED3480309A4DDC60F102D00EF1DCF4F774ED7FBE25F2F53EEFA7)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xyMrDKLiR2aqOSzgE0P-HA/zh-cn_image_0000002179498072.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=4999C38AAD5859FDF5924F911E1C663C4429F7AC1B0681A96C38284386B43916)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/0wxkXinOQrC4VIYAuUdYtQ/zh-cn_image_0000002179498132.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=84929B677B40423ECEF069C65867B354F6AA74E7ACE8BF7AF0D15C4D684C316F)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qXhaBS1uQtq4f5Rx_WmJ8w/zh-cn_image_0000002278063192.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=45F7D6A72107D32B4A3428AC35368B351731326DDA3BAACF8BF6EA0FF24904DE)
7. 点击“Trigger”， 将会触发执行用户函数代码。执行结果将展示在“Result”框内，“cloudfunctions”窗口同时打印调试日志。

   说明

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/LB_yCafAREiBMo_xxNgj-g/zh-cn_image_0000002503613920.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=81DAE1B2DC3F3DD56EBD2B0483DCABFD5CBBF6648539C39B37A2C259DB2F63E0)
8. （可选）如[配置了环境变量](agc-harmonyos-clouddev-debugfunc.md#li15793566149)，可将变量信息传入到函数执行环境中，用于函数运行时读取。

   ```
   1. logger.info(context.env.name);//name为环境变量名称
   ```

   如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/50JlVcKZRguM0sEz_Ig14w/zh-cn_image_0000002503615754.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=B8975006DA1895E5A09E459D5E914140F514FFF5717E6F75277691D0F5028F4C)
9. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/vJ2QWSe9Rc6t8TOLa_tKTg/zh-cn_image_0000002179338396.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=69DA03A3D6C5ABCF3BC9ADC21C8BF566931D6B6C1AA1440A97C0E796122708D9)，可停止调试。
10. 根据调试结果修改函数代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Rh2uTpjOTtCMgYNfGjuzKA/zh-cn_image_0000002179338420.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=B1C2BFF747A5955899E3A292E44348702DBD7EC849407B6E6A36A4B6EDB4393D)重新以Debug模式启动调试，直至没有问题。
11. 参考步骤5~10，完成其他函数的调试。

## 通过远程调用方式调试函数

您还可以将函数部署至AGC云端，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署函数](agc-harmonyos-clouddev-deployfunc.md)将需要调试的函数部署至AGC云端。
2. （可选）如函数代码涉及访问环境变量，需在AGC Portal函数列表中点击函数名称，为函数配置环境变量的值，供函数在运行时读取和使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/1ZxD_Ws3SQ6qrJFRO1BUig/zh-cn_image_0000002214858729.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=4260ABAE1A448BEFE92F09549569F20E00FE4E97041A80B3BE29B6C71401CBF7)
3. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/wOQMN5rcQzid0pX5aBz6ag/zh-cn_image_0000002179498140.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=685A4CBB2013C3D014052F6BAC5F1E8676ACAEC90835A22E5B120A1E32D88EA8)
4. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处依然以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Remote”，表示远程调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/kBmNLeOaQuWw2uk9stZyhA/zh-cn_image_0000002179338388.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=158AA5D749C31E6B277B24C1601915FF34D25192FB7F9D77461920E3E3CA4B08)
5. 点击“Trigger”， 将会触发执行用户函数代码，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/z-OG0FyUQ3KDBDQfjpO_sw/zh-cn_image_0000002214704345.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=772DC850C4D89915CCE3E6B64E0AEBCF1251094031EDB5C39BBBDCBEF2A81D7B)
6. 点击“Logs”页签，可查看打印的日志定位问题。修改函数代码、重新部署函数后再次执行远程调用，直至没有问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/I4eF3VglTT-7-d26Gmz4AQ/zh-cn_image_0000002535303613.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=2405E789F3AC9857807752FF2CBC8B07AFE77C6D75DB41D2C5E9B090FA1E3EDA)
7. 参考步骤1~5，完成其他函数的调试。

## （可选）自定义Run/Debug配置

直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。

1. 在菜单栏选择“Run > Edit Configurations”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/9SZofqOETEOfVettgrSEEg/zh-cn_image_0000002179498096.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=189CB09F0FB954BB3007C129C32D557D6B9A14B919ED426325E2EFC24F0CA2EC)
2. 在“Run/Debug Configurations”窗口，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/EYRl2IMyRTCrDp05kAdLKQ/zh-cn_image_0000002214858773.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=B8B77C42F8BB9BF91D11FB0CC9E967CE403E2D8A0FD89E0A93F19921EB28F3C5)，选择“Cloud Functions”，新增一个Run/Debug配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/AEf5hUnYRTynTce6iupYHg/zh-cn_image_0000002214704341.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=AB4E8F841D7231DE397A10EA4F1D695976D16B2EE1F26307404A03FC11B529F0)
3. 自定义Run/Debug配置，完成后点击“Run”或“Debug”即可立即按当前自定义配置启动本地调试。

   如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NwPAGGnhSX-5czQXXMeBnA/zh-cn_image_0000002179338416.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=FCA054AB0D463B1D1604453E4EADE06FE32C3A11E4E368274DEF02660D8050D1)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/OHpcPl7bQ5Sg9-aLutf7UQ/zh-cn_image_0000002214704373.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=DE13700CCDF0D41C62C22CD43CFF3E2CB625B1F18201700023E34D4BFBDF00FA)进行Run或Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/XOsx--IATsehOkYWdfbFqw/zh-cn_image_0000002214704377.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=0C42A82A5F2A2DC276131EA14930144121AD7BC58D65021071218F047F9A7567)
   * Name：Run/Debug配置的名称，如“functions-custom1”。
   * Server IP Address：HTTP服务端监听IP地址，默认为localhost，支持切换为您的局域网IP地址。
   * Server Port：HTTP服务端监听端口。默认为“18090”，自定义端口号建议大于1024。勾选“Auto increment”表示如当前端口被占用则端口号自动加“1”。
   * Environment variables：函数运行的环境变量，为key-value形式。

     点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/vWz8ebkQSea-awWijJ6RSQ/zh-cn_image_0000002179338424.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=B74B130EF787856B760C4823C5CAE1187C25F164E705927447C8465287816CA8)
