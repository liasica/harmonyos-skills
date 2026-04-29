---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie-releasenote
title: 版本说明
breadcrumb: 指南 > 使用AI智能辅助编程 > 版本说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:08+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4dd5f676700f2adcf1ff0ba354ee8c9d111f71f21a03d3c00e2a3b34f6265035
---

## 6.1.0.830

### 新增特性

* 新增支持配置Skills。具体请参考[技能（Skills）配置](ide-skills.md)。

### 变更特性

* HarmonyOS Ask智能体和HarmonyOS Act智能体不再限制字符数。

## 6.1.0.818

### 变更特性

* HarmonyOS Ask智能体和HarmonyOS Act智能体的限制字符数放开到100000字符。

## 6.1.0.816

### 新增特性

* HarmonyOS Ask智能体支持切换模型和配置三方模型。
* 新增工程问答能力。具体请参考[工程问答](ide-project-ask.md)。
* 代码续写支持添加模型和提示词。具体请参考[代码续写](ide-code-continuation.md)。
* 页面生成支持使用和切换模型，支持查看历史生成信息和生成文件信息。具体请参考[万能卡片生成](ide-codegenie-service-widget.md)。
* 支持在智慧调优中使用和切换模型。具体请参考[智慧调优](ide-ai-profiler.md)。
* 支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，支持从MCP市场添加MCP工具。具体请参考[模型上下文协议（MCP）配置](ide-agent-mcp.md)。
* 支持通过服务提供商接入三方模型，支持接入Ollama协议的三方模型。具体请参考[模型（Model）配置](ide-agent-model.md)。
* 规则设置新增Quality first和Token efficiency first的规则长度限制。具体请参考[规则（Rules）配置](ide-agent-rules.md)。
* 自定义智能体（Agent）新增Web Rag内置工具，BlockList变更为AllowList。具体请参考[自定义智能体（Agent）配置和调用](ide-agent-use.md)。
* CodeGenie搭载长期记忆功能，支持记忆配置。[记忆（Memory）配置](ide-memory.md)。
* 支持添加和管理提示词库。具体请参考[自定义提示词库（Prompts）配置](ide-prompts.md)。

### 变更特性

* 编辑区代码生成的入口名称由Code Generation变更为Code Completion & Inline Chat，代码续写开启的设置项名称、自动续写的设置项名称等均发生变化。

## 6.0.2.646

### 新增特性

* HarmonyOS Act智能体支持切换模型和配置三方模型。
* 支持通过服务提供商接入第三方模型，URL接入时支持使用Ollama协议的三方模型。具体请参考[模型（Model）配置](ide-agent-model.md)。
* 自定义智能体（Agent）配置时，DevEco Studio内置工具新增To Do工具，智能体支持切换模型和配置三方模型。具体请参考[自定义智能体（Agent）配置和调用](ide-agent-use.md)。

### 增强特性

* 优化了大模型调用构建工具执行构建命令时可能发生的异常问题。

## 6.1.0.609

### 新增特性

* Inline Edit入口名称变更为Inline Chat。具体请参考[编辑区对话](ide-edit-area-code-generation.md)。
* 通过CodeGenie生成页面后，预览时支持切换亮色和暗色模式。具体请参考[页面生成](ide-page-generation.md)。
* 智慧调优增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄露次数分析等内存问题场景。具体请参考[智慧调优](ide-ai-profiler.md)。
* CodeGenie页面的字体大小可通过鼠标滚轮调节，字体大小范围为8pt~24pt，以及字体大小可被记忆。

## 6.0.2.640

### 增强特性

* 新增HarmonyOS Act智能体，该智能体可读取和修改工程代码；HarmonyOS Ask智能体仅读取工程内容，不修改工程代码。

## 6.0.2.636

### 新增特性

* Inline Edit支持选择三方模型，对代码文件分析和生成分析报告，以及参数校验、代码注释、代码优化。具体请参考[编辑区代码生成](ide-edit-area-code-generation.md)。
* 增加OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。具体请参考[智慧调优](ide-ai-profiler.md)。
* 编译报错修复的交互过程进一步优化，支持编辑区显示修改前后的差异点，以及开启自动编译验证。具体请参考[编译报错智能分析](ide-compilation-error-analysis.md)。
* 支持用户配置全局级别或工程级别的开发规则（Rules），在自定义智能体模式下，可生成更加符合Rules规范的代码。具体请参考[规则（Rules）配置](ide-agent-rules.md)。
* 在模块右键新增页面生成入口。具体请参考[页面生成](ide-page-generation.md)。
* 自定义智能体配置时支持开启DevEco Studio内置工具Built-in Tools、Auto Run和Blocklist。具体请参考[自定义智能体（Agent）配置和调用](ide-agent-use.md)。

### 增强特性

* HarmonyOS Ask智能体可读取和修改工程代码，以及在问答区编译验证。
* 删除对话框中用于上下文定位的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BbHdkgx-RxCCxFPn7xtTQA/zh-cn_image_0000002530753628.png?HW-CC-KV=V1&HW-CC-Date=20260429T054507Z&HW-CC-Expire=86400&HW-CC-Sign=59150CA6CADDE8DA22F6DF0DAE34863F8758481A2609CDB63870A7D7D3C06BA3)图标，可直接对选中的代码段或代码文件分析。
* 智能问答和代码生成能力增强，更加高效理解用户意图。

## 6.0.1.246

### 新增特性

* 新增支持生成内容可与文件内容可快速对比和采纳功能。具体请参考[代码修改](ide-code-modify.md)。
* CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。具体请参考[自定义智能体](ide-agent.md)。

## 6.0.0.848

### 新增特性

* 新增生成意图装饰器和添加意图插件能力，以及DevEco Studio新增内嵌的小艺智能平台。具体请参考[意图装饰器生成和智能体创建](ide-insight-intent2.md)。
* 智能问答新增添加本地的知识库，并根据知识库进行指定风格的上下文问答功能。具体请参考[本地知识库配置](ide-ocal-knowledge.md)。

## 6.0.0.828

### 新增特性

* 新增编辑区代码续写逐行接纳能力。具体请参考[编辑区代码续写使用方法](ide-code-continuation.md#section1877616170312)。
* 新增支持上传页面参考图片，进行页面生成能力。具体请参考[页面生成](ide-page-generation.md)。

### 增强特性

* 页面生成增加教育垂域。具体请参考[页面生成](ide-page-generation.md)。
* 智能问答，代码智能解读以及单元测试用例生成限制字符数放开到30000字符。

## 6.0.0.456

### 新增特性

* 智能问答支持指定上下文进行交流，支持指定对单个或多个代码文件进行分析。具体请参考[代码分析](ide-code-analyse.md)。
* 新增页面生成功能，支持通过自然语言进行多轮对话，生成应用/元服务可用的页面代码，快速完成页面搭建。具体请参考[页面生成](ide-page-generation.md)。
* 针对编译构建场景的语法错误问题，提供问题修复能力。具体请参考[编译报错智能分析](ide-compilation-error-analysis.md)。
* 新增生成意图装饰器和添加意图插件能力，以及DevEco Studio新增内嵌的小艺智能平台。具体请参考[意图装饰器生成和智能体创建](ide-insight-intent2.md)。

### 增强特性

* 智能知识问答和自然语言代码生成入口合一，简化自然语言代码生成操作。具体请参考[自然语言代码生成](ide--code-generation.md)。
* 增强上下文解析能力，优化代码续写和Inline Edit模型回复效果。

## 5.1.0.828

* 支持智能问答，通过查询生成、内容优选服务高效理解用户意图，交互式地获取编码相关知识。具体请参考[智能知识问答](ide-harmonyos-ask.md)。
* 支持自然语言代码生成，Inline Edit能力以及代码续写，智能生成代码。具体请参考[代码生成](ide-codegenie-code-edit.md)。
* 支持万能卡片生成，通过对话式的交互智能生成HarmonyOS万能卡片工程。具体请参考[万能卡片生成](ide-codegenie-service-widget.md)。
* 支持代码智能解读功能，对框选的代码片段进行逐条解释，总结代码段含义。具体请参考[代码智能解读](ide-explain-code.md)。
* 新增单元测试用例生成功能，自动生成对应单元测试用例。具体请参考[单元测试用例生成](ide-ut-generation.md)。
