---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-customscan
title: 自定义界面扫码
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 自定义界面扫码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0144a4e190098c3d36913128f3d8b4e20c051e9a517460fc846d680e9949d05c
---

## 基本概念

自定义界面扫码能力提供了相机流控制接口，可根据自身需求自定义扫码界面，适用于对扫码界面有定制化需求的应用开发。

说明

通过自定义界面扫码可以实现应用内的扫码功能，为了获得更好的应用体验，推荐同时[接入“扫码直达”服务](scan-directservice.md)，应用可以同时支持系统扫码入口（控制中心扫一扫）和应用内扫码两种方式跳转到指定服务页面。

## 场景介绍

自定义界面扫码能力提供扫码相机流控制接口，支持相机流的初始化、开启、暂停、释放、重新扫码功能；支持闪光灯的状态获取、开启、关闭；支持变焦比的获取和设置；支持设置相机焦点和连续自动对焦；支持对条形码、二维码、MULTIFUNCTIONAL CODE进行扫码识别（具体类型参见[ScanType](../harmonyos-references/scan-scancore.md#scantype)），并获得码类型、码值、码位置、相机预览流（YUV）等信息。该能力可用于单码和多码的扫描识别。

开发者集成自定义界面扫码能力可以自行定义扫码的界面样式，请按照业务流程完成扫码接口调用实现实时扫码功能。建议开发者基于[Sample Code](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)做个性化修改。

扫码页面UX设计规范：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/to3tTqiwTWy3a6S8yoGdlw/zh-cn_image_0000002583478613.png?HW-CC-KV=V1&HW-CC-Date=20260427T234640Z&HW-CC-Expire=86400&HW-CC-Sign=E3EF574A0384CACAF320081A368032579549A0E0DD8D9106CA36675B8A2E0A8E)

说明

YUV（相机预览流图像数据）适合于扫码和识物的综合识别场景，开发者需要自己控制相机流，普通扫码场景无需关注。

## 约束与限制

* 从6.1.0(23)版本开始，自定义界面扫码能力支持带后置相机的Wearable，可以通过[cameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。
* 需要请求相机的使用权限。
* 需要开发者自行实现扫码的人机交互界面。例如：多码场景需要暂停相机流由用户选择一个码图进行识别。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/r_497SwRSi-TpgX0aCMYkg/zh-cn_image_0000002552798964.png?HW-CC-KV=V1&HW-CC-Date=20260427T234640Z&HW-CC-Expire=86400&HW-CC-Sign=B71C5B54C8BC379FB8C81BDBB6ECD66CB66AF839DD083375CDFA8F1DD3310B37)

1. **发起请求：** 用户向开发者的应用发起扫码请求，应用拉起已定义好的扫码界面。
2. **申请授权：** 应用需要向用户申请相机权限授权。若未同意授权，则无法使用此功能。
3. **启动自定义界面扫码：** 在扫码前必须调用init接口初始化自定义界面扫码，加载资源。相机流初始化结束后，调用start接口开始扫码。
4. **自定义界面扫码相机操作：** 可以配置自定义界面扫码相机操作参数，调整相应功能，包括闪光灯、变焦、焦距、暂停、重启扫码等。例如：

   * 根据当前码图位置，比如当前码图太远或太近时，调用getZoom获取变焦比，setZoom接口设置变焦比，调整焦距以便于用户扫码。
   * 根据当前扫码的光线条件或根据on('lightingFlash')监听闪光灯开启或关闭时机，通过getFlashLightStatus接口先获取闪光灯状态，再调用openFlashLight/closeFlashLight接口控制闪光灯开启或关闭，以便于用户进行扫码。
   * 调用setFocusPoint设置对焦位置，resetFocus恢复默认对焦模式，以便于用户进行扫码。
   * 在应用处于前后台或其他特殊场景需要中断/重新进行扫码时，可调用stop或start接口来控制相机流达到暂停或重新扫码的目的。
5. **自定义界面扫码：** Scan Kit API在扫码完成后会返回扫码结果。同时根据开发者的需要，Scan Kit API会返回每帧相机预览流数据。如需不重启相机并重新触发一次扫码，可以在start接口的Callback异步回调中，调用rescan接口。完成扫码后，需调用release接口进行释放扫码资源的操作。
6. **获取结果：** 解析码值结果跳转应用服务页。

## 接口说明

自定义界面扫码提供init、start、stop、release、getFlashLightStatus、openFlashLight、closeFlashLight、setZoom、getZoom、setFocusPoint、resetFocus、rescan、on('lightingFlash')、off('lightingFlash')接口，其中部分接口返回值有两种返回形式：Callback和Promise回调。Callback和Promise回调函数只是返回值方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/scan-customscan-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/scan-customscan-api.md#customscaninit)(options?: scanBarcode.[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)): void | 初始化自定义界面扫码，加载资源。无返回结果。 |
| [start](../harmonyos-references/scan-customscan-api.md#customscanstart)(viewControl: [ViewControl](../harmonyos-references/scan-customscan-api.md#viewcontrol)): Promise<Array<scanBarcode.[ScanResult](../harmonyos-references/scan-scanbarcode-api.md#scanresult)>> | 启动扫码相机流获取扫码结果。使用Promise异步回调。 |
| [stop](../harmonyos-references/scan-customscan-api.md#customscanstop)(): Promise<void> | 暂停扫码相机流。使用Promise异步回调。 |
| [release](../harmonyos-references/scan-customscan-api.md#customscanrelease)(): Promise<void> | 释放扫码相机流。使用Promise异步回调。 |
| [start](../harmonyos-references/scan-customscan-api.md#customscanstart-1)(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<[ScanFrame](../harmonyos-references/scan-customscan-api.md#scanframe)>): void | 启动扫码相机流获取扫码结果以及YUV图像数据。使用callback异步回调。 |
| [getFlashLightStatus](../harmonyos-references/scan-customscan-api.md#customscangetflashlightstatus)(): boolean | 获取闪光灯状态。返回结果为布尔值，true为打开状态，false为关闭状态。 |
| [openFlashLight](../harmonyos-references/scan-customscan-api.md#customscanopenflashlight)(): void | 开启闪光灯。无返回结果。 |
| [closeFlashLight](../harmonyos-references/scan-customscan-api.md#customscancloseflashlight)(): void | 关闭闪光灯。无返回结果。 |
| [setZoom](../harmonyos-references/scan-customscan-api.md#customscansetzoom)(zoomValue : number): void | 设置变焦比。无返回结果。 |
| [getZoom](../harmonyos-references/scan-customscan-api.md#customscangetzoom)(): number | 获取当前的变焦比。 |
| [setFocusPoint](../harmonyos-references/scan-customscan-api.md#customscansetfocuspoint)(point: scanBarcode.[Point](../harmonyos-references/scan-scanbarcode-api.md#point)): void | 设置相机焦点。 |
| [resetFocus](../harmonyos-references/scan-customscan-api.md#customscanresetfocus)(): void | 设置连续自动对焦模式。 |
| [rescan](../harmonyos-references/scan-customscan-api.md#customscanrescan)(): void | 触发一次重新扫码。仅对start接口Callback异步回调有效，Promise异步回调无效。 |
| [stop](../harmonyos-references/scan-customscan-api.md#customscanstop-1)(callback: AsyncCallback<void>): void | 暂停扫码相机流。使用callback异步回调。 |
| [release](../harmonyos-references/scan-customscan-api.md#customscanrelease-1)(callback: AsyncCallback<void>): void | 释放扫码相机流。使用callback异步回调。 |
| [on](../harmonyos-references/scan-customscan-api.md#customscanonlightingflash)(type: 'lightingFlash', callback: AsyncCallback<boolean>): void | 订阅闪光灯状态监听事件，当环境暗、亮状态变化时返回闪光灯开启或关闭时机。使用callback异步回调。 |
| [off](../harmonyos-references/scan-customscan-api.md#customscanofflightingflash)(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void | 注销闪光灯状态监听事件。使用callback异步回调。 |

## 开发步骤

自定义界面扫码接口支持自定义UI界面，识别相机流中的条形码，二维码以及MULTIFUNCTIONAL CODE，并返回码类型、码值、码位置（码图最小外接矩形左上角和右下角的坐标）、相机预览流（YUV）等信息。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

以下示例为调用自定义界面扫码接口拉起相机流并返回扫码结果和相机预览流（YUV）。

1. 在开发应用前，需要先申请相机相关权限，确保应用拥有访问相机的权限。在module.json5文件中配置相机权限，具体配置方式，请参见[声明权限](declare-permissions.md)。

   | 权限名 | 说明 | 授权方式 |
   | --- | --- | --- |
   | ohos.permission.CAMERA | 允许应用使用相机扫码。 | user\_grant |
2. 使用接口[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)请求用户授权。具体申请方式及校验方式，请参见[向用户申请授权](request-user-authorization.md)。
3. 导入自定义界面扫码接口以及相关接口模块，导入方法如下。

   ```
   1. import { scanCore, scanBarcode, customScan } from '@kit.ScanKit';
   2. // 导入功能涉及的权限申请、回调接口
   3. import { display } from '@kit.ArkUI';
   4. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   ```
4. 遵循[业务流程](scan-customscan.md#业务流程)完成自定义界面扫码功能。

   说明

   1. 在设置start接口的viewControl参数时，width和height与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的宽高值相同，start接口会根据XComponent的宽高比例从相机的分辨率选择最优分辨率，如果比例与相机的分辨率比例相差过大会影响预览流体验。

      当前支持的分辨率比例为16:9、4:3、1:1。竖屏场景下，XComponent的高度需要大于宽度，且高宽比在支持的分辨率比例中。横屏场景下，XComponent的宽度需要大于高度，且宽高比在支持的分辨率比例中。
   2. XComponent的宽高需根据使用场景计算适配。例如：在开发设备为折叠屏时，需按照折叠屏的展开态和折叠态分别计算XComponent的宽高，start接口会根据XComponent的宽高适配对应的相机分辨率。设备屏幕宽高可通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取（获取的为px单位，需要通过[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)方法转为vp）。

   * 通过Promise方式回调，调用自定义界面扫码接口拉起相机流并返回扫码结果。

     ```
     1. const TAG: string = '[customScanPage]';

     3. @Entry
     4. @Component
     5. struct CustomScanPage {
     6. @State userGrant: boolean = false // 是否已申请相机权限
     7. @State surfaceId: string = '' // XComponent组件生成id
     8. @State isShowBack: boolean = false // 是否已经返回扫码结果
     9. @State isFlashLightEnable: boolean = false // 是否开启了闪光灯
     10. @State isSensorLight: boolean = false // 记录当前环境亮暗状态
     11. @State cameraHeight: number = 640 // 设置预览流高度，默认单位：vp
     12. @State cameraWidth: number = 360 // 设置预览流宽度，默认单位：vp
     13. @State offsetX: number = 0 // 设置预览流x轴方向偏移量，默认单位：vp
     14. @State offsetY: number = 0 // 设置预览流y轴方向偏移量，默认单位：vp
     15. @State zoomValue: number = 1 // 预览流缩放比例
     16. @State setZoomValue: number = 1 // 已设置的预览流缩放比例
     17. @State scaleValue: number = 1 // 屏幕缩放比
     18. @State pinchValue: number = 1 // 双指缩放比例
     19. @State displayHeight: number = 0 // 屏幕高度，单位vp
     20. @State displayWidth: number = 0 // 屏幕宽度，单位vp
     21. @State scanResult: Array<scanBarcode.ScanResult> = [] // 扫码结果
     22. private mXComponentController: XComponentController = new XComponentController()

     24. async onPageShow() {
     25. // 自定义启动第一步，用户申请权限
     26. await this.requestCameraPermission();
     27. // 多码扫码识别，enableMultiMode: true 单码扫码识别enableMultiMode: false
     28. let options: scanBarcode.ScanOptions = {
     29. scanTypes: [scanCore.ScanType.ALL],
     30. enableMultiMode: true,
     31. enableAlbum: true
     32. }
     33. // 自定义启动第二步：设置预览流布局尺寸
     34. this.setDisplay();
     35. try {
     36. // 自定义启动第三步，初始化接口
     37. customScan.init(options);
     38. } catch (err) {
     39. hilog.error(0x0001, TAG, `Failed to init customScan. Code: ${err.code}, message: ${err.message}`);
     40. }
     41. }

     43. onPageHide() {
     44. // 页面消失或隐藏时，停止并释放相机流
     45. this.userGrant = false;
     46. this.isFlashLightEnable = false;
     47. this.isSensorLight = false;
     48. try {
     49. customScan.off('lightingFlash');
     50. } catch (err) {
     51. hilog.error(0x0001, TAG, `Failed to off lightingFlash. Code: ${err.code}, message: ${err.message}`);
     52. }
     53. this.customScanStop();
     54. try {
     55. // 自定义相机流释放接口
     56. customScan.release().catch((err: BusinessError) => {
     57. hilog.error(0x0001, TAG,
     58. `Failed to release customScan by promise. Code: ${err.code}, message: ${err.message}`);
     59. })
     60. } catch (err) {
     61. hilog.error(0x0001, TAG, `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
     62. }
     63. }

     65. // 用户申请权限
     66. async reqPermissionsFromUser(): Promise<number[]> {
     67. hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
     68. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     69. let atManager = abilityAccessCtrl.createAtManager();
     70. try {
     71. const grantStatus: PermissionRequestResult =
     72. await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);
     73. return grantStatus.authResults;
     74. } catch (err) {
     75. hilog.error(0x0001, TAG, `Failed to requestPermissionsFromUser. Code: ${err.code}, message: ${err.message}`);
     76. return [];
     77. }
     78. }

     80. // 用户申请相机权限
     81. async requestCameraPermission() {
     82. let grantStatus = await this.reqPermissionsFromUser();
     83. for (let i = 0; i < grantStatus.length; i++) {
     84. if (grantStatus[i] === 0) {
     85. // 用户授权，可以继续访问目标操作
     86. hilog.info(0x0001, TAG, 'Succeeded in getting permissions.');
     87. this.userGrant = true;
     88. break;
     89. }
     90. }
     91. }

     93. // 竖屏时获取屏幕尺寸，设置预览流全屏示例
     94. setDisplay() {
     95. try {
     96. // 默认竖屏
     97. let displayClass = display.getDefaultDisplaySync();
     98. this.displayHeight = this.getUIContext().px2vp(displayClass.height);
     99. this.displayWidth = this.getUIContext().px2vp(displayClass.width);
     100. let maxLen: number = Math.max(this.displayWidth, this.displayHeight);
     101. let minLen: number = Math.min(this.displayWidth, this.displayHeight);
     102. const RATIO: number = 16 / 9;
     103. this.cameraHeight = maxLen;
     104. this.cameraWidth = maxLen / RATIO;
     105. this.offsetX = (minLen - this.cameraWidth) / 2;
     106. } catch (err) {
     107. hilog.error(0x0001, TAG, `Failed to getDefaultDisplaySync. Code: ${err.code}, message: ${err.message}`);
     108. }
     109. }

     111. // toast显示扫码结果
     112. showScanResult(data: scanBarcode.ScanResult) {
     113. try {
     114. // 使用toast显示出扫码结果
     115. this.getUIContext().getPromptAction().showToast({
     116. message: JSON.stringify(data),
     117. duration: 5000
     118. });
     119. } catch (err) {
     120. hilog.error(0x0001, TAG, `Failed to showToast. Code: ${err.code}, message: ${err.message}`);
     121. }
     122. }

     124. initCamera() {
     125. this.isShowBack = false;
     126. this.scanResult = [];
     127. let viewControl: customScan.ViewControl = {
     128. width: this.cameraWidth,
     129. height: this.cameraHeight,
     130. surfaceId: this.surfaceId
     131. };
     132. try {
     133. // 自定义启动第四步，请求扫码接口，通过Promise方式回调
     134. customScan.start(viewControl)
     135. .then((data: Array<scanBarcode.ScanResult>) => {
     136. hilog.info(0x0001, TAG, `result: ${JSON.stringify(data)}`);
     137. if (data.length) {
     138. // 解析码值结果跳转应用服务页
     139. this.scanResult = data;
     140. this.isShowBack = true;
     141. // 获取到扫描结果后暂停相机流
     142. this.customScanStop();
     143. }
     144. }).catch((err: BusinessError) => {
     145. hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
     146. });
     147. } catch (err) {
     148. hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
     149. }
     150. }

     152. customScanStop() {
     153. try {
     154. customScan.stop().catch((err: BusinessError) => {
     155. hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
     156. })
     157. } catch (err) {
     158. hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
     159. }
     160. }

     162. // 自定义扫码界面的顶部返回按钮和扫码提示
     163. @Builder
     164. TopTool() {
     165. Column() {
     166. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
     167. Text('返回')
     168. .onClick(() => {
     169. this.getUIContext().getRouter().back();
     170. })
     171. }.padding({ left: 24, right: 24, top: 40 })

     174. Column() {
     175. Text('扫描二维码/条形码')
     176. Text('对准二维码/条形码，即可自动扫描')
     177. }.margin({ left: 24, right: 24, top: 24 })
     178. }
     179. .height(146)
     180. .width('100%')
     181. }

     183. build() {
     184. Stack() {
     185. if (this.userGrant) {
     186. Column() {
     187. XComponent({
     188. id: 'componentId',
     189. type: XComponentType.SURFACE,
     190. controller: this.mXComponentController
     191. })
     192. .onLoad(() => {
     193. hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
     194. // 获取XComponent组件的surfaceId
     195. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
     196. hilog.info(0x0001, TAG, `Succeeded in getting surfaceId: ${this.surfaceId}`);
     197. this.initCamera();
     198. // 闪光灯监听接口
     199. customScan.on('lightingFlash', (err, isLightingFlash) => {
     200. if (err) {
     201. hilog.error(0x0001, TAG,
     202. `Failed to on lightingFlash. Code: ${err.code}, message: ${err.message}`);
     203. return;
     204. }
     205. if (isLightingFlash) {
     206. this.isFlashLightEnable = true;
     207. } else {
     208. try {
     209. if (!customScan.getFlashLightStatus()) {
     210. this.isFlashLightEnable = false;
     211. }
     212. } catch (err) {
     213. hilog.error(0x0001, TAG,
     214. `Failed to get flashLightStatus. Code: ${err.code}, message: ${err.message}`);
     215. }
     216. }
     217. this.isSensorLight = isLightingFlash;
     218. });
     219. })
     220. .width(this.cameraWidth)
     221. .height(this.cameraHeight)
     222. .position({ x: this.offsetX, y: this.offsetY })
     223. }
     224. .height('100%')
     225. .width('100%')
     226. }

     229. Column() {
     230. this.TopTool()
     231. Column() {
     232. }
     233. .layoutWeight(1)
     234. .width('100%')

     237. Column() {
     238. Row() {
     239. // 闪光灯按钮，启动相机流后才能使用
     240. Button('FlashLight')
     241. .onClick(() => {
     242. let lightStatus: boolean = false;
     243. try {
     244. lightStatus = customScan.getFlashLightStatus();
     245. } catch (err) {
     246. hilog.error(0x0001, TAG,
     247. `Failed to get flashLightStatus. Code: ${err.code}, message: ${err.message}`);
     248. }

     251. // 根据当前闪光灯状态，选择打开或关闭闪光灯
     252. if (lightStatus) {
     253. try {
     254. customScan.closeFlashLight();
     255. setTimeout(() => {
     256. this.isFlashLightEnable = this.isSensorLight;
     257. }, 200);
     258. } catch (err) {
     259. hilog.error(0x0001, TAG,
     260. `Failed to close flashLight. Code: ${err.code}, message: ${err.message}`);
     261. }
     262. } else {
     263. try {
     264. customScan.openFlashLight();
     265. } catch (err) {
     266. hilog.error(0x0001, TAG,
     267. `Failed to open flashLight. Code: ${err.code}, message: ${err.message}`);
     268. }
     269. }
     270. })
     271. .visibility((this.userGrant && this.isFlashLightEnable) ? Visibility.Visible : Visibility.None)

     274. // 扫码成功后，点击按钮后重新扫码
     275. Button('Scan')
     276. .onClick(() => {
     277. // 点击按钮重启相机流，重新扫码
     278. this.initCamera();
     279. })
     280. .visibility(this.isShowBack ? Visibility.Visible : Visibility.None)
     281. }

     284. Row() {
     285. // 预览流设置缩放比例
     286. Button('缩放比例,当前比例:' + this.setZoomValue)
     287. .onClick(() => {
     288. // 设置相机缩放比例
     289. if (!this.isShowBack) {
     290. if (!this.zoomValue || this.zoomValue === this.setZoomValue) {
     291. this.setZoomValue = this.customGetZoom();
     292. } else {
     293. this.zoomValue = this.zoomValue;
     294. this.customSetZoom(this.zoomValue);
     295. setTimeout(() => {
     296. if (!this.isShowBack) {
     297. this.setZoomValue = this.customGetZoom();
     298. }
     299. }, 1000);
     300. }
     301. }
     302. })
     303. }
     304. .margin({ top: 10, bottom: 10 })

     307. Row() {
     308. // 输入要设置的预览流缩放比例
     309. TextInput({ placeholder: '输入缩放倍数' })
     310. .type(InputType.Number)
     311. .borderWidth(1)
     312. .backgroundColor(Color.White)
     313. .onChange(value => {
     314. this.zoomValue = Number(value);
     315. })
     316. }
     317. }
     318. .width('50%')
     319. .height(180)
     320. }

     323. // 单码、多码扫描后，显示码图蓝点位置。点击toast码图信息
     324. ForEach(this.scanResult, (item: scanBarcode.ScanResult) => {
     325. if (item.scanCodeRect) {
     326. Image($rawfile('scan_selected2.svg')) // src/main/resources/rawfile/scan_selected2.svg
     327. .width(40)
     328. .height(40)
     329. .markAnchor({ x: 20, y: 20 })
     330. .position({
     331. x: (item.scanCodeRect.left + item?.scanCodeRect?.right) / 2 + this.offsetX,
     332. y: (item.scanCodeRect.top + item?.scanCodeRect?.bottom) / 2 + this.offsetY
     333. })
     334. .onClick(() => {
     335. this.showScanResult(item);
     336. })
     337. }
     338. }, (item: scanBarcode.ScanResult) => '' + item?.scanCodeRect?.left + item?.scanCodeRect?.right + 'px')
     339. }
     340. // 建议相机流设置为全屏
     341. .width('100%')
     342. .height('100%')
     343. .onClick((event: ClickEvent) => {
     344. // 是否已扫描到结果
     345. if (this.isShowBack) {
     346. return;
     347. }
     348. // 点击屏幕位置，获取点击位置(x,y)，设置相机焦点
     349. let x1 = event.displayY / (this.displayHeight + 0.0);
     350. let y1 = 1.0 - event.displayX / (this.displayWidth + 0.0);
     351. try {
     352. customScan.setFocusPoint({ x: x1, y: y1 });
     353. hilog.info(0x0001, TAG, `Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}`);
     354. } catch (err) {
     355. hilog.error(0x0001, TAG, `Failed to set focusPoint. Code: ${err.code}, message: ${err.message}`);
     356. }
     357. hilog.info(0x0001, TAG, `Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}`);
     358. // 设置连续自动对焦模式
     359. setTimeout(() => {
     360. try {
     361. customScan.resetFocus();
     362. } catch (err) {
     363. hilog.error(0x0001, TAG, `Failed to reset focus. Code: ${err.code}, message: ${err.message}`);
     364. }
     365. }, 200);
     366. }).gesture(PinchGesture({ fingers: 2 })
     367. .onActionStart(() => {
     368. hilog.info(0x0001, TAG, 'Pinch start');
     369. })
     370. .onActionUpdate((event: GestureEvent) => {
     371. if (event) {
     372. this.scaleValue = event.scale;
     373. }
     374. })
     375. .onActionEnd(() => {
     376. // 是否已扫描到结果
     377. if (this.isShowBack) {
     378. return;
     379. }
     380. // 获取双指缩放比例，设置变焦比
     381. try {
     382. let zoom = this.customGetZoom();
     383. this.pinchValue = this.scaleValue * zoom;
     384. this.customSetZoom(this.pinchValue);
     385. hilog.info(0x0001, TAG, 'Pinch end');
     386. } catch (err) {
     387. hilog.error(0x0001, TAG, `Failed to set zoom. Code: ${err.code}, message: ${err.message}`);
     388. }
     389. }))
     390. }

     392. public customGetZoom(): number {
     393. let zoom = 1;
     394. try {
     395. zoom = customScan.getZoom();
     396. hilog.info(0x0001, TAG, `Succeeded in getting zoom, zoom: ${zoom}`);
     397. } catch (err) {
     398. hilog.error(0x0001, TAG, `Failed to get zoom. Code: ${err.code}, message: ${err?.message}`);
     399. }
     400. return zoom;
     401. }

     403. public customSetZoom(pinchValue: number): void {
     404. try {
     405. customScan.setZoom(pinchValue);
     406. hilog.info(0x0001, TAG, `Succeeded in setting zoom.`);
     407. } catch (err) {
     408. hilog.error(0x0001, TAG, `Failed to set zoom. Code: ${err.code}, message: ${err?.message}`);
     409. }
     410. }
     411. }
     ```
   * 通过Callback方式回调，调用自定义界面扫码接口拉起相机流并返回扫码结果和相机预览流（YUV）。

     ```
     1. const TAG: string = '[customScanPage]';

     3. @Entry
     4. @Component
     5. struct CustomScanPage {
     6. @State userGrant: boolean = false // 是否已申请相机权限
     7. @State surfaceId: string = '' // XComponent组件生成id
     8. @State isShowBack: boolean = false // 是否已经返回扫码结果
     9. @State isFlashLightEnable: boolean = false // 是否开启了闪光灯
     10. @State isSensorLight: boolean = false // 记录当前环境亮暗状态
     11. @State cameraHeight: number = 640 // 设置预览流高度，默认单位：vp
     12. @State cameraWidth: number = 360 // 设置预览流宽度，默认单位：vp
     13. @State offsetX: number = 0 // 设置预览流x轴方向偏移量，默认单位：vp
     14. @State offsetY: number = 0 // 设置预览流y轴方向偏移量，默认单位：vp
     15. @State zoomValue: number = 1 // 预览流缩放比例
     16. @State setZoomValue: number = 1 // 已设置的预览流缩放比例
     17. @State scaleValue: number = 1 // 屏幕缩放比
     18. @State pinchValue: number = 1 // 双指缩放比例
     19. @State displayHeight: number = 0 // 屏幕高度，单位vp
     20. @State displayWidth: number = 0 // 屏幕宽度，单位vp
     21. @State scanResult: Array<scanBarcode.ScanResult> = [] // 扫码结果
     22. private mXComponentController: XComponentController = new XComponentController()
     23. // 返回自定义扫描结果的回调
     24. private callback: AsyncCallback<scanBarcode.ScanResult[]> =
     25. (err: BusinessError, data: scanBarcode.ScanResult[]) => {
     26. if (err && err.code) {
     27. hilog.error(0x0001, TAG,
     28. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
     29. return;
     30. }
     31. // 解析码值结果跳转应用服务页
     32. hilog.info(0x0001, TAG, `Succeeded in getting ScanResult by callback, result: ${JSON.stringify(data)}`);
     33. if (data.length) {
     34. // 解析码值结果跳转应用服务页
     35. this.scanResult = data;
     36. this.isShowBack = true;
     37. // 获取到扫描结果后暂停相机流
     38. this.customScanStop();
     39. }
     40. }
     41. // 返回相机帧的回调
     42. private frameCallback: AsyncCallback<customScan.ScanFrame> =
     43. (err: BusinessError, frameResult: customScan.ScanFrame) => {
     44. if (err) {
     45. hilog.error(0x0001, TAG, `Failed to get ScanFrame by callback. Code: ${err.code}, message: ${err.message}`);
     46. return;
     47. }
     48. // byteBuffer相机YUV图像数组
     49. hilog.info(0x0001, TAG,
     50. `Succeeded in getting ScanFrame.byteBuffer.byteLength: ${frameResult.byteBuffer.byteLength}`)
     51. hilog.info(0x0001, TAG, `Succeeded in getting ScanFrame.width: ${frameResult.width}`)
     52. hilog.info(0x0001, TAG, `Succeeded in getting ScanFrame.height: ${frameResult.height}`)
     53. }

     55. async onPageShow() {
     56. // 自定义启动第一步，用户申请权限
     57. await this.requestCameraPermission();
     58. // 多码扫码识别，enableMultiMode: true 单码扫码识别enableMultiMode: false
     59. let options: scanBarcode.ScanOptions = {
     60. scanTypes: [scanCore.ScanType.ALL],
     61. enableMultiMode: true,
     62. enableAlbum: true
     63. }
     64. // 自定义启动第二步：设置预览流布局尺寸
     65. this.setDisplay();
     66. try {
     67. // 自定义启动第三步，初始化接口
     68. customScan.init(options);
     69. } catch (err) {
     70. hilog.error(0x0001, TAG, `Failed to init customScan. Code: ${err.code}, message: ${err.message}`);
     71. }
     72. }

     74. onPageHide() {
     75. // 页面消失或隐藏时，停止并释放相机流
     76. this.userGrant = false;
     77. this.isFlashLightEnable = false;
     78. this.isSensorLight = false;
     79. try {
     80. customScan.off('lightingFlash');
     81. } catch (err) {
     82. hilog.error(0x0001, TAG, `Failed to off lightingFlash. Code: ${err.code}, message: ${err.message}`);
     83. }
     84. this.customScanStop();
     85. try {
     86. // 自定义相机流释放接口
     87. customScan.release().catch((err: BusinessError) => {
     88. hilog.error(0x0001, TAG,
     89. `Failed to release customScan by promise. Code: ${err.code}, message: ${err.message}`);
     90. })
     91. } catch (err) {
     92. hilog.error(0x0001, TAG, `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
     93. }
     94. }

     96. // 用户申请权限
     97. async reqPermissionsFromUser(): Promise<number[]> {
     98. hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
     99. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     100. let atManager = abilityAccessCtrl.createAtManager();
     101. try {
     102. const grantStatus: PermissionRequestResult =
     103. await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);
     104. return grantStatus.authResults;
     105. } catch (err) {
     106. hilog.error(0x0001, TAG, `Failed to requestPermissionsFromUser. Code: ${err.code}, message: ${err.message}`);
     107. return [];
     108. }
     109. }

     111. // 用户申请相机权限
     112. async requestCameraPermission() {
     113. let grantStatus = await this.reqPermissionsFromUser();
     114. for (let i = 0; i < grantStatus.length; i++) {
     115. if (grantStatus[i] === 0) {
     116. // 用户授权，可以继续访问目标操作
     117. hilog.info(0x0001, TAG, 'Succeeded in getting permissions.');
     118. this.userGrant = true;
     119. break;
     120. }
     121. }
     122. }

     124. // 竖屏时获取屏幕尺寸，设置预览流全屏示例
     125. setDisplay() {
     126. try {
     127. // 默认竖屏
     128. let displayClass = display.getDefaultDisplaySync();
     129. this.displayHeight = this.getUIContext().px2vp(displayClass.height);
     130. this.displayWidth = this.getUIContext().px2vp(displayClass.width);
     131. let maxLen: number = Math.max(this.displayWidth, this.displayHeight);
     132. let minLen: number = Math.min(this.displayWidth, this.displayHeight);
     133. const RATIO: number = 16 / 9;
     134. this.cameraHeight = maxLen;
     135. this.cameraWidth = maxLen / RATIO;
     136. this.offsetX = (minLen - this.cameraWidth) / 2;
     137. } catch (err) {
     138. hilog.error(0x0001, TAG, `Failed to getDefaultDisplaySync. Code: ${err.code}, message: ${err.message}`);
     139. }
     140. }

     142. // toast显示扫码结果
     143. showScanResult(data: scanBarcode.ScanResult) {
     144. try {
     145. // 使用toast显示出扫码结果
     146. this.getUIContext().getPromptAction().showToast({
     147. message: JSON.stringify(data),
     148. duration: 5000
     149. });
     150. } catch (err) {
     151. hilog.error(0x0001, TAG, `Failed to showToast. Code: ${err.code}, message: ${err.message}`);
     152. }
     153. }

     155. // 初始化相机流
     156. initCamera() {
     157. this.isShowBack = false;
     158. this.scanResult = [];
     159. let viewControl: customScan.ViewControl = {
     160. width: this.cameraWidth,
     161. height: this.cameraHeight,
     162. surfaceId: this.surfaceId
     163. };
     164. try {
     165. // 自定义启动第四步，请求扫码接口，通过callback方式回调
     166. customScan.start(viewControl, this.callback, this.frameCallback);
     167. } catch (err) {
     168. hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
     169. }

     171. }

     173. // 暂停相机流
     174. customScanStop() {
     175. try {
     176. customScan.stop().catch((err: BusinessError) => {
     177. hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
     178. })
     179. } catch (err) {
     180. hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
     181. }
     182. }

     184. // 自定义扫码界面的顶部返回按钮和扫码提示
     185. @Builder
     186. TopTool() {
     187. Column() {
     188. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
     189. Text('返回')
     190. .onClick(() => {
     191. this.getUIContext().getRouter().back();
     192. })
     193. }.padding({ left: 24, right: 24, top: 40 })

     196. Column() {
     197. Text('扫描二维码/条形码')
     198. Text('对准二维码/条形码，即可自动扫描')
     199. }.margin({ left: 24, right: 24, top: 24 })
     200. }
     201. .height(146)
     202. .width('100%')
     203. }

     205. build() {
     206. Stack() {
     207. if (this.userGrant) {
     208. Column() {
     209. XComponent({
     210. id: 'componentId',
     211. type: XComponentType.SURFACE,
     212. controller: this.mXComponentController
     213. })
     214. .onLoad(() => {
     215. hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
     216. // 获取XComponent组件的surfaceId
     217. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
     218. hilog.info(0x0001, TAG, `Succeeded in getting surfaceId: ${this.surfaceId}`);
     219. this.initCamera();
     220. // 闪光灯监听接口
     221. customScan.on('lightingFlash', (err, isLightingFlash) => {
     222. if (err) {
     223. hilog.error(0x0001, TAG,
     224. `Failed to on lightingFlash. Code: ${err.code}, message: ${err.message}`);
     225. return;
     226. }
     227. if (isLightingFlash) {
     228. this.isFlashLightEnable = true;
     229. } else {
     230. try {
     231. if (!customScan.getFlashLightStatus()) {
     232. this.isFlashLightEnable = false;
     233. }
     234. } catch (err) {
     235. hilog.error(0x0001, TAG,
     236. `Failed to get flashLightStatus. Code: ${err.code}, message: ${err.message}`);
     237. }
     238. }
     239. this.isSensorLight = isLightingFlash;
     240. });
     241. })
     242. .width(this.cameraWidth)
     243. .height(this.cameraHeight)
     244. .position({ x: this.offsetX, y: this.offsetY })
     245. }
     246. .height('100%')
     247. .width('100%')
     248. }

     251. Column() {
     252. this.TopTool()
     253. Column() {
     254. }
     255. .layoutWeight(1)
     256. .width('100%')

     259. Column() {
     260. Row() {
     261. // 闪光灯按钮，启动相机流后才能使用
     262. Button('FlashLight')
     263. .onClick(() => {
     264. let lightStatus: boolean = false;
     265. try {
     266. lightStatus = customScan.getFlashLightStatus();
     267. } catch (err) {
     268. hilog.error(0x0001, TAG,
     269. `Failed to get flashLightStatus. Code: ${err.code}, message: ${err.message}`);
     270. }

     273. // 根据当前闪光灯状态，选择打开或关闭闪光灯
     274. if (lightStatus) {
     275. try {
     276. customScan.closeFlashLight();
     277. setTimeout(() => {
     278. this.isFlashLightEnable = this.isSensorLight;
     279. }, 200);
     280. } catch (err) {
     281. hilog.error(0x0001, TAG,
     282. `Failed to close flashLight. Code: ${err.code}, message: ${err.message}`);
     283. }
     284. } else {
     285. try {
     286. customScan.openFlashLight();
     287. } catch (err) {
     288. hilog.error(0x0001, TAG,
     289. `Failed to open flashLight. Code: ${err.code}, message: ${err.message}`);
     290. }
     291. }
     292. })
     293. .visibility((this.userGrant && this.isFlashLightEnable) ? Visibility.Visible : Visibility.None)

     296. // 扫码成功后，点击按钮后重新扫码
     297. Button('Scan')
     298. .onClick(() => {
     299. // 点击按钮重启相机流，重新扫码
     300. this.initCamera();
     301. })
     302. .visibility(this.isShowBack ? Visibility.Visible : Visibility.None)
     303. }

     306. Row() {
     307. // 预览流设置缩放比例
     308. Button('缩放比例,当前比例:' + this.setZoomValue)
     309. .onClick(() => {
     310. // 设置相机缩放比例
     311. if (!this.isShowBack) {
     312. if (!this.zoomValue || this.zoomValue === this.setZoomValue) {
     313. this.setZoomValue = this.customGetZoom();
     314. } else {
     315. this.zoomValue = this.zoomValue;
     316. this.customSetZoom(this.zoomValue);
     317. setTimeout(() => {
     318. if (!this.isShowBack) {
     319. this.setZoomValue = this.customGetZoom();
     320. }
     321. }, 1000);
     322. }
     323. }
     324. })
     325. }
     326. .margin({ top: 10, bottom: 10 })

     329. Row() {
     330. // 输入要设置的预览流缩放比例
     331. TextInput({ placeholder: '输入缩放倍数' })
     332. .type(InputType.Number)
     333. .borderWidth(1)
     334. .backgroundColor(Color.White)
     335. .onChange(value => {
     336. this.zoomValue = Number(value);
     337. })
     338. }
     339. }
     340. .width('50%')
     341. .height(180)
     342. }

     345. // 单码、多码扫描后，显示码图蓝点位置。点击toast码图信息
     346. ForEach(this.scanResult, (item: scanBarcode.ScanResult) => {
     347. if (item.scanCodeRect) {
     348. Image($rawfile('scan_selected2.svg')) // src/main/resources/rawfile/scan_selected2.svg
     349. .width(40)
     350. .height(40)
     351. .markAnchor({ x: 20, y: 20 })
     352. .position({
     353. x: (item.scanCodeRect.left + item?.scanCodeRect?.right) / 2 + this.offsetX,
     354. y: (item.scanCodeRect.top + item?.scanCodeRect?.bottom) / 2 + this.offsetY
     355. })
     356. .onClick(() => {
     357. this.showScanResult(item);
     358. })
     359. }
     360. }, (item: scanBarcode.ScanResult) => '' + item?.scanCodeRect?.left + item?.scanCodeRect?.right + 'px')
     361. }
     362. // 建议相机流设置为全屏
     363. .width('100%')
     364. .height('100%')
     365. .onClick((event: ClickEvent) => {
     366. // 是否已扫描到结果
     367. if (this.isShowBack) {
     368. return;
     369. }
     370. // 点击屏幕位置，获取点击位置(x,y)，设置相机焦点
     371. let x1 = event.displayY / (this.displayHeight + 0.0);
     372. let y1 = 1.0 - event.displayX / (this.displayWidth + 0.0);
     373. try {
     374. customScan.setFocusPoint({ x: x1, y: y1 });
     375. hilog.info(0x0001, TAG, `Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}`);
     376. } catch (err) {
     377. hilog.error(0x0001, TAG, `Failed to set focusPoint. Code: ${err.code}, message: ${err.message}`);
     378. }
     379. hilog.info(0x0001, TAG, `Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}`);
     380. // 设置连续自动对焦模式
     381. setTimeout(() => {
     382. try {
     383. customScan.resetFocus();
     384. } catch (err) {
     385. hilog.error(0x0001, TAG, `Failed to reset focus. Code: ${err.code}, message: ${err.message}`);
     386. }
     387. }, 200);
     388. }).gesture(PinchGesture({ fingers: 2 })
     389. .onActionStart(() => {
     390. hilog.info(0x0001, TAG, 'Pinch start');
     391. })
     392. .onActionUpdate((event: GestureEvent) => {
     393. if (event) {
     394. this.scaleValue = event.scale;
     395. }
     396. })
     397. .onActionEnd(() => {
     398. // 是否已扫描到结果
     399. if (this.isShowBack) {
     400. return;
     401. }
     402. // 获取双指缩放比例，设置变焦比
     403. try {
     404. let zoom = this.customGetZoom();
     405. this.pinchValue = this.scaleValue * zoom;
     406. this.customSetZoom(this.pinchValue);
     407. hilog.info(0x0001, TAG, 'Pinch end');
     408. } catch (err) {
     409. hilog.error(0x0001, TAG, `Failed to set zoom. Code: ${err.code}, message: ${err.message}`);
     410. }
     411. }))
     412. }

     414. public customGetZoom(): number {
     415. let zoom = 1;
     416. try {
     417. zoom = customScan.getZoom();
     418. hilog.info(0x0001, TAG, `Succeeded in getting zoom, zoom: ${zoom}`);
     419. } catch (err) {
     420. hilog.error(0x0001, TAG, `Failed to get zoom. Code: ${err.code}, message: ${err?.message}`);
     421. }
     422. return zoom;
     423. }

     425. public customSetZoom(pinchValue: number): void {
     426. try {
     427. customScan.setZoom(pinchValue);
     428. hilog.info(0x0001, TAG, `Succeeded in setting zoom.`);
     429. } catch (err) {
     430. hilog.error(0x0001, TAG, `Failed to set zoom. Code: ${err.code}, message: ${err?.message}`);
     431. }
     432. }
     433. }
     ```
5. 通过scanCodeRect数据可确定码图中心点的位置。

   * 以设备竖屏、充电口向下为例，使用说明如下。

     + scanCodeRect的四个点坐标如下，可根据坐标点绘制码图外围矩形框
       - 左上角(x, y)：(left, top)
       - 右上角(x, y)：(right, top)
       - 左下角(x, y)：(left, bottom)
       - 右下角(x, y)：(right, bottom)
     + 由于码图中心点坐标需和XComponent的坐标保持一致，如果XComponent的x轴和y轴存在偏移，则码图位置需做相应的偏移。例如：x轴偏移量为：offsetX；y轴偏移量为：offsetY，中心点坐标最终转换为：
       - x = (left + right) / 2 + offsetX
       - y = (top + bottom) / 2 + offsetY
   * 如果设备涉及旋转，码图中心点位置需要根据屏幕旋转角度([Display.rotation](../harmonyos-references/js-apis-display.md#属性))进行变换，以保证在各旋转角度下码图中心位置正确。推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)。

     例如：XComponent宽度为width，高度为height，x轴偏移量为offsetX，y轴偏移量为offsetY：

     + 当[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 0时，中心点坐标为：
       - x = (left + right) / 2 + offsetX
       - y = (top + bottom) / 2 + offsetY
     + 当[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 1时，中心点坐标为：
       - x = width - (top + bottom) / 2 + offsetX
       - y = (left + right) / 2 + offsetY
     + 当[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 2时，中心点坐标为：
       - x = width - (left + right) / 2 + offsetX
       - y = height - (top + bottom) / 2 + offsetY
     + 当[Display.rotation](../harmonyos-references/js-apis-display.md#属性) = 3时，中心点坐标为：
       - x = (top + bottom) / 2 + offsetX
       - y = height - (left + right) / 2+ offsetY

   说明

   从5.0.2(14)开始，由于屏幕Display对象rotation和orientation属性变更，设备旋转不同角度后码图的位置需要重新适配。

   * 对于5.0.2(14)之前版本，可以使用Display对象中的rotation或者orientation属性处理设备旋转不同角度后的码图位置，且需要针对设备类型做特殊适配。
   * 对于5.0.2(14)及之后版本，需要统一使用Display对象的rotation属性处理设备旋转不同角度后的码图位置，无需针对设备类型做特殊适配。

## 模拟器开发

部分接口支持模拟器开发，模拟器使用指导请参见[使用模拟器运行应用](ide-run-emulator.md)。

* 从6.0.0(20)版本开始，模拟器支持部分自定义界面扫码接口开发（支持的接口包括[init](../harmonyos-references/scan-customscan-api.md#customscaninit)、[start](../harmonyos-references/scan-customscan-api.md#customscanstart)、[stop](../harmonyos-references/scan-customscan-api.md#customscanstop)、[release](../harmonyos-references/scan-customscan-api.md#customscanrelease)、[rescan](../harmonyos-references/scan-customscan-api.md#customscanrescan)），可实现自定义界面扫码能力的基本功能验证。
* 模拟器自定义界面扫码能力仅支持1280\*720分辨率，开发者传入其他分辨率会统一转换成1280\*720。
