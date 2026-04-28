---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-printextensionability
title: @ohos.app.ability.PrintExtensionAbility (打印扩展能力)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.app.ability.PrintExtensionAbility (打印扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f697d00c6a5c8d4739416f3db28623517e7ebf67c0b4861fc11ecac94a31cb8
---

该模块为打印扩展能力的操作API，提供调用打印扩展能力的接口。

说明

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1Tablet

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';
```

## PrintExtensionAbility

PhonePC/2in1Tablet

### onCreate

PhonePC/2in1Tablet

onCreate(want: Want): void

初始化扩展能力，会在系统首次连接打印扩展时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| want | [Want](js-apis-application-want.md#want) | 是 | 表示调用打印页面需要参数。 |

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class HWPrintExtension extends PrintExtensionAbility {
5. onCreate(want: Want): void {
6. console.info('onCreate');
7. // ...
8. }
9. }
```

### onStartDiscoverPrinter

PhonePC/2in1Tablet

onStartDiscoverPrinter(): void

开始发现与设备连接的打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';

3. export default class HWPrintExtension extends PrintExtensionAbility {
4. onStartDiscoverPrinter(): void {
5. console.info('onStartDiscoverPrinter enter');
6. // ...
7. }
8. }
```

### onStopDiscoverPrinter

PhonePC/2in1Tablet

onStopDiscoverPrinter(): void

停止发现打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';

3. export default class HWPrintExtension extends PrintExtensionAbility {
4. onStopDiscoverPrinter(): void {
5. console.info('onStopDiscoverPrinter enter');
6. // ...
7. }
8. }
```

### onConnectPrinter

PhonePC/2in1Tablet

onConnectPrinter(printerId: number): void

连接到特定打印机时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | number | 是 | 表示打印机ID。 |

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';

3. export default class HWPrintExtension extends PrintExtensionAbility {
4. onConnectPrinter(printerId: number): void {
5. console.info('onConnectPrinter enter');
6. // ...
7. }
8. }
```

### onDisconnectPrinter

PhonePC/2in1Tablet

onDisconnectPrinter(printerId: number): void

断开与特定打印机的连接时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| printerId | number | 是 | 表示打印机ID。 |

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';

3. export default class HWPrintExtension extends PrintExtensionAbility {
4. onDisconnectPrinter(printerId: number): void {
5. console.info('onDisconnectPrinter enter');
6. // ...
7. }
8. }
```

### onDestroy

PhonePC/2in1Tablet

onDestroy(): void

结束打印扩展时调用。

**系统能力：** SystemCapability.Print.PrintFramework

**示例：**

```
1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';

3. export default class HWPrintExtension extends PrintExtensionAbility {
4. onDestroy(): void {
5. console.info('onDestroy');
6. }
7. }
```
