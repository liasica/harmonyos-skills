---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:624d778b1834f513d9bdb41142e7eff4c02489bd987a696e03731082b8832d96
---

说明

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/CUgYreQbS2yJW_GiHyxlGQ/zh-cn_image_0000002589325223.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=41923790B77B6EB47EF3E43D12071AB5BFD5C26748DC37C73E6F0F28AEC480E4)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/MB8QhvRrRTyYYqaZajpRnQ/zh-cn_image_0000002589245159.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=E43B2EF500D2D3AFEE65DAB1A016191955D4B4F7314A718EEA31ADA6371FFCD6)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/z-Mc1cPTT0GFqFjYNCXMgA/zh-cn_image_0000002558765354.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=05BBDB8F255A6643DD35ABA12279EAD091133C445FCAB01F724FCF988928637A)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_R5Fnd1ARPuMJ30N-SjlkA/zh-cn_image_0000002558605698.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=316D828A2EE53F1838BB827301A616D035D7D9B5C465A8065EE94BACAAD37F39)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          说明

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/IzsomssSTaOEPN2uNWtFAQ/zh-cn_image_0000002589325225.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=A4AE0EF97A2F877EF9700A0ED3744D204120D90B3839253E5C2E501F3DCED8D2)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/pq1Vg4FgS826hLIe3kt7-Q/zh-cn_image_0000002589245161.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=51FE0DD961EEC0999523DBC07587702D9EB49AE278271AFAECA0BEF4D85BC8E2)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/XdZx-PVcTeC1euqaPJy8Ag/zh-cn_image_0000002558765356.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=9FE33B04B483C984DA64D8BFAC3B0350B882D594266343890CFC09C96B9865CB)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/hz8ANaSESR2CquPUzOjUKw/zh-cn_image_0000002558605700.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=F27F59CD2AD4105E13E501472B456D0854F72FACC926337A01EB2365B2F568AF)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/pYpywe5nSxaBtN4pCPe9Ew/zh-cn_image_0000002589325227.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=B05F265090EE7D51B8772B349755A41001B8BA21DAD2B2F8485EC29925893B70)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/EQAk0Dj3RPGHkb31HeA9RA/zh-cn_image_0000002589245163.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=F0656EA909EB6650D28320C4463B406BCA5303AC0BF320FAD57C1C3D6009C1FE)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Aw3-MPuDS5uLIZ31EEIgXg/zh-cn_image_0000002558765358.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=AB9EC359DDA14F06EAE99FA1E401FD013D329809FF349578F2EF4056D6B88C36)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/F7-CDkyTSFSTHwG8YwGJYw/zh-cn_image_0000002558605702.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=F2AB5923533735E68887259D01B897940B44A3FF84E225015AC32C61BD6415A3)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ol8UUcQ-Tay4UXfz3_O37g/zh-cn_image_0000002589325229.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=BD1A6BB1214E96C6E125302AFF3F33CE17569A055B02922994917D87D155BE8F)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     说明

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/DtZtmAPTSRuSe-xGWIIr2g/zh-cn_image_0000002589245165.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=7F5B00159504E9C346A724310C075C4008A7C2388634478B7627CC809309BC6C)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
