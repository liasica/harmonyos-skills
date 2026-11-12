---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:103b22834ea6c7abae5be01468791040e6c84ed73e91541846390ef4235f735a
---

**说明** 

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JaBITAu2QQ-zLhBA3JVb-w/zh-cn_image_0000002786520174.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=84BC7E4C1346A93C037F564AF17BBF9F4AE7E76AB7B919C34CA07D2E81BC4694)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/7WUhkjwYTwuPrzKMJmThmA/zh-cn_image_0000002786360246.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC96686BE552E09CA5680995E36CB03384B52FA4E38EC7EEA4C770BDF892C559)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/aXzuAEJ3REeTKbZ-ykNzWQ/zh-cn_image_0000002815559667.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=21F087D8D4A99140EF10724FF48D03AF483512133A30B13FB7D2FC779374CA39)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/vfKT4Zm7RrO6wS855ox9gQ/zh-cn_image_0000002815399751.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=85E09C05A5333576F9F5F990C87820AD17668FF76A1C992E8217239AFD567F30)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          **说明** 

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Z1q0RE94QIeVxFouM0uiyg/zh-cn_image_0000002786520176.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EC9A64DDCF59A9ED5B411D46CA83371E06F7648F4133DA71F16CCD39A75E1BB)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/S-RrYBDeSHmHVfxMjj7iOw/zh-cn_image_0000002786360248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A47FC7D0170709AED9CE4E8A205B6AC5EC9F834AF1C086EC4DFEFD4CB7B860B3)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/B98QVs30TKaikI8ytNHLqQ/zh-cn_image_0000002815559669.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D22F23B0683CD5B6D80AA41D4DE73EB7EA61910C92044D81330C8BB48350179C)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/rXBGzt0ZT1W-OQtsrOirvg/zh-cn_image_0000002815399753.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E765EDD1CE92B966910B540470AA89C748925FEC80266BFD78661F384133E492)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/0d50FyrZRdGYZW7PwI-oJg/zh-cn_image_0000002786520178.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC6B879830975E3ECE6CD761E879563DA7D19D381C0B4D9D8130E1D727E3BE0E)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/RwxX79C3QkCAZzKHYKlqwA/zh-cn_image_0000002786360250.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D71F5BB9A48CD0C6571DF1AB1CB4FD774890CB2249613A49EEE9FCBC4F4CC3D)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/dOnmh-XSR8O_3oGLi_sTSA/zh-cn_image_0000002815559671.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8F99F8B2DD556439E86E2B721B12000C95DD7A6D7A5D80F72BA3F3F69057A94)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/j9tMSXz_Ty-o_558ADv2ew/zh-cn_image_0000002815399755.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=8725C6083276D7BF69FFF20BA98CE9E91B5F336FBAC2DF5DBCA63A65B4E7BF48)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/PhIdrDIjTjefFr0D8np0Kg/zh-cn_image_0000002786520180.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB8CF4110F760B9975018E0EBEE385044CFFDAC752AD5B8DA91D0020C890B39C)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     **说明** 

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/6-ZHp7OTTbWEnalZmMqR4A/zh-cn_image_0000002786360252.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE40493578EF7FCB5D6A883BAA9F52919C931B57CBB9E97A5782C30A59D9B837)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
