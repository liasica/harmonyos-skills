---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screen-lock
title: "@ohos.screenLock (锁屏管理)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @ohos.screenLock (锁屏管理)
category: harmonyos-references
scraped_at: 2026-09-25T07:12:14+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:e7d5281bc64e3ff9e0feebb611eeec2b5ad49ed24bc0953a80f00e653c9e7b54
---

锁屏管理服务是HarmonyOS中的系统服务，为锁屏应用提供注册亮屏、灭屏、开启屏幕、结束休眠、退出动画、请求解锁结果监听，并提供回调结果给锁屏应用。锁屏管理服务向三方应用提供请求解锁、查询锁屏状态、查询是否设置锁屏密码的能力。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 在以下内容中，对于Lite Wearable设备类型，请参考“JS示例”；对于支持该模块的其他设备类型，请参考“ArkTS示例”。

## 导入模块

ArkTS示例：

```ts
import screenLock from '@ohos.screenLock';
```

JS示例：

```js
import screenLock from '@ohos.screenLock';
```

## screenLock.isScreenLocked(deprecated)

isScreenLocked(callback: AsyncCallback<boolean>): void

判断屏幕是否锁屏。使用callback异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。替代接口仅面向系统应用开放。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
});
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="text-content" on:click="isScreenLocked">点击调用 isScreenLocked</text>
    <text class="text-content">result: "{{ test_val }}"</text>
</div>
```

```css
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: aqua;
}
.text-content {
    color: black;
    font-size: 28fp;
    width: 100%;
    text-align: left;
    margin-top: 20px;
    padding-left: 50px;
    padding-right: 50px;
}
```

```js
// xxx.js
import screenLock from '@ohos.screenLock';

export default {
    data: {
        test_val: '未调用'
    },
    isScreenLocked() {
        this.test_val = '开始调用 isScreenLocked';
        try {
            screenLock.isScreenLocked((err, data) => {
                if (err) {
                    this.test_val = `isScreenLocked 报错: ${err.code}, message: ${err.message}`;
                    console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
                    return;
                }
                this.test_val = `isScreenLocked 成功: ${data}`;
                console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
            });
        } catch (err) {
            this.test_val = `isScreenLocked 调用异常: ${err.code} ${err.message}`;
        }
    }
}
```

## screenLock.isScreenLocked(deprecated)

isScreenLocked(): Promise<boolean>

判断屏幕是否锁屏。使用Promise异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示屏幕已锁屏；返回false表示屏幕未锁屏。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
});
```

**说明** 

Lite Wearable 不支持 Promise/async/await 等 ES6 语法，请使用上述 callback 形式的接口（[isScreenLocked(callback)](js-apis-screen-lock.md#screenlockisscreenlockeddeprecated)）。

## screenLock.isSecureMode(deprecated)

isSecureMode(callback: AsyncCallback<boolean>): void

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用callback异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode((err: BusinessError, data: Boolean)=>{
  if (err) {
    console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
});
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="text-content" on:click="isSecureMode">点击调用 isSecureMode</text>
    <text class="text-content">result: "{{ test_val }}"</text>
</div>
```

```css
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: aqua;
}
.text-content {
    color: black;
    font-size: 28fp;
    width: 100%;
    text-align: left;
    margin-top: 20px;
    padding-left: 50px;
    padding-right: 50px;
}
```

```js
// xxx.js
import screenLock from '@ohos.screenLock';

export default {
    data: {
        test_val: '未调用'
    },
    isSecureMode() {
        this.test_val = '开始调用 isSecureMode';
        try {
            screenLock.isSecureMode((err, data) => {
                if (err) {
                    this.test_val = `isSecureMode 报错: ${err.code}, message: ${err.message}`;
                    console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
                    return;
                }
                this.test_val = `isSecureMode 成功: ${data}`;
                console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
            });
        } catch (err) {
            this.test_val = `isSecureMode 调用异常: ${err.code} ${err.message}`;
        }
    }
}
```

## screenLock.isSecureMode(deprecated)

isSecureMode(): Promise<boolean>

判断当前设备的屏幕锁定是否安全（安全屏幕锁定意味着解锁屏幕需要密码、图案或其他用户身份识别）。使用Promise异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前设备的屏幕锁定安全；返回false表示当前设备的屏幕锁定不安全。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.isSecureMode().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the device is in secure mode. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the device is in secure mode, Code: ${err.code}, message: ${err.message}`);
});
```

**说明** 

Lite Wearable 不支持 Promise/async/await 等 ES6 语法，请使用上述 callback 形式的接口（[isSecureMode(callback)](js-apis-screen-lock.md#screenlockissecuremodedeprecated)）。

## screenLock.unlockScreen(deprecated)

unlockScreen(callback: AsyncCallback<void>): void

解锁屏幕。使用callback异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。解锁屏幕成功，err为undefined，否则为错误对象。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.unlockScreen((err: BusinessError) => {
  if (err) {
    console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded unlocking the screen.`);
});
```

JS示例：

```xml
<!-- xxx.hml -->
<div class="container">
    <text class="text-content" on:click="unlockScreen">点击调用 unlockScreen</text>
    <text class="text-content">result: "{{ test_val }}"</text>
</div>
```

```css
/* xxx.css */
.container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: aqua;
}
.text-content {
    color: black;
    font-size: 28fp;
    width: 100%;
    text-align: left;
    margin-top: 20px;
    padding-left: 50px;
    padding-right: 50px;
}
```

```js
// xxx.js
import screenLock from '@ohos.screenLock';

export default {
    data: {
        test_val: '未调用'
    },
    unlockScreen() {
        this.test_val = '开始调用 unlockScreen';
        try {
            screenLock.unlockScreen((err) => {
                if (err) {
                    this.test_val = `unlockScreen 报错: ${err.code}, message: ${err.message}`;
                    console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
                    return;
                }
                this.test_val = `unlockScreen 调用成功`;
                console.info(`Succeeded unlocking the screen.`);
            });
        } catch (err) {
            this.test_val = `unlockScreen 调用异常: ${err.code} ${err.message}`;
        }
    }
}
```

## screenLock.unlockScreen(deprecated)

unlockScreen(): Promise<void>

解锁屏幕。使用Promise异步回调。

**说明** 

从API version 7开始支持，除Lite Wearable外，从API version 9开始废弃。

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

ArkTS示例：

```ts
import { BusinessError } from '@ohos.base';

screenLock.unlockScreen().then(() => {
  console.info('Succeeded unlocking the screen.');
}).catch((err: BusinessError) => {
  console.error(`Failed to unlock the screen, Code: ${err.code}, message: ${err.message}`);
});
```

**说明** 

Lite Wearable 不支持 Promise/async/await 等 ES6 语法，请使用上述 callback 形式的接口（[unlockScreen(callback)](js-apis-screen-lock.md#screenlockunlockscreendeprecated)）。
