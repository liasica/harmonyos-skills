---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:41ad67b554d2eaa0fd459e667d9dd3dbc2012e68a046222a6190e9290c2d3802
---

## MCP注册配置操作步骤

1. 进入MCP配置操作入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/oBdmtGkARgSbQ_C6Cpvd6w/zh-cn_image_0000002815560185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B728BC87E91130AC6544A3F4DD72A79039BCAF010679A86733D1B1A588D470B4)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/0A3n2sFWQRuZsd6WbvhAYA/zh-cn_image_0000002815400269.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C47CD13375EB3F11464FB5B77C5921146BAD8C36557890ECCEEA2B202D70554B)
   3. 在资源库中点击“MCP”页签，即可到达MCP配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/n5S4QBgNTj-aunuXCVKPoA/zh-cn_image_0000002786520694.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E75520A1C6C1DF856C5D783AD0752C7306A3B59461C73265957D60B7BB9CAAB)
2. 新建MCP。

   1. 在资源库的“MCP”页签下，点击“新建MCP”按钮，创建一条MCP记录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/tB7ZPXLpROSOuz8fb45Wew/zh-cn_image_0000002786360766.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0440348D1CE12F8D5E8B4F5F760D1DD51519B4E145E0F5C6C4026DF9D143FA25)
   2. 选择“标准注册方式”并填写基本信息，创建MCP。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/joS8SkZnRuSVpo5JLpk4yg/zh-cn_image_0000002815560187.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F36798845B019E5A53B6F7585C54564C2A03A87ED4098B2B85878DE5AB3D973)

      * MCP名称：需唯一标识。
      * MCP描述：开发者自定义插件描述信息。
      * 分类：按业务场景选择。
      * MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      * 认证信息配置：MCP的鉴权信息（选择Header/Query其中一种认证方式进行填写）。
      * 协议类型：开发者根据自身MCP的实现方式进行选择。
   3. 选择“外部平台导入”方式创建MCP的步骤，可参考[外部平台导入](../service/mcp-plugin-import-0000002493437678.md)章节。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/J9AL-nioThexWwXMYajApw/zh-cn_image_0000002815400271.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=149F03EC8C8DC77B1350F10F23901EAF0FDDFB2E7131BD19249A5299D68D1715)
3. 创建MCP后，切换至“插件信息”页签，编辑并保存MCP插件的基本信息。

   1. 编辑基本信息：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/FnKw3KI_QbCoELTZ5jK7KA/zh-cn_image_0000002786520696.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D9EF38E0C0CFD1987E44111379E61234CE2F63E6D7E081269BF1CC4FC704EA9)

      * 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      * 图标：尺寸要求为192px\*192px；格式要求文件类型为png、jpg、jpeg任意一种；样式要求图标为方角图标且背景色不透明。
4. 工具检查：保存基本信息后，切换至"工具"页签。若基本信息配置无误，工具列表中会自动拉取出开发者该MCP下的所有工具信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/n6zSvRN2SzO8yjVwX9uyHw/zh-cn_image_0000002786360768.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7EB2F39FFF8F2F6F208350D2E557DDC09082EEB79C9565D1E88CF29BE02AE51)

   出现工具列表：请点击“配置”，检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/eWEqjQfQTuyVMEvU06C2wQ/zh-cn_image_0000002815560189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF1C08082F6F1DF2AE6EE80375D80A50B8789B4248A4B274B967A199C768AC87)

   未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。如果以上方法仍未解决您的问题，可以通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/13?level2=111)与我们进行联系，提交后的工单可在开发者联盟“管理中心”的“开发者中心 > 我的客服”页面查看工单处理进展。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/rNHwF_BcRLC8uVaRiSnlGw/zh-cn_image_0000002815400273.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=92A6C66A9E44DEBAAEC26807576EC1DF397066A59E22407B5A5D04FACE4E92B0)

      * 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。发布后即可上架成功，无需人工审核。
      * 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺App主对话调用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
      * 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供插件市场上其他的开发者发现和使用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
   2. 提交审核后，请耐心等待平台相关审核流程完成；审核完成后可在小艺开放平台内的[插件市场](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/agentHome/pluginShop)里找到您的工具。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Tpjnzo1VQmiINbmpTw2wNQ/zh-cn_image_0000002786520698.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9FF657AE17C5493A4B44265F75D4C449C4AF83501FE89E29031DF99CC73531C)
