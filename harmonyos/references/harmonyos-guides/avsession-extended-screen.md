---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-extended-screen
title: 扩展屏投播开发指导
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用投播组件 > 扩展屏投播开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c25d81018392a0319056d143012ea77b8661e045f15741cd004ae7fce0f685b3
---

通过本节开发指导，可在系统镜像投屏后，获取投屏设备信息，实现扩展屏模式的投播，实现双屏协作的能力。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/OdmTrOWQRGe99OQ-hhfXlA/zh-cn_image_0000002583478555.png?HW-CC-KV=V1&HW-CC-Date=20260427T234551Z&HW-CC-Expire=86400&HW-CC-Sign=2087E0A7DED6B100F68B976496F1066174EA1F796D4622872E011EA6D1D28868)

* **虚拟扩展屏**

  是在系统投屏启动过程中建立的，依据双端协商的投屏视频流的分辨率创建，支持1080P 及以上分辨率。默认镜像主屏内容，当虚拟扩展屏上有UIAbility绘制时，会投屏该屏内容。
* **UIAbility A（本机内容）**

  在本端主屏上显示的内容。假定UIAbility A 与 UIAbility B 属于同一应用，UIAbility A可以控制UIAbility B，实现双屏联动。
* **UIAbility B（投屏内容）**

  在虚拟扩展屏上绘制的内容，考虑到远端投屏用户体验，UIAbility B 应铺满全屏。从安全角度考虑，在启动UIAbility B 时，系统会校验主屏前台UIAbility是否归属同一应用，如果校验失败会禁止其在虚拟扩展屏启动。

## 约束与限制

需同时满足以下条件方可使用该功能：

* **设备限制**

  本端设备：HarmonyOS NEXT Developer Beta1及以上版本的手机设备。

  远端设备：支持Cast+或Miracast标准协议的设备，推荐使用华为智慧屏HarmonyOS2.0及以上版本。
* **使用限制**

  需要系统发起无线/有线投屏后才可通过接口获取有效的扩展投屏设备。

## 接口说明

在开发具体功能前，请先查阅参考文档，获取详细的接口说明。

| 接口 | 说明 |
| --- | --- |
| getAllCastDisplays(): Promise<Array<CastDisplayInfo>>; | 获取当前系统中所有支持扩展屏投播的显示设备。 |
| on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void; | 设置扩展屏投播显示设备变化的监听事件。 |
| off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void; | 取消扩展屏投播显示设备变化事件监听，关闭后，不再进行该事件回调。 |

## 开发步骤

1. UIAbility A创建AVSession, 获取可用扩展屏投播设备并注册监听。

   说明

   获取的屏幕信息CastDisplayInfo中包含屏幕ID，屏幕名称、状态以及分辨率宽度、高度基础属性，其中屏幕id 值同于[Display](../harmonyos-references/js-apis-display.md#display)的id，如需要获取更详细的信息可参考[Display获取设备信息说明](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import  { avSession }  from '@kit.AVSessionKit'; // 导入AVSession模块
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. export default class AbilityA extends UIAbility{
   6. private session: avSession.AVSession | undefined = undefined;
   7. private extCastDisplayInfo: avSession.CastDisplayInfo | undefined = undefined;
   8. // 注册监听可投屏设备变化事件
   9. private onCastDisplayChangedCallback = (castDisplayInfo: avSession.CastDisplayInfo) => {
   10. // 新增扩展屏,进入扩展屏显示
   11. if (this.extCastDisplayInfo === undefined && castDisplayInfo.state === avSession.CastDisplayState.STATE_ON) {
   12. console.info('Succeeded in opening the cast display');
   13. this.extCastDisplayInfo = castDisplayInfo;
   14. this.startExternalDisplay();
   15. } else if (this.extCastDisplayInfo?.id == castDisplayInfo.id) {
   16. this.extCastDisplayInfo = castDisplayInfo;
   17. // 扩展屏不可用，退出扩展屏显示
   18. if (castDisplayInfo.state === avSession.CastDisplayState.STATE_OFF){
   19. console.info('Succeeded in closing the cast display');
   20. this.stopExternalDisplay();
   21. this.extCastDisplayInfo = undefined;
   22. }
   23. }
   24. };

   26. // 创建AVSession, 获取可用扩展屏投播设备并注册监听
   27. initAVSession(context: Context) {
   28. avSession.createAVSession(context, 'CastDisplay', 'video').then((session: avSession.AVSession) => {
   29. this.session = session;
   30. this.session?.on('castDisplayChange', this.onCastDisplayChangedCallback);

   32. // 获取当前系统可用的扩展屏显示设备
   33. session.getAllCastDisplays().then((infoArr: avSession.CastDisplayInfo[]) => {
   34. // 有多个扩展屏时可以提供用户选择，也可使用其中任一个作为扩展屏使用。
   35. if (infoArr.length > 0) {
   36. this.extCastDisplayInfo = infoArr[0];
   37. this.startExternalDisplay();
   38. }
   39. }).catch((err: BusinessError<void>) => {
   40. console.error(`Failed to get all CastDisplay. Code: ${err.code}, message: ${err.message}`);
   41. });
   42. });
   43. }

   45. async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
   46. super.onCreate(want, launchParam);
   47. this.initAVSession(this.context);
   48. }

   50. onDestroy() {
   51. this.stopExternalDisplay();
   52. // 去注册监听
   53. this.session?.off('castDisplayChange');
   54. }
   55. }
   ```
2. 在UIAbilityA中构建扩展屏启动和退出能力。

   ```
   1. // 扩展屏启动UIAbilityB
   2. startExternalDisplay() {
   3. if (this.extCastDisplayInfo !== undefined &&
   4. this.extCastDisplayInfo.id !== 0 &&
   5. this.extCastDisplayInfo.state === avSession.CastDisplayState.STATE_ON) {
   6. let id = this.extCastDisplayInfo?.id;
   7. console.info(`Succeeded in starting ability and the id of display is ${id}`);
   8. this.context.startAbility({
   9. bundleName: 'com.example.myapplication', // 应用自有包名
   10. abilityName: 'AbilityB'
   11. }, {
   12. displayId: id // 扩展屏ID
   13. });
   14. AppStorage.setOrCreate('CastDisplayState', 1);
   15. }
   16. }

   18. // 停止使用扩展屏
   19. stopExternalDisplay() {
   20. AppStorage.setOrCreate('CastDisplayState', 0);
   21. // 更新本页面显示。
   22. }
   ```
3. UIAbilityB扩展屏显示内容绘制，需响应退出处理。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. export default class AbilityB extends UIAbility {
   6. onWindowStageCreate(windowStage: window.WindowStage): void {
   7. // Main window is created, set main page for this ability
   8. windowStage.getMainWindowSync().setWindowLayoutFullScreen(true); // 设置为全屏
   9. windowStage.loadContent('pages/CastPage', (err: BusinessError) => {
   10. if (err.code) {
   11. console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
   12. return;
   13. }
   14. console.info('Succeeded in loading the content. ');
   15. });
   16. }
   17. }
   ```

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { common } from '@kit.AbilityKit';

   4. @Entry
   5. @Component
   6. struct CastPage {
   7. // 监测到CastDisplayState变化后，当设备断开时，销毁本页内容。
   8. @StorageLink('CastDisplayState') @Watch('onDestroyExtend') private displayState: number = 1;

   10. private onDestroyExtend() {
   11. if (this.displayState === 1) return;
   12. let context = (getContext(this) as common.UIAbilityContext)
   13. context.terminateSelf().then(() => {
   14. console.info('CastPage finished');
   15. }).catch((err: BusinessError) => {
   16. console.error(`Failed to destroying CastPage. Code: ${err.code}, message: ${err.message}`);
   17. });
   18. }
   19. //...
   20. }
   ```
