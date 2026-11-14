---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-memory
title: 记忆
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > 记忆
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:95022c1b17065102a39eca7735af9bc04c766e0bfc9efbd7a38211e2e4ccf3ee
---

## 功能概述

记忆功能可以让工具在多次会话之间持续积累关于用户和项目的信息，不断提升后续交互的准确性和个性化程度，核心用途包括：

* **记住用户偏好：**如代码风格、常用语言，让后续生成内容更贴合个人习惯。
* **记住纠正行为：**用户纠正过工具的地方会被记下（如不要在测试中mock数据库），避免重复犯错。
* **积累项目上下文：**记录无法从代码或git直接推导的项目上下文，如项目动机、约束、决策原因、截止日期，避免每次都要重新说明。
* **保存资源指针：**记录外部资料、文档的链接（不复制内容），需要时快速引用。

工具有记忆后，会越来越了解开发者和项目，减少重复沟通、提高输出质量。

记忆类信息通常分为user、feedback、project、reference等类型，并设置不同的存活期（TTL），过期后由开发者确认保留或清理，兼顾便利与隐私性。记忆类型和存活期如下：

* **user类型：**用于记录用户角色、偏好、背景与工作风格，如用户是数据科学家、偏好TypeScript。默认存活期（TTL）为永不过期。
* **feedback类型：** 用于记录行为准则，即该做与不该做的事项，来源为开发者对工具的纠正与确认，如不要在测试中mock数据库。默认存活期（TTL）为180天。
* **project类型：** 用于记录无法从代码或git直接推导的项目上下文，包括项目动机、约束、截止日期，以及带有非显式理由的决策，如下周三起冻结非关键合并。默认存活期（TTL）为90天。
* **reference类型：** 用于记录外部资源与文档指针，只保存链接，不复制内容，如bug跟踪在某个issue系统中。默认存活期（TTL）为 30 天。

TTL以记录的最后更新时间开始计算，记忆过期后不会直接删除，而是进入待确认流程，开发者确认后可清理。

## 配置记忆

记忆由memory插件在对话中自动提取和写入，并在后续对话中按需召回。输入**/memory**命令打开记忆面板，在面板中开启或关闭记忆的相关功能。各开关的名称、作用和默认开启情况如下：

* **Auto memory：**自动记忆，记忆的总开关。关闭后不再向对话注入记忆，记忆工具停用，自动提取停止。默认已启用。
* **Auto dream（consolidation）：**自动梦境整合，随着记忆增多，可能会出现重复、过时、互相矛盾的记忆内容，该开关可帮助用户实现记忆的整理、合并、删除冗余冲突记忆等。默认已启用。

  有两种触发整合的方式：
  + 方式一：自动触发，需要满足如下两个要求。

    |  |  |
    | --- | --- |
    | **要求** | **说明** |
    | 时间要求 | 距上次记忆整合超过默认值。若从未整合过，无需等待可直接整合。默认为24小时。 |
    | 会话要求 | 距上次记忆整合累计使用超过2个会话（同一会话内多次发消息只计1次）。默认为2。 |
  + 方式二：手动触发，输入**/dream-force**命令，或输入“整理记忆”等自然语言，然后由模型调用dream-trigger工具开始整合。
* **Auto extraction：**自动提取记忆，会话空闲后自动从对话中提取新记忆。默认已启用。
* **Memory recall：**记忆召回，发送消息时按语义相关度召回记忆，注入当前上下文。默认已启用。
* **Show recall in chat：**对话中显示召回，在回复开头显示本轮召回的记忆。默认已启用。
* **Show memory writes in chat：**对话中显示写入，在回复开头显示本轮写入的记忆。默认已启用。
* **Skill extraction：**技能沉淀，可以把可复用的操作流程（如某类构建问题的排查步骤）沉淀为独立的skill文件。默认已禁用 。

  触发方式为：在对话框中输入“提取技能”、“总结成技能”等关键词，或输入**/auto-skill**命令，即可生成全局skill，开发者在后续应用开发中调用该skill。

通过空格或回车切换启用状态（已启用/已禁用），切换启用状态后需重启生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/U18My6BjTF2Mu1IaarKbkQ/zh-cn_image_0000002779406802.png?HW-CC-KV=V1&HW-CC-Date=20261114T004732Z&HW-CC-Expire=31536000000&HW-CC-Sign=C66CE5783E64F181C7587A8B7992F73F2F050332B1B0DAB2910126481D2ACE32)

## 查看记忆列表

输入**/memory**命令打开记忆面板后，可在Memories下查看当前项目的所有记忆，记忆行尾显示更新时间与类型，按更新时间倒序排列。若当前没有记忆，Memories下显示No memories yet（暂无记忆），以及记忆的存储位置：/Users/用户名/.local/share/deveco/memory/<项目标识>/（macOS：~/.local/share/deveco/memory/<项目标识>/）。

通过**空格**或**回车**查看记忆详情。详情页显示的信息包括：记忆描述、类型、创建/更新时间、默认存活时间（TTL）、正文与文件路径等，支持选中复制记忆内容。

通过**Esc**或**回车**，从详情页返回记忆列表。

通过**Ctrl+D**（macOS：**Command+D**）快捷键删除记忆，用户确认后即可删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Yqacm-EYT_-TZCf0TqbMIQ/zh-cn_image_0000002808886443.png?HW-CC-KV=V1&HW-CC-Date=20261114T004732Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9AC45D0338B4A8B078D511BC1AF9C1C8DB2E8FCB2B728258F7701443B8C6292)

## 触发记忆

记忆功能默认开启，开箱即用。第一次使用时，开发者可能看到如下的交互场景：

* 工具回复开头出现：Recalled N memories: 名称(类型), ...，则表示本次提问自动召回了相关记忆。
* 工具回复开头出现：Memory '名称' created/updated，则表示AI刚写入或更新了一条记忆。
* 以及每轮对话结束后，界面右上角弹出浮动提示（toast）“开始后台提取 (记忆)...”，会话列表短暂出现标题为记忆提取 — ... 的后台会话，完成后自动消失。

开发者可通过如下自然语言触发不同的记忆行为：

|  |  |
| --- | --- |
| **对话框输入的自然语言** | **记忆行为** |
| 记住/以后/默认/总是/千万别/我喜欢/remember/always/ never等 | 立即写入记忆 |
| 不对/ 错了/应该是/actually等 | 更新或新建纠正记忆 |
| 忘掉/删除记忆/forget等 | 删除对应记忆 |
| 整理记忆/清理记忆/合并记忆等 | 触发自动整合 |

示例：

```screen
（本次会话）
自然语言：记住本项目提交信息均用中文。
AI：（调用 memory-write）Memory 'commit-language-chinese' created
好的，已记住：本项目提交信息均用中文。

（新会话）
自然语言：帮我写一条提交信息。
AI：Recalled 1 memories: commit-language-chinese(feedback)
feat(tui): 修复滚动状态丢失问题
（已按你的偏好使用中文）
```
