---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-ux
title: UX设计稿生成代码
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > UX设计稿生成代码
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:59595e0c4b86078e00176b167c872405e1805c5c190acb7f18e0539a687e1436
---

DevEco Code插件支持将UX设计稿一键生成ArkTS代码。开发者仅需提供Pixso设计稿链接，工具即可自动将其转换为可构建、可运行的ArkTS代码。该能力以内置 Skill（hmos-design-to-arkts）的形式提供，随DevEco Code插件安装即生效，开发者无需手动安装或配置。

生成代码过程中，Agent会自动完成设计稿解析、工程理解、方案设计、页面实现、交互补全、HDS（HarmonyOS Design System）组件适配、质量审计与多轮视觉校准等环节。其中，多轮视觉校准持续进行，直至代码评分达标或达到校准轮数上限，评分阈值和轮数上限均支持通过自然语言修改，当前默认评分为 80分，轮数上限为5。

hmos-design-to-arkts内置完整工作流与精简工作流两种模式：完整工作流包含多轮视觉校准，适合对页面还原度要求较高的场景；精简工作流跳过视觉校准环节，生成速度更快，适合快速验证设计稿效果。开发者可根据实际场景选择不同模式。

## 约束与限制

* 鸿蒙电脑版DevEco Code不支持该功能。

## 操作步骤

1. 添加Pixso MCP。

   UX设计稿生成代码依赖[Pixso MCP](https://pixso.cn/pixso-mcp/)获取设计稿数据，使用前需确保该MCP服务已连接可用。当前需通过修改配置文件的方式添加MCP，以及仅支持用户级配置，配置文件路径如下，修改后保存并重启DevEco Studio即可生效。

   * Windows：C:\Users\用户名\AppData\Local\Huawei\DevEcoStudio26.0\deveco-code\v1\config\deveco.jsonc
   * macOS：~/Library/Caches/Huawei/DevEcoStudio26.0/deveco-code/v1/config/deveco.jsonc

   其中，DevEcoStudio26.0为版本目录名，请按实际安装的DevEco Studio版本调整。

   Pixso MCP支持多种配置方式，具体可参考[Pixso MCP开发者文档](https://pixso.cn/developer/zh/mcp/introduction.html)，如下为通过Pixso个人访问令牌方式的配置示例：

   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "mcp": {
       "pixso-mcp": {
         "type": "remote",
         "url": "https://pixso.cn/mcp",
         "headers": { "Token": "Pixso个人访问令牌" }
       }
     }
   }
   ```
2. 选择Agent模式，建议使用Goal或Build模式。选择Goal默认执行完整工作流，Build默认执行精简工作流；同时，开发者也可以在输入框中指定完整工作流或精简工作流。
3. 在对话框中输入Pixso设计稿链接和生成代码需求描述后，按**Enter键**或者点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/BZ-YgVUaTm-t15iEIwz9wA/zh-cn_image_0000002779406572.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=69EFBBD1F01C9A6EB9ED32C08CFB669CBF140A250FD1256A2E5BCB19B8928C6B)发送。例如：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/TCkrVTMzSr62YOylr1ZLAQ/zh-cn_image_0000002779566550.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=2693BC0855F25C681A2DCEFAD4E8DBFB892970E3C560B3DB7D405E0F423D11E7)
4. 等待Agent自动完成设计稿解析、工程理解、方案设计、页面实现等流程。
