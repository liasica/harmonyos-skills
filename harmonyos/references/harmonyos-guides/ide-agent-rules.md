---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:69ff6fa30a20af4c7c35e3603057b02666d60dc6615d471e4e50112300201396
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

* **Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。
* **Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

**说明** 

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/RmxLr9OjQ1Wp3qOy7c1U-Q/zh-cn_image_0000002779406532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=90025F1DF1D151819DA23E95F054D9E4E9AC7C5F6650C9DA11E8E6D75086A48E)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/i1LvAFAATt6wkDDkpo2xqQ/zh-cn_image_0000002779566500.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=34C219A73D509D6A7E457CEA3172271E9CDAA5DCD9F1F6C5E74FF83ABDA7167E)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/JibgvrM0STWA_KmmlO1WKA/zh-cn_image_0000002779406524.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A9CB3DB70FB24E04BFC5C925324617DCAA8EBE5364377E64E939C73127DFCA4)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/uuJITZ9uSySHh-2vJg6S8g/zh-cn_image_0000002779566494.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F5EB248BDC180118EACC3E0A7663FE8939B47F1F51575B68D72D3A533BC8621)
3. 以有网络环境为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/tiEx_CykSPeMJDF-pomkYA/zh-cn_image_0000002779566512.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA9A1C322F372404151B5F890BB57394C79D1BB8B7227E10ED2AB9C9D10E1053)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/N2fQwaszRjehQqzJd1mXJA/zh-cn_image_0000002779566508.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E477C8BA9B4F40E1DC7116896DBF87874B03069E3437CE4935D8CD96D8D21782)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ZqXR_EN6SROCCBPOi93yUg/zh-cn_image_0000002779406520.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5425F8976D89A1A635BE4D0AFFF5B446BE179CABA865CCB1DD4F9EDF52B9359)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/_IvbsBGEQoCwRjtspG6zrg/zh-cn_image_0000002779406536.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4BAA0D7E862F873E70DAF59B8A8D453172F13E3905C5603D89F02BFBCD1ED47)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/krVkO2X8Q_q0AHAXKZ95Qw/zh-cn_image_0000002808766077.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C1C02105401B16F87D05A85B9F1230713EA6819E25A320A47624288AE264A15)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/aAkmu-z5SaKoQxwsuaxRFA/zh-cn_image_0000002779566504.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=278C40C683425B2307410AF5771D1D1138743AB9398D612DBA3D488AC0CD0559)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/zKYuWZSLSv-18AMMccwTug/zh-cn_image_0000002779406516.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=13B3A2C2FEF831E8D4CB3AACDA8114CC0C0B497CD8A6684DA53BA165F2B71019)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/WuD2lEPoTSKsSmBdHdE1mw/zh-cn_image_0000002779406528.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=59A8430F7016051251F3B1917DB65A7E294922755FBAABB9E1787CB58E1D1B7A)
