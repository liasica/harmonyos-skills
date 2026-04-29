---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-continuation
title: 代码续写
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 代码续写
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:11+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:34e086b482304d01aea1fe86c07b399058dda9f5342eb246eda51ab7857b7cce
---

利用AI大模型分析并理解开发者在代码编辑区的上下文信息或自然语言描述信息，智能续写符合上下文的ArkTS或C++代码片段，减少重复编码工作。

## 使用约束

* 建议编辑区已有较丰富上下文，能够使AI模型对编程场景有一定理解的情况下进行续写。若编辑器中内容较少，AI模型可能无法有效理解用户的意图并生成相应的代码。
* AI模型反馈需满足规则：光标上文10行内，有效代码行数超过5行（排除单独{}、（）、[]括号行、空行、纯注释行场景）。

## 续写设置

### **DevEco Studio 6.1.0 Release及以上版本**

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ghqbEX7fQry4e4V4BA753g/zh-cn_image_0000002530913706.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=FD60C796DB0E3D848B8AD47BDD63A5068220DC7905CEEB6466B1F90D2D61B010)

### **DevEco Studio 6.1.0 Beta2**

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Completion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

**快捷键和续写开启设置**选项**：**

* **Show trigger shortcut tips**：在编辑区空行显示触发代码续写等功能的快捷键。
* **Enable code completion**：启用代码续写能力。
* **Show accept shortcut tips**：在续写结果最后的位置显示采纳代码的快捷键。

**自动续写设置**选项**：**

* **Enable code auto completion**：自动续写开关，开启后将会根据代码上下文在合适位置自动触发代码续写。
* **Frequency**：控制自动续写的触发频率。
* **Auto-completion is allowed when code completion is triggerd**：是否允许自动续写与编辑器联想功能同时存在。取消勾选后，编辑器联想功能优先级更高。

**续写模型设置**选项**：**

CodeGenie为续写功能提供了内置的模型，也可使用三方模型和提示词进行续写。当前续写仅支持OpenAI和Ollama两种协议的模型，同时模型需支持FIM（Fill-in-Middle）补全能力。

* **Model**：选择代码续写的模型，模型内容请参考：[模型（Model）配置](ide-agent-model.md)。
* **Prompt format**：提示词格式，此处列出了主流的FIM提示词格式，并自动与模型选项联动。设置时需要选择与模型匹配的提示词格式，续写才能正常工作，开发者可在模型官网或者模型技术报告获取提示词格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/0JXDZyPeQ1-63DiNKBSbSQ/zh-cn_image_0000002530913702.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=47DD4F798833AB8E81150ACFADF9CB175B27D049E1CD689436114A64FA083A40)

### **DevEco Studio 6.1.0 Beta2以下版本**

进入**File > Settings...**（macOS为****DevEco Studio > Preferences/Settings****）**>** **CodeGenie > Code Generation**页面勾选**Enable code generation**，开启代码续写功能。如果已经熟悉了CodeGenie常用的快捷键，想要更加沉浸的体验，可以在该页面勾选**Do not disturb** **mode**，隐藏代码生成工具栏及快捷键提示。

同时，根据编码习惯，选择**Enable snippet generation**（片段续写）和**Enable inline generation**（行内续写），以及设置续写时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Tb6bNBQjRhWlnkNpKnKAhA/zh-cn_image_0000002530753714.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=55EBAF9571769B11CCBCC6E7CE511E36FDC8CEA179FF0FDD61637563C39B842F)

## 续写触发和采纳

### 续写触发

**DevEco Studio 6.1.0 Release及以上版本**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Auto Suggestion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/0ZwqRX6eR5O0FaMKhvDicg/zh-cn_image_0000002530913708.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=B4E2DA9E26E53E532A9485937826F607F441D7698745598782740E9766F58DC4)

**DevEco Studio 6.1.0 Beta2**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Enable code auto completion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/1f3tSB9sSqGs-LWhImnmdw/zh-cn_image_0000002561753647.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=97FF6BF887B4E6019C655DE20FE3B80D5756E70ACFE4C7CB5980D11B34B24433)

**DevEco Studio 6.1.0 Beta2以下版本**

* **Enable inline generation**（行内续写）：在编码时稍作停顿，CodeGenie将在当前代码行即时续写代码。
* **Enable snippet generation**（片段续写）：输入回车，CodeGenie将根据上下文生成代码片段。
* 在编辑区输入**Alt+C**快捷键（macOS上为**Option+C**）触发代码续写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Dt7jfI3hSq-aG89mlBW4Hw/zh-cn_image_0000002530753712.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=EB3A238662728A5B93BFFDDC3BE1918E0CAE71A267E415EFCA7B8FB3C2711F79)

### 续写采纳

**续写内容采纳方式****：**

* 可通过按**Ta****b**键采纳该内容。
* **Ctrl + ↓（**macOS中为**Command + ↓****）**逐行采纳该内容。
* **Ctrl + →****（**macOS中为**Option + →****）**逐单词采纳该内容。
* 通过按**ESC**键忽略该内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/LODTQYkeTGqIY2XdmGSAQQ/zh-cn_image_0000002530753710.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=4E063027A0FBC47493A42B6F4867C5A3C4EE1A5BB7B8FBAC75DE6B8E2AB236AE)

**CodeGenie续写常用快捷键如下：**

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
