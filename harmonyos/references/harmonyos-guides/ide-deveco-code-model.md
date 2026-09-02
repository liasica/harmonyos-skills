---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-model
title: 模型配置
breadcrumb: 指南 > AI Coding > DevEco Code > 模型配置
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:239bff8c3912fda3307bc58c95071f199742fcfbc9ebd524d1eb49ac404beb64
---

DevEco Code当前内置GLM-5.1模型，单账号默认每分钟50次请求，登录后即可使用，无需额外配置。如需使用第三方模型，可以通过如下方式配置。

在DevEco Code对话框输入**/models**进入模型切换界面。

## 通过Provider配置

在DevEco Code对话框输入**/connect**进入，选择提供商（如ZhipuAI、Alibaba）、输入API Key、选择模型。

**说明** 

多模态模型（仅支持Qwen系列）支持图片输入。

## 通过deveco.jsonc文件配置

在本地PC查找和编辑deveco.jsonc文件。若该文件不存在，需新建该文件。

配置文件优先级：

* Windows：.deveco/deveco.jsonc（项目级） > C:/Users/用户名/.config/deveco/deveco.jsonc（用户级）
* macOS：.deveco/deveco.jsonc（项目级） > ~/.config/deveco/deveco.jsonc（用户级）

示例：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {                 
    "deveco": {
      "name": "DevEco Code",
      "models": {
        "glm-5.1": { // 模型名称，需要自行配置
          "tool_call": true,
          "limit": {
            "context": 200000,
            "output": 8192
          }
        }
      },
      "options": {
        "baseURL": "https://api.openbitfun.com/v1", // 模型的访问地址，需要自行配置
        "apiKey": "{env:DEVECO_API_KEY}" // 模型的访问密钥，需要自行配置
      }
    }
  }
}
```

## UI检查配置

UI检查是功能验证阶段的可选能力，用于验证界面是否符合需求描述。

该功能需调用多模态模型（仅用于UI检查，不作为主对话模型）：已登录账号时默认使用内置Qwen3-VL模型，未登录时则跳过UI检查。

如需配置第三方多模态模型（仅支持Qwen系列），可在deveco.jsonc的agent中指定，以qwen3-vl-plus为例：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "alibaba",
      "options": {
        "baseURL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "apiKey": "your-api-key",
      },
      "models": {
        "qwen3-vl-plus": { // 模型名称，需要自行配置
          "modalities": {
            "input": ["text", "image"],
            "output": ["text"],
          },
        },
      },
    },
  },
  "agent": {
    "ui_verification": {
      "mode": "subagent",
      "model": "myprovider/qwen3-vl-plus", // 格式为<provider-name>/<model-name>
      "hidden": true,
    },
  },
}
```
