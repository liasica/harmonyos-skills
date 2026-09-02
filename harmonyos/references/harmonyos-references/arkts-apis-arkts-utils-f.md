---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-f
title: Functions
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.utils (ArkTS工具库) > Functions
category: harmonyos-references
scraped_at: 2026-09-02T15:00:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eff48e94b9d9c3f24b59624a4157eeb9fbeee4249c2f60f8d802b923499721a1
---

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

```ts
import { ArkTSUtils } from '@kit.ArkTS';
```

## ArkTSUtils.isSendable

isSendable(value: Object | null | undefined): boolean

该方法用于判断value是否为Sendable数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | null | undefined | 是 | 待判断是否为Sendable数据类型的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | value是否为Sendable数据类型，true表示value是Sendable数据类型，否则为false。 |

**示例：**

```ts
import { ArkTSUtils } from '@kit.ArkTS';

@Sendable
function sendableFunc() {
  console.info("sendableFunc");
}

if (ArkTSUtils.isSendable(sendableFunc)) {
  console.info("sendableFunc is Sendable");
} else {
  console.info("sendableFunc is not Sendable");
}
// 期望输出: 'sendableFunc is Sendable'
```
