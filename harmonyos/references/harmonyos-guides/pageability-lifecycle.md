---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability-lifecycle
title: PageAbility的生命周期
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > PageAbility的生命周期
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:56+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:05edac7c231188533bc94af26101607fe06df6f3da18fa67fd1a29e8618c4aba
---

## 概述

PageAbility生命周期是PageAbility被调度到INACTIVE、ACTIVE、BACKGROUND等各个状态的统称。PageAbility生命周期流转及状态说明如图1、表1所示。

**图1** PageAbility生命周期流转

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/-N7Jw2AwQ56eWfqJ5wWqCA/zh-cn_image_0000002583437557.png?HW-CC-KV=V1&HW-CC-Date=20260427T233755Z&HW-CC-Expire=86400&HW-CC-Sign=A1AC90E1CD463B063658685268EC5559430D3F4D80601697FA8E15297072C7C3)

**表1** PageAbility生命周期状态说明

| 生命周期状态 | 生命周期状态说明 |
| --- | --- |
| UNINITIALIZED | 未初始状态，为临时状态，PageAbility被创建后会由UNINITIALIZED状态进入INITIAL状态。 |
| INITIAL | 初始化状态，也表示停止状态，表示当前PageAbility未运行，PageAbility被启动后由INITIAL态进入INACTIVE状态。 |
| INACTIVE | 失去焦点状态，表示当前窗口已显示但是无焦点状态。 |
| ACTIVE | 前台激活状态，表示当前窗口已显示，并获取焦点。 |
| BACKGROUND | 后台状态，表示当前PageAbility退到后台，PageAbility在被销毁后由BACKGROUND状态进入INITIAL状态，或者重新被激活后由BACKGROUND状态进入ACTIVE状态。 |

开发者可以在app.js/app.ets中实现生命周期相关回调函数，PageAbility生命周期相关回调函数见下表。

**表2** PageAbility生命周期回调接口说明

| 接口名 | 接口描述 |
| --- | --- |
| onCreate() | Ability第一次启动时调用onCreate方法，开发者可以在该方法里做一些应用初始化工作。 |
| onDestroy() | 应用退出，销毁Ability对象前调用onDestroy方法，开发者可以在该方法里做一些回收资源、清空缓存等应用退出前的准备工作。 |
| onActive() | Ability切换到前台，并且已经获取焦点时调用onActive方法。 |
| onInactive() | Ability失去焦点时调用onInactive方法，Ability在进入后台状态时会先失去焦点，再进入后台。 |
| onShow() | Ability由后台不可见状态切换到前台可见状态调用onShow方法，此时用户在屏幕可以看到该Ability。 |
| onHide() | Ability由前台切换到后台不可见状态时调用onHide方法，此时用户在屏幕看不到该Ability。 |
| onSaveData() | 当系统需要回收页面内存或页面配置变更时调用，用于保存页面的临时状态数据。 |
| onRestoreData() | 当页面从回收状态恢复时调用，用于恢复之前保存的页面状态数据。 |

PageAbility生命周期回调与生命周期状态的关系如下图所示。

**图2** PageAbility生命周期回调与生命周期状态的关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/TwoXZmHuQX-kdlPUZLv7gQ/zh-cn_image_0000002552957512.png?HW-CC-KV=V1&HW-CC-Date=20260427T233755Z&HW-CC-Expire=86400&HW-CC-Sign=0ABA90399B6514CE85EEDB237E7DF4BB8259F67E846F2002A3F7F2FEDC4B1F23)

说明

1. PageAbility的生命周期回调均为同步接口。
2. 目前app.js环境中仅支持onCreate和onDestroy回调，app.ets环境支持全量生命周期回调。

## 开发指导

下面通过一个完整的示例展示FA模型PageAbility生命周期的使用。

1. 在app.ets文件中实现Ability生命周期回调。

   ```
   1. // app.ets示例代码如下：
   2. import commonEvent from '@ohos.commonEvent';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG = "Fa:MainAbility:";
   6. const listPush = "Fa_MainAbility_";

   8. class Test {
   9. onCreate() {
   10. console.info(TAG, `onCreate`);
   11. }

   13. onDestroy() {
   14. console.info(TAG, `onDestroy`);
   15. // 发送事件通知Ability已销毁
   16. commonEvent.publish("Fa_MainAbility_onDestroy", (err: BusinessError) => {
   17. console.info(TAG, listPush, `onDestroy`, `err: ${JSON.stringify(err)}`);
   18. });
   19. }

   21. onActive() {
   22. console.info(TAG, `onActive`);
   23. }

   25. onInactive() {
   26. console.info(TAG, `onInactive`);
   27. }

   29. onShow() {
   30. console.info(TAG, `onShow`);
   31. }

   33. onHide() {
   34. console.info(TAG, `onHide`);
   35. }

   37. onContinue(wantParam: Record<string, Object>) {
   38. console.info(TAG, `onContinue`);
   39. return true;
   40. }

   42. onNewWant(want: Record<string, Object>, launchParam: Record<string, number>) {
   43. console.info(TAG, `onNewWant`);
   44. }

   46. onSaveData(saveData: Object) {
   47. console.info(TAG, `onSaveData`);
   48. return true;
   49. }

   51. onRestoreData(restoreData: Object) {
   52. console.info(TAG, `onRestoreData`);
   53. }
   54. }

   56. export default new Test()
   ```
2. Index.ets页面提供一个"terminateSelf"按钮，点击后调用[featureAbility.terminateSelf](../harmonyos-references/js-apis-ability-featureability.md#featureabilityterminateself7-1)接口关闭Ability，从而触发onDestroy生命周期回调。

   ```
   1. // Index.ets示例代码如下：
   2. import ability_featureAbility from '@ohos.ability.featureAbility';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'FA Model Lifecycle Demo';

   10. // 点击terminateSelf按钮关闭自己
   11. terminateSelf() {
   12. console.info(`Index: terminateSelf called`);
   13. ability_featureAbility.terminateSelf().then((data) => {
   14. console.info(`Index: terminateSelf success data = : ${JSON.stringify(data)}`);
   15. }).catch((err: BusinessError) => {
   16. console.info(`Index: terminateSelf err = ${JSON.stringify(err)}`);
   17. });
   18. }

   20. build() {
   21. Row() {
   22. Column() {
   23. Text(this.message)
   24. .fontSize(30)
   25. .fontWeight(FontWeight.Bold)
   26. .margin({ bottom: 20 })

   28. Text('点击下方按钮关闭Ability')
   29. .fontSize(18)
   30. .margin({ bottom: 20 })

   32. Button('terminateSelf')
   33. .fontSize(20)
   34. .width(200)
   35. .height(50)
   36. .onClick(() => {
   37. this.terminateSelf();
   38. })
   39. }
   40. .width('100%')
   41. .padding(20)
   42. }
   43. .height('100%')
   44. }
   45. }
   ```
3. 运行验证生命周期流程。

   | 回调函数 | 触发时机 | 典型使用场景 |
   | --- | --- | --- |
   | onCreate | Ability第一次启动时 | 应用初始化、资源加载 |
   | onActive | Ability切换到前台且获取焦点 | 刷新UI、恢复动画 |
   | onInactive | Ability失去焦点 | 暂停动画、保存临时数据 |
   | onShow | Ability由后台切换到前台可见 | 显示UI、准备用户交互 |
   | onHide | Ability由前台切换到后台不可见 | 隐藏UI、释放显示资源 |
   | onDestroy | Ability被销毁前 | 回收资源、清空缓存 |
   | onSaveData | 系统需要回收页面时 | 保存页面状态、存储临时数据 |
   | onRestoreData | 页面从回收状态恢复时 | 恢复页面状态、重新加载数据 |

   通过运行上述示例，开发者可以观察到完整的生命周期回调流程：

   * 应用启动时依次调用：onCreate → onActive
   * 点击按钮调用terminateSelf后依次调用：onInactive → onHide → onDestroy
