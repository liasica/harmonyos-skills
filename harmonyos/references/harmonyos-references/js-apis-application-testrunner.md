---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-testrunner
title: @ohos.application.testRunner (TestRunner)
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > @ohos.application.testRunner (TestRunner)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28165d121bd52a1f604cf4091fd03d42abe68b669ca38f2c07e74cea6ca29bee
---

TestRunner模块提供了框架测试的能力。包括准备单元测试环境、运行测试用例。

如果您想实现自己的单元测试框架，您必须继承这个类并覆盖它的所有方法。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TestRunner } from '@kit.TestKit';
```

## TestRunner.onPrepare

PhonePC/2in1TabletTVWearable

onPrepare(): void

为运行测试用例准备单元测试环境。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```
1. import { TestRunner } from '@kit.TestKit';

3. export default class UserTestRunner implements TestRunner {
4. onPrepare() {
5. console.info('Trigger onPrepare');
6. }

8. onRun() {
9. }
10. }
```

## TestRunner.onRun

PhonePC/2in1TabletTVWearable

onRun(): void

运行测试用例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```
1. import { TestRunner } from '@kit.TestKit';

3. export default class UserTestRunner implements TestRunner {
4. onPrepare() {
5. }

7. onRun() {
8. console.info('Trigger onRun');
9. }
10. }
```
