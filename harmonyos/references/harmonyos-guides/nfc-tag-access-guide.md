---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide
title: NFC标签读写开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > NFC > NFC标签读写开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2a70c6398fdf98c23d5d07fd715579326a0b1297d34a6090b1db810146d31d16
---

## 简介

近场通信(Near Field Communication，NFC)是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。电子设备可以通过NFC通信技术和NFC标签通信，从标签中读取数据，或写入数据到标签。

NFC标签支持一种或多种通信技术，具体技术如下：

* NfcA (也称为 ISO 14443-3A)
* NfcB (也称为 ISO 14443-3B)
* NfcF (也称为 JIS 6319-4)
* NfcV (也称为 ISO 15693)
* IsoDep (也称为 ISO 14443-4)
* NDEF
* MifareClassic
* MifareUltralight

## 场景介绍

电子设备通过NFC天线位置触碰NFC标签卡片，完成NFC标签卡片的读取或写入。从使用场景上，可以分成NFC标签前台读写和NFC标签后台读写。

* NFC标签前台读写

  前台读写是指在触碰NFC标签之前，用户先在电子设备上打开特定的应用程序，用户明确想使用所打开的应用程序和NFC标签进行读写操作。用户打开应用程序在前台，并且进入应用的刷卡页面之后，电子设备触碰NFC标签，只会把读取到的卡片分发给前台应用。
* NFC标签后台读写

  后台读写是指不打开特定的NFC标签应用程序，电子设备触碰发现NFC标签后，根据NFC标签的技术类型，分发给能够处理的应用程序。如果能匹配到多个应用程序，则弹出应用选择器列举出应用列表给用户手动选择。用户选择指定的应用后，自动跳转到应用程序的NFC标签读写卡页面。
* 常用读写NDEF格式Tag定制功能

  读取定制Tag内容拉起AirTouch服务，通过碰一碰服务直达，满足用户碎片化需求，如：NFC碰一碰点单、支付、活动推广等，详细应用开发接入指导及标签制作参考[AirTouch服务](https://developer.huawei.com/consumer/cn/airtouch/)。更多NDEF标签格式规范请关注[NFC论坛](https://nfc-forum.org/)。
* 标签读写约束条件

  不管是前台读写，还是后台读写，电子设备能够发现NFC标签的前提条件是设备必须是亮屏和解锁状态。

## 接口说明

NFC标签读写完整的JS API说明以及实例代码请参考：[NFC标签接口](../harmonyos-references/js-apis-nfctag.md)。

获取不同技术类型标签对象的接口说明如下表，根据不同技术的标签对象来执行NFC标签的读写。

| 接口名 | 支持版本 | 功能描述 |
| --- | --- | --- |
| getNfcA(tagInfo: TagInfo): NfcATag | 从API version 9开始支持 | 获取NfcA技术类型的标签对象。 |
| getNfcB(tagInfo: TagInfo): NfcBTag | 从API version 9开始支持 | 获取NfcB技术类型的标签对象。 |
| getNfcF(tagInfo: TagInfo): NfcFTag | 从API version 9开始支持 | 获取NfcF技术类型的标签对象。 |
| getNfcV(tagInfo: TagInfo): NfcVTag | 从API version 9开始支持 | 获取NfcV技术类型的标签对象。 |
| getIsoDep(tagInfo: TagInfo): IsoDepTag | 从API version 9开始支持 | 获取IsoDep技术类型的标签对象。 |
| getNdef(tagInfo: TagInfo): NdefTag | 从API version 9开始支持 | 获取NDEF技术类型的标签对象。 |
| getMifareClassic(tagInfo: TagInfo): MifareClassicTag | 从API version 9开始支持 | 获取MIFARE Classic技术类型的标签对象。 |
| getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag | 从API version 9开始支持 | 获取MifareUltralight技术类型的标签对象。 |

## 开发准备

### NFC标签前台读写或后台读写的选择

NFC标签读写应用开发者根据业务需要，可以选择实现前台读卡或者后台读卡。两种不同的读卡方式，代码实现上会存在一些差异。

* NFC标签前台读写

1. 在配置文件module.json5中，不需要静态声明过滤读取NFC标签的技术类型，而是通过[tag.registerForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagregisterforegrounddispatch10)或者[tag.on](../harmonyos-references/js-apis-nfctag.md#tagon11)来完成动态注册。
2. 通过tag.registerForegroundDispatch或tag.on来动态注册前台读写标签时，入参中必须指定需要读取NFC标签的技术类型。
3. 如果选择tag.registerForegroundDispatch注册，当应用运行在前台并进入该页面，NFC的卡模拟功能在打开时，可以同时完成刷卡。如果选择tag.on注册，当应用运行在前台并进入该页面时，NFC的卡模拟是关闭的，无法同时进行刷卡功能。
4. 当应用页面切换到后台时，需要显式调用[tag.unregisterForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagunregisterforegrounddispatch10)或者[tag.off](../harmonyos-references/js-apis-nfctag.md#tagoff11)来取消注册，退出前台读卡优先功能。

* NFC标签后台读写

1. 在配置文件module.json5中，需要静态声明过滤读取NFC标签的技术类型。根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述。
2. 技术类型的描述字符，必须完整匹配并区分大小写，需要严格匹配。

注意

* 从API version 9之后的应用开发新增支持[Stage模型](ability-terminology.md#stage模型)，作为目前主推并长期演进的模型。
* NFC标签读写示例代码的提供，全部按照[Stage模型](ability-terminology.md#stage模型)来说明。

## 开发步骤

### 前台读取标签

1. 在module.json5文件中声明NFC标签读取的权限，以及声明NFC标签特定的action。
2. import需要的tag模块和其他相关的模块。
3. 判断设备是否支持NFC能力。
4. 调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能。
5. 获取特定技术类型的NFC标签对象。
6. 执行读写接口完成标签数据的读取或写入数据到标签。
7. 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能。

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

19. // actions必须包含"ohos.nfc.tag.action.TAG_FOUND"
20. "ohos.nfc.tag.action.TAG_FOUND"
21. ]
22. }
23. ]
24. }
25. ],
26. "requestPermissions": [
27. {
28. // 添加NFC标签操作的权限
29. "name": "ohos.permission.NFC_TAG",
30. "reason": "$string:app_name",
31. }
32. ]
```

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

6. let nfcTagElementName: bundleManager.ElementName;
7. let foregroundRegister: boolean;

9. async function readerModeCb(error: BusinessError, tagInfo: tag.TagInfo) {
10. if (!error) {
11. // 获取特定技术类型的NFC标签对象
12. if (tagInfo == null) {
13. hilog.error(0x0000, 'testTag', 'readerModeCb tagInfo is invalid');
14. return;
15. }
16. if (tagInfo.uid == null) {
17. hilog.error(0x0000, 'testTag', 'readerModeCb uid is invalid');
18. return;
19. }
20. if (tagInfo.technology == null || tagInfo.technology.length == 0) {
21. hilog.error(0x0000, 'testTag', 'readerModeCb technology is invalid');
22. return;
23. }

25. // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入
26. // 下面示例代码，使用IsoDep完成标签数据的读取或写入
27. let isoDep: tag.IsoDepTag | null = null;
28. for (let i = 0; i < tagInfo.technology.length; i++) {
29. if (tagInfo.technology[i] == tag.ISO_DEP) {
30. try {
31. isoDep = tag.getIsoDep(tagInfo);
32. } catch (error) {
33. hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep error = %{public}s', JSON.stringify(error));
34. return;
35. }
36. }
37. // 也可以按需选择其它类型的技术读写标签
38. }
39. if (isoDep == null) {
40. hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep is invalid');
41. return;
42. }

44. // 使用IsoDep技术连接到NFC标签
45. try {
46. isoDep.connect();
47. } catch (error) {
48. hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.connect() error = %{public}s', JSON.stringify(error));
49. return;
50. }
51. if (!isoDep.isConnected()) {
52. hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.isConnected() false.');
53. return;
54. }

56. // 发送指令到已连接的标签，获取标签的响应数据
57. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据
58. try {
59. isoDep.transmit(cmdData).then((response: number[]) => {
60. hilog.info(0x0000, 'testTag', 'readerModeCb isoDep.transmit() response = %{public}s.', JSON.stringify(response));
61. }).catch((err: BusinessError) => {
62. hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() err = %{public}s.', JSON.stringify(err));
63. return;
64. });
65. } catch (businessError) {
66. hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError));
67. return;
68. }
69. } else {
70. hilog.info(0x0000, 'testTag', 'readerModeCb readerModeCb error %{public}s', JSON.stringify(error));
71. }
72. }

74. export default class EntryAbility extends UIAbility {
75. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
76. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

78. // 判断设备是否支持NFC能力
79. if (!canIUse("SystemCapability.Communication.NFC.Core")) {
80. hilog.error(0x0000, 'testTag', 'nfc unavailable.');
81. return;
82. }

84. // 根据应用程序信息，初始化正确的值
85. nfcTagElementName = {
86. bundleName: want.bundleName ?? '',
87. abilityName: want.abilityName ?? '',
88. moduleName: want.moduleName,
89. }
90. }

92. onForeground() {
93. // 应用进入前台，调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能
94. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
95. if (nfcTagElementName != undefined) {
96. // 根据业务需要，选择需要读取标签的通信技术
97. let techList: number[] = [tag.NFC_A, tag.NFC_B, tag.NFC_F, tag.NFC_V];
98. try {
99. tag.on('readerMode', nfcTagElementName, techList, readerModeCb);
100. foregroundRegister = true;
101. } catch (error) {
102. hilog.error(0x0000, 'testTag', 'on readerMode error = %{public}s', JSON.stringify(error));
103. }
104. }
105. }

107. onBackground() {
108. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
109. // 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能
110. if (foregroundRegister) {
111. foregroundRegister = false;
112. try {
113. tag.off('readerMode', nfcTagElementName);
114. } catch (error) {
115. hilog.error(0x0000, 'testTag', 'off readerMode error = %{public}s', JSON.stringify(error));
116. }
117. }
118. }
119. }
```

### 后台读取标签

1. 在module.json5文件中声明NFC标签读取的权限，声明NFC标签特定的action，以及声明本应用程序的能够处理的NFC标签技术类型。
2. import需要的tag模块和其他相关的模块。
3. 获取特定技术类型的NFC标签对象。
4. 执行读写接口完成标签数据的读取或写入数据到标签。

应用程序需要支持后台读卡时，需要在应用的属性配置文件中，声明与NFC相关的属性值。比如，在module.json5文件中，声明下面属性值。

说明

1. 声明"actions"字段的内容填写，必须包含"ohos.nfc.tag.action.TAG\_FOUND"，不能更改。
2. 声明技术时"uris"中"type"字段的内容填写，前缀必须是"tag-tech/"，后面接着NfcA/NfcB/NfcF/NfcV/IsoDep/Ndef/MifareClassic/MifareUL/NdefFormatable"中的一个。如果存在多个"type"时，需要分行填写。填写错误会造成解析失败。
3. 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC\_TAG"，不能更改。
4. Wearable设备不支持后台读卡。

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

19. // actions必须包含"ohos.nfc.tag.action.TAG_FOUND"
20. "ohos.nfc.tag.action.TAG_FOUND"
21. ],

23. // 根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述
24. "uris": [
25. {
26. "type":"tag-tech/NfcA"
27. },
28. {
29. "type":"tag-tech/IsoDep"
30. }
31. // 必要时可添加其他技术类型
32. // 例如: NfcB/NfcF/NfcV/Ndef/MifareClassic/MifareUL/NdefFormatable
33. ]
34. }
35. ]
36. }
37. ],
38. "requestPermissions": [
39. {
40. // 添加NFC标签操作的权限
41. "name": "ohos.permission.NFC_TAG",
42. "reason": "$string:app_name",
43. }
44. ]
```

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

10. // 获取特定技术类型的NFC标签对象
11. let tagInfo: tag.TagInfo;
12. try {
13. tagInfo = tag.getTagInfo(want);
14. } catch (error) {
15. hilog.error(0x0000, 'testTag', 'getTagInfo error = %{public}s', JSON.stringify(error));
16. return;
17. }

19. if (tagInfo == null) {
20. hilog.error(0x0000, 'testTag', 'tagInfo is invalid');
21. return;
22. }
23. if (tagInfo.uid == null) {
24. hilog.error(0x0000, 'testTag', 'uid is invalid');
25. return;
26. }
27. if (tagInfo.technology == null || tagInfo.technology.length == 0) {
28. hilog.error(0x0000, 'testTag', 'technology is invalid');
29. return;
30. }

32. // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入
33. // 下面示例代码，使用IsoDep完成标签数据的读取或写入
34. let isoDep: tag.IsoDepTag | null = null;
35. for (let i = 0; i < tagInfo.technology.length; i++) {
36. if (tagInfo.technology[i] == tag.ISO_DEP) {
37. try {
38. isoDep = tag.getIsoDep(tagInfo);
39. } catch (error) {
40. hilog.error(0x0000, 'testTag', 'getIsoDep error = %{public}s', JSON.stringify(error));
41. return;
42. }
43. }
44. // 也可以按需选择其它类型的技术读写标签
45. }
46. if (isoDep == null) {
47. hilog.error(0x0000, 'testTag', 'getIsoDep is invalid');
48. return;
49. }

51. // 使用IsoDep技术连接到NFC标签
52. try {
53. isoDep.connect();
54. } catch (error) {
55. hilog.error(0x0000, 'testTag', 'isoDep.connect() error = %{public}s', JSON.stringify(error));
56. return;
57. }
58. if (!isoDep.isConnected()) {
59. hilog.error(0x0000, 'testTag', 'isoDep.isConnected() false.');
60. return;
61. }

63. // 发送指令到已连接的标签，获取标签的响应数据
64. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据
65. try {
66. isoDep.transmit(cmdData).then((response: number[]) => {
67. hilog.info(0x0000, 'testTag', 'isoDep.transmit() response = %{public}s.', JSON.stringify(response));
68. }).catch((err: BusinessError) => {
69. hilog.error(0x0000, 'testTag', 'isoDep.transmit() err = %{public}s.', JSON.stringify(err));
70. return;
71. });
72. } catch (businessError) {
73. hilog.error(0x0000, 'testTag', 'isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError));
74. return;
75. }
76. }
77. }
```
