---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b071
title: 针对API 12应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Release引入的接口行为变更 > 针对API 12应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a341cd945a93dc9e4315f15522a828b477a52579e06b25d4040fb593c83197ae
---

## ArkUI

### Navigation嵌套使用时的生命周期行为优化

**变更原因**

在嵌套使用Navigation的场景下,如果内层Navigation处于不可见的状态，不应该触发对应的onShown生命周期。

**变更影响**

此变更涉及应用适配。

变更前：在嵌套Navigation的场景下如果内层的Navigation不可见，此时如果应用对不可见的Navigation进行栈操作，会触发对应的onShown生命周期。

变更后：在嵌套Navigation的场景下如果内层的Navigation不可见，此时如果应用对不可见的Navigation进行栈操作，不会触发对应的onShown生命周期。

**起始API Level**

12

**变更的接口/组件**

onShown生命周期。

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。
