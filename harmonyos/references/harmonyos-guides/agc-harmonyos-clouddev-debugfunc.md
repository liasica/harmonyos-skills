---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugfunc
title: 调试函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 调试函数
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:eb0bca536e8f622c7c8790286da06bd9f434a366f78fd387b05d4a5b5ed7d42e
---

函数开发完成后，您可以对函数进行调试，以验证函数代码运行是否正常。

目前DevEco Studio函数调试支持本地调用和远程调用，请根据实际场景选择使用：

* [通过本地调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section248615546567)：在DevEco Studio调试本地开发好的函数。支持单个调试和批量调试，并支持Run和Debug两种模式，调试功能丰富，常在函数开发过程或问题定位过程中使用。
* [通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)：先将函数部署至HarmonyOS 开发者中心，然后直接在DevEco Studio调用云端函数。此方式主要用于测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调用方式中发现的问题。

## 前提条件

* 请确保您已登录。
* 如果您的工程有代码逻辑涉及云函数调用云数据库，您需在调试前先[将整个云工程部署到HarmonyOS 开发者中心](agc-harmonyos-clouddev-deploy.md)，否则云端将没有相关数据及环境变量。

## 通过本地调用方式调试函数

您可在DevEco Studio调试本地开发好的函数，支持单个调试和批量调试，并支持Run和Debug两种模式。

* 单个调试和批量调试流程相同，区别仅在于：单个调试是一次只为一个函数启动本地调试，之后只能调用该函数；批量调试是一次为“cloudfunctions”目录下所有函数启动本地调试、然后逐个调用各个函数。
* Run模式和Debug模式的区别在于：Debug模式支持使用断点来追踪函数的运行情况，Run模式则不支持。

下文以Debug模式下调试单个函数“my-cloud-function”为例，介绍如何在DevEco Studio调试本地函数。

1. 右击“my-cloud-function”函数目录，选择“Debug 'my-cloud-function'”。

   **说明** 

   * 直接从当前路径下Debug，使用的是默认的Debug配置，您也可[自定义Debug配置](agc-harmonyos-clouddev-debugfunc.md#section65830284215)。自定义Debug配置后再从此路径下Debug，将优先采用自定义Debug配置。
   * 如需批量调试多个函数，右击“cloudfunctions”目录，选择“Debug Cloud Functions”，即可启动该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，将会启动所有的云函数和云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/F8F7QDX_RRy51NQq9kDb6A/zh-cn_image_0000002214858717.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=CECDA2ABF2A6FE196D3E8DB315CF2CFBBF671AC07C9585115B3CE815C34A530C)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示函数成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/bJsBUZkyR2yJeLDtHhmZ5g/zh-cn_image_0000002214704369.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=13CA8D86CC0C4ECE46A21B21ADBC5143CB25D20003EC12331BC2A175CF77BC43)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行15）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/1UPlaEowSUu6GG31NaUNVg/zh-cn_image_0000002533684069.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=D55E2EBCA52F5777CC06D9EC87A46C3EE61DBC0DE21382023D6C44610FCCF8B3)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/xI00ubjOSO2-GFD0cPj0HA/zh-cn_image_0000002179338456.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=23DD66462DA419D8B4D6B48D00B1004B5EC47A553C8D2F0E9412BAD2BB7D7910)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Local”，表示本地调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/wPKMttQYSumZ3TPd4M3OfQ/zh-cn_image_0000002179338412.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=A340B96FD0A569EC5BEA223986A5093700457563361B4B4DD5846097C2BBB1EC)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/s1WcvyYUSvGl4bjxszSdZw/zh-cn_image_0000002179498072.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=507B83245B7B56EEB5C59944D2F9EB72CCD32BCF0B06160373050E736DDAD26E)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/asrNnVCATDmLYbf0jYY8sA/zh-cn_image_0000002179498132.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A8ED5EB893B9127F39E7EFA45D12EDA9D5277EEEBCCD07F84D80FBC7AF7773A)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/aeVw7VzMToC6drNa40IUiA/zh-cn_image_0000002278063192.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=128360060ED07EC92EB3CFF164F6E52A3C0188FCBAD4881E78C521179BB5D91D)
7. 点击“Trigger”， 将会触发执行用户函数代码。执行结果将展示在“Result”框内，“cloudfunctions”窗口同时打印调试日志。

   **说明** 

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/UBLV6Mb6S9SXMyyhlgcnvQ/zh-cn_image_0000002503613920.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D53C40EB73BA72E2D16B52E0EC9844770E3AC6E84B683F5DD3ACB63E6C4AEB9)
8. （可选）如[配置了环境变量](agc-harmonyos-clouddev-debugfunc.md#li15793566149)，可将变量信息传入到函数执行环境中，用于函数运行时读取。

   ```screen
   logger.info(context.env.name);//name为环境变量名称
   ```

   如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/l02vgeLtT7ejII1moQAtJw/zh-cn_image_0000002503615754.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9483543CC85497F1027CA352AF00D79BB4B8C1DF3BD0292ACB508954B9D5E08)
9. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/h-2N3lokSXGmWPB3S9SimQ/zh-cn_image_0000002179338396.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFD8156E825E3034CD80854DA262A96C496767BA72278F491CC54C71349D2434)，可停止调试。
10. 根据调试结果修改函数代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/QBdbHWooRvm5o7FlEG6qdg/zh-cn_image_0000002179338420.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9E99472AB3E6FFB6946E01EF0654FF565E90FB1C1CFF0F3BDC6A51191257C36)重新以Debug模式启动调试，直至没有问题。
11. 参考步骤5~10，完成其他函数的调试。

## 通过远程调用方式调试函数

您还可以将函数部署至HarmonyOS 开发者中心，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署函数](agc-harmonyos-clouddev-deployfunc.md)将需要调试的函数部署至HarmonyOS 开发者中心。
2. （可选）如函数代码涉及访问环境变量，需在HarmonyOS 开发者中心函数列表中点击函数名称，为函数配置环境变量的值，供函数在运行时读取和使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/4takNw2ESxKfqeTgoTAISA/zh-cn_image_0000002214858729.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=47C416256FDB9758609A6A80B51BC2418C2F03E4D1D48D2D26F531F7EEC7ACDE)
3. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/FTGVZf1xS2yH4wvMylVTHw/zh-cn_image_0000002179498140.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7B5DF7D88D9ACCD9DDBF08EB746B3A4AC99E7003D2990A8DD06081D26FEEAC2)
4. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处依然以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Remote”，表示远程调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/z7L063eETvmDlrdT4PlAlw/zh-cn_image_0000002179338388.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=0126E2195B7CB309ACD5BAE52521988F3DB718706E5DD2EACEADB7C7F9B6CAA5)
5. 点击“Trigger”， 将会触发执行用户函数代码，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/zKgnbbF7Qumv5CO098n3jQ/zh-cn_image_0000002214704345.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F43C32C55C24353C217F949C452BE6A1B4F7005E90666157583E73524922BB7)
6. 点击“Logs”页签，可查看打印的日志定位问题。修改函数代码、重新部署函数后再次执行远程调用，直至没有问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GJwR2tdLRrWOXXdHPnKeHw/zh-cn_image_0000002535303613.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BDB13C3B9FF9C369DF56E09592F6BA7BD70BC96E672FF73D01922CE075E28B1)
7. 参考步骤1~5，完成其他函数的调试。

## （可选）自定义Run/Debug配置

直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。

1. 在菜单栏选择“Run > Edit Configurations”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/-sg9moJ1TFaqEJdJDMZI2w/zh-cn_image_0000002179498096.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDE7951ACC1DEC1EB06D44C092DBA22CEB6414F94A509A84E6169FE9C9D45EF3)
2. 在“Run/Debug Configurations”窗口，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/vC66ACGAR76pfVL0J3pnug/zh-cn_image_0000002214858773.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=119094E0F6A36C01400734311DEEFDBE6F52908B84E64F1CA172A9335C8A9456)，选择“Cloud Functions”，新增一个Run/Debug配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/McDnuOg6Q7OeYhwFClM4rw/zh-cn_image_0000002214704341.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=2249F4E8AA56A2F0CA66D57A62AE61E45555872896BD83DE2961AEE62CC522E2)
3. 自定义Run/Debug配置，完成后点击“Run”或“Debug”即可立即按当前自定义配置启动本地调试。

   如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/GN4YAGrVTymkKMUYK-cdfQ/zh-cn_image_0000002179338416.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AE37E07495B6B2F8B21088E8DC3320DFB71C78FA0542CF758A864C90E217F27)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/1OdPdO9zRom7Wp_qam9nPA/zh-cn_image_0000002214704373.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5B23872CBED91A1F6949367FAC5B027AF844399A009EB14723EABB0A73C5146)进行Run或Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/mgsQBQjuRb-aD2eUAZ5wwg/zh-cn_image_0000002214704377.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F528A620AC5E7DCF97AD2172DC39ECCD5F8F8F274A1153709738353E5D31D1F)
   * Name：Run/Debug配置的名称，如“functions-custom1”。
   * Server IP Address：HTTP服务端监听IP地址，默认为localhost，支持切换为您的局域网IP地址。
   * Server Port：HTTP服务端监听端口。默认为“18090”，自定义端口号建议大于1024。勾选“Auto increment”表示如当前端口被占用则端口号自动加“1”。
   * Environment variables：函数运行的环境变量，为key-value形式。

     点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/RX5O5FbrRXyuGT54peg-Ag/zh-cn_image_0000002179338424.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=969814FF03F16AC5AE34BB99549564C110396AC93E623A2FA7640A51740D688A)
