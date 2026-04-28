---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-skills
title: 技能（Skills）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 技能（Skills）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60a2472e65e4776b8152717fea0e0d2efc3bfed6937b7ab3a96efbdbc1971527
---

## 功能介绍

在日常工作中，我们经常需要处理重复性任务，如调整文档结构、撰写周报告等，每次都需要输入格式要求、偏好、操作流程，这种模式不仅耗时，也容易遗漏关键细节。Skills是一份标准化的教程，会指导CodeGenie面对任务时如何思考、遵循什么步骤、输出什么格式、注意事项是什么。开发者只需要定义一次，CodeGenie便能在后续的每次对话中自动识别并应用，实现“一次定义，长期稳定复用”效果。

Skills实际是一个包含SKILL.md文件的文件夹，在SKILL.md文件中以自然语言描述技能的名称、触发条件和执行步骤，让开发者能快速定义自动化工作流。SKILL.md文件写作时，严格遵循业界YAML Frontmatter（元数据） + Markdown Body（正文） 的统一规范，以及要确保内容结构清晰、触发词准确、没有错误处理，提升Skill可维护和可复用性，使Agent能够稳定执行。

从DevEco Studio 6.1.0 Release（6.1.0.830）版本开始，CodeGenie支持导入Global Skills（全局技能）和Project Skills（项目技能）两种。其中，Global Skills支持当前用户在本地所有项目中使用，不可跨设备同步；Project Skills适用于当前项目。开发者根据业务需要导入对应的Skills。

### 约束与限制

* 当前自定义Agent和HarmonyOS Act智能体支持使用Skills。
* SKILL.md中name的要求：长度不超过64个字符，由小写字母，数字和-组成，不能以-开头或结尾，不能包含连续的-，与所在文件夹命名一致。
* SKILL.md中description的要求：长度不超过1024个字符。
* SKILL.md中正文指令的要求：长度不超过32768个字符。
* SKILL.md所在文件夹的要求：大小不超过100MB。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7RuUy5uxRCWKavvSjfkfiQ/zh-cn_image_0000002574920487.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=2F624608E91BA60D891BE5F07450F3B1B8B048274253F550EB5441B00A909B4B)按钮，或者点击界面右上方**Settings**按钮，选择**Skills**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/jFwZDh-eTS6Chi_yb2st7w/zh-cn_image_0000002544400266.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=6448A4F9BBC6AEA485A49A130DFBBA11514972CAE34C2634A9A5E5716FAB1440 "点击放大")
2. 在**Global Skills**或**Project Skills**下，首次导入时，点击**Import**导入技能文件；若已存在技能文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/7qqpU7lSQJqIeFWECfIA6A/zh-cn_image_0000002575080479.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=7350A78812A48E181651AC4EC430077BFD7C8DC488A2802D78AB5D989F85A414)按钮进行导入。

   说明

   * 若选择的文件夹中存在SKILL.md，则作为单个skill导入。
   * 若选择的文件夹中不存在SKILL.md，则遍历下一级文件夹，检查下一级文件夹中是否包含SKILL.md，遍历到的SKILL.md将作为skill导入。若下一级文件夹遍历出多个SKILL.md，将批量导入。仅支持遍历所选择文件夹的下一级，不支持更深级的遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/qjMOvK_1T_ONxKMiLBoXUw/zh-cn_image_0000002544240608.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=9AE6B95C78E3E93BA9FC5F652477C07247F426F736E3B4ED0675E3E9C4A21BDA "点击放大")
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括技能名称（如openharmony-build）、描述信息、启用状态。同时，将鼠标悬浮在技能信息上会显示编辑和删除的操作按钮，点击可在代码编辑区打开SKILL.md文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/VOqXwzV4QYWAHAqHH2NyWA/zh-cn_image_0000002574920489.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=FB6B304988D936A844BF892EA164D903EFFE70C11577827C23C7ECDFC3CECF8B "点击放大")
4. 返回CodeGenie对话框调用Skills，在对话框输入时需要带有技能的name（如openharmony-build）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/uZRo4RXST2GB2cNS915ysQ/zh-cn_image_0000002575141233.png?HW-CC-KV=V1&HW-CC-Date=20260427T235517Z&HW-CC-Expire=86400&HW-CC-Sign=01E0B82F68670CDDD4141278D803B3C734E42CD3F34939370968BB4D21C7F06D)
