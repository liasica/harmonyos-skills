---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenlockfilemanager
title: @ohos.ability.screenLockFileManager (锁屏敏感数据管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.ability.screenLockFileManager (锁屏敏感数据管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:baa82c15903b3ec75acb0617de3525270dc7d2c0063e8a6e7bbb889d666fbeed
---

敏感数据密钥在锁屏后会触发销毁，销毁后敏感数据无法读写，需解锁屏幕触发恢复敏感数据密钥后方可访问。本模块提供应用锁屏下敏感数据保护的能力，支持申请和释放锁屏下敏感数据访问权限等。

说明

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { screenLockFileManager } from '@kit.AbilityKit';
```

## DataType

PhonePC/2in1Tablet

枚举，指定锁屏下访问的敏感数据类型。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_DATA | 0x00000001 | 媒体类型数据。 |
| ALL\_DATA | 0xffffffff | 所有敏感加密数据。 |

## AccessStatus

PhonePC/2in1Tablet

表示锁屏下敏感数据访问权限申请的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCESS\_DENIED | -1 | 拒绝授予锁屏下敏感数据访问。 |
| ACCESS\_GRANTED | 0 | 授予锁屏下敏感数据访问。 |

## ReleaseStatus

PhonePC/2in1Tablet

表示锁屏下敏感数据访问权限释放的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RELEASE\_DENIED | -1 | 拒绝锁屏下敏感数据访问释放。 |
| RELEASE\_GRANTED | 0 | 释放锁屏下敏感数据访问。 |

## KeyStatus18+

PhonePC/2in1Tablet

表示锁屏下敏感数据访问权限的状态枚举。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEY\_NOT\_EXIST | -2 | 应用未开启锁屏敏感数据保护功能。 |
| KEY\_RELEASED | -1 | 锁屏敏感数据访问权限已释放。 |
| KEY\_EXIST | 0 | 应用可以访问锁屏敏感数据。 |

## screenLockFileManager.acquireAccess

PhonePC/2in1Tablet

acquireAccess(): AccessStatus

以同步方法申请锁屏下应用敏感数据访问权限。锁屏后，敏感数据无法被访问，但可通过调用该方法，访问本应用的敏感数据。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AccessStatus](js-apis-screenlockfilemanager.md#accessstatus) | 锁屏下敏感数据访问权限申请的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ohos.screenLockFileManager错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability work abnormally. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300004 | File access is denied. |

**示例：**

```
1. // 申请锁屏下应用敏感数据访问权限
2. import { screenLockFileManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. try {
7. let acquireStatus = screenLockFileManager.acquireAccess();
8. if (acquireStatus === screenLockFileManager.AccessStatus.ACCESS_GRANTED) {
9. hilog.info(0x0000, 'testTag', 'acquireAccess successfully.');
10. }
11. } catch (err) {
12. let message = (err as BusinessError).message;
13. hilog.error(0x0000, 'testTag', 'acquireAccess failed: %{public}s', message);
14. }
```

## screenLockFileManager.releaseAccess

PhonePC/2in1Tablet

releaseAccess(): ReleaseStatus

以同步方法取消锁屏下本应用敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReleaseStatus](js-apis-screenlockfilemanager.md#releasestatus) | 锁屏下敏感数据访问权限释放的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ohos.screenLockFileManager错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability work abnormally. |
| 29300003 | The application is not enabled the data protection under lock screen. |
| 29300005 | File access was not acquired. |

**示例：**

```
1. // 释放锁屏下应用敏感数据访问权限
2. import { screenLockFileManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. try {
7. let releaseStatus = screenLockFileManager.releaseAccess();
8. if (releaseStatus === screenLockFileManager.ReleaseStatus.RELEASE_GRANTED) {
9. hilog.info(0x0000, 'testTag', 'releaseAccess successfully.');
10. }
11. } catch (err) {
12. let message = (err as BusinessError).message;
13. hilog.error(0x0000, 'testTag', 'releaseAccess failed: %{public}s', message);
14. }
```

## screenLockFileManager.queryAppKeyState18+

PhonePC/2in1Tablet

queryAppKeyState(): KeyStatus

以同步方法查询锁屏下本应用敏感数据访问权限。

**系统能力：** SystemCapability.Security.ScreenLockFileManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyStatus](js-apis-screenlockfilemanager.md#keystatus18) | 锁屏下敏感数据访问权限的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ohos.screenLockFileManager错误码](errorcode-screenlockfilemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 29300002 | The system ability work abnormally. |

**示例：**

```
1. // 查询锁屏下应用敏感数据访问权限
2. import { screenLockFileManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. try {
7. let keyStatus = screenLockFileManager.queryAppKeyState();
8. if (keyStatus === screenLockFileManager.KeyStatus.KEY_NOT_EXIST) {
9. hilog.info(0x0000, 'testTag', 'Key does not exist.');
10. } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_RELEASED) {
11. hilog.info(0x0000, 'testTag', 'Key has been released.');
12. } else if (keyStatus === screenLockFileManager.KeyStatus.KEY_EXIST) {
13. hilog.info(0x0000, 'testTag', 'Key exists.');
14. }
15. } catch (err) {
16. let message = (err as BusinessError).message;
17. hilog.error(0x0000, 'testTag', 'queryAppKeyState failed: %{public}s', message);
18. }
```
