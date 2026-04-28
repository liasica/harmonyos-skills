---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-f
title: Functions
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.utils (ArkTS工具库) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dd78fa28828809298c3dfaad833f3d1cf617d5ba2984c91f2ed4c7a6c010b0a5
---

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ArkTSUtils } from '@kit.ArkTS'
```

## ArkTSUtils.isSendable

PhonePC/2in1TabletTVWearable

isSendable(value: Object | null | undefined): boolean

该方法用于判断value是否为Sendable数据类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | null | undefined | 是 | 待校验的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | value是否为Sendable数据类型，true表示value是Sendable数据类型，否则为false。 |

**示例：**

```
1. import { ArkTSUtils } from '@kit.ArkTS';

3. @Sendable
4. function sendableFunc() {
5. console.info("sendableFunc");
6. }

8. if (ArkTSUtils.isSendable(sendableFunc)) {
9. console.info("sendableFunc is Sendable");
10. } else {
11. console.info("sendableFunc is not Sendable");
12. }
13. // 期望输出: 'SendableFunc is Sendable'
```
