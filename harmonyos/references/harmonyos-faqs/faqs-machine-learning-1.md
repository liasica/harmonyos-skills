---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-machine-learning-1
title: 拉起智能体对话框，通过queryText预设的问题没生效如何解决
breadcrumb: FAQ > AI功能开发 > 机器学习 > 拉起智能体对话框，通过queryText预设的问题没生效如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:ccb3303386ae031de4f07a957e1c774f1508b626c83948e2a5aa2766ea8b419e
---

## 问题现象

使用FunctionComponent创建智能体，通过queryText预设问题。但是拉起智能体对话框，通过queryText预设的问题未生效。

## 背景知识

通过Function组件拉起智能体[开发前准备](../harmonyos-guides/hmaf-function.md#开发前准备)：

* 创建智能体，具体请参见[快速创建智能体](../service/developing-intelligent-agents-0000002435989592.md)。
* 关联应用，具体请参见[关联应用](../service/related-applications-0000002437785706.md)。
* 确保已在终端设备上登录华为账号，并且处于联网状态。

## 问题定位

日志信息如下：

```txt
relatedApps = undefined
```

说明智能体与应用未成功关联。

## 分析结论

智能体与应用之间的关联配置存在问题。

## 修改建议

1. 确保应用接入的智能体AgentId准确，并且该智能体已完成上架，参考[快速创建智能体](../service/developing-intelligent-agents-0000002435989592.md)。
2. 在组件加载前通过[isAgentSupport](../harmonyos-references/hmaf-function-component.md#isagentsupport)来判断当前的AgentId是否可用，若AgentId有效且Agent功能支持时再加载组件；
3. 在智能体中配置了关联的应用信息，确保关联的应用包名、appId等信息一致并且在配置中开启关联应用。参考[关联应用](../service/related-applications-0000002437785706.md)。
