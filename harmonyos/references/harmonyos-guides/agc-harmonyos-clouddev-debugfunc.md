---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugfunc
title: 调试函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 调试函数
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:ead62aca225f3f2201ca8fb1fd538724af01ee1c0a64789cb92b6203372361f9
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/oR71GmBWTfCEkWGWel-vCA/zh-cn_image_0000002214858717.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5E94BE0EA1FE1CBFAF387FCFD26DBA7BD155B5CD1CD88550BE26EE02D7D4372)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示函数成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Tntdj9bfTYyRrTFXPzMEbw/zh-cn_image_0000002214704369.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7AB1D28D51DC217D6896D5CF45C4180183E8133802B4800F22B81CE6D9B813C)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行15）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/DnbNt6fPQ3S-Y0CxMTGivQ/zh-cn_image_0000002533684069.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB1FB3EA0A1BB41A4914D9711CC4FD1177D56F25F56D99A277247237BEAD40EC)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Ks8N_x6ITQ2eleaPgWT6mg/zh-cn_image_0000002179338456.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A185AB7C37616E79F3E39E312ACAE0B4BB4CB5CBCF421A7DE2D2AD9A691C2CB)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Local”，表示本地调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/sHhmDZNkS9iyIqH_22Otvw/zh-cn_image_0000002179338412.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE581B32872B8E8CCFD71BDAAD70C1E4C25A38E0C8C8C65547E1614153D6C973)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/NANPdwdASHWZJR5qwuGOZw/zh-cn_image_0000002179498072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=40EE317922BCB5522D1C0A7D017D9DCA74AA3CC18C9EAE42B654DAF177A8E852)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/8fQumSSQSjmWyeCqD6mtkQ/zh-cn_image_0000002179498132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D3489C7831A5F6EEDA1EE5B4821F4D5E640286816B807C587EE4C1CB57C1A55)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/pZ09lOoaR5uZv88gzP13eA/zh-cn_image_0000002278063192.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9D1DE35B35FC5D7CC0CCFA5B8DC411225A7AFF2576BF4B022D0B6ADF0D7C031)
7. 点击“Trigger”， 将会触发执行用户函数代码。执行结果将展示在“Result”框内，“cloudfunctions”窗口同时打印调试日志。

   **说明** 

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/KddQNKFiT9ybNpFLeJ0IBw/zh-cn_image_0000002503613920.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF7AF917E9DCAF27B5CC671D769C6DCB7E3023201EB619322C5EA39B8ADDEBCC)
8. （可选）如[配置了环境变量](agc-harmonyos-clouddev-debugfunc.md#li15793566149)，可将变量信息传入到函数执行环境中，用于函数运行时读取。

   ```screen
   logger.info(context.env.name);//name为环境变量名称
   ```

   如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/mZAx6P-DTZGK34etq1B2lw/zh-cn_image_0000002503615754.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=95E055AB518F2C13AC542F42FEC37E75E2F0882691AD80A0ABE4A1841A35B845)
9. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/MocKxUUVSyC34bvzf15N6w/zh-cn_image_0000002179338396.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B4E83D178A117FE3E4AEE6B46FED3FEDD6B34F27337CDAEE2C6C1EDC8DC785C)，可停止调试。
10. 根据调试结果修改函数代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/QCykoqSnStiTRCkajVf2fQ/zh-cn_image_0000002179338420.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFC7A130F656386DB71AA18601448BDE8464F85E77FE5C5D2E8C82D525C3F147)重新以Debug模式启动调试，直至没有问题。
11. 参考步骤5~10，完成其他函数的调试。

## 通过远程调用方式调试函数

您还可以将函数部署至HarmonyOS 开发者中心，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署函数](agc-harmonyos-clouddev-deployfunc.md)将需要调试的函数部署至HarmonyOS 开发者中心。
2. （可选）如函数代码涉及访问环境变量，需在HarmonyOS 开发者中心函数列表中点击函数名称，为函数配置环境变量的值，供函数在运行时读取和使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/QbG9frFGTYa33XWVvrRvTg/zh-cn_image_0000002214858729.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E029E540C7C6491BF7B8C65A4A5DDB317374EBAC5076FB88810F705C25AE610E)
3. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/dDleS7ZtT7qr9ZnbHUSFOw/zh-cn_image_0000002179498140.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0BF0E177272EA0A254248F151825352A26F2C37E950952D8F39820128BD2252)
4. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处依然以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Remote”，表示远程调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/gT4KzxXVQX-4SroGBzFQZQ/zh-cn_image_0000002179338388.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FC343E4C59B76C5647E3E9E827962751EA2B5F1C2A794EBACF3DE2ADD07C6A6)
5. 点击“Trigger”， 将会触发执行用户函数代码，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/j09q0zLfTT-ieEGVVXYmSg/zh-cn_image_0000002214704345.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C34F85BC0DEFBF3B04D80A0EA578A494384AD94507E8D5ABBBBDE2EF0ABAF43)
6. 点击“Logs”页签，可查看打印的日志定位问题。修改函数代码、重新部署函数后再次执行远程调用，直至没有问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/_UQhzcK9TRqPBnsw0764-A/zh-cn_image_0000002535303613.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DBD5857FADF4AAF2950F4CD5D360C5F6BBB6DACB7699BB796F6C8C78166FDC2)
7. 参考步骤1~5，完成其他函数的调试。

## （可选）自定义Run/Debug配置

直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。

1. 在菜单栏选择“Run > Edit Configurations”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/7Tqd9cIHQwWj3aOgwPft8Q/zh-cn_image_0000002179498096.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1343E6197F73AA4C013BAA36E89DF210E6C6B5A3820CC10C2C8C4423337473E)
2. 在“Run/Debug Configurations”窗口，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/5fUT-dOUSAGB1TJk1XvonQ/zh-cn_image_0000002214858773.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7799F03DB2E2595C81F770B1FC1E207798FD904AE391B30C4C3B2DD15E14229)，选择“Cloud Functions”，新增一个Run/Debug配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Ka-egxkfTKuvX2UK6knwFg/zh-cn_image_0000002214704341.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=242E0CADD70CF1F46C776027C2D6ACC0432FD7B0F086F13F076ED065FBC88361)
3. 自定义Run/Debug配置，完成后点击“Run”或“Debug”即可立即按当前自定义配置启动本地调试。

   如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/NqcCAUIoRVmPlm-GYhV7Cg/zh-cn_image_0000002179338416.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=5496FCBE221C14595021622DE23A3690046E49FDC90AE6992EE7554D60C2260A)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/P-IMFgAJS0mOGJpzHFBxtQ/zh-cn_image_0000002214704373.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=850DA33E5AEA474A6B7C9D6BD5735744FACD954E233B93CC266A25A5B6C919CE)进行Run或Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/9xXyFjwoTfinzyq4_A3ghw/zh-cn_image_0000002214704377.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A11E77416B336CDF275D8381823594C9B292300ED0BAF3AD4CFFA0B823A12A34)
   * Name：Run/Debug配置的名称，如“functions-custom1”。
   * Server IP Address：HTTP服务端监听IP地址，默认为localhost，支持切换为您的局域网IP地址。
   * Server Port：HTTP服务端监听端口。默认为“18090”，自定义端口号建议大于1024。勾选“Auto increment”表示如当前端口被占用则端口号自动加“1”。
   * Environment variables：函数运行的环境变量，为key-value形式。

     点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/LqGmcXd7RFOYm1oBT9vqQA/zh-cn_image_0000002179338424.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1F30FCD23CC1043B6485F17E8821395E4011B380075A02F10D29311B0C3AFA9)
