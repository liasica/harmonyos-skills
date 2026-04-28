---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-hce-guide
title: HCE卡模拟开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > NFC > HCE卡模拟开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:01783ffd7c9ed2cfa40273484dcf50164ff200a15bf68f76feeaef2ad36cb09a
---

## 简介

近场通信(Near Field Communication，NFC)是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。HCE(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，电子设备上的应用程序模拟NFC卡片和NFC读卡器通信，实现NFC刷卡业务。从API version 22开始支持OFFHOST(Off Host Card Emulation)，称为基于安全单元的卡模拟，卡由设备中的一个单独芯片(称为安全单元)进行模拟。无线运营商部分SIM卡也包含安全单元。

## 场景介绍

应用程序模拟NFC卡片，和NFC读卡器通信完成NFC刷卡业务。从使用场景上，可以分成HCE应用前台刷卡和HCE应用后台刷卡。

* HCE应用前台刷卡

  前台刷卡是指在触碰NFC读卡器之前，用户明确想使用在电子设备上打开特定的应用程序和NFC读卡器进行刷卡操作。当用户打开应用程序在前台，并且进入应用的刷卡页面时，电子设备触碰NFC读卡器后，会把刷卡交易数据分发给前台应用。若应用切换至后台或退出运行时，前台优先分发规则也随即被暂停。
* HCE应用后台刷卡

  后台刷卡是指不打开特定的HCE应用程序，当电子设备触碰NFC读卡器时，根据NFC读卡器选择的应用ID（Applet ID，AID，参考ISO/IEC 7816-4规范）匹配到HCE应用程序，并自动和匹配的HCE应用程序通信完成刷卡交易。如果NFC读卡器选择的应用ID，匹配到多个HCE应用程序时，说明存在冲突，需要用户打开指定的HCE应用，重新靠近NFC读卡器触发刷卡。

安全单元模拟NFC卡片，和NFC读卡器完成NFC刷卡业务。要模拟的卡片通过应用配置到安全单元中，当电子设备触碰到NFC读卡器时，数据不经过设备CPU处理，而是直接发送到安全单元，完成刷卡。

## HCE应用刷卡的约束条件

1. 基于刷卡安全性考虑，不论HCE应用是前台方式还是后台方式刷卡，均不支持电子设备在灭屏或熄屏状态下的HCE刷卡操作。
2. 电子设备必须具备NFC控制器芯片，才支持HCE刷卡能力。对于是否具有NFC安全单元芯片，没有约束要求。
3. HCE应用程序需要声明NFC卡模拟权限，具体见示例。

## 接口说明

NFC卡模拟完整的API说明以及实例代码请参考：[NFC卡模拟接口](../harmonyos-references/js-apis-cardemulation.md)。

完成HCE卡模拟功能，需要使用到下面的接口。

| 接口名 | 支持版本 | 功能描述 |
| --- | --- | --- |
| hasHceCapability(): boolean | 从API version 9开始支持 | 判断设备是否支持HCE卡模拟功能。 |
| isDefaultService(elementName: ElementName, type: CardType): boolean | 从API version 9开始支持 | 判断指定的应用是否为指定业务类型的默认应用。 |
| start(elementName: ElementName, aidList: string[]): void | 从API version 9开始支持 | 启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。 |
| stop(elementName: ElementName): void | 从API version 9开始支持 | 停止HCE业务功能。包括取消APDU数据接收的订阅、退出当前应用前台优先、释放动态注册的AID列表。 |
| on(type: 'hceCmd', callback: AsyncCallback<number[]>): void | 从API version 8开始支持 | 订阅回调，用于接收对端读卡设备发送的APDU数据。 |
| transmit(response: number[]): Promise<void> | 从API version 9开始支持 | 发送APDU数据到对端读卡设备。 |
| off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void | 从API version 18开始支持 | 取消APDU数据接收的订阅。 |

## 开发准备

### HCE应用支持前台或后台刷卡的选择

HCE应用开发者根据业务需要，可以选择实现前台刷卡或者后台刷卡。两种不同的刷卡方式，代码实现上会存在一些差异。

* HCE应用前台刷卡

1. 在配置文件module.json5中，不需要静态声明NFC读卡器选择的应用ID（AID，参考ISO/IEC 7816-4规范），而是通过[start](../harmonyos-references/js-apis-cardemulation.md#start9)来动态注册。
2. HCE应用的刷卡页面退出时，需要显式调用[stop](../harmonyos-references/js-apis-cardemulation.md#stop9)来释放动态注册的AID刷卡配置项。

* HCE应用后台刷卡

1. 在配置文件module.json5中，需要静态声明NFC读卡器选择的应用ID（AID）。根据业务选择， 选择声明的AID是属于Payment类型，还是Other类型。
2. 如果选择Payment类型，该HCE应用会在系统设置页面的NFC"默认付款应用"里出现。用户必须选择该HCE应用作为默认支付应用后，才能实现后台刷卡功能。由于提供了默认支付应用的选项， 因此Payment类型的HCE应用，不会出现多个冲突的情况。
3. 如果选择Other类型，该HCE应用不会出现在系统设置页面的NFC"默认付款应用"里，但是多个HCE应用如果都声明了相同的Other类型的AID时，会出现冲突的可能。
4. HCE应用后台刷卡的实现，不需要调用接口start和stop。
5. HCE应用后台刷卡建议使用单独专用的HceAbility实现，以减少[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)函数耗时。
6. HceAbility的OnCreate函数中除了[hceService.on](../harmonyos-references/js-apis-cardemulation.md#on8)外，尽量减少其它操作。
7. HceAbility的OnCreate函数中hceService.on要同步执行，不能异步执行，以免影响HCE通信时序。

注意

* 从API version 9之后的应用开发新增支持[Stage模型](ability-terminology.md#stage模型)，作为目前主推并长期演进的模型。
* HCE示例代码的提供，全部按照[Stage模型](ability-terminology.md#stage模型)来说明。

## 开发步骤

### HCE应用前台刷卡

1. 在module.json5文件中声明NFC卡模拟权限，以及声明HCE特定的action。
2. import需要的NFC卡模拟模块和其他相关的模块。
3. 判断设备是否支持NFC能力和HCE能力。
4. 使能前台HCE应用程序优先处理NFC刷卡功能。
5. 订阅HCE APDU数据的接收。
6. 完成HCE刷卡APDU数据的接收和发送。
7. 退出应用程序NFC刷卡页面时，退出前台优先功能。

```
1. "abilities": [
2. {
3. // 以下使用的变量名若无默认值需先声明定义
4. "name": "EntryAbility",
5. "srcEntry": "./ets/entryability/EntryAbility.ts",
6. "description": "$string:EntryAbility_desc",
7. "icon": "$media:icon",
8. "label": "$string:EntryAbility_label",
9. "startWindowIcon": "$media:icon",
10. "startWindowBackground": "$color:start_window_background",
11. "exported": true,
12. "skills": [
13. {
14. "entities": [
15. "entity.system.home"
16. ],
17. "actions": [
18. "ohos.want.action.home",

20. // actions必须包含"ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
21. "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
22. ]
23. }
24. ]
25. }
26. ],
27. "requestPermissions": [
28. {
29. // 添加使用NFC卡模拟需要的权限
30. "name": "ohos.permission.NFC_CARD_EMULATION",
31. "reason": "$string:app_name",
32. }
33. ]
```

```
1. import { cardEmulation } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { AsyncCallback } from '@kit.BasicServicesKit';
5. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

7. let hceElementName: bundleManager.ElementName;
8. let hceService: cardEmulation.HceService;

10. const hceCommandCb: AsyncCallback<number[]> = (error: BusinessError, hceCommand: number[]) => {
11. if (!error) {
12. if (hceCommand == null) {
13. hilog.error(0x0000, 'testTag', 'hceCommandCb has invalid hceCommand.');
14. return;
15. }
16. // 应用程序根据自己业务实现，检查接收到的指令内容，发送匹配的响应数据
17. hilog.info(0x0000, 'testTag', 'hceCommand = %{public}s', JSON.stringify(hceCommand));
18. let responseData = [0x90, 0x00]; // 根据接收到的不同指令更改响应数据
19. hceService.transmit(responseData).then(() => {
20. hilog.info(0x0000, 'testTag', 'hceService transmit Promise success.');
21. }).catch((err: BusinessError) => {
22. hilog.error(0x0000, 'testTag', 'hceService transmit Promise error = %{public}s', JSON.stringify(err));
23. });
24. } else {
25. hilog.error(0x0000, 'testTag', 'hceCommandCb error %{public}s', JSON.stringify(error));
26. }
27. }

29. export default class EntryAbility extends UIAbility {
30. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
31. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

33. // 判断设备是否支持NFC能力和HCE能力
34. if (!canIUse("SystemCapability.Communication.NFC.Core")) {
35. hilog.error(0x0000, 'testTag', 'nfc unavailable.');
36. return;
37. }
38. if (!cardEmulation.hasHceCapability()) {
39. hilog.error(0x0000, 'testTag', 'hce unavailable.');
40. return;
41. }

43. // hceElementName中元素不能为空，通过want获取应用的elementname或按应用实际信息填写
44. hceElementName = {
45. bundleName: want.bundleName ?? '',
46. abilityName: want.abilityName ?? '',
47. moduleName: want.moduleName,
48. }
49. hceService = new cardEmulation.HceService();
50. }

52. onForeground() {
53. // 应用进入前台
54. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
55. if (hceElementName != undefined) {
56. try {
57. // 调用接口使能前台HCE应用程序优先处理NFC刷卡功能
58. let aidList = ["A0000000031010", "A0000000031011"]; // 修改为正确的aid
59. hceService.start(hceElementName, aidList);

61. // 订阅HCE APDU数据的接收
62. hceService.on('hceCmd', hceCommandCb);
63. } catch (error) {
64. hilog.error(0x0000, 'testTag', 'hceService.start error = %{public}s', JSON.stringify(error));
65. }
66. }
67. }

69. onBackground() {
70. // 应用退到后台
71. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
72. // 应用程序退出前台，停止HCE业务功能
73. if (hceElementName != undefined) {
74. try {
75. hceService.stop(hceElementName);
76. } catch (error) {
77. hilog.error(0x0000, 'testTag', 'hceService.stop error = %{public}s', JSON.stringify(error));
78. }
79. }
80. }
81. }
```

### HCE应用后台刷卡

1. 在module.json5文件中声明NFC卡模拟权限，声明HCE特定的action，声明应用能够处理的AID。
2. import需要的NFC卡模拟模块和其他相关的模块。
3. 判断设备是否支持NFC能力和HCE能力。
4. 订阅HCE APDU数据的接收。
5. 完成HCE刷卡APDU数据的接收和发送。
6. 退出应用程序时，退出订阅功能。

```
1. "abilities": [
2. {
3. "name": "HceUIAbility",
4. "srcEntry": "./ets/hceuiability/HceUIAbility.ts",
5. "description": "$string:EntryAbility_desc",
6. "icon": "$media:icon",
7. "label": "$string:EntryAbility_label",
8. "startWindowIcon": "$media:icon",
9. "startWindowBackground": "$color:start_window_background",
10. "exported": true,
11. "skills": [
12. {
13. "entities": [
14. "entity.system.home"
15. ],
16. "actions": [
17. "ohos.want.action.home",

19. // actions必须包含"ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
20. "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
21. ]
22. }
23. ],

25. // 根据业务需要至少定义一个Payment类型或Other类型的AID，可以定义多个
26. "metadata": [
27. {
28. "name": "payment-aid",
29. "value": "A0000000031010" // 定义Payment类型的AID
30. },
31. {
32. "name": "other-aid",
33. "value": "A0000000031011" // 定义Other类型的AID
34. }
35. ]
36. }
37. ],
38. "requestPermissions": [
39. {
40. // 添加使用NFC卡模拟需要的权限
41. "name": "ohos.permission.NFC_CARD_EMULATION",
42. "reason": "$string:app_name",
43. }
44. ]
```

```
1. import { cardEmulation } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { AsyncCallback } from '@kit.BasicServicesKit';
5. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

7. let hceElementName: bundleManager.ElementName;
8. let hceService: cardEmulation.HceService;

10. const hceCommandCb: AsyncCallback<number[]> = (error: BusinessError, hceCommand: number[]) => {
11. if (!error) {
12. if (hceCommand == null) {
13. hilog.error(0x0000, 'testTag', 'hceCommandCb has invalid hceCommand.');
14. return;
15. }

17. // 应用程序根据自己业务实现，检查接收到的指令内容，发送匹配的响应数据
18. hilog.info(0x0000, 'testTag', 'hceCommand = %{public}s', JSON.stringify(hceCommand));
19. let responseData = [0x90, 0x00]; // 根据接收到的不同指令更改响应数据
20. hceService.transmit(responseData).then(() => {
21. hilog.info(0x0000, 'testTag', 'hceService transmit Promise success.');
22. }).catch((err: BusinessError) => {
23. hilog.error(0x0000, 'testTag', 'hceService transmit Promise error = %{public}s', JSON.stringify(err));
24. });
25. } else {
26. hilog.error(0x0000, 'testTag', 'hceCommandCb error %{public}s', JSON.stringify(error));
27. }
28. }

30. // 使用单独专用的HceAbility实现，以减少OnCreate函数耗时
31. export default class HceUIAbility extends UIAbility {
32. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
33. // OnCreate函数中除了hceService.on外，尽量减少其它操作
34. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

36. // 判断设备是否支持NFC能力和HCE能力
37. if (!canIUse("SystemCapability.Communication.NFC.Core")) {
38. hilog.error(0x0000, 'testTag', 'nfc unavailable.');
39. return;
40. }
41. if (!cardEmulation.hasHceCapability()) {
42. hilog.error(0x0000, 'testTag', 'hce unavailable.');
43. return;
44. }

46. // 应用程序被运行到前台时，订阅HCE刷卡数据的接收
47. hceService = new cardEmulation.HceService();
48. // hceService.on同步执行，不能异步执行，以免影响HCE通信时序
49. hceService.on('hceCmd', hceCommandCb);
50. }

52. onForeground() {
53. // 应用进入前台
54. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
55. }

57. onDestroy() {
58. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
59. // 退出应用程序，取消订阅接受HCE刷卡数据
60. hceService.off('hceCmd', hceCommandCb);
61. }
62. }
```

### OFFHOST应用刷卡

1. 在module.json5文件中声明OFFHOST特定的action，声明应用能够处理的AID，声明安全单元。
2. 将OFFHOST应用设置为默认付款应用。

说明

* 从 API version 22开始支持OFFHOST能力。
* 当前只支持payment类型的AID。
* 当前只支持SIM作为安全单元。

```
1. "abilities": [
2. {
3. "name": "EntryAbility",
4. "srcEntry": "./ets/entryability/EntryAbility.ts",
5. "description": "$string:EntryAbility_desc",
6. "icon": "$media:icon",
7. "label": "$string:EntryAbility_label",
8. "startWindowIcon": "$media:icon",
9. "startWindowBackground": "$color:start_window_background",
10. "exported": true,
11. "skills": [
12. {
13. "entities": [
14. "entity.system.home"
15. ],
16. "actions": [
17. "ohos.want.action.home",

19. // actions必须包含"ohos.nfc.cardemulation.action.OFF_HOST_APDU_SERVICE"
20. "ohos.nfc.cardemulation.action.OFF_HOST_APDU_SERVICE"
21. ]
22. }
23. ]
24. // 根据业务需要至少定义一个Payment类型的AID，可以定义多个
25. "metadata": [
26. {
27. "name": "payment-aid",
28. "value": "A0000000031010" // 定义Payment类型的AID，需要修改为正确的AID
29. },
30. {
31. "name": "secureElement",
32. "value": "SIM" // 定义secureElement
33. },
34. ]
35. }
36. ]
```
