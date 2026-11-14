---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-skills
title: 技能（Skills）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 技能（Skills）配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c259058d5dc8a41a4c42c4fbd829cd7504b906e9e37dde7a59942b78a51945f4
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

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/6LFQpK0iQnOIccI9KjnE2w/zh-cn_image_0000002779567222.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=E86E7BC29B5D47FFE9809555AFC5B575D8FEE5943521F694D464342E9564E034 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/4cFP4FMeSqilHdjmL_4evQ/zh-cn_image_0000002779407240.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=06DB5231A96CC704B604A4D410F8B053F5C64567D02595750B037C082100197E)按钮，选择**Skills**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/sp-XnELzRg-oXLKy0AEYrg/zh-cn_image_0000002808886883.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=681496279030726116C50D696E20453C8DDF691105DEEF0B72A4EF8D18F781C8 "点击放大")
2. 在**Global Skills**或**Project Skills**下，首次导入时，点击**Import**导入技能文件；若已存在技能文件，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/9okMFToZRMywzzyaeqH45A/zh-cn_image_0000002808766799.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9EE9DC1A3EA686FE3E2B07AE1671954B8208A01B9B2142949633E388A2C3FA5 "点击放大")按钮进行导入。

   **说明** 

   * 若选择的文件夹中存在SKILL.md，则作为单个skill导入。
   * 若选择的文件夹中不存在SKILL.md，则遍历下一级文件夹，检查下一级文件夹中是否包含SKILL.md，遍历到的SKILL.md将作为skill导入。若下一级文件夹遍历出多个SKILL.md，将批量导入。仅支持遍历所选择文件夹的下一级，不支持更深层级的遍历。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/D6GTsX1sTmOogrP3334-vQ/zh-cn_image_0000002808886881.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C8F100DFDF80012329A0210AD320064A5B0D82E6A05A4AFA93083636AC9D76F "点击放大")
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括技能名称（如openharmony-build）、描述信息、启用状态。同时，将鼠标悬浮在技能信息上会显示编辑和删除的操作按钮，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/LQ9gBaORSUe7q-t4jxntjw/zh-cn_image_0000002779407242.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E51E5B49C194D6653C44AED1A3D08C54757FB48CF998DF818336A0541458349)可在代码编辑区打开SKILL.md文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/p7KNvmboR_GrVAFt3wiS7Q/zh-cn_image_0000002808766803.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C62AA3ABCE1B23405A90987C432967E76455FF581A6C58A967AAED5F5D4D8A8 "点击放大")
4. 返回CodeGenie对话框调用Skills，在对话框输入时需要带有技能的name（如openharmony-build）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/24I8EZHnQIqp9wTTZE6aJw/zh-cn_image_0000002779567220.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F8D449D713FCD57AB15159E473B9758AEB2BAED41DE9E690A8FA2D7FFB3F76B)
