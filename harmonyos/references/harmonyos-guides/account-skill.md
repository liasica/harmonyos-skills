---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-skill
title: Account Kit Skill能力开放
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit Skill能力开放
category: harmonyos-guides
scraped_at: 2026-10-29T07:57:32+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:f8f3c1d0d789e479d5dc8812704810311cdfe432e9bd154fadae94aef3fb88f9
---

## 概述

Account Kit接入Skills，旨在帮助开发者快速集成Account Kit开放能力。开放Skills包含客户端与服务端两部分，可自动生成客户端页面代码与服务端接口工程，支持端到端验证，有效简化接入流程、降低开发成本。

### 能力覆盖范围

* **华为账号一键登录Skill**：帮助开发者快速接入华为账号一键登录能力。其中：
  + [客户端Skill](https://matrix.openharmony.cn/#/skillSquare/details?id=6a215e9b8428f219b71f84a2)负责生成ArkTS华为账号一键登录页面、配置工程依赖与添加权限，并实现页面跳转逻辑。
  + [服务端Skill](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-serverdemo/tree/Java/huawei-account-kit-quicklogin-server)负责生成服务端工程代码，实现授权码换取用户信息的接口。
* **华为账号登录Skill**：帮助开发者快速接入华为账号登录能力。
  + [客户端Skill](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/02-development/account-kit/hmos-account-kit-login-button-client)负责生成华为账号标准登录页面（使用华为标准登录按钮）、配置工程依赖与添加权限，实现页面跳转逻辑。
* **自定义按钮登录Skill**：帮助开发者快速接入华为账号自定义按钮登录能力。
  + [客户端Skill](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/02-development/account-kit/hmos-account-kit-login-api-client) 负责生成自定义登录按钮组件（支持纯图标、纯文本、图文混合三种模式）、配置工程依赖与添加权限，实现登录请求逻辑。

## 快速开始

1. 下载并配置Skill：请在[能力覆盖范围](account-skill.md#能力覆盖范围)章节中点击对应Skill的超链接进行下载，并放到AI编码工具（如OpenCode、Claude Code等）的Skill配置目录下（不同工具规范不一致，按工具要求处理）。
2. 配置DevEco CLI（服务端Skill无需此项配置）：在终端执行以下命令安装DevEco CLI，更多详情请参考[DevEco CLI](ide-deveco-cli.md)官方文档。

```json5
 npm install -g @deveco/deveco-cli@latest
```

**验证是否生效：**

1. 确定Skill是否生效：打开AI编码工具，输入“帮我接入华为账号一键登录”。如果Skill已生效，会进行前置检查并遵循接入步骤执行，而不是直接开始编码。
2. 确定CLI是否生效：可通过以下命令验证。

   ```json5
   devecocli --version
   devecocli --help
   ```

## 使用方式

在AI编码工具中通过关键词或Skill名称触发，以华为账号一键登录客户端Skill为例。

**关键词触发**：帮我接入华为账号一键登录

**Skill名称强制触发**：使用“hmos-account-kit-quicklogin-client”Skill，帮我接入华为账号一键登录

| 技能 | Skill名称 | 关键词 |
| --- | --- | --- |
| 华为账号一键登录客户端Skill | hmos-account-kit-quicklogin-client | 帮我接入华为账号一键登录 |
| 华为账号一键登录服务端Skill | huawei-account-kit-quicklogin-server | 帮我生成华为账号一键登录服务端java代码 |

## 注意事项

* 客户端Skill生成的代码需在ArkTS工程中运行，当前仅支持ArkTS开发框架。
* 请务必在集成发布前，在测试环境中充分验证所生成代码的正确性与安全性。
* 使用Skill前，请确保已阅读并同意本指南中的**免责声明**。

## 免责声明

为保障平台及开发者双方的合法权益，特此声明如下：

**代码生成责任**：我方不对生成代码的正确性、安全性做任何担保。使用本Skill文档自动生成的代码，开发者在使用过程中应自行审核、测试并确保其适用性与准确性。因代码错误、不兼容或使用不当所引发的任何直接或间接损失，包括但不限于经济损失、数据丢失、系统故障等，均由开发者自行承担全部责任。

**平台免责**：开发者应自行选择合法合规的AI工具，严格遵循所选AI工具的版权规定及使用规范。我们不对因使用本Skill文档生成的代码所导致的任何问题承担责任，包括但不限于法律纠纷、第三方索赔、系统运行异常等。

**使用前提**：开发者在使用本Skill文档前，应充分理解并接受其使用风险，建议在正式上线前进行充分测试与验证。

**合规提示**：开发者应确保其使用行为符合相关法律法规及行业规范，平台不对开发者的行为合法性进行担保或审查。

**版权声明**：本Skill文档的版权归属我方所有，开发者不得擅自篡改、传播、转售、出租本文档，不得用于与接入华为账号服务无关的其他用途。如开发者存在前述违规使用行为，我方有权追究法律责任。
