---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-aaid-api
title: AAID（应用匿名标识符）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > AAID（应用匿名标识符）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:55c29e9b06053cdc431f9224e85840ac6cf2ac518f29ff43121452d1a1a649de
---

AAID（Anonymous Application Identifier）是应用匿名标识符，标识运行在移动智能终端设备上的应用实例，只有该应用实例才能访问该标识符，它只存在于应用的安装期，总长度36个字符。与无法重置的设备级硬件ID相比，AAID具有更好的隐私属性。

AAID具有以下特性：

* AAID和已有的任何标识符都不关联，并且每个应用只能访问应用本身的AAID。
* 同一个设备上，同一个开发者的多个应用，AAID取值不同。
* 同一个设备上，不同开发者的应用，AAID取值不同。
* 不同设备上，同一个开发者的应用，AAID取值不同。
* 不同设备上，不同开发者的应用，AAID取值不同。

AAID会在包括但不限于下述场景中发生变化：

* 应用卸载重装。
* 应用调用[deleteAAID](push-aaid-api.md#aaiddeleteaaid)接口。
* 用户恢复出厂设置。
* 用户清除应用数据。

开发者可基于AAID构建用户画像，并与[Push Token](push-pushservice.md)建立绑定关系，从而实现精准消息推送。本模块为开发者提供AAID的获取与删除能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { AAID } from '@kit.PushKit';
```

## AAID.getAAID

getAAID(callback: AsyncCallback<string>): void

获取AAID，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取AAID成功，err为undefined，aaid为获取到的AAID，字符长度为36；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```typescript
import { AAID } from '@kit.PushKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  private retryCount = 0;

  private readonly MAX_RETRY_COUNT = 3;

  private readonly RETRY_INTERVAL = 1000; // 重试间隔1s

  private readonly RETRY_ERROR_CODES = [
    1000900001,
    1000900006,
    1000900007
  ];

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    super.onCreate(want, launchParam);

    this.getAAID();
  }
  
  /**
   * 获取AAID
   */
  private getAAID(): void {
    try {
      AAID.getAAID((err: BusinessError, aaid: string) => {
        if (err) {
          hilog.error(LOG_DOMAIN, LOG_TAG, 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
          // 重试逻辑
          this.handleRetry(err.code);
        } else {
          hilog.info(LOG_DOMAIN, LOG_TAG, 'Succeeded in getting AAID: %{public}s', aaid);
        }
      });
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'Get AAID occur err: %{public}d %{public}s', e.code, e.message);
    }
  }

  /**
   * 重试逻辑
   * 开发者可根据业务控制重试次数与间隔
   * @param errorCode 错误码
   */
  private handleRetry(errorCode: number): void {
    if (this.retryCount < this.MAX_RETRY_COUNT && this.RETRY_ERROR_CODES.includes(errorCode)) {
      this.retryCount++;
      hilog.warn(LOG_DOMAIN, LOG_TAG, 'getAAID retry count %{public}d', this.retryCount);

      // 延迟重试，避免频繁调用
      setTimeout(() => {
        this.getAAID();
      }, this.RETRY_INTERVAL);
    }
  }
}
```

## AAID.getAAID

getAAID(): Promise<string>

获取AAID，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回AAID，字符长度为36。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```typescript
import { AAID } from '@kit.PushKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  private retryCount = 0;

  private readonly MAX_RETRY_COUNT = 3;

  private readonly RETRY_INTERVAL = 1000; // 重试间隔1s

  private readonly RETRY_ERROR_CODES = [
    1000900001,
    1000900006,
    1000900007
  ];

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    super.onCreate(want, launchParam);

    this.getAAID();
  }

  /**
   * 获取AAID
   */
  private getAAID(): void {
    AAID.getAAID().then((aaid: string) => {
      hilog.info(LOG_DOMAIN, LOG_TAG, 'Succeeded in getting AAID: %{public}s', aaid);
    }).catch((err: BusinessError) => {
      hilog.error(LOG_DOMAIN, LOG_TAG, 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
      // 重试逻辑
      this.handleRetry(err.code);
    });
  }

  /**
   * 重试逻辑
   * 开发者可根据业务控制重试次数与间隔
   * @param errorCode 错误码
   */
  private handleRetry(errorCode: number): void {
    if (this.retryCount < this.MAX_RETRY_COUNT && this.RETRY_ERROR_CODES.includes(errorCode)) {
      this.retryCount++;
      hilog.warn(LOG_DOMAIN, LOG_TAG, 'getAAID retry count %{public}d', this.retryCount);

      // 延迟重试，避免频繁调用
      setTimeout(() => {
        this.getAAID();
      }, this.RETRY_INTERVAL);
    }
  }
}
```

## AAID.deleteAAID

deleteAAID(callback: AsyncCallback<void>): void

删除AAID，使用callback异步回调。不建议调用该接口，调用后重新调用[getToken](push-pushservice.md#pushservicegettoken)()所获取的Push Token将发生变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除AAID成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```typescript
import { AAID } from '@kit.PushKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  /**
   * 删除AAID
   * 开发者可根据自身业务需要自行调用deleteAAID，非必要不调用该接口
   */
  private deleteAAID(): void {
    try {
      AAID.deleteAAID((err: BusinessError) => {
        if (err) {
          hilog.error(LOG_DOMAIN, LOG_TAG, 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
        } else {
          hilog.info(LOG_DOMAIN, LOG_TAG, 'Succeeded in deleting AAID.');
        }
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'Delete AAID occur err: %{public}d %{public}s', e.code, e.message);
    }
  }
}
```

## AAID.deleteAAID

deleteAAID(): Promise<void>

删除AAID，使用Promise异步回调。不建议调用该接口，调用后重新调用[getToken](push-pushservice.md#pushservicegettoken)()所获取的Push Token将发生变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```typescript
import { AAID } from '@kit.PushKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  /**
   * 删除AAID
   * 开发者可根据自身业务需要自行调用deleteAAID，非必要不调用该接口
   */
  private deleteAAID(): void {
    try {
      AAID.deleteAAID().then(() => {
        hilog.info(LOG_DOMAIN, LOG_TAG, 'Succeeded in deleting AAID.');
      }).catch((err: BusinessError) => {
        hilog.error(LOG_DOMAIN, LOG_TAG, 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'Delete AAID occur err: %{public}d %{public}s', e.code, e.message);
    }
  }
}
```
