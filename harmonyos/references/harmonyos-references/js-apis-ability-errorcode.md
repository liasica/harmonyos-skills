---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-errorcode
title: "@ohos.ability.errorCode (ErrorCode)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.ability.errorCode (ErrorCode)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b9454bf30e6fc1d929adb6389d3e1f58d4151c812d66ba9ce367cb61cf5ac2ad
---

ErrorCode定义启动Ability时返回的错误码，包括无效的参数、权限拒绝等。

**说明** 

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { ErrorCode } from '@kit.AbilityKit';
```

## ErrorCode

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_ERROR | 0 | 启动成功，无错误。 |
| INVALID\_PARAMETER | -1 | 无效的参数。 |
| ABILITY\_NOT\_FOUND | -2 | 找不到Ability。 |
| PERMISSION\_DENY | -3 | 权限拒绝。 |
