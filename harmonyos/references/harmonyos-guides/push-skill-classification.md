---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-skill-classification
title: 通知消息自分类权益推荐Skill
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > （可选）接入Skill > 通知消息自分类权益推荐Skill
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:18+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a8132d91590ed56314b4b03fd4b2c2fe69bb232439c194dbbbc14a3e8b71c2b9
---

## 概述

通知消息自分类权益推荐Skill，旨在帮助开发者快速选择合适的推送消息分类。开发者只需描述应用类型和推送场景，Skill即可推荐最合适的自分类权益类别，有效降低申请驳回率。

## 能力覆盖范围

通知消息自分类权益推荐Skill的能力如下：

* **智能推荐**：根据应用类型和推送场景自动推荐最佳分类。
* **错误规避**：分析高频驳回原因，提前规避常见错误。
* **格式指导**：各类消息的标题、内容格式规范。
* **申请指导**：涉及多个场景时，提供选择策略。

## 注意事项

* 营销类型为默认权益，未申请或使用错误类别时默认走营销通道。
* 营销类消息每天每台设备最多收到2条或5条提醒。
* 不同类别对标题、内容格式有不同要求，申请前请确认格式正确。

## 使用方式

1. **下载并配置Skill**：点击[通知消息自分类权益推荐Skill](https://gitcode.com/HarmonyOS_Samples/push-kit_-sample-code_-server-demo_-java/tree/master/hmos-push-kit-recommend-self-classification)下载，并放到AI编码工具（如DevEco CodeGenie、Claude Code等）的Skill配置目录下（不同工具规范不一致，按工具要求处理）。
2. **触发Skill**：向AI编码工具描述应用类型和推送场景，并在对话中加入关键词或者Skill名称触发Skill。见以下示例。

   | 使用方式 | 示例 |
   | --- | --- |
   | 关键词触发 | “帮我使用Push自分类推荐”、“帮我推荐xxx场景用什么push分类” |
   | Skill名称触发 | “请使用hmos-push-kit-recommend-self-classification推荐自分类权益” |
3. **获取推荐结果**：Skill分析后返回推荐类别和申请材料清单。
4. **准备材料并申请通知消息自分类权益**：根据推荐结果准备相应材料，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站提交申请，详情见[申请步骤](push-apply-right.md#申请步骤)。下图为金融应用的示例，描述场景然后通过Skill名称触发调用，AI返回相应推荐结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/q5hMO1FSRmWjDlqFgCtYMA/zh-cn_image_0000002742124317.png)
