---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-continuation
title: 代码续写
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 编辑区代码生成 > 代码续写
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:e6a5297f04d18d65c019cc9bb125d44f7f546abf703adb04a1b81693b495978e
---

利用AI大模型分析并理解开发者在代码编辑区的上下文信息或自然语言描述信息，智能续写符合上下文的ArkTS代码片段，减少重复编码工作。

## 使用约束

* 建议编辑区已有较丰富上下文，能够使AI模型对编程场景有一定理解的情况下进行续写。若编辑器中内容较少，AI模型可能无法有效理解用户的意图并生成相应的代码。
* AI模型反馈需满足规则：光标上文10行内，有效代码行数超过5行（排除单独{}、（）、[]括号行、空行、纯注释行场景）。

## 续写设置

### 26.0.0 Beta1及以上版本

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings） > CodeGenie > Code Suggestion**，勾选**Enable Flow Editor**，点击**OK**或**Apply**，开启续写设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/6F5LYvNuRFGKGOiKOezbKA/zh-cn_image_0000002808887251.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE2B188F681FBD7CA2C782E35C760DBB3014CE993761845863068319D887A327)

### DevEco Studio 6.1.0 Release及以上版本

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Suggestion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

**快捷键和续写开启设置**选项**：**

* **Display hints for code suggestion inline chat**：在编辑区空行显示触发代码续写等功能的快捷键。
* **Enable**：启用代码续写能力。
* **Display hints for accept shortcuts**：在续写结果最后的位置显示采纳代码的快捷键。

**自动续写设置**选项**：**

* **Auto Suggestion**：自动续写开关，开启后将会根据代码上下文在合适位置自动触发代码续写。
* **Frequency**：控制自动续写的触发频率。
* **Allow auto suggestion for code completion**：是否允许自动续写与编辑器联想功能同时存在。取消勾选后，编辑器联想功能优先级更高。

**续写模型设置**选项**：**

CodeGenie为续写功能提供了内置的模型，也可使用三方模型和提示词进行续写。当前续写仅支持OpenAI和Ollama两种协议的模型，同时模型需支持FIM（Fill-in-Middle）补全能力。

* **Model**：选择代码续写的模型，模型内容请参考：[模型（Model）配置](ide-agent-model.md)。
* **Prompt format**：提示词格式，此处列出了主流的FIM提示词格式，并自动与模型选项联动。设置时需要选择与模型匹配的提示词格式，续写才能正常工作，开发者可在模型官网或者模型技术报告获取提示词格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/481WyU_4TrSJz_ux2TjAHw/zh-cn_image_0000002779407614.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5592DA91518B2C50256DF45F7D622207FAA4E683C82D3C2511069B4B86255B3)

### DevEco Studio 6.1.0 Beta2

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Completion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

**快捷键和续写开启设置**选项**：**

* **Show trigger shortcut tips**：在编辑区空行显示触发代码续写等功能的快捷键。
* **Enable code completion**：启用代码续写能力。
* **Show accept shortcut tips**：在续写结果最后的位置显示采纳代码的快捷键。

**自动续写设置**选项**：**

* **Enable code auto completion**：自动续写开关，开启后将会根据代码上下文在合适位置自动触发代码续写。
* **Frequency**：控制自动续写的触发频率。
* **Auto-completion is allowed when code completion is triggered**：是否允许自动续写与编辑器联想功能同时存在。取消勾选后，编辑器联想功能优先级更高。

**续写模型设置**选项**：**

CodeGenie为续写功能提供了内置的模型，也可使用三方模型和提示词进行续写。当前续写仅支持OpenAI和Ollama两种协议的模型，同时模型需支持FIM（Fill-in-Middle）补全能力。

* **Model**：选择代码续写的模型，模型内容请参考：[模型（Model）配置](ide-agent-model.md)。
* **Prompt format**：提示词格式，此处列出了主流的FIM提示词格式，并自动与模型选项联动。设置时需要选择与模型匹配的提示词格式，续写才能正常工作，开发者可在模型官网或者模型技术报告获取提示词格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/uwdR-2xdSQ2ggyUI24SEnA/zh-cn_image_0000002808767165.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D9931C8F65E414BC3D3BF05D7E88FE4E9990F9B526B22B0C2385F12E01129C2)

### DevEco Studio 6.1.0 Beta2以下版本

进入**File > Settings...**（macOS为****DevEco Studio > Preferences/Settings****）**>** **CodeGenie > Code Generation**页面勾选**Enable code generation**，开启代码续写功能。如果已经熟悉了CodeGenie常用的快捷键，想要更加沉浸的体验，可以在该页面勾选**Do not disturb** **mode**，隐藏代码生成工具栏及快捷键提示。

同时，根据编码习惯，选择**Enable snippet generation**（片段续写）和**Enable inline generation**（行内续写），以及设置续写时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/MR_zsbytSUSeLxHDVMZvxw/zh-cn_image_0000002779407612.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FF909B91934BD40AB29DA40A912BF9E1B1D74819710BA8DB9910A396499E497)

## 续写触发和采纳

### 续写触发

**26.0.0 Beta1及以上版本**

打开续写设置后，在代码编辑器区域，会自动续写代码和给出代码修改建议。

因续写为自动触发，可能会与LSP共存，使用**Alt + S**快捷键（macOS上为**Option+S**）可切换至仅开启代码续写功能。

**DevEco Studio 6.1.0 Release及以上版本**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Auto Suggestion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/wZc43325QAuvaUMYs7fW6Q/zh-cn_image_0000002779567590.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0ADCA4527D5D5901D891ED7BA6E0F2ACAE5919B5136756E7D07A3C3C3F76826)

**DevEco Studio 6.1.0 Beta2**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Enable code auto completion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/rmciAnqbSWKqi42U5cpPxA/zh-cn_image_0000002808887249.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=58275C33B9E16B8CC93807ED498C53EC46A45385CF566F378DE6E9099F6D1904)

**DevEco Studio 6.1.0 Beta2以下版本**

* **Enable inline generation**（行内续写）：在编码时稍作停顿，CodeGenie将在当前代码行即时续写代码。
* **Enable snippet generation**（片段续写）：输入回车，CodeGenie将根据上下文生成代码片段。
* 在编辑区输入**Alt+C**快捷键（macOS上为**Option+C**）触发代码续写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/nUB3sSEbT6Gg6bIR0wLzPw/zh-cn_image_0000002808767163.png?HW-CC-KV=V1&HW-CC-Date=20261114T004908Z&HW-CC-Expire=31536000000&HW-CC-Sign=82441333192BC6EB777A49D848082678070A5B833B0945238AC090EFD74B66F4)

### 续写触发和采纳快捷键

**26.0.0 Beta1及以上版本**

|  |  |  |
| --- | --- | --- |
| **操作** | **macOS** | **Windows** |
| 采纳续写生成的代码 | Tab | Tab |
| 忽略续写生成的代码 | Esc | Esc |
| 代码逐行采纳 | Command + ↓ | Ctrl + ↓ |
| 代码逐行取消 | Command + ↑ | Ctrl + ↑ |

**26.0.0 Beta1以下版本**

|  |  |  |
| --- | --- | --- |
| **操作** | **macOS** | **Windows** |
| 触发多行代码续写 | Enter、Option+C | Enter、Alt+C |
| 触发单行代码续写 | Option+X | Alt+X |
| 采纳续写生成的代码 | Tab | Tab |
| 忽略续写生成的代码 | Esc | Esc |
| 查看上一个代码续写结果 | Option +[ | Alt + [ |
| 查看下一个代码续写结果 | Option + ] | Alt + ] |
| 重新生成代码内容（最多支持重新生成5次） | Option + R | Alt + R |
| 代码逐行采纳 | Command + ↓ | Ctrl + ↓ |
| 代码逐单词采纳 | Option + → | Ctrl + → |
