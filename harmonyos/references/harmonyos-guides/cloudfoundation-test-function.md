---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db086bdc0fca11a96574435f4556ea18d9d7b4835990ec6397f622dc25512693
---

说明

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/z1GtNOOnRLGWlFp2a3pPkw/zh-cn_image_0000002552799204.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=ACC45D9CFA892861CFCD7F7108883F827C375106CAD652581F72D3D46B0E0DE9)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/z9YyvYcwQWaNMR31ZLntjw/zh-cn_image_0000002583438899.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=F40D8BE44DDDEFFAE4B0939BE531C32C9AE36436F315006105632C53733C01A5)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/XrrFV_aBRl6CAPHBIb2eUg/zh-cn_image_0000002552958854.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=24551C87614AAAAF477C1B33A29796B60947F08666C05FA1838F7CDE14DB7BEE)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/_CJZUau7Qm6hk3xwlH2Pkw/zh-cn_image_0000002583478855.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=762AC79A6797BC63D79219EA4A77D23551BA9C3C9756C989A09BE7D570957FA8)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          说明

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/itzDBev7Sh-vUhpsW7aRDQ/zh-cn_image_0000002552799206.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=C8A619F91B725B3438E9505EB15EFDD7619F79D7F309766328C5DFBED18A282C)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/4gQLL5osRve-fHFfg2KyQQ/zh-cn_image_0000002583438901.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=B320F754FBFD1D31A208641A600506F8215814836504E46F5FA2989EDC6DE0C9)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/eqvRSHD_RMq5mysDnAiVRQ/zh-cn_image_0000002552958856.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=5BE14D6609ACE5FC1DF3E79C13F21EB46AE4039720E97341512D19A86D7C08A4)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/3JpiGaO5QhCBVdIZMtTqHw/zh-cn_image_0000002583478857.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=C09647607B4647A5094504E074B6DD9AEAC9C4033798D97A8566BB31B42563E2)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/eFDmDV9nR96bbuMDelaLEg/zh-cn_image_0000002552799208.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=D9007E59791685C1B36C45D8E04B781E220C4EBF8E8FF406AF2E5B6523DD43C9)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/HJNa7SRyR6e_cph6Vlnzuw/zh-cn_image_0000002583438903.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=6FCB2D1248E75FC4E9C454A7D8994EFF820BACD8052E2EC443EBDE37F1A5950B)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/wYqha9i8RiuhkAkmFZP_LA/zh-cn_image_0000002552958858.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=9FFCF560A8ABB8CC829E60D580C3572F2EBD982D300E52AC70BFAE7842A14345)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/oQpGD3x5R5WhkUqTJLfYcA/zh-cn_image_0000002583478859.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=5A47B7503597264744ACEB57976C61E41EFAF767EB54DC3402B2B7AACB5FEFB2)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/1F6MI4qEQiGY26ll6-amAg/zh-cn_image_0000002552799210.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=C2E5D6CDFE025E01E90C9B0E659EAC7737F8761DFA1B9EE87110D991F666C7F6)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     说明

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/6LlVCoZsRbyO3Iji_8wsEQ/zh-cn_image_0000002583438905.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=71D1AD3D5A8C71F52A86F90D3DF92FA77E30D636727856E17C2AB65C723D05BB)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
