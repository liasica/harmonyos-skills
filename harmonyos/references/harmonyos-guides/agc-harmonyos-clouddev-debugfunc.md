---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-debugfunc
title: 调试函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 调试函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:00+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:244df0cda404078a0a446d96ca6e04a3cc44455c33a1e41cc0c44a665f07263a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/89xgRt--TbmYLfYtjknPpg/zh-cn_image_0000002214858717.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=F8B24CDBEACE7431F0B29014A65966F8169649C3028EC7D13F2C3AC580D7CCEF)
2. 在下方通知栏“cloudfunctions”窗口，查看调试日志。如果出现“Cloud Functions loaded successfully”，表示函数成功加载到本地运行的HTTP Server中，并生成对应的Function URI。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/sf-4RQ0PQK-93Jh1ORLrng/zh-cn_image_0000002214704369.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=7C3930AEA782837F6672B61B286786305E2735C62620B45DAAC2155A485E40D3)
3. 如需设置断点调试，在函数代码中选定要设置断点的有效代码行，在行号（如下图行15）后单击鼠标左键设置断点（如下图的红点）。

   设置断点后，调试能够在断点处中断，并高亮显示该行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/6n6YoNUAQxOPMTo7ffu64w/zh-cn_image_0000002533684069.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=89C41F468A2EC7F58D3ACAC44F205A7D30994C21B91EE6249C09E79CC0AECE8A)
4. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/OfFCGXeZQimxj5G1whkLMQ/zh-cn_image_0000002179338456.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=41B6FF960D508227F93704F5DFD662B137794122AF7780906DA2347E513C1EC6)
5. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Local”，表示本地调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/QhuZZwfkQaefjW3i9nLNdQ/zh-cn_image_0000002179338412.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=1CADF5E2FF59117E9AD1C15A6434467F1FEA8DAEB2A3A1900A3DB31CDAA9147E)
6. （可选）点击“Save”，可保存当前触发事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/SA9_ozguQjy6pcML6Tz_ng/zh-cn_image_0000002179498072.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=8EB0880AA856B1685ED27E3C72F0AC194186F010C72F85A997DAD9ED14406FE3)

   点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Q3NhnYokQVKFXUNZxhWyFQ/zh-cn_image_0000002179498132.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=53DFBB5AA3173CB5E4A3A39600DF9BE7384FB3FBE4D1B450F5FF393D3836930C)可展开保存的触发事件，后续可直接点击“Load”加载事件。对于不需要保存的触发事件，也可以点击“Delete”删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bXvaZywkRIqxKdXngMJ_qg/zh-cn_image_0000002278063192.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=FD3F68255CB65B2A7360A73413B8AE7B89E7BA1E16A6B846D7981E56AE523C83)
7. 点击“Trigger”， 将会触发执行用户函数代码。执行结果将展示在“Result”框内，“cloudfunctions”窗口同时打印调试日志。

   说明

   “Result”框右侧的“Logs”面板仅用于在[通过远程调用方式调试函数](agc-harmonyos-clouddev-debugfunc.md#section123191549587)时查看日志。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5OHWGqFWTyaKh6B8Dg0Xag/zh-cn_image_0000002503613920.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=B167228C9023AB8B384F5F7488B993E72D51474A973D28EDF117428BD151BBB2)
8. （可选）如[配置了环境变量](agc-harmonyos-clouddev-debugfunc.md#li15793566149)，可将变量信息传入到函数执行环境中，用于函数运行时读取。

   ```
   1. logger.info(context.env.name);//name为环境变量名称
   ```

   如下图，函数“my-cloud-function”配置了环境变量“env1”，可成功访问环境变量“env1”的值“value1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/LFn9ExOjRIap3wPSBEAQ-Q/zh-cn_image_0000002503615754.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=53131C8FDB8E63798E2D0912CC148D5AF3861BF9116B5A50FDD6951196062EFB)
9. 点击菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/T553THveRlaGtJxXcvo0Ug/zh-cn_image_0000002179338396.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=870738571A5E1A825E00B09580F955C6DC00FB34F8D67C7EF5D7C0E722B7E3ED)，可停止调试。
10. 根据调试结果修改函数代码后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/k3TIRFh7SJyBk1BmEm2JsA/zh-cn_image_0000002179338420.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=BA45C471862BDF4E5B86452A0836FCF88D26FA1C5B03F62EB5E8736233C0630F)重新以Debug模式启动调试，直至没有问题。
11. 参考步骤5~10，完成其他函数的调试。

## 通过远程调用方式调试函数

您还可以将函数部署至AGC云端，然后在DevEco Studio调用云端函数，以测试函数在云端的运行情况、或补充测试因各种因素限制未能在本地调试中发现的问题。

1. 参考[部署函数](agc-harmonyos-clouddev-deployfunc.md)将需要调试的函数部署至AGC云端。
2. （可选）如函数代码涉及访问环境变量，需在AGC Portal函数列表中点击函数名称，为函数配置环境变量的值，供函数在运行时读取和使用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/v1OnVDVIR5WBXNc6FuDhrQ/zh-cn_image_0000002214858729.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=33FCB5C06CC506294AB30427ECB7E628C35839210B8FE21D853B486540D3116A)
3. 在菜单栏选择“View > Tool Windows > Cloud Functions Requestor”，使用事件模拟器（Cloud Functions Requestor）触发函数调用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/r4j-ZiQ9QHahgYuQj1ggNQ/zh-cn_image_0000002179498140.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=11C1CD460845A2D3072D434A5C4AFDDC77AB27191DEAF8A0399019FCCA373DC6)
4. 在弹出的“Cloud Functions Requestor”面板，配置触发事件参数。
   * Cloud Function：选择需要触发的云函数，此处依然以函数“my-cloud-function”为例。
   * Environment：选择函数调用环境。此处选择“Remote”，表示远程调用。
   * Event：输入事件参数，内容为JSON格式请求体数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/lMZ-zPZhRsy9nldkCgKp-A/zh-cn_image_0000002179338388.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=E1C1A8120BDFDB6907F282E0F0B61871A25F9F1D8648504E2235383F8EC87D77)
5. 点击“Trigger”， 将会触发执行用户函数代码，执行结果将展示在“Result”框内。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/mWeMWhSrTCOkAxWytKEU9w/zh-cn_image_0000002214704345.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=819D99ECB905E6446F5AB4A90AD309B6FC27CE5FC1F804117970933A1A214244)
6. 点击“Logs”页签，可查看打印的日志定位问题。修改函数代码、重新部署函数后再次执行远程调用，直至没有问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/tIxQ4RcpRLyGKiAo85jliQ/zh-cn_image_0000002535303613.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=C0A5AF8949D02D59FAA8EBE63019EAC87DB309FFE5D3A6636D1A0869F6AD7CBB)
7. 参考步骤1~5，完成其他函数的调试。

## （可选）自定义Run/Debug配置

直接启动函数调试采用的是默认的Run/Debug配置。如有特殊需求，您也可使用自定义Run/Debug配置项来进行调试。

1. 在菜单栏选择“Run > Edit Configurations”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dnj4BPwERdmPmpMCfYirWw/zh-cn_image_0000002179498096.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=FCFE3470849A943958280D29DC2C61C6DEF929CF5D5A939B24524A5F19367698)
2. 在“Run/Debug Configurations”窗口，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/8ltbf45kTFGfN9WudBD_ZQ/zh-cn_image_0000002214858773.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=F942BF584AD025A8198685F45D7C7BE3DB703859DF1CECF7952061FEBB855729)，选择“Cloud Functions”，新增一个Run/Debug配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/kzTsFf3_SzCNk6kXTEdLmw/zh-cn_image_0000002214704341.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=ADCA8C72608C9D487E98F719C8DC5F15D9BA52779FD174FD428913D6A74DEA2C)
3. 自定义Run/Debug配置，完成后点击“Run”或“Debug”即可立即按当前自定义配置启动本地调试。

   如当前暂不使用自定义配置，可点击“OK”保存配置。后续有需要时再选择自定义配置，分别点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VS-0k_GiTGiRFyK_JDhLlA/zh-cn_image_0000002179338416.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=5CA89431CC60E574BABE2BAD3A2C9DF7BFE28DF70D395892A3E59E1173ECFE54)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/VpQNrYoUSFC1ddYlJyCW-A/zh-cn_image_0000002214704373.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=65A956143364A22AA61A0A19316D5AD06B5091163A6B8FA40A4E22EFF7CB5643)进行Run或Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/KAZhroSBTeOKYI7KfXTgsw/zh-cn_image_0000002214704377.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=802B0E08F83921BDFAFE15A85DB7057660B2D0B576D84BF778381BC174FA6175)
   * Name：Run/Debug配置的名称，如“functions-custom1”。
   * Server IP Address：HTTP服务端监听IP地址，默认为localhost，支持切换为您的局域网IP地址。
   * Server Port：HTTP服务端监听端口。默认为“18090”，自定义端口号建议大于1024。勾选“Auto increment”表示如当前端口被占用则端口号自动加“1”。
   * Environment variables：函数运行的环境变量，为key-value形式。

     点击“Edit environment variables”按钮，在“Environment Variables”弹窗中点击“+”添加一个环境变量，然后点击“OK”。添加成功后，您便可以将变量配置信息传入到函数执行环境中，用于函数运行时读取。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/6rFKAhZnShSR-QJ7_RLdSA/zh-cn_image_0000002179338424.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=DAAE2808C73176DCAF29669B0AD8D754441DAA518376216388F85C2AE71CEF24)
