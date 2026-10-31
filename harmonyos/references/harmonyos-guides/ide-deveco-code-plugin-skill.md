---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-skill
title: 配置Skill
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 操作指南 > 配置Skill
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:14+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:b3ea3981f2fce36116dff744b2b7f7bcbc8f5225e420bcd8fe893225a9f72ed6
---

在日常工作中，我们经常需要处理重复性任务，如调整文档结构、撰写周报告等，每次都需要输入格式要求、偏好、操作流程，这种模式不仅耗时，也容易遗漏关键细节。Skill是一份标准化的操作指导教程，用于规范DevEco Code处理任务时的思考方式、执行步骤、输出格式及注意事项。开发者只需要定义一次，DevEco Code便能在后续的每次对话中自动识别并应用，实现“一次定义，长期稳定复用”。

DevEco Code支持导入Global Skills和Project Skills两种。其中，Global Skills支持当前用户在本地所有项目中使用，不可跨设备同步；Project Skills仅适用于当前项目。开发者根据业务需要选择导入对应的Skills。

## Skill的结构

Skill实际是一个包含SKILL.md文件的文件夹，在SKILL.md文件中以自然语言描述技能的名称、触发条件和执行步骤，定义自动化工作流。

SKILL.md文件写作时，严格遵循业界YAML Frontmatter（元数据） + Markdown Body（正文） 的统一规范，以及要确保内容结构清晰、触发词准确、没有错误处理，提升Skill可维护性和可复用性，使Agent能够稳定执行。

**Skill目录结构**

一个Skill中须包含SKILL.md文件，还可以根据实际需求添加其他文件，例如开发指南和API参考资料、可执行代码等。

```txt
<name>/                              # 技能根目录
│
├── SKILL.md                         # 【必填】技能的唯一入口文件
├── references/                      # 【可选】开发指南和API参考资料，帮助工具生成精准内容
│   ├── ref1.md
│   └── ref2.md
├── scripts/                         # 【可选】用于确定性、可靠性要求高或被反复重写的任务的可执行代码
│   └── helper.sh
├── assets/                          # 【可选】生成输出时的引用文件，如PPT模板
│   └── template.txt
└── 其他文件/文件夹                    # 【可选】其他更多文件/文件夹
```

**SKILL.md****文件格式**

```md
---
name:必填，技能名称
description:必填，简要描述这个技能的功能和使用场景
when_to_use:选填
license:选填
metadata:选填
---

# 技能名称

正文指令内容...
```

* SKILL.md命名固定，区分大小写，不支持修改，且SKILL.md文件大小不超过100MB。
* SKILL.md中Frontmatter要求：以“---”开始，以"---"或"..." 结束。
* SKILL.md中name要求：长度不超过128个字符，由字母、数字、点号、中划线、下划线组成，以字母或数字开头。
* SKILL.md中正文要求：必须有一级标题（技能名称），正文指令内容以纯净Markdown格式书写。
* Skill文件夹和压缩包的要求：压缩包的大小不超过100MB，其中文件个数不超过2048个；文件夹或压缩包中均为常规文件（不可为符号链接和设备文件等）；文件夹或压缩包中仅包含一个SKILL.md。

## 操作步骤

1. 点击DevEco Code界面**Menu**中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/x_Soi5-UQfuWnNLlF9KIGQ/zh-cn_image_0000002806153093.png "点击放大")Skill卡片，或点击菜单栏**File > Setti**n**gs > AI > Skills**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/935LcF62S6uOQfKYh9ovMA/zh-cn_image_0000002776999528.png "点击放大")
2. 在**Global Skills**或**Project Skills**下，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/EzI_3Q8cQKG9KNTuc6kT6g/zh-cn_image_0000002806073193.png)导入Skill文件夹或文件夹的压缩包（.zip格式），点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/KHAyBJfNR0qsFph4DC8gfQ/zh-cn_image_0000002776953472.png)删除。SKILL.md的父目录为技能根目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ilwlHulbRhGC7QuqCgmPNA/zh-cn_image_0000002776839548.png "点击放大")
3. 在**Global Skills**和**Project Skills**列表中，显示已导入的技能信息，包括启用状态、技能名称、描述信息（最多显示60字符）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/u_zXTBKJSCWaYnNVVZsBjA/zh-cn_image_0000002806239319.png "点击放大")
4. 返回DevEco Code，在输入框输入"**/**"可以查看所有的Skills，选择对应Skill后进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/mGvUC8qITI-qlQvJafBb7Q/zh-cn_image_0000002806236299.png "点击放大")
