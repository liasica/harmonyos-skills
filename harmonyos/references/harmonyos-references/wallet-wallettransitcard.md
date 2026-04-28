---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-wallettransitcard
title: walletTransitCard（交通卡能力）
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > ArkTS API > walletTransitCard（交通卡能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d10045ae588cb26cec08bce7215a694452da5083b708f51c347ca7bdf7238e7
---

本模块提供接入钱包交通卡服务的能力。

**起始版本：** 5.0.0(12)

## 导入模块

Phone

```
1. import { walletTransitCard } from '@kit.WalletKit';
```

## TransitCardClient

Phone

钱包交通卡的功能入口类，与钱包卡券有关的所有方法从此处接入。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

### constructor

Phone

constructor(context: common.UIAbilityContext, callerId: string)

构造函数。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| callerId | string | 是 | 接口调用方ID，调用方联系钱包运营申请交通卡服务时获取，仅对**受邀应用**开放申请。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';

4. @Entry
5. @Component
6. struct Index {
7. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

9. build() {
10. // your application UI
11. }
12. }
```

### getCardMetadataInDevice

Phone

getCardMetadataInDevice(specifiedDeviceType: DeviceType, callerToken?: string): Promise<CardMetadataInDevice[]>

获取当前设备中可开卡和已经开通的交通卡信息，包含设备信息和设备支持的卡的元数据。 在没有eSE的情况下，将返回一个空数组。 如果设备没有支持的卡，则无法在阵列中添加设备的CardMetadataInDevice。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| specifiedDeviceType | [DeviceType](wallet-wallettransitcard.md#devicetype) | 是 | 指定设备的枚举值。 |
| callerToken | string | 否 | 小程序在微信、支付宝等中的鉴权token，要求使用JWT格式生成。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)[]> | Promise对象，返回一个CardMetadataInDevice元数据数组，包含设备信息和卡的元数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210701 | Failed to verify the caller token. |
| 1010210702 | Failed to get the metadata of the cards. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async getCardMetadataInDevice() {
11. this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE_PHONE).then((result) => {
12. console.info(`Succeeded in getting cardMetadataInDevice`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
15. })
16. }

18. build() {
19. // your application UI
20. }
21. }
```

### getTransitCardInfo

Phone

getTransitCardInfo(logicalCardNumber: string, specifiedDeviceId: string, callerToken?: string): Promise<TransitCardInfo>

查询指定的cardNumber交通卡信息。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice) 返回的 [CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice) 中的[CardMetadata](wallet-wallettransitcard.md#cardmetadata) 对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice) 返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice) 对应的deviceId。 |
| callerToken | string | 否 | 小程序在微信、支付宝等中的鉴权token，要求使用JWT格式生成。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<[TransitCardInfo](wallet-wallettransitcard.md#transitcardinfo)> | Promise对象，返回cardNumber指定卡的详细信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210101 | The card status is not correct. |
| 1010210119 | Failed to read the card data. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210102 | Failed to verify the caller token. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async getTransitCardInfo() {
11. // number of the enabled traffic card returned by the getCardMetadataInDevice interface
12. const logicalCardNumber = 'logicalCardNumber';
13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
14. const specifiedDeviceId = 'specifiedDeviceId';
15. // JWT token for authentication in applications such as WeChat and Alipay
16. const callerToken= 'callerToken';
17. this.transitCardClient.getTransitCardInfo(logicalCardNumber, specifiedDeviceId, callerToken).then((result) => {
18. console.info(`Succeeded in getting TransitCardInfo`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to get TransitCardInfo, code:${err.code}, message:${err.message}`);
21. })
22. }

24. build() {
25. // your application UI
26. }
27. }
```

### canAddTransitCard

Phone

canAddTransitCard(issuerId: string, specifiedDeviceId: string): Promise<string>

判断issuerId在当前设备中是否可以开卡，返回一个令牌字符串，指示是否可以在指定设备的钱包中添加issuerId指定的卡。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| issuerId | string | 是 | 城市的一种交通卡产品的ID，要求使用 [getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice) 返回的 [CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)中的 [CardMetadata](wallet-wallettransitcard.md#cardmetadata) 对应的issuerId。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用 [getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice) 返回的 [CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)对应的deviceId。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回一个用于添加卡片的token令牌。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200007 | The OS version is too old. Please upgrade the OS version. |
| 1010200008 | The wallet version is too old. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200016 | This card is not available for the current country or region. |
| 1010210201 | The device does not support adding the card specified by issuerId. |
| 1010210202 | A card conflicting with the specified card already exists in the device. |
| 1010210203 | The specified card already exists. |
| 1010210204 | The card addition service is temporarily offline. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async canAddTransitCard() {
11. // the issuerId returned by the getCardMetadataInDevice interface
12. const issuerId = 'issuerId';
13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
14. const specifiedDeviceId = 'specifiedDeviceId';
15. this.transitCardClient.canAddTransitCard(issuerId, specifiedDeviceId).then((result) => {
16. console.info(`Succeeded in canning AddTransitCard`);
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to can AddTransitCard, code:${err.code}, message:${err.message}`);
19. })
20. }

22. build() {
23. // your application UI
24. }
25. }
```

### setupWalletEnvironment

Phone

setupWalletEnvironment(): Promise<void>

设置Wallet应用程序的environment。当开发者从另一个api得到1010200003错误代码时，你应该调用这个api来设置Wallet应用。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1010200002 | Wallet app not found. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200011 | Failed to initialize the environment. |
| 1010200017 | The Wallet app was closed by the user. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async setupWalletEnvironment() {
11. this.transitCardClient.setupWalletEnvironment().then(() => {
12. console.info(`Succeeded in setting up WalletEnvironment`);
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to setup WalletEnvironment, code:${err.code}, message:${err.message}`);
15. })
16. }

18. build() {
19. // your application UI
20. }
21. }
```

### addTransitCard

Phone

addTransitCard(addCardOpaqueData: string, serverOrderId: string): Promise<CardMetadata>

将指定的卡添加到钱包中，并返回CardMetadata。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| addCardOpaqueData | string | 是 | 开卡令牌，要求使用[canAddTransitCard](wallet-wallettransitcard.md#canaddtransitcard)接口返回的字符串。 |
| serverOrderId | string | 是 | 开卡订单ID，要求是加卡业务在服务商后台服务器上生成的订单ID。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<[CardMetadata](wallet-wallettransitcard.md#cardmetadata)> | Promise对象，返回添加的卡片数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210301 | The card adding conditions are not met. The order can be refunded to end the card addition process. |
| 1010200016 | This card is not available for the current country or region. |
| 1010200017 | The Wallet app was closed by the user. |
| 1010210319 | Failed to add the card. |
| 1010210302 | Failed to confirm the order. The order can be refunded to end the card addition process. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async addTransitCard() {
11. // order ID generated after payment in a developer's app, which is implemented by the developer
12. let serverOrderId = 'serverOrderId';
13. // the addCardOpaqueData returned by the canAddTransitCard interface
14. let addCardOpaqueData = 'addCardOpaqueData';
15. this.transitCardClient.addTransitCard(addCardOpaqueData, serverOrderId).then((result) => {
16. console.info(`Succeeded in adding TransitCard`);
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to add TransitCard, code:${err.code}, message:${err.message}`);
19. })
20. }

22. build() {
23. // your application UI
24. }
25. }
```

### rechargeTransitCard

Phone

rechargeTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<number>

交通卡充值接口，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行充值，充值完成后返回当前余额。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 卡的序列号，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)中的[CardMetadata](wallet-wallettransitcard.md#cardmetadata)对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)对应的deviceId。 |
| serverOrderId | string | 是 | 卡充值订单ID，要求是余额充值业务在服务商后台服务器上生成的订单ID。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<number> | Promise对象，返回新的交通卡余额。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210401 | The specified card does not exist. |
| 1010210402 | The status of the specified card is incorrect. |
| 1010210419 | Failed to recharge the card. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210403 | Failed to confirm the order. The order can be refunded to end the recharging process. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async rechargeTransitCard() {
11. // number of the enabled traffic card returned by the getCardMetadataInDevice interface
12. const logicalCardNumber = 'logicalCardNumber';
13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
14. const specifiedDeviceId = 'specifiedDeviceId';
15. // order ID generated after payment in a developer's app, which is implemented by the developer
16. const serverOrderId = 'serverOrderId';
17. this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then((result) => {
18. console.info(`Succeeded in recharging TransitCard`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to recharge TransitCard, code:${err.code}, message:${err.message}`);
21. })
22. }

24. build() {
25. // your application UI
26. }
27. }
```

### updateTransitCard

Phone

updateTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

更新交通卡信息，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行数据更新。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)中的[CardMetadata](wallet-wallettransitcard.md#cardmetadata)对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 卡所在的设备ID，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)对应的deviceId。 |
| serverOrderId | string | 是 | 更新卡信息订单ID，要求是卡数据更新服务在服务提供商后台服务器上生成的订单ID。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210501 | The specified card does not exist. |
| 1010210502 | The status of the specified card is incorrect. |
| 1010210503 | Failed to confirm the order. |
| 1010210519 | Failed to update the card data. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async updateTransitCard() {
11. // number of the enabled traffic card returned by the getCardMetadataInDevice interface
12. const logicalCardNumber = 'logicalCardNumber';
13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
14. const specifiedDeviceId = 'specifiedDeviceId';
15. // order ID generated after payment in a developer's app, which is implemented by the developer
16. const serverOrderId = 'serverOrderId';
17. this.transitCardClient.updateTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
18. console.info(`Succeeded in updating TransitCard`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to update TransitCard, code:${err.code}, message:${err.message}`);
21. })
22. }

24. build() {
25. // your application UI
26. }
27. }
```

### deleteTransitCard

Phone

deleteTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

删除交通卡，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行删卡。

使用Promise异步回调。

不支持多线程调用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)中的[CardMetadata](wallet-wallettransitcard.md#cardmetadata)对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 卡所在的设备ID，要求使用[getCardMetadataInDevice](wallet-wallettransitcard.md#getcardmetadataindevice)返回的[CardMetadataInDevice](wallet-wallettransitcard.md#cardmetadataindevice)对应的deviceId。 |
| serverOrderId | string | 是 | 删卡订单id，要求是服务提供商的后端服务器上为删卡业务生成的订单id。 |

**返回值：**

| 类型 | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](wallet-error-code.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210619 | Failed to delete the card. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210601 | Failed to confirm the order. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { walletTransitCard } from '@kit.WalletKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

10. async deleteTransitCard() {
11. // number of the enabled traffic card returned by the getCardMetadataInDevice interface
12. const logicalCardNumber = 'logicalCardNumber';
13. // the specifiedDeviceId returned by the getCardMetadataInDevice interface
14. const specifiedDeviceId = 'specifiedDeviceId';
15. // order ID generated after payment in a developer's app, which is implemented by the developer
16. const serverOrderId = 'serverOrderId';
17. this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
18. console.info(`Succeeded in deleting TransitCard`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to delete TransitCard, code:${err.code}, message:${err.message}`);
21. })
22. }

24. build() {
25. // your application UI
26. }
27. }
```

## CardMetadata

Phone

描述卡的元数据信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| issuerId | string | 否 | 否 | 交通卡产品的id |
| aid | string | 否 | 否 | SE芯片中卡的小程序应用程序ID。 |
| logicalCardNumber | string | 否 | 是 | 卡的序列号。仅当设备中存在转接卡时会存在。 |
| cardNumber | string | 否 | 是 | 显示卡号（30个字符以内），如果该卡存在于设备中则会返回 |
| balance | number | 否 | 是 | 卡的余额（如果设备中存在卡） |

## CardMetadataInDevice

Phone

设备的接口和设备支持的卡元数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID，开发者使用。 |
| deviceType | [DeviceType](wallet-wallettransitcard.md#devicetype) | 否 | 否 | 设备的类型 |
| displayName | string | 否 | 否 | 要显示的设备名称 |
| cardMetadata | [CardMetadata](wallet-wallettransitcard.md#cardmetadata)[] | 否 | 否 | 设备支持的卡的数据。 |

## TransitCardInfo

Phone

交通卡信息。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cardNumber | string | 否 | 否 | 显示卡号 |
| customCardData | string | 否 | 是 | 服务提供商的自定义卡数据。json数据结构如下。  - balance：卡余额，单位分。  - expireDate：卡片过期时间。  - metroStatus：地铁刷卡进出站状态，其他交通卡不涉及。  - 1：已进站  - 2：已出站  - 3：未知  - records：交易记录，包括充值和消费两种类型。records包括以下字段。  - type：记录类型 。1：充值 ；2：消费  - amount：交易金额。单位：分。  - transDate：交易时间。  - transactionNo：交易序号。 |

## DeviceType

Phone

设备类型的枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.Wallet

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_PHONE | 0 | 手机设备类型 |
| DEVICE\_WATCH | 1 | 穿戴手表设备类型 |
