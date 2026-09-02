---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs
title: AbilityDelegatorArgs
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 接口依赖的元素及定义 > AbilityDelegatorArgs
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:24364f884693ec1adca8399af506bd7215a4430c15d7b45bb58747367769ff6a
---

AbilityDelegatorArgs封装和提供测试用例参数的数据，通过AbilityDelegatorRegistry中[getArguments](js-apis-app-ability-abilitydelegatorregistry.md#abilitydelegatorregistrygetarguments)方法获取，包含bundleName、parameters、testCaseNames等关键测试信息，为测试脚本提供了标准化的参数访问方式。

该模块适用于编写单元测试脚本时需要获取测试参数进行条件判断或配置测试环境的场景。需要注意的是，其接口仅限测试框架中使用，不应在正式业务代码中调用。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## AbilityDelegatorArgs

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 当前被测试应用的包名。 |
| parameters | Record<string, string> | 否 | 否 | 当前启动单元测试的参数。 |
| testCaseNames | string | 否 | 否 | 测试用例名称。 |
| testRunnerClassName | string | 否 | 否 | 执行测试用例的测试执行器名称。 |

**示例：**

```ts
// 导入测试注册模块
import { abilityDelegatorRegistry } from '@kit.TestKit';

// 通过AbilityDelegatorRegistry获取AbilityDelegatorArgs对象
let args: abilityDelegatorRegistry.AbilityDelegatorArgs = abilityDelegatorRegistry.getArguments();
```
