---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol
title: MCP协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > MCP协议上架指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:40+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:24b8ac516d9f6afcaa3e62d3c0fdd9c4714fbf01e5ba8a1d8f87e4177e7ee65d
---

## MCP注册配置操作步骤

1. 进入MCP配置操作入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/aKA4LKP6Ryy2girF6CT1fQ/zh-cn_image_0000002788308498.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=158510A22DBA0489AF7FBCCE2376562FADA42FFC701482B8B5265B020A064AD2)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/YFsbxnXyQ6O0Mc5IjEsKbA/zh-cn_image_0000002817427861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=A582D4F033DAEE96D1E38CDF3D3D17AD3520C6EDA572E3C1C4EBD19EC7FED16D)
   3. 在资源库中点击“MCP”页签，即可到达MCP配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/2G9dtsCkR8eU0HJ2ZHjyKg/zh-cn_image_0000002788468442.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EF9B8D03697481263AAF33976CBE72BA222B4DFB1B6132AB22FDF9EC66AA92F)
2. 新建MCP。

   1. 在资源库的“MCP”页签下，点击“新建MCP”按钮，创建一条MCP记录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/U-7RyU9mT3WPqV2vjnkGcw/zh-cn_image_0000002817507931.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F4B07ED314EA3B67F0FB3947690BBA3EAE62D7420CA1A19A07CBB4E772DA0F8)
   2. 选择“标准注册方式”并填写基本信息，创建MCP。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/dtxg5QdJSb6UoANy30Invw/zh-cn_image_0000002788308500.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF3AEFF9B7F01D672F7CA51F0FDC616F2AE437104DCE7FBFD998BFF84C9F2343)

      * MCP名称：需唯一标识。
      * MCP描述：开发者自定义插件描述信息。
      * 分类：按业务场景选择。
      * MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
      * 认证信息配置：MCP的鉴权信息（选择Header/Query其中一种认证方式进行填写）。
      * 协议类型：开发者根据自身MCP的实现方式进行选择。
   3. 选择“外部平台导入”方式创建MCP的步骤，可参考[外部平台导入](../service/mcp-plugin-import-0000002493437678.md)章节。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/t77uxTkpQkqfZEf472g7Sw/zh-cn_image_0000002817427863.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=706CEEA581CAE4DE3F26386BBB965BF9F90B4FDBFB05336720AE642AD127D1B7)
3. 创建MCP后，切换至“插件信息”页签，编辑并保存MCP插件的基本信息。

   1. 编辑基本信息：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ilXitO6YRqSqEwf9R8FweQ/zh-cn_image_0000002788468444.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=7399BCF853F0A4BA39D81E80C57C91A051661BEDD6676CBACD12B530080F08A8)

      * 开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
      * 图标：尺寸要求为192px\*192px；格式要求文件类型为png、jpg、jpeg任意一种；样式要求图标为方角图标且背景色不透明。
4. 工具检查：保存基本信息后，切换至"工具"页签。若基本信息配置无误，工具列表中会自动拉取出开发者该MCP下的所有工具信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/wLxK_D-eSmmEBHRfZVe5vg/zh-cn_image_0000002817507933.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A482862EB5F1629D3978CC673308801D3EED6B90014DB0B80BB3E50FD4589AF)

   出现工具列表：请点击“配置”，检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/1OXUk-0mRWaBF2bKT_3q5Q/zh-cn_image_0000002788308502.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AF5A16553FA10E008DE428DD611700FFCF228FAE91368E03EFE17017980457C)

   未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。如果以上方法仍未解决您的问题，可以通过[在线工单系统](https://developer.huawei.com/consumer/cn/support/feedback/#/add/13?level2=111)与我们进行联系，提交后的工单可在开发者联盟“管理中心”的“开发者中心 > 我的客服”页面查看工单处理进展。
5. 审核：切换至“发布”页签，点击“提交审核”。

   1. 选择发布渠道，点击确定，提交审核。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/2DnlEssrRuqOi-oarG3HCA/zh-cn_image_0000002817427865.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=55701C0DE6695C141AD69D6EF684F9AFA6098663EF5C18875059F050C95E01C8)

      * 智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。发布后即可上架成功，无需人工审核。
      * 小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺App主对话调用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
      * 插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供插件市场上其他的开发者发现和使用，发布后必须经过意图框架人工审核。请根据[Intents Kit接入流程](intents-access-flow.md)，提交意图框架的技能调用方案能力申请，明确此次MCP发布的相关需求背景和审核诉求。
   2. 提交审核后，请耐心等待平台相关审核流程完成；审核完成后可在小艺开放平台内的[插件市场](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/agentHome/pluginShop)里找到您的工具。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/EwjnRKNaTwuJ8yuT4FL7ng/zh-cn_image_0000002788468446.png?HW-CC-KV=V1&HW-CC-Date=20261114T004655Z&HW-CC-Expire=31536000000&HW-CC-Sign=591645561C3B1A1A8972F18E41245F9A0065C0F3BB7539A476B8914BC955D2F8)
