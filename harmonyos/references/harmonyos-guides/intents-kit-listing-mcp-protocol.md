---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:777e5bfdc707410e6fae54cd25e734832c9fcadcd2931ca5ef450c9ff5663b3b
---

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口。

      如发布渠道为“智能体/小艺对话”只能使用与应用上架相同的账号登录。反之发布渠道为“插件市场”无特殊账号要求。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/qpXbmqpNT5WxafF2pnpebQ/zh-cn_image_0000002558606184.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=E93A0BDF4C8A56CAA2AAC8290A991B8D05425847823E034D8BC582CA5BF525BB)
   2. 点击“立即体验”即可进入意图注册入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/hlPaZqqpQxSGI5ax3hTXcA/zh-cn_image_0000002589325711.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=6B69A550B76BA318B36CEE4A538FC5E0BCEE3267C5221CA8367E13E4E9EE3B17)
2. 注册意图集

   1. 如图，点击“注册意图”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/bf1ME2oUQf6mDKfbAJvjqQ/zh-cn_image_0000002589245651.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=BD8FDAEF2E7E27B5B8F7C920A2B34C600497730D644853B4F785A82F1C67FDF4)
   2. 选择“MCP协议”并填写基本信息创建意图集。

      1. 意图集（插件）名称：需唯一标识。
      2. 意图集（插件）描述：开发者自定义插件描述信息。
      3. 分类：按业务场景选择。
      4. MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      5. 认证信息配置：对应鉴权信息（注意放在Header/Query）。
      6. 协议类型：根据情况选择，提供SSE/Streamable两种。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/iQ0reUqiREqDrnmVPif-aA/zh-cn_image_0000002558765842.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=E96E2AD209CA1B5DFEC866DF1477E31F01D3463E9BC6042F5F418BA2433AB4D7)
3. 编辑：创建后自动进入”插件编辑“页面。

   1. 编辑基本信息：

      1. 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      2. 图标：192\*192。
      3. 使用描述：需使用Markdown格式。（需对server的功能概述、apikey申请方式表达准确清晰）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/H3EtGXZvQamETRAiiIJR0g/zh-cn_image_0000002558606186.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=F411E7E861417009905090159C88CCBBE1B74C99F38501722EB6A03BF0117511)
4. 工具检查：保存后切换至"工具"页签。若基本信息配置无误，工具列表中会根据基本信息内容自动生成1条/多条信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/XMu1iAAVTn2o6pKm-wrBLQ/zh-cn_image_0000002589325713.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=103ECD03366F1849A1C5C339A658B248B690644C7AA6DD2135BC78F662B97A62)

   1. 出现工具列表：请检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WoSTGcERRTSlqNeyBY2pew/zh-cn_image_0000002589245653.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=3838798C96515C62BE0BF65FD95AD5AC9A816DA5B868E99EEA19523B65973850)
   2. 未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。多次尝试后仍未解决，请通过邮箱联系华为意图框架同学（hagservice@huawei.com） 。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。
      1. 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。
      2. 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺APP主对话调用（当前暂不支持开发者独立在小艺主对话上线该能力，需联系华为意图框架同学）。
      3. 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供平台上其他开发者开发智能体时调用（回到开发者源头平台去开服）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8Px5NuDbQQW-zVr-ERlTdg/zh-cn_image_0000002558765844.png?HW-CC-KV=V1&HW-CC-Date=20260429T054339Z&HW-CC-Expire=86400&HW-CC-Sign=D03E5FBAA9CA2E74D1FB46ADA3B12F42A42088516716A30C43ADC42EC6727CC9)
   2. 提交审核后，请耐心等待平台相关审核流程完成；完成后即可在“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架 > 小艺插件市场”中找到您的工具。
