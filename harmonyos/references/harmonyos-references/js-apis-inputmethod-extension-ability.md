---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability
title: @ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2700e9fb5c78526348541d81e88ab256cdad5d26198f56a0ec7b012fe17afc19
---

本模块支持开发者自行开发输入法应用，以及管理输入法Extension的生命周期。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InputMethodExtensionAbility } from '@kit.IMEKit';
```

## InputMethodExtensionAbility

PhonePC/2in1TabletTVWearable

输入法Extension ability类。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

### 属性

PhonePC/2in1TabletTVWearable

输入法Extension ability的上下文信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [InputMethodExtensionContext](js-apis-inputmethod-extension-context.md) | 否 | 否 | InputMethodExtension的上下文环境，继承于ExtensionContext。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

Extension生命周期回调，在拉起输入法Extension时调用，执行初始化输入法应用操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**示例：**

```
1. import { InputMethodExtensionAbility } from '@kit.IMEKit';
2. import { Want } from '@kit.AbilityKit';

4. class InputMethodExt extends InputMethodExtensionAbility {
5. onCreate(want: Want): void {
6. console.info('onCreate, want:' + want.abilityName);
7. }
8. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

Extension生命周期回调，在销毁输入法应用时回调，执行资源清理等操作。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```
1. import { InputMethodExtensionAbility } from '@kit.IMEKit';

3. class InputMethodExt extends InputMethodExtensionAbility {
4. onDestroy(): void {
5. console.info('onDestroy');
6. }
7. }
```
