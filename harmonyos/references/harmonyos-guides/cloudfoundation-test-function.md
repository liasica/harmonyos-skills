---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a0d1a4f51fb86e2796d7159e34bf392266b9d4fc61273936560420e948e8e40
---

**说明** 

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yc662jZSTsSEibmCqMiWIA/zh-cn_image_0000002820406259.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC6E928DAC5C41C862B8BC2D6B026BABCA6E8D32B9FA85690B39B30E024F7689)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/xsGVzq5HTSanJUlt9uJ8eg/zh-cn_image_0000002791726280.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A76CCDE98B538C0024B425D249C0C238C509C1E0A2E95D8EE943D12D3F39DC5)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/AjQmYOL6T1i3xI5pIefXCg/zh-cn_image_0000002791566308.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=A050DFBD48030CEB09C94CE81A381F0005DA50B7845F41D07B6BA64D268C29E0)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/NdLfPZIuQr-DOi7AzRn0aQ/zh-cn_image_0000002820526261.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=4875CC9FBB671C6A2513C75CB4A8343683CEBB5FEFEC68815885B49F82BD23DE)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          **说明** 

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WKTT4gYnTIqnoU4XWaftlw/zh-cn_image_0000002820406261.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAF43C41C853287D3D1FD1C96E892209CE364C1135A55616D01E665DD157E2B0)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ivHRarwbRI-p4Yv21HdUcw/zh-cn_image_0000002791726282.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=592F4FD352FEA763A4397381541775914CF8E765CA852EB1818A89EB37230D4A)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/7O8HXB_WRK-JkZngkkH88w/zh-cn_image_0000002791566310.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A91C0CFE85B88EBA527D223FC2A105D70C6E087EF6EFFAF6F7560337C020187)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/rT9vSGW2TdmXjQp09DJMfQ/zh-cn_image_0000002820526263.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=F59BC253A8AAC95E5F343D4CC8E1CB48E146651C222CD376228D0E9EFE5320A5)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/tc9MzIjvTWmUPaDEg5nPCg/zh-cn_image_0000002820406263.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=202A4CA77F8DA682BECA775D5DADF64950B68B9CE9BEC481379405994E145A10)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/yq_xNJ7OTS6E1rYHjSIdXQ/zh-cn_image_0000002791726284.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FB99A58E5B300F963FBD86D0E39A0C2FF35D689E125449BF4F9F4EF01900169)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/VnpMSRV4SIaHosnaGWxNjg/zh-cn_image_0000002791566312.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=904F0E7354F5FC516240897C2A5AE0A7ABF25B46398CCE701A40FBCAEB84936D)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/JxZb8Ky2Qxy9UstAC7WAaw/zh-cn_image_0000002820526265.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=28F4CE2584E2B7D2971F404035D99533F700FA739AECC3A67BDF9DE231D9446D)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/53CvqbbWRAOHDo5bmP3MKQ/zh-cn_image_0000002820406265.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3BEEF523B3A5B54894BC890CB784B6AAF2C3C89A002E80C421E3C0B60116D24)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     **说明** 

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Wi09Y61IQECGMPP29ERVpA/zh-cn_image_0000002791726286.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5F89E3D43CF3EDBF2EB926AC508CB0590E42209EBCF4F98CC2B4E215D013D7F)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
