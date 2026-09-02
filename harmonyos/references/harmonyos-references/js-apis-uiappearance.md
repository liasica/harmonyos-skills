---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uiappearance
title: "@ohos.uiAppearance (用户界面外观)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.uiAppearance (用户界面外观)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b6a6511f5b48ec5843574468048dd0b5dbb74d7779018e4ed19a7883a6908d36
---

用户界面外观提供获取系统外观的一些基础能力，包括获取深浅色模式、字体大小缩放比例、字体粗细缩放比例。

**说明** 

从API version 20开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

```ts
import { uiAppearance } from '@kit.ArkUI';
```

## DarkMode

深色模式枚举。

**系统能力：** SystemCapability.ArkUI.UiAppearance

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALWAYS\_DARK | 0 | 系统始终为深色。 |
| ALWAYS\_LIGHT | 1 | 系统始终为浅色。 |

## uiAppearance.getDarkMode

getDarkMode(): DarkMode

获取系统当前的深色模式配置。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DarkMode](js-apis-uiappearance.md#darkmode) | 系统当前的深色模式配置。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](errorcode-uiappearance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get dark-mode failed, ' + message);
}
```

## uiAppearance.getFontScale

getFontScale(): number

获取系统当前的字体大小缩放比例。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 系统当前的字体大小缩放比例。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](errorcode-uiappearance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontScale = uiAppearance.getFontScale();
  console.info('Get fontScale ' + fontScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontScale failed, ' + message);
}
```

## uiAppearance.getFontWeightScale

getFontWeightScale(): number

获取系统当前的字体粗细缩放比例。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 系统当前的字体粗细缩放比例。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](errorcode-uiappearance.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontWeightScale = uiAppearance.getFontWeightScale();
  console.info('Get fontWeightScale ' + fontWeightScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontWeightScale failed, ' + message);
}
```
