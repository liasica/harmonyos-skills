---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-settings-lite
title: "@ohos.settingsLite (设置信息)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.settingsLite (设置信息)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:33d2f8ee5c28a0f2b334183ea69a4f5293793841d73fe95856713c488ba5e1f9
---

本模块提供轻量级设置能力，支持跳转至设置页面。

**说明** 

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import settingsLite from '@ohos.settingsLite';
```

## settingsLite.openPinSettingPage

openPinSettingPage(): void

打开密码设置页面。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**示例：**

```js
import settingsLite from '@ohos.settingsLite';

settingsLite.openPinSettingPage();
```

## settingsLite.openNfcSettingsPage

openNfcSettingsPage(): void

打开NFC设置页面。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**示例：**

```js
import settingsLite from '@ohos.settingsLite';

settingsLite.openNfcSettingsPage();
```

## settingsLite.openDoubleClickSettingsPage

openDoubleClickSettingsPage(): void

打开按键设置-双击下按键页面。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**示例：**

```js
import settingsLite from '@ohos.settingsLite';

settingsLite.openDoubleClickSettingsPage();
```

## settingsLite.isDoubleClickAppForSelf

isDoubleClickAppForSelf(callback: ClickCallback): void

判断双击下按键的默认启动应用是否为本应用。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClickCallback](js-apis-settings-lite.md#clickcallback) | 是 | 返回检查结果。 |

**示例：**

```js
import settingsLite from '@ohos.settingsLite';

settingsLite.isDoubleClickAppForSelf({
    onResult(result) {
        console.info('isDoubleClickAppForSelf result: ' + result);
    }
});
```

## ClickCallback

按键设置-双击下按键页面检查回调。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

### onResult

onResult(result: boolean):void

双击结果回调。

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | 返回检查结果 |
