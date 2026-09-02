---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-shellcmdresult
title: ShellCmdResult
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > 接口依赖的元素及定义 > ShellCmdResult
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:adfc0209b95ac8afeadf65a02a5f56f7d8d5bd9998ff8c4b7d7258dd2a58051d
---

ShellCmdResult是测试框架中用于封装Shell命令执行结果的数据对象，它包含stdResult（标准输出内容）和exitCode（退出码）两个关键属性，为测试脚本提供了结构化的命令执行结果访问方式。

该模块适用于需要验证Shell命令执行结果或处理命令返回数据的测试场景，通过abilityDelegator的[executeShellCommand](js-apis-inner-application-abilitydelegator.md#executeshellcommand)方法获取。需要注意的是，其接口仅限测试框架中使用，不应在正式业务代码中调用。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](../harmonyos-guides/unittest-guidelines.md)中使用。

## 导入模块

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## 使用说明

调用abilityDelegator中的[executeShellCommand](js-apis-inner-application-abilitydelegator.md#executeshellcommand)方法获取ShellCmdResult实例。调用成功后，返回ShellCmdResult对象，包含Shell命令的标准输出内容（stdResult）和退出码（exitCode）。

**示例：**

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';

// 获取AbilityDelegator实例
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 执行Shell命令，通过回调获取执行结果
abilityDelegator.executeShellCommand(cmd, (error: BusinessError, data) => {
  if (error) {
    console.error(`executeShellCommand fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`executeShellCommand success, data: ${JSON.stringify(data)}`);
  }
});
```

## ShellCmdResult

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stdResult | string | 否 | 否 | Shell命令的标准输出内容。 |
| exitCode | number | 否 | 否 | Shell命令的退出码。返回值为0表示命令执行成功，非0表示命令执行失败。 |
