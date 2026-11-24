---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-skills
title: 技能（Skills）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 技能（Skills）配置
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:928db9115d0bb01f036fc05b50bb0e122139524b075edf1c2dde464cace53dea
---

## 功能介绍

在日常工作中，我们经常需要处理重复性任务，如调整文档结构、撰写周报告等，每次都需要输入格式要求、偏好、操作流程，这种模式不仅耗时，也容易遗漏关键细节。Skills是一份标准化的教程，会指导CodeGenie面对任务时如何思考、遵循什么步骤、输出什么格式、注意事项是什么。开发者只需要定义一次，CodeGenie便能在后续的每次对话中自动识别并应用，实现“一次定义，长期稳定复用”效果。

Skills实际是一个包含SKILL.md文件（区分大小写）的文件夹，在SKILL.md文件中以自然语言描述技能的名称、触发条件和执行步骤，让开发者能快速定义自动化工作流。SKILL.md文件写作时，严格遵循业界YAML Frontmatter（元数据） + Markdown Body（正文） 的统一规范，以及要确保内容结构清晰、触发词准确、没有错误处理，提升Skills可维护性和可复用性，使Agent能够稳定执行。

从DevEco Studio 6.1.0 Release（6.1.0.830）版本开始，CodeGenie支持导入Global Skills（全局技能）和Project Skills（项目技能）两种。其中，Global Skills支持当前用户在本地所有项目中使用，不可跨设备同步；Project Skills适用于当前项目。开发者根据业务需要导入对应的Skills。

### 使用约束

* 当前自定义Agent和HarmonyOS Act智能体支持使用Skills。
* SKILL.md中name的要求：长度不超过64个字符，由小写字母，数字、中划线组成，不能以-开头或结尾，不能包含连续的-，与所在文件夹命名一致。
* SKILL.md中description的要求：长度不超过1024个字符。
* SKILL.md中正文指令的要求：长度不超过32768个字符。
* SKILL.md所在文件夹的要求：大小不超过100MB。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/IxLfuxwcRfWi4jOkyPozog/zh-cn_image_0000002779567222.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=0005BCE7323AC933EFE791FB060191F0C8DDFE1AED6D1BF1D5837DD0F3FEAA00 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/nSlQwlJISk-Gp8pFw7LO3Q/zh-cn_image_0000002779407240.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=12D9FAA52419C58328FF56725CA623BC88F83875517AA1E8B8A3AED4718E745F)按钮，选择**Skills**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/zWCUUv70RqCKd6xHdCRMAw/zh-cn_image_0000002808886883.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C6EF2E72CE927E83F7D2F34B7E35578EDAFCB72A6236104F43E5156766C00C9 "点击放大")
2. 在**Global Skills**或**Project Skills**下，首次导入时，点击**Import**导入技能文件；若已存在技能文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/E3HsDiGbQAuEhl5F9FGlpg/zh-cn_image_0000002808766799.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=76057598D5AAC35156E9AC902C81217D75DD1D4F1062E624484DDEA3B32BF3B8 "点击放大")按钮进行导入。

   **说明** 

   * 若选择的文件夹中存在SKILL.md，则作为单个skill导入。
   * 若选择的文件夹中不存在SKILL.md，则遍历下一级文件夹，检查下一级文件夹中是否包含SKILL.md，遍历到的SKILL.md将作为skill导入。若下一级文件夹遍历出多个SKILL.md，将批量导入。仅支持遍历所选择文件夹的下一级，不支持更深层级的遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/AQJh_kkZQXucF0XVS_YCSQ/zh-cn_image_0000002808886881.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=714A1A0D82C6AD3557ED15E8F6291FA9809C8D811211446F85D7543D78CACF13 "点击放大")
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括技能名称（如openharmony-build）、描述信息、启用状态。同时，将鼠标悬浮在技能信息上会显示编辑和删除的操作按钮，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/9HDGaUXLTtCD73y_-OnRzw/zh-cn_image_0000002779407242.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCD3F27741263AEE55229404C29C22496E489D6E19E15A032C33A4F85067726A)可在代码编辑区打开SKILL.md文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/ntuOH-yuQLesQRN69SOPvg/zh-cn_image_0000002808766803.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=33FCF357EBAAB3EA448A64B0060ABCB4FD0BD1ED396E2ED09035B5BA744ADA24 "点击放大")
4. 返回CodeGenie对话框调用Skills，在对话框输入时需要带有技能的name（如openharmony-build）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/3o5JETyiRFakh7JD7ISm7Q/zh-cn_image_0000002779567220.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=5906DECE9BD8DF089B87E054EEEFDFB91049B5D2055AFFB68F0612A96610BDF7)
