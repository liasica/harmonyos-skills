---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1841e513fca8a5d575b3419bd217735be4a9ef663da5709253bfbcac8bf0dc8d
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

* **Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。
* **Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

**说明** 

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/hnhYhzHXR8CLoQgmzBiIvg/zh-cn_image_0000002731381899.png)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/NsintOyWRTyRCMHICJtTig/zh-cn_image_0000002701822582.png)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/rNWpAaz6R3Gtw8Z5RBNJ-w/zh-cn_image_0000002701822586.png)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/uLokvxWCQkOtGv5uZ5q7ow/zh-cn_image_0000002701662654.png)
3. 以有网络环境为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Yg78TeUJQFe2bAaba4aBGg/zh-cn_image_0000002731541871.png)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/KWZjjydURW-y6NkL7qpTUQ/zh-cn_image_0000002701822596.png)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/O74qG0CeT66FxoEN4WkgjA/zh-cn_image_0000002731541853.png)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/BlyX1ph0TO-U5ynlq8QiOg/zh-cn_image_0000002731541875.png)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_7o3sbDFThWyCSKKbn5ULQ/zh-cn_image_0000002731541849.png)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/SthuzRsTRZKlSixi8dSo1A/zh-cn_image_0000002731381891.png)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ptmjLNcnRciYACaOwZ8etg/zh-cn_image_0000002701662652.png)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/01GnHe52SrWf_tdTmovcMA/zh-cn_image_0000002701662672.png)
