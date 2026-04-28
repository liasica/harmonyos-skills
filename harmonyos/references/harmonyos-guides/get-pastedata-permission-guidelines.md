---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines
title: 申请访问剪贴板权限
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 剪贴板服务 > 申请访问剪贴板权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0e22df4bf5145fa1194b3c7211c7667ab6d4c5995e67f21745d495c366b9cf1
---

## 概述

API version 12及之后，系统为提升用户隐私安全保护能力，剪贴板读取接口增加权限管控。

涉及接口如下：

| 名称 | 说明 |
| --- | --- |
| [getData(callback: AsyncCallback<PasteData>): void](../harmonyos-references/js-apis-pasteboard.md#getdata9) | 读取系统剪贴板内容，使用callback异步回调。 |
| [getData(): Promise<PasteData>](../harmonyos-references/js-apis-pasteboard.md#getdata9-1) | 读取系统剪贴板内容，使用Promise异步回调。 |
| [getDataSync(): PasteData](../harmonyos-references/js-apis-pasteboard.md#getdatasync11) | 读取系统剪贴板内容, 此接口为同步接口。 |
| [getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>](../harmonyos-references/js-apis-pasteboard.md#getunifieddata12) | 从系统剪贴板中读取统一数据对象的数据。 |
| [getUnifiedDataSync(): unifiedDataChannel.UnifiedData](../harmonyos-references/js-apis-pasteboard.md#getunifieddatasync12) | 从系统剪贴板中读取统一数据对象的数据，此接口为同步接口。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetData (OH\_Pasteboard \*pasteboard, int \*status)](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getdata) | 获取剪贴板中的数据。 |
| [getDataWithProgress(params: GetDataParams): Promise<PasteData>](../harmonyos-references/js-apis-pasteboard.md#getdatawithprogress15) | 获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params, int\* status)](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getdatawithprogress) | 获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。 |

说明

申请访问剪贴板权限前，需提前判断剪贴板上的内容是否包含应用所需数据，包括不限于hasData检查是否有数据、hasDataType/getMimeTypes检查是否有应用所需类型、getChangeCount检查数据是否改变，详见[剪贴板弹窗适配优化](get-pastedata-permission-guidelines.md#剪贴板弹窗适配优化)。

## 访问剪贴板内容

剪贴板为应用提供如下两种访问内容的方式。

* 使用安全控件

  [使用粘贴控件](pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

  已经使用了安全控件的应用无需做任何适配就可以访问剪贴板内容。
* 申请ohos.permission.READ\_PASTEBOARD权限

  ohos.permission.READ\_PASTEBOARD是受限的user\_grant（用户授权）权限，使用自定义控件的应用申请此权限后，在用户授权场景下可访问剪贴板内容。

  权限申请步骤：

1. 查看[READ\_PASTEBOARD](restricted-permissions.md#ohospermissionread_pasteboard)介绍，审视应用是否符合申请该权限的使用场景。
2. [在AGC侧申请Profile文件](../app/agc-help-add-releaseprofile-0000001914714796.md)，将用于后续的应用签名信息配置。
3. 在module.json5配置文件中[声明权限](declare-permissions.md)。
4. 通过弹窗向[用户申请权限](request-user-authorization.md)。

## 剪贴板弹窗适配优化

应用申请剪贴板权限需要提前判断剪贴板上的内容是否包含所需数据，避免出现无效弹框。

* 使用[hasData](../harmonyos-references/js-apis-pasteboard.md#hasdata9)判断剪贴板是否有数据，无数据则不访问剪贴板。
* 使用[hasDataType](../harmonyos-references/js-apis-pasteboard.md#hasdatatype11)/[getMimeTypes](../harmonyos-references/js-apis-pasteboard.md#getmimetypes14)判断是否包含应用当前场景支持处理的数据类型，如果没有对应的数据类型，则不访问剪贴板。
* 使用[getChangeCount](../harmonyos-references/js-apis-pasteboard.md#getchangecount18)获取剪贴板的内容变化次数，与上次读取剪贴板时查询的变化次数比较是否一致，一致则剪贴板内容无变化，不访问剪贴板。
* 使用[detectPatterns](../harmonyos-references/js-apis-pasteboard.md#detectpatterns13)判断是否包含应用自身口令的格式，如果格式不匹配，则不访问剪贴板。应用读取口令后如果确认是自身的口令，建议使用[clearData](../harmonyos-references/js-apis-pasteboard.md#cleardata9)清除剪贴板口令内容。

## 示例代码

```
1. import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
2. import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
3. import { preferences } from '@kit.ArkData';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const permissions: Permissions[] = ['ohos.permission.READ_PASTEBOARD'];
7. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
8. const patterns: pasteboard.Pattern[] = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];
9. let dataPreferences: preferences.Preferences | null = null;
10. // ...
11. async function isNeedGetPermissionFromUser(): Promise<boolean> {
12. try {
13. let hasData: boolean = await systemPasteboard.hasData();
14. if (!hasData) {
15. // 剪贴板不存在数据，无需申请权限
16. return false;
17. }
18. // 获取剪贴板的内容变化次数
19. let result: number = systemPasteboard.getChangeCount();
20. hilog.info(0xFF00, '[Sample_pasteboard]', 'Succeeded in getting the ChangeCount. Result: ${result}');
21. // 从 Preferences 中读取上次保存的 changeCount
22. let storedChangeCount: number = dataPreferences ? Number(dataPreferences.getSync('pasteboardChangeCount', 0)) : 0;
23. if (result === storedChangeCount) {
24. // 剪贴板无数据变化，无需申请权限
25. return false;
26. }
27. } catch (err) {
28. hilog.error(0xFF00, '[Sample_pasteboard]', 'Failed to get the ChangeCount. Cause: ${err.message}');
29. return false;
30. };

32. // 查询剪贴板是否存在应用所需数据类型
33. try {
34. // (可选)判断是否有应用需要的数据类型
35. let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
36. hilog.info(0xFF00, '[Sample_pasteboard]', 'Succeeded in checking the DataType. Result: ${result}');
37. if (!result) {
38. // 剪贴板不存在应用所需数据类型，无需申请权限
39. return false;
40. }
41. // (可选)涉及口令等应用自身特殊复制内容的，使用detectPatterns过滤口令格式
42. let data: pasteboard.Pattern[] = await systemPasteboard.detectPatterns(patterns);
43. if (patterns.sort().join('') != data.sort().join('')) {
44. hilog.info(0xFF00, '[Sample_pasteboard]', 'Not all needed patterns detected, no need to get data.');
45. return false;
46. }
47. } catch (err) {
48. hilog.error(0xFF00, '[Sample_pasteboard]', 'Failed to check the DataType. Cause:' + err.message);
49. return false;
50. };
51. return true;
52. }

54. @Entry
55. @Component
56. struct Index {
57. // ...

59. build() {
60. Row() {
61. Column() {
62. // ...
63. Button('粘贴')
64. // ...
65. .onClick(() => {
66. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
67. if (!isNeedGetPermissionFromUser()) {
68. hilog.info(0xFF00, '[Sample_pasteboard]', 'No need to bring up the permission pop-up window');
69. return;
70. }
71. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
72. // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
73. atManager.requestPermissionsFromUser(context, permissions).then((data) => {
74. let grantStatus: number[] = data.authResults;
75. for (const status of grantStatus) {
76. if (status === 0) {
77. // 用户授权，使用get操作读取剪贴板内容。
78. // ...
79. // 执行判断口令逻辑，如果是本应用口令，建议获取完数据后使用cleardata清除剪贴板口令内容
80. systemPasteboard.clearData().then((data: void) => {
81. hilog.info(0xFF00, '[Sample_pasteboard]', 'Succeeded in clearing the pasteboard.');
82. }).catch((err: BusinessError) => {
83. hilog.error(0xFF00, '[Sample_pasteboard]', 'Failed to clear the pasteboard. Cause: ${err.message}');
84. });
85. // 获取当前 ChangeCount
86. let currentChangeCount: number = systemPasteboard.getChangeCount();
87. hilog.info(0xFF00, '[Sample_pasteboard]', 'Current ChangeCount: ' + currentChangeCount);
88. // 更新 Preferences 中的 ChangeCount
89. if (dataPreferences) {
90. dataPreferences.putSync('pasteboardChangeCount', currentChangeCount);
91. dataPreferences.flushSync(); // 确保数据写入持久化存储
92. hilog.info(0xFF00, '[Sample_pasteboard]', 'ChangeCount has been updated to: ' + currentChangeCount);
93. }
94. } else {
95. // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限。
96. return;
97. }
98. }
99. // 授权成功。
100. }).catch((err: BusinessError) => {
101. hilog.error(0xFF00, '[Sample_pasteboard]', 'Failed to request permissions from user. ');
102. })
103. })
104. // ...
105. }
106. // ...
107. }
108. // ...
109. }
110. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/pasteboard/pasteboard_arkts_sample/entry/src/main/ets/pages/Index.ets#L17-L183)
