---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74794741a09f3084df49ce8c4d4aa3124a4e8cc53cb3921bda8916f27a4e481c
---

**说明** 

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/kQolMNXjRpC03KRtRyK4gQ/zh-cn_image_0000002792877960.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBC435DD9514E53DB28751037DE555FEBF9B5D139CBA0D8696F6B07C5CC78EC6)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/OZdIcfdlQ6Wmc_upHtCsrg/zh-cn_image_0000002821837867.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=783137E0A4CD008794AAF30564F55ACD3E1F04150A53437EA09AC0A14444F964)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eBEamvllSgqdNpPJY_ht-w/zh-cn_image_0000002821757869.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B669A38EE5E92D236F1FD9C5522312FDB6C402736E2DA6D0906C7B2BF068A94A)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/A8ZjkzpTSAabgFetbZFNzA/zh-cn_image_0000002793037932.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=946EC9CEC1ACB89F7BA5EDDD4EF77D5ADB2BF347D74E96B0B4F78102C9B7CEC8)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          **说明** 

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/aRg7aKuHTJWW7Ww-I0JDeg/zh-cn_image_0000002792877962.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5F5E3D94AE698BB90B9FFEE149B2A3F2298510A0732D194A0FAC4CB7AE19B3C)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/TgepHMlrQoKydvFMHiGtkg/zh-cn_image_0000002821837869.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE1C9853E69B49E1D0C49F06296328D7A4611EDAAA3359D22A471C9ED6824D7D)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/TtNdIEiYQzOY3W6qgOgPqA/zh-cn_image_0000002821757871.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C90BD175F63CE0027C0DB6AFE6D0962EEC270C6DC69A71AF57B5510C4D3B7667)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/mHZJ_AZ4TwOZ6uqFN4rFlQ/zh-cn_image_0000002793037934.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=294BA035C4F330347F8E6EB86C386CF8F325E28415CFC1B471CC8EA8B581B176)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Da85GDzlQEKccaUKyk_kNQ/zh-cn_image_0000002792877964.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=746E006955F46A43CED26BC41146F1B9D7440C18098808CDA1A2BDCA7F9C2827)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/HueOjptmQOeqmjrubw6KOQ/zh-cn_image_0000002821837871.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C55205EA6488376E3F2F4F9F8D851CB281BAD586907AC51E6CDBFD95B34E2653)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/IhIKJZizS_mAl_cmfMC11Q/zh-cn_image_0000002821757873.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=72154C5A490C00B9E0B9B151F7565813DE4D2010B543934AF7376C9329C63847)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/zAtoyln-Qciz016L2u4v2Q/zh-cn_image_0000002793037936.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB5E984ABA68AF37AAC1833AFAF064C55BAA5926C5486794C1818C93FCAB7D45)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/HV-oBRYsT5--MtJdhPAZsw/zh-cn_image_0000002792877966.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=F89CCFEC9920DFF4DE038B91F12DAB9F0EE763B7F73C21E3A499F9C5E19A1810)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     **说明** 

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/kwLClQyEQW6eHWpEDSAcRg/zh-cn_image_0000002821837873.png?HW-CC-KV=V1&HW-CC-Date=20261121T011220Z&HW-CC-Expire=31536000000&HW-CC-Sign=D06B97CBF1DFC6D2F2C515CD49DFB7EDF9EF1724357D5A17128D185108B5AEF2)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
