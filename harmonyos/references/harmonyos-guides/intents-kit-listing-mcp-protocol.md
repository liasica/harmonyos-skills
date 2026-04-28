---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94fed1ab8883969597d7e493f33a8bfb9658f2c5bf589daa5fe8d8bca4932114
---

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口。

      如发布渠道为“智能体/小艺对话”只能使用与应用上架相同的账号登录。反之发布渠道为“插件市场”无特殊账号要求。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/dJ1u8A6gRX-WTp0XUVZoNA/zh-cn_image_0000002552799690.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=1B71C11B9CEE2487A5D61370ACBF94DA006636668FC2A061D6344778550E8614)
   2. 点击“立即体验”即可进入意图注册入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/bLvfLt3uS3-nKq11n21gsA/zh-cn_image_0000002583439385.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=B0D2BB62D97D421CF5E0A9F32151C6DC782F0A8669B35680586F966C0C14FA2B)
2. 注册意图集

   1. 如图，点击“注册意图”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/XBSWgLdxTiGjGL2_qlISig/zh-cn_image_0000002552959340.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=11BAE1A1E0987BDA283081E34E1729D80D5EB0E8CCE653354572BC1B71F783E1)
   2. 选择“MCP协议”并填写基本信息创建意图集。

      1. 意图集（插件）名称：需唯一标识。
      2. 意图集（插件）描述：开发者自定义插件描述信息。
      3. 分类：按业务场景选择。
      4. MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      5. 认证信息配置：对应鉴权信息（注意放在Header/Query）。
      6. 协议类型：根据情况选择，提供SSE/Streamable两种。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/I7iwg67eRnKj5i6WFNv4ZA/zh-cn_image_0000002583479341.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=BD97E3B22E30583510A89E6ABBCBB82EE23CB3D1A2A3B7A5CBE7968280F16997)
3. 编辑：创建后自动进入”插件编辑“页面。

   1. 编辑基本信息：

      1. 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      2. 图标：192\*192。
      3. 使用描述：需使用Markdown格式。（需对server的功能概述、apikey申请方式表达准确清晰）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/MAYdT4VYQZKnNxUoLOBfVA/zh-cn_image_0000002552799692.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=3E0E20633A80684C385F52BC81FB86C497BDC06EC69A19FF43BA9FA79E5490B6)
4. 工具检查：保存后切换至"工具"页签。若基本信息配置无误，工具列表中会根据基本信息内容自动生成1条/多条信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/xkWmOaZIQ6e6yIF1m0R8lw/zh-cn_image_0000002583439387.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=163A9CF46FA678F6408A73B42AD6813CB8DB6032717EE7D9F262EC7D8C6C28E7)

   1. 出现工具列表：请检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/L_8HOTC6TjOEAjHMvtVoDg/zh-cn_image_0000002552959342.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=51C438F62199FB54B79D81B59DB975BE6E7639F4DC17353FBABA9FC78A1AD972)
   2. 未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。多次尝试后仍未解决，请通过邮箱联系华为意图框架同学（hagservice@huawei.com） 。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。
      1. 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。
      2. 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺APP主对话调用（当前暂不支持开发者独立在小艺主对话上线该能力，需联系华为意图框架同学）。
      3. 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供平台上其他开发者开发智能体时调用（回到开发者源头平台去开服）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/nBKFfjSfQdGlSyUYtJJz1A/zh-cn_image_0000002583479343.png?HW-CC-KV=V1&HW-CC-Date=20260427T235343Z&HW-CC-Expire=86400&HW-CC-Sign=C6D749FEF83D554CEF7CFFDD859EF01C19A23515695920F828A9A5E68F59E736)
   2. 提交审核后，请耐心等待平台相关审核流程完成；完成后即可在“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架 > 小艺插件市场”中找到您的工具。
