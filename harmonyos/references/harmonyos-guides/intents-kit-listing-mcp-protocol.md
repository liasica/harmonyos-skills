---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:374837ad8ea143019a00e7baeef92ac0581233fdee1b7a8b7e8c9766f058fac8
---

## MCP注册配置操作步骤

1. 进入MCP配置操作入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/PCzmfj-_T9OlcbI0f9jW3g/zh-cn_image_0000002820406779.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=500FAB8ACB5BCF47F24857EB8DB71E67044584E99357F258F85B288BCB9B6B52)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/jAUkK01eQViHjKICWCxCLA/zh-cn_image_0000002791726800.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CFD8748F5C390C3C5C20C274EEC5CE2A36009A7A5CCE66F3FE3FFD5CEC1777B)
   3. 在资源库中点击“MCP”页签，即可到达MCP配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/yX0x0pO_Rg-cPOxlbTnALg/zh-cn_image_0000002791566828.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=A219BE2B4A17EA075C2D39B30D1284E0F5C2881E7429DE4E2041E76A5FD97025)
2. 新建MCP。

   1. 在资源库的“MCP”页签下，点击“新建MCP”按钮，创建一条MCP记录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/cx20NbnpSKiKrgYAwBStEA/zh-cn_image_0000002820526781.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=7751B982455574B7F8B1A1B6DB28E292B77C6E1268CA8CCD4CBDC2D824F8D3B8)
   2. 选择“标准注册方式”并填写基本信息，创建MCP。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/7TVzQSN0Q7OsWqcyRWLJdQ/zh-cn_image_0000002820406781.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=526DF0E79827FC6830057462E8B406B1304FE1D9386157308B65FEAE80137F58)

      * MCP名称：需唯一标识。
      * MCP描述：开发者自定义插件描述信息。
      * 分类：按业务场景选择。
      * MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      * 认证信息配置：MCP的鉴权信息（选择Header/Query其中一种认证方式进行填写）。
      * 协议类型：开发者根据自身MCP的实现方式进行选择。
   3. 选择“外部平台导入”方式创建MCP的步骤，可参考[外部平台导入](../service/mcp-plugin-import-0000002493437678.md)章节。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/F9WGBbGyQjqYw5ah88CVsw/zh-cn_image_0000002791726802.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B929F642CEA74930856355EF7620541E37F7A71E4B1BBF9E32509671D23026B)
3. 创建MCP后，切换至“插件信息”页签，编辑并保存MCP插件的基本信息。

   1. 编辑基本信息：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/SgKgmuAnSJGZPZUEZLX_Cw/zh-cn_image_0000002791566830.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=F998680EEE4B41F75B24F81E943C2377D4043DC340347B370E3C51AF861FEC67)

      * 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      * 图标：尺寸要求为192px\*192px；格式要求文件类型为png、jpg、jpeg任意一种；样式要求图标为方角图标且背景色不透明。
4. 工具检查：保存基本信息后，切换至"工具"页签。若基本信息配置无误，工具列表中会自动拉取出开发者该MCP下的所有工具信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7H5zVZ_hR0-M78FLQZf0xA/zh-cn_image_0000002820526783.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=903B285A22DFD31D7F319ACAAAD0D9738892CE99CDA372FCC5243E5234C9114F)

   出现工具列表：请点击“配置”，检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/miiJMlKbQoCOluwHfk6cAw/zh-cn_image_0000002820406783.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AFC1B7FD6C20A81574DF6B1DD94E1328C44F64D228B78DDD605E24C2B71F192)

   未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。如果以上方法仍未解决您的问题，可以通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/13?level2=111)与我们进行联系，提交后的工单可在开发者联盟“管理中心”的“开发者中心 > 我的客服”页面查看工单处理进展。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Q6oFTCfPS-KgsntGglTBAA/zh-cn_image_0000002791726804.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ABDB3CEB655EDFF8CDDCDA15727FBA270C11A02DCC468D84AD301919C18063B)

      * 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。发布后即可上架成功，无需人工审核。
      * 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺App主对话调用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
      * 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供插件市场上其他的开发者发现和使用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
   2. 提交审核后，请耐心等待平台相关审核流程完成；审核完成后可在小艺开放平台内的[插件市场](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/agentHome/pluginShop)里找到您的工具。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/eT2xUjZgS3iEZvzzeH9qig/zh-cn_image_0000002791566832.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=32C00981113050C0EBADF7EE2900FEDBB39C0758E962E583AC24A7D061E5B56E)
