---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screen-lock
title: @ohos.screenLock (锁屏管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @ohos.screenLock (锁屏管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd4aa0653904ee2214eccf67a373dec6bfede3dc7356c29255f98661ba52ffb1
---

锁屏管理服务是HarmonyOS中的系统服务，为锁屏应用提供注册亮屏、灭屏、开启屏幕、结束休眠、退出动画、请求解锁结果监听，并提供回调结果给锁屏应用。锁屏管理服务向三方应用提供请求解锁、查询锁屏状态、查询是否设置锁屏密码的能力。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import screenLock from '@ohos.screenLock';
```

## screenLock.isScreenLocked(deprecated)

PhonePC/2in1TabletTVWearable

isScreenLocked(callback: AsyncCallback<boolean>): void

判断屏幕是否锁屏。使用callback异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。替代接口仅面向系统应用开放。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.isScreenLocked((err: BusinessError, data: Boolean)=>{
4. if (err) {
5. console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
9. });
```

## screenLock.isScreenLocked(deprecated)

PhonePC/2in1TabletTVWearable

isScreenLocked(): Promise<boolean>

判断屏幕是否锁屏。使用Promise异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.isScreenLocked().then((data: Boolean) => {
4. console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
7. });
```

## screenLock.isSecureMode(deprecated)

PhonePC/2in1TabletTVWearable

isSecureMode(callback: AsyncCallback<boolean>): void

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用callback异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.isSecureMode((err: BusinessError, data: Boolean)=>{
4. if (err) {
5. console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
9. });
```

## screenLock.isSecureMode(deprecated)

PhonePC/2in1TabletTVWearable

isSecureMode(): Promise<boolean>

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用Promise异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.isSecureMode().then((data: Boolean) => {
4. console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
7. });
```

## screenLock.unlockScreen(deprecated)

PhonePC/2in1TabletTVWearable

unlockScreen(callback: AsyncCallback<void>): void

解锁屏幕。使用callback异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。解锁屏幕成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.unlockScreen((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info(`Succeeded unlocking the screen.`);
9. });
```

## screenLock.unlockScreen(deprecated)

PhonePC/2in1TabletTVWearable

unlockScreen(): Promise<void>

解锁屏幕。使用Promise异步回调。

说明

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@ohos.base';

3. screenLock.unlockScreen().then(() => {
4. console.info('Succeeded unlocking the screen.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
7. });
```
