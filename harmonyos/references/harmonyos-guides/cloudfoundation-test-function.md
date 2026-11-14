---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-test-function
title: 测试函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 测试函数
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:533886fa60065d68940a3f85d2d4470582e0fd2717a1f035761bcd13a93ea082
---

**说明** 

下文以函数latest版本为例介绍测试方法。如果需要测试函数的已发布版本，可在已发布版本详情页面选择“函数代码”页签，参考方式二进行测试。

函数创建后可以在AGC控制台测试函数的代码运行是否正常。进入测试界面有两种方式：

* 方式一：函数列表中点击函数名称右侧“操作”列的“测试”，在右侧弹出的“测试函数”界面进行测试。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/kQt63xCnQaaCKot7aUVpdQ/zh-cn_image_0000002788307978.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=D20EA859A2C330398ACC77A8C6F9561813B37D9310E52812BF89EC0ED7A6854D)
* 方式二：

  1. 在函数列表中点击已创建的函数名称，进入函数详情页面。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/GH81oUZrSQ-Mkz_FWSFkZA/zh-cn_image_0000002817427341.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=44517CFB43794D808996C1921780B808BF2A023EB42D2F82D3FFB9213C20B420)
  2. 选择“函数代码”页签，点击“测试函数”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/3SKq2W6QRYyViSn-nnkHlQ/zh-cn_image_0000002788467922.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=10470734470D22EE1F65B07A7ECE0D738A10AEE08D0D2CE5546451A0F185FCB5)
  3. 在右侧弹出的“测试函数”界面，使用默认测试事件、创建新测试事件或者使用已保存测试事件进行测试。

     + 使用默认测试事件：直接点击“测试”对函数进行测试。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/jNHWizpqTVeKDNcoUb5nKA/zh-cn_image_0000002817507411.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=863A19D267AB0D3FFA9CF43E6288C0ED71AEF73D072468FC6BF69B036199D671)
     + 创建新测试事件：如果需要设置调用函数的请求消息体，可按照如下步骤配置测试参数，并可保存为测试事件方便后续继续使用。

       1. 在“事件”文本框中输入JSON格式的事件参数，点击“保存”。然后在“提示”弹出框中输入事件名称，配置完成后点击弹出框右下角的“确认”。

          **说明** 

          “事件”文本框内输入的JSON对象，对应的是触发器的event事件格式，会透传给函数。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/n5jLbd6CTBaNweBejVjA9w/zh-cn_image_0000002788307980.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=F84B75DEC96F16EC79F3607B4A9E4CFC005170E8C203043201B4B5DD267F5605)
       2. 点击“测试”，函数处理事件并返回测试结果。
     + 使用已保存测试事件

       1. 在“测试函数”界面，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/JarHev2wTDO084WKnwg9Ig/zh-cn_image_0000002817427343.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=79BD5209DD8C9CF1130331E5DBAA89D5B5DBFB218107432DCAA3A1565AB7E0D7)展开已保存的测试事件列表，选择已配置的事件名称右侧的“加载”，然后点击“测试”，函数处理事件并返回测试结果。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ip27SF1LTgapAPKqbAztTQ/zh-cn_image_0000002788467924.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBFC3B6726F800B2CBB10DFCD7AA0FBD596C5CD27DFF99AB825D1D4E48EB266C)
       2. （可选）如果需要删除已添加的测试事件，可在测试事件列表中点击事件名称右侧的“删除”即可删除测试事件。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/JFIzKLJDRfenPzzdVVf50w/zh-cn_image_0000002817507413.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF62031B8B2927301E87151EBFA195A0EA303D7E2330DCEB28FDBC00B088AF09)
  4. 查看测试结果。

     + 执行结果：展示测试后获得的响应结果。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/gOjadFf3RHq1aifNag4sTQ/zh-cn_image_0000002788307982.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1361F8D206E2374CEC29AFE6A9EC4C968E8A41A84E91BCDC41A7C7856DCD0B3)
     + 运行日志：展示函数运行过程中，通过logger API打印的日志，支持输出debug级别及以上日志（以下仅为日志输出示例）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/CXJOgp4RTyC0Z0WpnTBasA/zh-cn_image_0000002817427345.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=69A9D41ECEC69B1D1AC79480DEB561975515CE9CD3FDE1C0F31E1592E1C98E0B)
     + 执行摘要：展示该次测试请求相关信息。

       - 请求ID：该条测试请求的RequestID，在后台日志中体现为X-Trace-ID。
       - 持续时间：函数执行的端到端时间。
       - 执行版本：该次调用测试的具体函数版本。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/GbOPpPi_Tg-ast9bcwWqRA/zh-cn_image_0000002788467926.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=53AA2D96B37855FE03223479AC3141E93B7C5A4EA9B1D75151D081DE27CF2FD4)
  5. “代码输入类型”为“在线编辑”的函数，测试过程中，如果需要修改函数入口文件代码，可直接在“函数代码”页签的代码编辑器中修改，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/p-voRlDYSFuhw_3T6BmisA/zh-cn_image_0000002817507415.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=A68D9DDEB5D0D5CF00A3C3DEF36FF7812F630304A8205F00B9BF610A6008B1BB)

     “代码输入类型”为“.zip文件”的函数，测试过程中，如果需要修改函数代码文件，可在本地修改且打包完成后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/3do0eiPxRICmPoLkMIT2yQ/zh-cn_image_0000002788307984.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=292717E9D8856F8CF66E9023C3E5DD3C603FF1D3C4C91DD7F3C7A906AB4513DD)重新上传函数部署包，然后点击页面底部的“提交”。当界面提示更新函数成功时，则可以点击“测试函数”对更改后的代码进行测试。

     **说明** 

     如果代码更新量比较大，需要调整函数内存配置，可点击“内存配置”下拉框进行调整，然后再上传函数部署包。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/0e17V1PyR0O3iKJcesjXyA/zh-cn_image_0000002817427347.png?HW-CC-KV=V1&HW-CC-Date=20261114T004814Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F1C29295B3A816D6E33D8CD7643E0B0BC937E92340E294732A8A68147F62EFE)
  6. 函数测试无误后，可在“函数代码”页签点击“导出函数”导出函数部署包。导出包以“函数名称+函数版本.zip”格式命名，可查看函数结构和文件内容。
