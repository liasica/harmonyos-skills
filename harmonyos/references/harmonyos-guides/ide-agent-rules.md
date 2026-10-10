---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:13+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5b23c83aaccc95cd790546acf769357b2f326764c8ce9ef7addb2cef2b9446d9
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

* **Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。
* **Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

**说明** 

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/HeMPapiOQUu6NcgOCXXyHA/zh-cn_image_0000002731381899.png)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/l4uRJVxoTZquHlZzIrOr_Q/zh-cn_image_0000002701822582.png)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/E6g-GdsVRtKnCE1z_pAUsQ/zh-cn_image_0000002701822586.png)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/wKOfF5boQwm9y7rtrT8ZGA/zh-cn_image_0000002701662654.png)
3. 以有网络环境为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/GvTvj16-TIqZMIeu1Qu27Q/zh-cn_image_0000002731541871.png)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/flY5pkXJQqy__xLXzSLb-g/zh-cn_image_0000002701822596.png)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dEzla7KFTMGuufxgms4jFw/zh-cn_image_0000002731541853.png)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/KkQ8jahQS_OQnlcHEyYwaQ/zh-cn_image_0000002731541875.png)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/y_QYdyz1QCircs9LvNosJg/zh-cn_image_0000002731541849.png)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Bmy6EAy3TSSmGaldJdulFw/zh-cn_image_0000002731381891.png)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/7xphLnWzR6-wao_v7HGFag/zh-cn_image_0000002701662652.png)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/GjrapHHqQC27dlVd69kHBA/zh-cn_image_0000002701662672.png)
