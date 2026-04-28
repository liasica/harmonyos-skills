---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-continuation
title: 代码续写
breadcrumb: 指南 > 使用AI智能辅助编程 > 编辑区代码生成 > 代码续写
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d51a80ab18d340863b6989ef31f13a5a39461d62890002f4005ce0724be04d8
---

利用AI大模型分析并理解开发者在代码编辑区的上下文信息或自然语言描述信息，智能续写符合上下文的ArkTS或C++代码片段，减少重复编码工作。

从DevEco Studio 6.1.0 Beta2版本开始，代码续写入口变更为Code Completion & Inline Chat，续写启动等设置相关选项的入口发生变化；支持添加模型和提示词。

## 使用约束

* 建议编辑区已有较丰富上下文，能够使AI模型对编程场景有一定理解的情况下进行续写。若编辑器中内容较少，AI模型可能无法有效理解用户的意图并生成相应的代码。
* AI模型反馈需满足规则：光标上文10行内，有效代码行数超过5行（排除单独{}、（）、[]括号行、空行、纯注释行场景）。

## 续写设置

### **DevEco Studio 6.1.0 Release及以上版本**

进入**File > Settings...**（macOS为**DevEco Studio > Preferences/Settings**）**>** **CodeGenie > Code Completion** **& Inline Chat**页面进行设置，若没登录华为开发者账号请先登录。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/X0HXx_-pTAOg79kIw52UOw/zh-cn_image_0000002530913706.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=4A0D8A108140C2B67AF880AC6020D20E2A49A0B9541E9D766984731CA94EF5DC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/uSp2yAsERRuXKg7jocJjGg/zh-cn_image_0000002530913702.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=812EB7182BAE3D771C86F499ECAB30C9C7680ECD36FA4E7D795932302FCA5467)

### **DevEco Studio 6.1.0 Beta2以下版本**

进入**File > Settings...**（macOS为****DevEco Studio > Preferences/Settings****）**>** **CodeGenie > Code Generation**页面勾选**Enable code generation**，开启代码续写功能。如果已经熟悉了CodeGenie常用的快捷键，想要更加沉浸的体验，可以在该页面勾选**Do not disturb** **mode**，隐藏代码生成工具栏及快捷键提示。

同时，根据编码习惯，选择**Enable snippet generation**（片段续写）和**Enable inline generation**（行内续写），以及设置续写时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/-LOKwuw1TXGJr48F9BXh9w/zh-cn_image_0000002530753714.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=5C52099F97A83A3177E4693CAD0D23B571CC3D89C412FEE18A0CBD7A686111EF)

## 续写触发和采纳

### 续写触发

**DevEco Studio 6.1.0 Release及以上版本**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Auto Suggestion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/l7sC2C3DTwCMQeYH17mrug/zh-cn_image_0000002530913708.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=65B11CA76314B0F8F578229BDCF5D14F9630A76CD2D6C26C9DAE183AD30E012D)

**DevEco Studio 6.1.0 Beta2**

Enable inline generation（行内续写）与Enable snippet generation（片段续写）合并为**Enable code auto completion**，取消了**Delay**设置项，通过设置**Frequency**调整自动续写的触发频次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/E3K2SuMHSEShCCq3RCxqiw/zh-cn_image_0000002561753647.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=CDB9B7502750824D003CE281E95962F7CB262D61274E86B8BF0171BB61625B74)

**DevEco Studio 6.1.0 Beta2以下版本**

* **Enable inline generation**（行内续写）：在编码时稍作停顿，CodeGenie将在当前代码行即时续写代码。
* **Enable snippet generation**（片段续写）：输入回车，CodeGenie将根据上下文生成代码片段。
* 在编辑区输入**Alt+C**快捷键（macOS上为**Option+C**）触发代码续写。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ivltSfsqSA28if2HKkAn8w/zh-cn_image_0000002530753712.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=A9527247117CD1954E3206F1470D5725D69CF9975374E76537844C551774753F)

### 续写采纳

**续写内容采纳方式****：**

* 可通过按**Ta****b**键采纳该内容。
* **Ctrl + ↓（**macOS中为**Command + ↓****）**逐行采纳该内容。
* **Ctrl + →****（**macOS中为**Option + →****）**逐单词采纳该内容。
* 通过按**ESC**键忽略该内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/-w2devqxS4ih27di_FPfoA/zh-cn_image_0000002530753710.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=5BA561A94BCEEE05CACBF4716010CB09CB06956A0974FEB594D0BD0EB89A333A)

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
| 展示CodeGenie面板 | Option + U | Alt + U |
| 代码逐行采纳 | Command + ↓ | Ctrl + ↓ |
| 代码逐单词采纳 | Option + → | Ctrl + → |
