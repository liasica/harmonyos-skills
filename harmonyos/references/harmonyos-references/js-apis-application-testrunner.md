---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-testrunner
title: "@ohos.application.testRunner (TestRunner)"
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > @ohos.application.testRunner (TestRunner)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0f49925ee36071726a21dfd903e7a46c8a51271514338ef5c3b783dcd6672576
---

TestRunner是自动化测试框架中的基础模板类，它提供了测试环境准备和测试用例运行的标准接口。开发者通过继承并实现onPrepare()和onRun()方法，可以构建自定义的测试执行逻辑，为测试框架提供了可扩展的基础。

该模块适用于需要实现自定义单元测试框架或扩展测试功能的场景，但仅限在自动化测试框架中使用，不应在正式业务代码中调用。如果需要自定义测试执行流程，必须继承该类并覆盖其所有方法。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

```ts
import { TestRunner } from '@kit.TestKit';
```

## TestRunner

TestRunner是单元测试框架的模板，开发者可通过继承这个类并覆盖它的所有方法，实现自定义的单元测试框架能力。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onStop | [OnStopFn](js-apis-application-testrunner.md#onstopfn) | 否 | 是 | 当测试完成时，系统会在测试环境退出前触发该回调。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

**示例：**

```ts
import { TestRunner } from '@kit.TestKit';

// 实现自定义测试运行器
export default class UserTestRunner implements TestRunner {
  // 准备单元测试环境
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  // 运行测试用例
  onRun() {
    console.info('Trigger onRun');
  }

  // 测试完成时的回调处理
  onStop() {
    console.info('Trigger onStop');
  }
}
```

### onPrepare

onPrepare(): void

为运行测试用例准备单元测试环境。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ts
import { TestRunner } from '@kit.TestKit';

// 实现自定义测试运行器
export default class UserTestRunner implements TestRunner {
  // 准备单元测试环境
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
  }
}
```

### onRun

onRun(): void

当测试框架开始执行测试时，系统会触发该回调，用于运行测试用例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ts
import { TestRunner } from '@kit.TestKit';

// 实现自定义测试运行器
export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  // 运行测试用例
  onRun() {
    console.info('Trigger onRun');
  }
}
```

## OnStopFn

type OnStopFn = () => void

当测试完成时，系统会在测试环境退出前触发该回调。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
