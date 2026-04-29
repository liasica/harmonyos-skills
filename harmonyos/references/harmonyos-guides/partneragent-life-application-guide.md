---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/partneragent-life-application-guide
title: 伙伴设备与HarmonyOS设备互通的开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 融合短距 > 伙伴设备与HarmonyOS设备互通的开发指南
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:35+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3a0ad16ed45b0b98bf8847bbc8e912361a7a623f16f6280dbbbd21ceebf2b018
---

## 简介

伙伴设备需要与HarmonyOS设备互通，比如以下主要场景：

* 媒体控制：手表显示HarmonyOS设备当前播放的音乐、视频；手表或耳机等伙伴设备可以控制HarmonyOS设备媒体播放（上/下一首、播放暂停等）。
* 电话反控：HarmonyOS设备来电通知手表，手表显示来电号码，联系人名称；手表或耳机等伙伴设备可以接听、拒接HarmonyOS设备来电。
* 健康监测：穿戴设备实时采集人体数据上报给HarmonyOS设备；HarmonyOS设备可实时浏览健康检测数据。

这些场景需要保证伙伴设备长时间与HarmonyOS设备保持互通，当存在数据交互比如媒体控制、电话控制、人体健康等数据时，应用需要保证活动。本指南主要提供了应用进程保持可唤醒状态解决方案，保证伙伴设备需要的伙伴设备厂商应用在数据交互时可被唤醒并正常运行。

## 关键流程

1. 伙伴设备应用需要先实现[PartnerAgentExtensionAbility](../harmonyos-references/is-fusionconnectivity-partneragentextensionability.md)，里面实现应用被系统唤醒后需要实现的数据传输业务操作。
2. 伙伴设备触发和伙伴设备的[蓝牙配对](br-pair-device-development-guide.md)操作，再调用 **bindDevice** 接口注册伙伴设备。PartnerAgent服务感知到伙伴设备注册后，才会调用蓝牙服务接口进行[BLE](terminology.md#ble)扫描和监听蓝牙连接状态去发现伙伴设备，进而拉起伙伴设备[ExtensionAbility](../harmonyos-references/is-fusionconnectivity-partneragentextensionability.md)。若伙伴设备未注册，PartnerAgent服务不会拉起伙伴设备Extension。
3. 该注册信息会持久化存储，HarmonyOS设备重启后依旧生效。
4. 伙伴设备应用不需要使用该设备后，可调用 **unbindDevice** 接口解注册设备。

## 约束与限制

为了降低PartnerAgentExtensionAbility能力被三方应用滥用的风险，现通过基础访问模式的功能约束对应用进行安全管控。

说明

严格遵从基础访问模式的功能约束。在此模式下，开发者应仅提供伙伴设备业务通知功能。系统会逐步增加基础访问模式的安全管控能力，包括但不限于：不允许申请长短时任务、不允许调用相机、不允许使用录音、不允许使用媒体、不允许使用定位、不允许使用联系人&通话、不允许使用WIFI、不允许使用NFC。因此未遵从此约定可能会导致功能异常。

## 开发步骤

### 创建文件目录层级

开发者在实现一个伙伴设备生命周期管理应用时，需要在DevEco Studio工程中新建一个PartnerAgentExtensionAbility，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，并命名为entryability。
2. 在entryability目录下，右键选择“New > File”，新建两个文件，分别为EntryAbility.ets、PartnerAgentAbility.ets。目录如下：

   ```
   1. /src/main/
   2. ├── ets/entryability
   3. │       └──EntryAbility.ets               # 显示按钮交互界面
   4. │       └──PartnerAgentAbility.ets        # 自定义类继承PartnerAgentExtensionAbility并加上需要的生命周期回调
   5. │   ├───pages
   6. │       └── Index.ets                     # 绘制按钮交互页面，注册/解注册设备功能
   7. ├── resources/base/profile/main_pages.json
   ```

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### PartnerAgentExtensionAbility实现

应用需要实现[PartnerAgentExtensionAbility](../harmonyos-references/is-fusionconnectivity-partneragentextensionability.md)，本模块会在HarmonyOS设备BLE扫描到或连上**已注册**的伙伴设备时被拉起，HarmonyOS设备和已注册伙伴设备断开蓝牙连接后，本模块会延迟3分钟销毁伙伴设备Extension进程。它通过提供以下函数运行保持应用可唤醒。

* **onDeviceDiscovered(deviceAddress: PartnerDeviceAddress)**

  已注册设备[ACL](terminology.md#acl)连接成功或BLE扫描发现时触发该回调，开发者可以在此进行一些数据传输业务操作，如蓝牙[SPP连接](spp-development-guide.md)、设备发现信息打印等。
* **onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason)**

  当不再使用服务且准备将该实例销毁时，触发该回调，回调中通知销毁该实例原因，开发者可以在该回调中清理资源，如解绑设备、设备丢失信息打印等。

  ```
  1. import { partnerAgent } from '@kit.ConnectivityKit';
  2. import { PartnerAgentExtensionAbility } from '@kit.ConnectivityKit';

  4. export default class PartnerAgentAbility extends PartnerAgentExtensionAbility {
  5. onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
  6. console.info(`[testTag] onDeviceDiscovered success: ${deviceAddress.bluetoothAddress?.address} ${deviceAddress.bluetoothAddress?.addressType}`);
  7. }

  9. onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
  10. console.info(`[testTag] onDestroyWithReason is: ${reason}`);
  11. }
  12. }
  ```

### 注册设备流程

调用[bindDevice](../harmonyos-references/js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)接口注册设备，注册过的设备才会触发伙伴设备Extension拉起流程。

* 注册前需要调用接口[isDeviceControlEnabled](../harmonyos-references/js-apis-fusionconnectivity-partneragent.md#partneragentisdevicecontrolenabled)判断当前设备的互通功能是否打开。
* 该设备在注册前需要保证与本机蓝牙处于配对状态。
* 拉起Ability的name为工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册PartnerAgentExtensionAbility，type标签设置为“partnerAgent”的ability的name。需与应用模块级配置文件[module.json5](module-configuration-file.md) 中的[extensionabilities](module-configuration-file.md#extensionabilities标签) name属性值相同。

```
1. // 注册的设备地址信息
2. let btAddr: common.BluetoothAddress = {
3. "address": 'XX:XX:XX:XX:XX:XX',
4. "addressType": common.BluetoothAddressType.VIRTUAL,
5. };
6. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
7. "bluetoothAddress": btAddr,
8. };

10. // 判断当前设备的互通功能是否已经打开
11. let isEnabled = partnerAgent.isDeviceControlEnabled(deviceAddress);
12. console.info(`[testTag] device ${btAddr.address} is enabled: ${isEnabled}`);

14. // 注册设备支持的能力
15. let capability: partnerAgent.DeviceCapability = {
16. "supportBR": true,
17. "supportBleAdvertiser": true,
18. };
19. // 应用注册设备的业务功能，包括媒体控制、通话控制。
20. let businessCap: partnerAgent.BusinessCapability = {
21. "supportMediaControl": true,
22. "supportTelephonyControl": false,
23. };
24. if (isEnabled == false) {
25. // PartnerAgentAbility为设备发现时拉起的ability的name
26. partnerAgent.bindDevice(deviceAddress, capability, businessCap, "PartnerAgentAbility")
27. .then(() => {
28. console.info(`[testTag] bind device success:  ${btAddr.address}`);
29. })
30. .catch((err: BusinessError) => {
31. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
32. });
33. }
```

### 解注册设备流程

当伙伴设备应用不再需要被系统保持可唤醒状态，调用应用解注册设备接口[unbindDevice](../harmonyos-references/js-apis-fusionconnectivity-partneragent.md#partneragentunbinddevice)

* 解注册前需要调用接口建议调用[isDeviceBound](../harmonyos-references/js-apis-fusionconnectivity-partneragent.md#partneragentisdevicebound)接口判断设备注册状态，已注册设备再进行解注册。
* 解注册后，应用的PartnerAgentExtensionAbility进程将不再接收此设备的发现和下线状态通知。

```
1. // 获取应用当前注册过的所有设备
2. let devices: partnerAgent.PartnerDeviceAddress[] = partnerAgent.getBoundDevices();
3. for (let i = 0; i < devices.length; i++) {
4. let addr = devices[i].bluetoothAddress;
5. if (addr) {
6. console.info(`[testTag] bound device (addr: ${addr.address}, addressType: ${addr.addressType},
7. rawAddressType: ${addr.rawAddressType})`);
8. }
9. }

11. let btAddr: common.BluetoothAddress = {
12. "address": 'XX:XX:XX:XX:XX:XX',
13. "addressType": common.BluetoothAddressType.VIRTUAL,
14. };
15. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
16. "bluetoothAddress": btAddr,
17. };

19. // 判断当前应用是否已注册过该设备
20. let isBound = partnerAgent.isDeviceBound(deviceAddress);
21. console.info(`[testTag] device ${btAddr.address} is bound: ${isBound}`);

23. if (isBound == true) {
24. partnerAgent.unbindDevice(deviceAddress)
25. .then(() => {
26. console.info(`[testTag] unbindDevice device success:  ${btAddr.address}`);
27. })
28. .catch((err: BusinessError) => {
29. console.error(`[testTag] errCode: ${err.code}, errMessage: ${err.message}`);
30. });
31. }
```

* 具体工程搭建可参考本章节[完整示例](partneragent-life-application-guide.md#完整示例)。

## 完整示例

1. PartnerAgentAbility.ets文件。

   在PartnerAgentAbility.ets文件中，增加导入PartnerAgentExtensionAbility的依赖包，自定义类继承PartnerAgentExtensionAbility并加上需要的生命周期回调。

   ```
   1. import { partnerAgent } from '@kit.ConnectivityKit';
   2. import { PartnerAgentExtensionAbility } from '@kit.ConnectivityKit';

   4. export default class PartnerAgentAbility extends PartnerAgentExtensionAbility {
   5. onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
   6. console.info(`[testTag] onDeviceDiscovered success: ${deviceAddress.bluetoothAddress?.address} ${deviceAddress.bluetoothAddress?.addressType}`);
   7. }

   9. onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
   10. console.info(`[testTag] onDestroyWithReason is: ${reason}`);
   11. }
   12. }
   ```
2. EntryAbility.ets文件。

   EntryAbility中加载ets/pages/Index.ets绘制的页面，请求用户授予访问蓝牙权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/iCp4enuATgCFuNAQ7siwQQ/zh-cn_image_0000002589324789.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053234Z&HW-CC-Expire=86400&HW-CC-Sign=D4BA53B0A95F074C27CB1ABC6DE2DFE5DC673FB467115224DC033DDB9ADA6A62)

   ```
   1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { window } from '@kit.ArkUI';

   5. const DOMAIN = 0x0000;

   7. export default class EntryAbility extends UIAbility {
   8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   9. try {
   10. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   11. } catch (err) {
   12. hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
   13. }
   14. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   15. }

   17. onDestroy(): void {
   18. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
   19. }

   21. onWindowStageCreate(windowStage: window.WindowStage): void {
   22. // Main window is created, set main page for this ability
   23. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   25. windowStage.loadContent('pages/Index', (err) => {
   26. if (err.code) {
   27. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
   28. return;
   29. }
   30. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   31. });
   32. }

   34. onWindowStageDestroy(): void {
   35. // Main window is destroyed, release UI related resources
   36. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
   37. }

   39. onForeground(): void {
   40. // Ability has brought to foreground
   41. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
   42. }

   44. onBackground(): void {
   45. // Ability has back to background
   46. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
   47. }
   48. }
   ```
3. Index.ets文件。

   调用注册设备等功能接口。Index.ets中输入要注册的设备蓝牙地址，注册输入的蓝牙设备，去注册输入的蓝牙设备、查询设备的绑定状态，获取本机绑定的设备列表等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Oh0uQlwWQWuKIyGcZC2s3A/zh-cn_image_0000002589244727.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053234Z&HW-CC-Expire=86400&HW-CC-Sign=803DF762CCBD26FC4255D8F1D020486FBFAC4607BA4E8A8EFA6E1373D00AB50E)

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import common from '@ohos.bluetooth.common';
   3. import partnerAgent from '@ohos.FusionConnectivity.partnerAgent';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State perBtAddress: string = '';

   10. build() {
   11. Column() {
   12. Text("@ohos.BtDataWithExtension")
   13. .fontSize(20)
   14. .margin({ bottom: 16 })
   15. .fontWeight(FontWeight.Bold)
   16. TextInput({ placeholder: '请输入要绑定的设备地址', text: this.perBtAddress })
   17. .margin(1)
   18. .width('90%')
   19. .height(50)
   20. .type(InputType.Normal)
   21. .onChange((value: string) => {
   22. this.perBtAddress = value;
   23. })
   24. Row() {
   25. Button("bindDevice").width(300).margin(5).onClick(() => {
   26. console.info("[testTag] bindDevice");
   27. let btAddr: common.BluetoothAddress = {
   28. "address": this.perBtAddress,
   29. "addressType": common.BluetoothAddressType.VIRTUAL,
   30. };
   31. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
   32. "bluetoothAddress": btAddr,
   33. };
   34. let capability: partnerAgent.DeviceCapability = {
   35. "supportBR": true,
   36. "supportBleAdvertiser": true,
   37. };
   38. let businessCap: partnerAgent.BusinessCapability = {
   39. "supportMediaControl": true,
   40. "supportTelephonyControl": false,
   41. };
   42. partnerAgent.bindDevice(deviceAddress, capability, businessCap, "PartnerAgentAbility")
   43. .then(() => {
   44. console.info(`[testTag] bind device success:  ${btAddr.address}`);
   45. })
   46. .catch((err: BusinessError) => {
   47. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
   48. });
   49. })
   50. }

   52. Row() {
   53. Button("unbindDevice").width(300).margin(5).onClick(() => {
   54. console.info("[testTag] unbindDevice");
   55. let btAddr: common.BluetoothAddress = {
   56. "address": this.perBtAddress,
   57. "addressType": common.BluetoothAddressType.VIRTUAL,
   58. };
   59. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
   60. "bluetoothAddress": btAddr,
   61. };
   62. partnerAgent.unbindDevice(deviceAddress)
   63. .then(() => {
   64. console.info(`[testTag] unbindDevice device success:  ${btAddr.address}`);
   65. })
   66. .catch((err: BusinessError) => {
   67. console.error(`[testTag] errCode: ${err.code}, errMessage: ${err.message}`);
   68. });
   69. })
   70. }

   72. Row() {
   73. Button("isDeviceControlEnabled").width(300).margin(5).onClick(() => {
   74. console.info("[testTag] isEnable");
   75. try {
   76. let btAddr: common.BluetoothAddress = {
   77. "address": this.perBtAddress,
   78. "addressType": common.BluetoothAddressType.VIRTUAL,
   79. };
   80. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
   81. "bluetoothAddress": btAddr,
   82. };
   83. let isEnabled = partnerAgent.isDeviceControlEnabled(deviceAddress);
   84. console.info(`[testTag] device ${btAddr.address} is enabled: ${isEnabled}`);
   85. } catch (err) {
   86. console.error(`[testTag] errCode: ${err.code}, errMessage: ${err.message}`);
   87. }
   88. })
   89. }
   90. Row() {
   91. Button("isDeviceBound").width(300).margin(5).onClick(() => {
   92. console.info("[testTag] isBound");
   93. try {
   94. let btAddr: common.BluetoothAddress = {
   95. "address": this.perBtAddress,
   96. "addressType": common.BluetoothAddressType.VIRTUAL,
   97. };
   98. let deviceAddress: partnerAgent.PartnerDeviceAddress = {
   99. "bluetoothAddress": btAddr,
   100. };
   101. let isBound = partnerAgent.isDeviceBound(deviceAddress);
   102. console.info(`[testTag] device ${btAddr.address} is bound: ${isBound}`);
   103. } catch (err) {
   104. console.error(`[testTag] errCode: ${err.code}, errMessage: ${err.message}`);
   105. }
   106. })
   107. }
   108. Row() {
   109. Button("getBoundDevices").width(300).margin(5).onClick(() => {
   110. console.info("[testTag] Get bound devices");
   111. try {
   112. let devices: partnerAgent.PartnerDeviceAddress[] = partnerAgent.getBoundDevices();
   113. for (let i = 0; i < devices.length; i++) {
   114. let btAddr = devices[i].bluetoothAddress;
   115. if (btAddr) {
   116. console.info(`[testTag] bound device (addr: ${btAddr.address}, addressType: ${btAddr.addressType},
   117. rawAddressType: ${btAddr.rawAddressType})`);
   118. }
   119. }
   120. } catch (err) {
   121. console.error(`[testTag] errCode: ${err.code}, errMessage: ${err.message}`);
   122. }
   123. })
   124. }
   125. }
   126. }
   127. }
   ```
4. main\_pages.json文件。对应ets/pages/路径下伙伴设备管理功能按钮的绘制页面。

   ```
   1. {
   2. "src": [
   3. "pages/Index"
   4. ]
   5. }
   ```
5. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册PartnerAgentExtensionAbility，type标签需要设置为“partnerAgent”，srcEntry标签表示当前PartnerAgentExtensionAbility组件所对应的代码路径。

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "PartnerAgentAbility",
   4. "srcEntry": "./ets/entryability/PartnerAgentAbility.ets",
   5. "description": "service",
   6. "icon": "$media:layered_image",
   7. "type": "partnerAgent",
   8. "exported": true
   9. }
   10. ],
   11. "requestPermissions": [
   12. {
   13. "name": "ohos.permission.ACCESS_BLUETOOTH",
   14. "reason": "$string:module_desc",
   15. "usedScene": {
   16. "abilities": [
   17. "EntryFormAbility"
   18. ],
   19. "when": "inuse"
   20. }
   21. }
   22. ]
   ```
