---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-128
title: 切换自由多窗后会重新进入应用
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 切换自由多窗后会重新进入应用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:45144bc110b6b8f545260330fc35a14bdb19d79fd011281cb2c9683be4babb82
---

## 问题现象

### 场景一

平板设备打开系统下拉控制栏的自由多窗开关，接着打开应用进入核心页面，然后再关闭自由多窗，发现会重新进入应用，正常情况应该是应用的功能和页面显示表现正常。

### 场景二

游戏过程中，切换自由多窗、悬浮窗、分屏模式，游戏会中断并重新回到首页。

## 背景知识

* [onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)：当应用的UIAbility实例已创建，再次调用方法启动该UIAbility实例时，系统触发该UIAbility的onNewWant()回调。开发者可以在该回调中更新要加载的资源和数据等，用于后续的UI展示。当已在前台运行过的UIAbility实例切换至后台后，被再次拉起时（即热启动场景），会触发onNewWant()生命周期回调。
* [onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)：UIAbility实例创建完成之后，在进入前台之前，系统会创建一个WindowStage。WindowStage创建完成后会进入onWindowStageCreate()回调，开发者可以在该回调中进行UI加载、WindowStage的事件订阅。

## 问题定位

根据场景一和场景二的问题现象，怀疑是切换自由多窗时触发了应用生命周期函数中的资源释放、加载等相关逻辑，导致应用重新进入页面，按照该思路继续排查应用的日志和代码。

* 查看问题发生时间附近的日志，可以看到当关闭自由多窗后，根据关键日志“app cold start finished”看出应用属于从小窗形态变全屏形态，被再次拉起时的热启动场景，此时根据关键日志“OnNewWant: Window [name:younghs0, id:144]”得知触发了onNewWant()生命周期回调函数，也根据关键日志“Ability onWindowStageCreate”得知触发了onWindowStageCreate()回调函数。

  ```screen
  07-03 15:23:15.231 22149 22296 I C03F00/com.hm.example/ArkCompiler: [dict][gc] SmartGC: app cold start finished
  07-03 15:23:16.077  4216  4216 W C0393B/com.ohos.sceneboard/AceWindowScene: [dict][(100000:100000:scope)] OnDetachFromFrameNode id: 144, node id: 32188, type: 1, name: com.hm.example
  07-03 15:23:16.088 22149 22292 I C04200/com.hm.example/WindowSceneSessionImpl: [dict](4076)UpdateWindowMode: UpdateWindowMode 144 mode 1
  07-03 15:23:16.088  4216  4697 I C0420A/com.ohos.sceneboard/WMSLife: [dict][] RequestSceneSessionActivationInner(2412): id 144 want-ability: EntryAbility, bundle: com.hm.example, module: entry, uri: /com.hm.example/entry/EntryAbility, appIndex: 0, tmpSpecifiedId:0
  07-03 15:23:16.098  4216 22596 I C01336/com.ohos.sceneboard/AMS: [dict][ability_manager_client.cpp:351]scb call, StartUIAbilityBySCB target: /com.hm.example/entry/EntryAbility.
  07-03 15:23:16.110  1475  2537 I C011FF/foundation/ERMS: [dict][RULE_ENGINE_IMPL(GetSceneExperienceFromCache:502)] GetSceneExperienceFromCache set SceneCode! bundleName is = com.hm.example
  07-03 15:23:16.111  1475  2537 I C01336/foundation/AMS: [dict][ui_ability_lifecycle_manager.cpp:114]StartUIAbility session:144. bundle:com.hm.example, ability:EntryAbility, reuseDelegator: 0
  07-03 15:23:16.111 22149 22319 I C01332/com.hm.example/UIAbility: [dict][ui_ability_thread.cpp:323]name:EntryAbility,targeState:5,isNewWant:1
  07-03 15:23:16.111   884 21215 I C01705/resource_schedule_service/EXACT_PREREAD: [dict][(HandleAppStartupPrereadWork):112] App has preread, skip current preread work: com.hm.example20020453 
  07-03 15:23:16.112 22149 22149 I C01332/com.hm.example/UIAbility: [dict][ui_ability_thread.cpp:240]Lifecycle:name EntryAbility
  07-03 15:23:16.112 22149 22149 I C04200/com.hm.example/WindowSessionImpl: [dict](1967)OnNewWant: Window [name:younghs0, id:144]
  07-03 15:23:16.112 22149 22149 I C03900/com.hm.example/Ace: [dict][(-1:100000:singleton)] [com.hm.example][entry][100000]: UIContent OnNewWant
  07-03 15:23:16.112 22149 22149 I A0FF00/com.hm.example/WidgetCalleeEntryAbility: Ability onNewWant: {"moduleName":"entry","ohos.aafwk.param.displayId":0}
  07-03 15:23:16.112 22149 22149 I A00000/com.hm.example/testTag: Ability onWindowStageCreate
  07-03 15:23:16.112 22149 22149 I C04200/com.hm.example/JsWindowStage: [dict](87)LoadContent: [NAPI]
  07-03 15:23:16.112 22149 22149 I C01332/com.hm.example/UIAbility: [dict][js_ui_ability.cpp:1408]end, name: onNewWant, time: 0
  ```
* 排查代码中的EntryAbility文件的代码逻辑，分析如下：
  + 实现了onNewWant()生命周期回调函数，具体的代码逻辑是判断变量currentWindowStage是否为null，如果不为null则触发onWindowStageCreate()函数加载UI页面。
  + 当首次进入应用时，onWindowStageCreate()函数中会初始化变量currentWindowStage，在关闭自由多窗后会重新进入应用时会触发了onNewWant()函数的逻辑，导致重新加载UI页面，也就是表现出来的重新进入应用的现象。

    ```screen
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';

    export default class EntryAbility extends UIAbility {
      private currentWindowStage: window.WindowStage | undefined = undefined;

      onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        console.info('ability onNewWant');
        if (this.currentWindowStage !== undefined) {
          this.onWindowStageCreate(this.currentWindowStage);
        }
      }

      onWindowStageCreate(windowStage: window.WindowStage): void {
        console.info('ability onWindowStageCreate');
        this.currentWindowStage = windowStage;
        windowStage.loadContent('pages/Index', (err) => {
          console.info('ability loadContent');
          if (err.code) {
            return;
          }
        });
      }
    }
    ```

## 分析结论

onNewWant()生命周期函数中有调用onWindowStageCreate()函数的逻辑，导致应用从background状态进入foreground状态时，触发onNewWant()重新加载UI页面。

## 修改建议

建议开发者在onNewWant()生命周期函数中优化资源和数据的加载和更新等代码逻辑，避免从后台进入前台时发生重新进入应用等非预期的效果。
