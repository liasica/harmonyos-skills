---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-walletpass
title: walletPass（Pass卡片能力）
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > ArkTS API > walletPass（Pass卡片能力）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0ba05fcf3bded709f084c4d3a9fff18cbc2bdf1146544dbbf109e6b3814d601
---

本模块提供接入钱包服务的能力。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { walletPass } from '@kit.WalletKit';
```

## WalletPassClient

钱包卡券的功能入口类，与钱包卡券有关的所有方法从此处接入。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

### constructor

constructor(context: common.UIAbilityContext)

构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);

  build() {
  }
}
```

### queryPassDeviceInfo

queryPassDeviceInfo(passStr: string): Promise<string>

查询当前设备唯一标识及设备能力，用于关联已开通的云侧卡券，同时开卡过程可指定目标设备标识，提升安全性。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、targetDeviceType。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - targetDeviceType：目标设备类型。取值如下  - phone：手机  - wear：穿戴  - all：手机+穿戴 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回设备标识及设备能力。JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。  key包括deviceType、passDeviceId、deviceModel、passCapabilityVersion、deviceModelNumber、deviceCapabilities。  - deviceType：设备类型。取值如下  - phone：手机  - wear：穿戴  - passDeviceId：账号/设备联合标识符。  - deviceModel：设备名，用于展示可开通的设备名称。  - passCapabilityVersion：WalletKit开放能力版本号，用于版本兼容处理，初始为 1。  - deviceModelNumber：设备型号编码，用于获取匹配的标定数据。  - deviceCapabilities：能力集，同步返回是否支持NFC/BLE/UWB/SLE  - NFC：0200  - NFC+BLE：0201  - UWB：0202  - SLE：0203 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 设备类型
  private targetDeviceType: string = '';

  queryPassDeviceInfo() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in querying passDeviceInfo, result:${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### canAddPass

canAddPass(passStr: string): Promise<string>

检查当前设备是否支持添加卡券，返回结果码。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、targetDeviceType。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - targetDeviceType：目标设备类型。取值如下  - phone: 手机  - wear：穿戴  - all：手机+穿戴 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回是否支持添卡的结果。JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。  key包括passType、deviceType、passDeviceId、deviceModel、result。  - passType：服务号  - deviceType：设备类型。取值如下  - phone：手机  - wear：穿戴  - passDeviceId：账号/设备联合标识符。  - deviceModel：设备名，用于展示可开通的设备名称。  - result：结果码。取值如下  0：支持添加  1：ROM版本过低  2：钱包版本过低  3：ROM版本和钱包版本均过低 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200004 | The device does not support this card. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200010 | Network connection error. |
| 1010220002 | The card already exists in the specified device. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200015 | This card is not available for a child account. |
| 1010200016 | This card is not available for the current country or region. |
| 1010220005 | The number of cards has reached the upper limit. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 设备类型
  private targetDeviceType: string = '';

  canAddPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.canAddPass(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in checking addPass, result:${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to check addPass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### initWalletEnvironment

initWalletEnvironment(passStr: string): Promise<void>

初始化钱包开通卡券的同意协议或是登录账号，引导用户跳转钱包完成应用初始化。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括targetDeviceType。  - targetDeviceType：目标设备类型。取值如下  - phone: 手机  - wear：穿戴  - all：手机+穿戴 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200011 | Failed to initialize the environment. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200017 | The Wallet app was closed by the user. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 设备类型
  private targetDeviceType: string = '';

  initWalletEnvironment() {
    let passStr = JSON.stringify({
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.initWalletEnvironment(passStr).then(() => {
      // 接口调用成功
      console.info(`Succeeded in initiating walletEnvironment`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### addPass

addPass(passStr: string): Promise<string>

用户主动发起开卡时，跳转钱包应用，携带开卡JWE数据，开通卡券到钱包并激活。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括jweContent。  - jweContent：开发者服务端生成的开卡签名数据包。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回卡片数据。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括passType、serialNumber、deviceType、passDeviceId。  - passType： 开通的卡片服务号 。  - serialNumber： 开通的 Pass 卡片唯一标识 。  - deviceType：开卡设备的类型。取值如下  - phone: 手机  - wear：穿戴  - all：手机+穿戴  - passDeviceId： 开卡设备的帐号/设备联合标识符。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200002 | Wallet app not found. |
| 1010200004 | The device does not support this card. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200012 | Duplicate request. |
| 1010220002 | The card already exists in the specified device. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220401 | Failed to add the card because the signature verification failed. |
| 1010220402 | Failed to add the card because the data decryption failed. |
| 1010220403 | Failed to add the card because the instance ID does not exist. |
| 1010220404 | Failed to add the card because the instance ID has been used. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200015 | This card is not available for a child account. |
| 1010200016 | This card is not available for the current country or region. |
| 1010200017 | The Wallet app was closed by the user. |
| 1010220005 | The number of cards has reached the upper limit. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // jwe数据，需要从云侧获取
  private jweContent: string = '';

  addPass() {
    let passStr = JSON.stringify({
      jweContent: this.jweContent
    });
    this.walletPassClient.addPass(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in adding pass, result:${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to add pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### queryPass

queryPass(passStr: string): Promise<string>

检查当前设备卡券的开通情况。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回卡片数据。JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。  key包括passType、serialNumber、deviceType、passDeviceId、deviceModel、cardStatus。  - passType：服务号  - serialNumber：卡券唯一标识  - deviceType：设备类型。取值如下  - phone：手机  - wear：穿戴  - passDeviceId：账号/设备联合标识符。  - deviceModel：设备名，用于展示可开通的设备名称。  - cardStatus：卡片状态 。取值如下  0：可用  1：不可用 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220501 | No card that meets the search criteria is found. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  queryPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.queryPass(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in querying pass, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to query pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### viewPass

viewPass(passStr: string): Promise<void>

跳转钱包查看已开通的卡券详情页。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1010200002 | Wallet app not found. |
| 1010200013 | Operation failed because of an internal error. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  async viewPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    try {
      await this.walletPassClient.viewPass(passStr);
      // 接口调用成功
      console.info(`Succeeded in viewing pass`);
    } catch (err) {
      // 接口调用失败
      console.error(`Failed to view pass, code:${err.code}, message:${err.message}`);
    }
  }

  build() {
  }
}
```

### updatePass

updatePass(passStr: string): Promise<string>

卡券更新（预留接口，暂不提供具体功能）。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回卡片更新结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括result。  - result：卡券更新结果0，全部更新完成后返回操作成功。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220701 | Failed to update the card because no update is detected. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  updatePass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.updatePass(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in updating pass,result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to update pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### deletePass

deletePass(passStr: string): Promise<string>

卡券删除（预留接口，暂不提供具体功能）。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回卡片删除结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括result。  - result：卡券删除结果0，全部删除完成后返回操作成功。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200012 | Duplicate request. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220004 | The card does not exist in the specified device. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |
| 1010220801 | Failed to delete the card because the signature verification failed. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  deletePass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.deletePass(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in deleting pass, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to delete pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### queryICCEConnectionState

queryICCEConnectionState(rkeStr: string): Promise<string>

查询车控连接状态。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回连接状态。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括deviceType、passDeviceId、deviceModel、connectionState、authState。  - deviceType：设备类型。取值如下  - phone：手机  - wear：穿戴  - passDeviceId：账号/设备联合标识符。  - deviceModel：设备名，用于展示可开通的设备名称。  - connectionState：连接状态。取值如下  0：异常状态  1：正在连接  2：连接成功  3：未连接  4：连接超时  10：未配对  11：配对中  12：已配对  - authState：认证状态。取值如下  0：未认证/认证失败  1：认证成功 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted.  适用版本：5.0.1(13)+ |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  queryICCEConnectionState() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.queryICCEConnectionState(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in querying ICCEConnectionState, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to query ICCEConnectionState, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### startICCEConnection

startICCEConnection(rkeStr: string): Promise<string>

车控连接。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回连接结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括result、deviceType、passDeviceId、deviceModel、connectionState、authState、reasonCode。  result：认证状态。取值如下  0：已配对已连接  1：已配对未连接  2：未配对  deviceType：设备类型。取值如下  phone：手机  wear：穿戴  passDeviceId：账号/设备联合标识符。  deviceModel：设备名，用于展示可开通的设备名称。  connectionState：连接状态。取值如下  0：异常状态  1：正在连接  2：连接成功  3：未连接  4：连接超时  10：未配对  11：配对中  12：已配对  authState：认证状态。取值如下  0：未认证/认证失败  1：认证成功  reasonCode：异常原因码，只有result为2时才会返回。取值如下  1：表侧星闪开关未开启 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user.  适用版本：5.0.1(13)+ |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200012 | Duplicate request. |
| 1010221001 | Connection failed because the pairing code is not obtained. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted.  适用版本：5.0.1(13)+ |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 卡券唯一标识
  private serialNumber: string = '';

  startICCEConnection() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.startICCEConnection(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in starting ICCEConnection, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to start ICCEConnection, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### registerICCEListener

registerICCEListener(rkeStr: string, eventNotifyListener: rpc.RemoteObject): Promise<string>

注册监听。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、registerName。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - registerName：注册监听的应用名称，一般为包名。 |
| eventNotifyListener | [rpc.RemoteObject](js-apis-rpc.md#remoteobject) | 是 | 回调事件，[rpc.RemoteObject](js-apis-rpc.md#remoteobject)格式。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回注册结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括result。  result：注册成功结果0。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010221101 | Registration failed because of duplicate register name. |
| 1010200012 | Duplicate request. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

// 注册的回调对象
class ICCECallBack extends rpc.RemoteObject {
  constructor() {
    super('ICCECallBack');
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence): Promise<boolean> {
    // 接收到钱包发送的数据，此时可以进行数据通信
    console.info(`OnRemoteMessageRequest successed, code: ${code} data: ${data.readString()}`);
    reply.writeString('Test');
    return true;
  }
}

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 注册的回调对象
  private callback: rpc.RemoteObject | null = null;
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 注册名，推荐使用包名
  private registerName: string = '';

  registerICCEListener() {
    let passStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
    });
    this.callback = new ICCECallBack();
    this.walletPassClient.registerICCEListener(passStr, this.callback).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in registering ICCEListener, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to register ICCEListener, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### unregisterICCEListener

unregisterICCEListener(rkeStr: string): Promise<string>

解注册监听。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、registerName。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - registerName：注册监听的应用名称，一般为包名。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回解注册结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括result。  result：解注册成功结果0。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010221201 | The registration may have been unregistered before. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 注册的回调对象
  private callback: rpc.RemoteObject | null = null;
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 注册名，推荐使用包名
  private registerName: string = '';

  unregisterICCEListener() {
    let passStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
    });

    this.walletPassClient.unregisterICCEListener(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in unregistering ICCEListener, result: ${result}`);
      this.callback = null;
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to unregister ICCEListener, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```

### sendICCERKEMessage

sendICCERKEMessage(rkeStr: string): Promise<string>

发送车控指令。

使用Promise异步回调。

不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。  key包括passType、serialNumber、rkeCommand、encryptFlag、directionFlag。  - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。  - serialNumber：开发者服务器申请卡券时定义的唯一标识。  - rkeCommand：请求指令。  - encryptFlag：加密指示位。取值如下  0：不加密  1：需要基于通道会话秘钥加密  - directionFlag：方向指示位。取值如下  0：上报结果  1：发送指令 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回车控结果。JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。  key包括deviceType、passDeviceId、deviceModel、result。  - deviceType：设备类型。取值如下  - phone：手机  - wear：穿戴  - passDeviceId：账号/设备联合标识符。  - deviceModel：设备名，用于展示可开通的设备名称。  - result：车控发起结果，发送至车辆后立即返回。取值如下  - 0：发送成功 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-wallet.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200012 | Duplicate request. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted.  适用版本：5.0.1(13)+ |
| 1010221301 | Failed to send the RKE message because of a connection failure. |
| 1010221302 | Failed to send the RKE message because of an authentication failure. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 初始化，需要传入应用的UIAbilityContext
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 卡券唯一标识
  private serialNumber: string = '';
  // 创建WalletKit服务申请的服务号
  private passType: string = '';
  // 车控指令
  private rkeCommand: string = '';

  sendICCERKEMessage() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber,
      rkeCommand: this.rkeCommand,
      encryptFlag: '0',
      directionFlag: '1'
    });
    this.walletPassClient.sendICCERKEMessage(passStr).then((result: string) => {
      // 接口调用成功
      console.info(`Succeeded in sending ICCERKEMessage, result: ${result}`);
    }).catch((err: BusinessError) => {
      // 接口调用失败
      console.error(`Failed to send ICCERKEMessage, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
  }
}
```
