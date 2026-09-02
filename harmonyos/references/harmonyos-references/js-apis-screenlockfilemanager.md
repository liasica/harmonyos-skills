---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenlockfilemanager
title: "@ohos.ability.screenLockFileManager (锁屏敏感数据管理)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.ability.screenLockFileManager (锁屏敏感数据管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:511fc402ca4552e07b849003f8422e1f23433c5b308d06d65a2a0cd8625262db
---

本模块提供锁屏下应用敏感数据保护的能力，支持申请和释放锁屏下应用敏感数据访问权限，以及查询敏感数据密钥的状态。当敏感数据密钥的引用计数归零，且屏幕被锁定达到系统配置的时长阈值后，密钥会被销毁，此时无法对该数据进行操作。这些密钥只有在屏幕解锁后才能恢复。通过调用本模块的[acquireAccess](js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口，可以防止密钥在屏幕被锁定达到系统配置的时长阈值后被销毁。

**说明** 

* 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 应用开启锁屏下敏感数据保护功能，需在[requestPermissions](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)中配置权限ohos.permission.PROTECT\_SCREEN\_LOCK\_DATA。

## 导入模块

```ts
import { screenLockFileManager } from '@kit.AbilityKit';
```

## DataType

表示锁屏下访问敏感数据类型的枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_DATA | 0x00000001 | 媒体数据类型。 |
| ALL\_DATA | 0xffffffff | 所有敏感数据类型。 |

## AccessStatus

表示锁屏下敏感数据访问权限申请状态的枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCESS\_DENIED | -1 | 申请锁屏下敏感数据访问权限被拒绝。 |
| ACCESS\_GRANTED | 0 | 申请锁屏下敏感数据访问权限被允许。 |

## ReleaseStatus

表示锁屏下敏感数据访问权限释放状态的枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RELEASE\_DENIED | -1 | 释放锁屏下敏感数据访问权限被拒绝。 |
| RELEASE\_GRANTED | 0 | 释放锁屏下敏感数据访问权限被允许。 |

## KeyStatus18+

表示锁屏下敏感数据密钥状态的枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEY\_NOT\_EXIST | -2 | 密钥不存在。此状态表示应用未开启锁屏下敏感数据保护功能，或当前设备上该保护功能不可用。 |
| KEY\_RELEASED | -1 | 密钥已释放。此状态表示锁屏下敏感数据无法被操作。 |
| KEY\_EXIST | 0 | 密钥存在。此状态表示锁屏下敏感数据可以被正常操作。 |

## screenLockFileManager.acquireAccess

acquireAccess(): AccessStatus

以同步方法申请调用方应用锁屏下敏感数据访问权限。申请成功后，敏感数据密钥的引用计数增加，防止密钥在屏幕被锁定达到系统配置的时长阈值后被销毁。该方法需与[releaseAccess](js-apis-screenlockfilemanager.md#screenlockfilemanagerreleaseaccess)配对使用。

调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并通过[queryAppKeyState](js-apis-screenlockfilemanager.md#screenlockfilemanagerqueryappkeystate18)接口查询密钥状态为KEY\_EXIST。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AccessStatus](js-apis-screenlockfilemanager.md#accessstatus) | 锁屏下敏感数据访问权限的申请状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[锁屏敏感数据管理错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability works abnormally. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300004 | File access is denied. |

**示例：**

```ts
// 申请锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // 申请访问权限
    let acquireStatus = screenLockFileManager.acquireAccess();
    if (acquireStatus === screenLockFileManager.AccessStatus.ACCESS_GRANTED) {
        hilog.info(0x0000, 'testTag', 'acquireAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'acquireAccess failed: %{public}s', message);
}
```

## screenLockFileManager.releaseAccess

releaseAccess(): ReleaseStatus

以同步方法释放调用方应用锁屏下敏感数据访问权限。释放成功后，敏感数据密钥的引用计数减少，当计数归零时，密钥可以在屏幕被锁定达到系统配置的时长阈值后被销毁。

调用此接口前，请确保应用已开启锁屏下敏感数据保护功能，并且先调用[acquireAccess](js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口成功申请权限后才能使用。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReleaseStatus](js-apis-screenlockfilemanager.md#releasestatus) | 锁屏下敏感数据访问权限的释放状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[锁屏敏感数据管理错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability works abnormally. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300005 | File access was not acquired. |

**示例：**

```ts
// 释放锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // 释放访问权限
    let releaseStatus = screenLockFileManager.releaseAccess();
    if (releaseStatus === screenLockFileManager.ReleaseStatus.RELEASE_GRANTED) {
        hilog.info(0x0000, 'testTag', 'releaseAccess successfully.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'releaseAccess failed: %{public}s', message);
}
```

## screenLockFileManager.queryAppKeyState18+

queryAppKeyState(): KeyStatus

以同步方法查询调用方应用锁屏下敏感数据密钥的状态。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyStatus](js-apis-screenlockfilemanager.md#keystatus18) | 锁屏下敏感数据密钥的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[锁屏敏感数据管理错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability works abnormally. |

**示例：**

```ts
// 查询锁屏下应用敏感数据访问权限
import { screenLockFileManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    // 查询密钥状态
    let keyStatus = screenLockFileManager.queryAppKeyState();
    // 判断密钥状态并处理不同情况
    if (keyStatus === screenLockFileManager.KeyStatus.KEY_NOT_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key does not exist.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_RELEASED) {
        hilog.info(0x0000, 'testTag', 'Key has been released.');
    } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_EXIST) {
        hilog.info(0x0000, 'testTag', 'Key exists.');
    }
} catch (err) {
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'queryAppKeyState failed: %{public}s', message);
}
```
