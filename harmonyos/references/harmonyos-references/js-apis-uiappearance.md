---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uiappearance
title: @ohos.uiAppearance (用户界面外观)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.uiAppearance (用户界面外观)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b8ffa903cc7c66f65c4886e66dfcc9a6de30cb038d0d68f59a7e4f3243406bd
---

用户界面外观提供获取系统外观的一些基础能力，包括获取深浅色模式、字体大小缩放比例、字体粗细缩放比例。

说明

从API version 20开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { uiAppearance } from '@kit.ArkUI';
```

## DarkMode

PhonePC/2in1TabletTVWearable

深色模式枚举。

**系统能力：** SystemCapability.ArkUI.UiAppearance

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALWAYS\_DARK | 0 | 系统始终为深色。 |
| ALWAYS\_LIGHT | 1 | 系统始终为浅色。 |

## uiAppearance.getDarkMode

PhonePC/2in1TabletTVWearable

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

```
1. import { uiAppearance } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let darkMode = uiAppearance.getDarkMode();
6. console.info('Get dark-mode ' + darkMode);
7. } catch (error) {
8. let message = (error as BusinessError).message;
9. console.error('Get dark-mode failed, ' + message);
10. }
```

## uiAppearance.getFontScale

PhonePC/2in1TabletTVWearable

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

```
1. import { uiAppearance } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let fontScale = uiAppearance.getFontScale();
6. console.info('Get fontScale ' + fontScale);
7. } catch (error) {
8. let message = (error as BusinessError).message;
9. console.error('Get fontScale failed, ' + message);
10. }
```

## uiAppearance.getFontWeightScale

PhonePC/2in1TabletTVWearable

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

```
1. import { uiAppearance } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let fontWeightScale = uiAppearance.getFontWeightScale();
6. console.info('Get fontScale ' + fontWeightScale);
7. } catch (error) {
8. let message = (error as BusinessError).message;
9. console.error('Get fontWeightScale failed, ' + message);
10. }
```
