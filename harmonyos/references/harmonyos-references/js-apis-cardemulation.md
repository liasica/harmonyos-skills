---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cardemulation
title: @ohos.nfc.cardEmulation (标准NFC-cardEmulation)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.nfc.cardEmulation (标准NFC-cardEmulation)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c03f334436400402b31867bfbe61b18eb6127fbb5aa5433e87e01d6bd3e5f083
---

本模块主要提供NFC卡模拟业务，包括判断支持哪种卡模拟类型，HCE卡模拟的业务实现等。

HCE(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，应用程序模拟NFC卡片，可以通过NFC服务和NFC读卡器通信。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## HCE卡模拟和AID列表的声明定义

PhoneWearableLite Wearable

开发HCE卡模拟相关应用时，需要在应用的属性配置文件中，声明与NFC相关的属性值，比如，在module.json5文件中，声明下面属性值：

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. {
3. "module": {
4. // 其他已声明的属性
5. "abilities": [
6. {
7. // 其他已声明的属性
8. "skills": [
9. {
10. "actions": [
11. "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
12. ]
13. }
14. ],
15. "metadata": [
16. {
17. "name": "payment-aid",
18. "value": "your payment aid"
19. },
20. {
21. "name": "other-aid",
22. "value": "your other aid"
23. }
24. ]
25. }
26. ],
27. "requestPermissions": [
28. {
29. "name": "ohos.permission.NFC_CARD_EMULATION",
30. // 必须要添加reason: card_emulation_reason
31. "reason": "$string:card_emulation_reason"
32. }
33. ]
34. }
35. }
```

```
1. // 轻量级智能穿戴设备
2. {
3. "module": {
4. // 其他已声明的属性
5. "abilities": [
6. {
7. // 其他已声明的属性
8. "metaData": {
9. "customizeData": [
10. {
11. "name": "paymentAid",
12. "value": "A0000000041012"
13. },
14. {
15. "name": "otherAid",
16. "value": "A0000000041010"
17. }
18. ]
19. },
20. "skills": [
21. {
22. "entities": [
23. "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
24. ],
25. "actions": [
26. "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
27. ]
28. }
29. ]
30. }
31. ],
32. "reqPermissions": [
33. {
34. "name": "ohos.permission.NFC_CARD_EMULATION",
35. // 必须要添加reason: card_emulation_reason
36. "reason": "$string:card_emulation_reason",
37. "usedScene":{
38. "ability":[
39. "FormAbility"
40. ],
41. "when":"always"
42. }
43. },
44. {
45. "name": "ohos.permission.NFC_TAG",
46. // 必须要添加reason: card_emulation_reason
47. "reason": "$string:card_emulation_reason",
48. "usedScene":{
49. "ability":[
50. "FormAbility"
51. ],
52. "when":"always"
53. }
54. }
55. ]
56. }
57. }
```

注意

1. 声明"actions"字段的内容填写，必须包含"ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"，不能更改。
2. 声明aid（参考ISO/IEC 7816-4规范）时，name必须为payment-aid或者other-aid。填写错误会造成解析失败。
3. 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC\_CARD\_EMULATION"，不能更改。
4. 轻量级智能穿戴产品不同于其他设备，仅支持[FA模型](../harmonyos-guides/ability-terminology.md#fa模型)，属性配置和接口调用方式与其他设备有所区别，详见示例。

## 导入模块

PhoneWearableLite Wearable

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';
```

```
1. // 轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';
```

## FeatureType(deprecated)

PhoneWearableLite Wearable

定义不同的NFC卡模拟类型。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[hasHceCapability](js-apis-cardemulation.md#cardemulationhashcecapability9)替代。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HCE | 0 | HCE 卡模拟。 |
| UICC | 1 | SIM 卡模拟。 |
| ESE | 2 | ESE 卡模拟。 |

## CardType9+

PhoneWearableLite Wearable

定义卡模拟应用所使用的业务类型，是支付类型，还是其他类型。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAYMENT | "payment" | 卡模拟应用所使用的业务是支付类型。 |
| OTHER | "other" | 卡模拟应用所使用的业务是其他类型。 |

## cardEmulation.isSupported(deprecated)

PhoneWearableLite Wearable

isSupported(feature: number): boolean

是否支持某种类型的卡模拟。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[hasHceCapability](js-apis-cardemulation.md#cardemulationhashcecapability9)替代。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feature | number | 是 | 卡模拟类型值，详细请见[FeatureType](js-apis-cardemulation.md#featuretypedeprecated)枚举值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 支持该类型卡模拟， false: 不支持该类型卡模拟。 |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';

4. let isHceSupported: boolean = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
5. if (!isHceSupported) {
6. console.info('this device is not supported for HCE, ignore it.');
7. }
```

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let isHceSupported = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
5. if (!isHceSupported) {
6. console.error('this device is not supported for HCE, ignore it.');
7. }
```

## cardEmulation.hasHceCapability9+

PhoneWearableLite Wearable

hasHceCapability(): boolean

判断设备是否支持HCE卡模拟功能。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 支持HCE， false: 不支持HCE。 |

**错误码**：

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';

4. let hasHceCap: boolean = cardEmulation.hasHceCapability();
5. if (!hasHceCap) {
6. console.error('this device hasHceCapability false, ignore it.');
7. }
```

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let hasHceCap = cardEmulation.hasHceCapability();
5. if (!hasHceCap) {
6. console.error('this device hasHceCapability false, ignore it.');
7. }
```

## cardEmulation.isDefaultService9+

PhoneWearableLite Wearable

isDefaultService(elementName: ElementName, type: CardType): boolean

判断指定的应用是否为指定业务类型的默认应用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| type | [CardType](js-apis-cardemulation.md#cardtype9) | 是 | 卡模拟业务类型。目前只支持默认支付应用查询。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 是默认支付应用， false: 不是默认支付应用。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';
3. import { bundleManager, Want } from '@kit.AbilityKit';

5. // 需要初始化 elementName、bundleName、abilityName，根据实际应用信息更改为正确的值
6. let elementName: bundleManager.ElementName = {
7. bundleName: "com.example.myapplication",
8. moduleName: "entry",
9. abilityName: "EntryAbility"
10. };

12. let isDefaultService: boolean = cardEmulation.isDefaultService(elementName, cardEmulation.CardType.PAYMENT);
```

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let appName = "com.example.testquestionlite";
5. let isDefaultService = cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
```

## HceService8+

PhoneWearableLite Wearable

提供HCE卡模拟的实现，主要包括接收对端读卡设备的APDU数据，并响应APDU数据到对端读卡设备。使用HCE相关接口前，必须先判断设备是否支持HCE卡模拟能力。

### startHCE(deprecated)

PhoneWearableLite Wearable

startHCE(aidList: string[]): boolean

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[start](js-apis-cardemulation.md#start9)替代。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aidList | string[] | 是 | 动态注册卡模拟的AID列表。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 启动HCE功能或HCE已启动， false: 启动失败。 |

### start9+

PhoneWearableLite Wearable

start(elementName: [ElementName](js-apis-bundlemanager-elementname.md), aidList: string[]): void

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| aidList | string[] | 是 | 动态注册卡模拟的AID列表，允许为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

### stopHCE(deprecated)

PhoneWearableLite Wearable

stopHCE(): boolean

停止HCE业务功能。包括退出当前应用前台优先，释放动态注册的AID列表，释放hceCmd的订阅。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[stop](js-apis-cardemulation.md#stop9)替代。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 禁用HCE功能或HCE已禁用，false: 禁用失败。 |

**示例：**

示例请参见[on](js-apis-cardemulation.md#on8)接口的示例。

### stop9+

PhoneWearableLite Wearable

stop(elementName: [ElementName](js-apis-bundlemanager-elementname.md)): void

停止HCE业务功能。包括取消APDU数据接收的订阅，退出当前应用前台优先，释放动态注册的AID列表。应用程序需要在HCE卡模拟页面的onDestroy函数里调用该接口。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

### on8+

PhoneWearableLite Wearable

on(type: 'hceCmd', callback: AsyncCallback<number[]>): void

订阅回调，用于接收对端读卡设备发送的APDU数据，应用程序需要在HCE卡模拟页面的onCreate函数里面调用该订阅函数。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要订阅的回调类型，固定填"hceCmd"字符串。 |
| callback | AsyncCallback<number[]> | 是 | 回调函数，返回的是符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { cardEmulation } from '@kit.ConnectivityKit';
4. import { AsyncCallback } from '@kit.BasicServicesKit';
5. import { ElementName } from './bundleManager/ElementName'
6. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

8. let hceService: cardEmulation.HceService = new cardEmulation.HceService();
9. let element: ElementName;

11. export default class EntryAbility extends UIAbility {
12. onCreate(want: Want, param: AbilityConstant.LaunchParam) {
13. hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
14. element = {
15. bundleName: want.bundleName ?? '',
16. abilityName: want.abilityName ?? '',
17. moduleName: want.moduleName
18. }
19. const apduCallback: AsyncCallback<number[]> = (err, data) => {
20. // 处理数据和异常
21. console.info("got apdu data");
22. };
23. hceService.on('hceCmd', apduCallback);
24. }
25. onDestroy() {
26. hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
27. hceService.stop(element);
28. }
29. // 生命周期内的其他功能
30. }
```

**示例：**

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let appName = "com.example.testquestionlite";

6. export default {
7. data:{
8. fontSize: '30px',
9. fontColor: '#50609f',
10. hide: 'show',
11. headCon: appName,
12. paymentAid: ["A0000000041010", "A0000000041012"]
13. },
14. onCreate() {
15. console.info('onCreate');
16. },
17. onReady() {
18. cardEmulation.hasHceCapability();
19. cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
20. cardEmulation.isDefaultService(appName, cardEmulation.CardType.OTHER);
21. let HceService = new cardEmulation.HceService();

23. HceService.start(appName, this.paymentAid);
24. HceService.on("hceCmd", (data) => {
25. console.info('data:' + data);
26. // 应用程序实际想要发送的数据， 此处仅作为示例
27. let responseData = [0x1, 0x2];
28. HceService.transmit(responseData, () => {
29. console.info('sendResponse start');
30. });
31. console.info('sendResponse end');
32. });
33. },
34. onDestroy() {
35. }
36. // 生命周期内的其他功能
37. }
```

### off18+

PhoneWearableLite Wearable

off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void

取消APDU数据接收的订阅。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消订阅的事件类型，固定填"hceCmd"字符串。 |
| callback | AsyncCallback<number[]> | 否 | 回调函数，返回的每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { cardEmulation } from '@kit.ConnectivityKit';
4. import { AsyncCallback } from '@kit.BasicServicesKit';
5. import { ElementName } from './bundleManager/ElementName'
6. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

8. let hceService: cardEmulation.HceService = new cardEmulation.HceService();
9. let element: ElementName;
10. const apduCallback: AsyncCallback<number[]> = (err, data) => {
11. // 处理数据和异常
12. console.info("AsyncCallback got apdu data");
13. };

15. export default class EntryAbility extends UIAbility {
16. onCreate(want: Want, param: AbilityConstant.LaunchParam) {
17. hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
18. element = {
19. bundleName: want.bundleName ?? '',
20. abilityName: want.abilityName ?? '',
21. moduleName: want.moduleName
22. }
23. hceService.on('hceCmd', apduCallback);
24. }
25. onDestroy() {
26. hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
27. hceService.off('hceCmd', apduCallback);
28. hceService.stop(element);
29. }
30. // 生命周期内的其他功能
31. }
```

### sendResponse(deprecated)

PhoneWearableLite Wearable

sendResponse(responseApdu: number[]): void

发送APDU数据到对端读卡设备。

说明

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[transmit](js-apis-cardemulation.md#transmit9)替代。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| responseApdu | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

### transmit9+

PhoneWearableLite Wearable

transmit(response: number[]): Promise<void>

发送APDU数据到对端读卡设备，使用Promise异步回调。应用程序必须在[on](js-apis-cardemulation.md#on8)收到读卡设备发送的APDU数据后，才调用该接口响应数据。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let hceService: cardEmulation.HceService = new cardEmulation.HceService();

7. // 应用程序实际想要发送的数据， 此处仅作为示例
8. const responseData = [0x1, 0x2];
9. hceService.transmit(responseData).then(() => {
10. // 处理 promise 的回调
11. console.info("transmit Promise success.");
12. }).catch((err: BusinessError) => {
13. console.error("transmit Promise error:", err);
14. });
```

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let hceService = new cardEmulation.HceService();

6. // 应用程序实际想要发送的数据， 此处仅作为示例
7. let responseData = [0x1, 0x2];
8. hceService.transmit(responseData).then(() => {
9. // 处理 promise 的回调
10. console.info("transmit Promise success.");
11. });
12. console.info("transmit Promise end.");
```

### transmit9+

PhoneWearableLite Wearable

transmit(response: number[], callback: AsyncCallback<void>): void

发送APDU数据到对端读卡设备，应用程序必须在[on](js-apis-cardemulation.md#on8)收到读卡设备发送的APDU数据后，才调用该接口响应数据。使用Callback异步回调。

**需要权限：** ohos.permission.NFC\_CARD\_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发送APDU数据成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**示例：**

```
1. // 适用于除轻量级智能穿戴产品之外其他设备
2. import { cardEmulation } from '@kit.ConnectivityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let hceService: cardEmulation.HceService = new cardEmulation.HceService();

7. // 应用程序实际想要发送的数据， 此处仅作为示例
8. try {
9. const responseData = [0x1, 0x2];

11. hceService.transmit(responseData, (err : BusinessError)=> {
12. if (err) {
13. console.error(`transmit AsyncCallback err Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info("transmit AsyncCallback success.");
16. }
17. });
18. } catch (error) {
19. console.error(`transmit AsyncCallback catch Code: ${(error as BusinessError).code}, ` +
20. `message: ${(error as BusinessError).message}`);
21. }
```

```
1. // 适用于轻量级智能穿戴设备
2. import cardEmulation from '@ohos.nfc.cardEmulation';

4. let hceService = new cardEmulation.HceService();

6. // 应用程序实际想要发送的数据， 此处仅作为示例
7. let responseData = [0x1, 0x2];
8. hceService.transmit(responseData, () => {
9. console.info("transmit Promise success.");
10. });
11. console.info("transmit Promise end.");
```
