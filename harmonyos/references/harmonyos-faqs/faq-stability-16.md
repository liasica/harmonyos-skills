---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-16
title: 未申请JIT权限导致应用卡死在启动页
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 未申请JIT权限导致应用卡死在启动页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af22d75765031ca420996fbe44059417065386a4f1da4c13ef8ca233318ef70d
---

## 问题现象

应用启动，卡死在启动页，安全隐私协议弹窗无法正常弹出。

## 背景知识

* 应用启动流程，应用启动大致分为6个阶段：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/A7DtsEkEScu8H7lSDSsASg/zh-cn_image_0000002628476146.png "点击放大")

  1. AbilityManagerService请求AppSpawn创建应用进程。
  2. AppManagerService触发应用启动流程、应用进程加载应用包—handleLaunchApplication。
  3. AppManagerService触发Ability启动流程、应用进程加载Ability资源、根据应用生命周期定义，触发生命周期回调—HandleLaunchAbility。
  4. 创建UI Ability持有的Window对象。
  5. 绘制UI界面首帧。
  6. 首页加载绘制完成。
* API18之前JIT功能默认开启，API18以后JIT功能默认关闭，具体变更可以参考[JIT功能默认关闭，需申请权限证书并通过审核后启用](../harmonyos-releases/changelogs-for-all-apps-5101.md#section398)。

## 问题定位

1. 问题复现：

   在新版本和老版本系统分别测试，初步判断卡死问题是否和系统变更有关。本案例中，5.0系统上应用启动正常，5.1(API18)上问题稳定复现，应用卡在启动页，未弹出隐私弹框。
2. 问题分析：

   应用卡在启动页，从应用启动流程开始分析。

   * 首先分析AppSpawn孵化应用进程是否正常，通过日志分析确认，应用进程孵化成功，pid为7994：

     ```txt
     06-10 19:41:43.783   663   663 I C02C11/appspawn/APPSPAWN: [appspawn_service.c:1058]Child process com.hx.example success pid 7994 appId: 525 result: 0
     06-10 19:41:43.783   663   663 I C02C11/appspawn/APPSPAWN: [appspawn_appmgr.c:172]Add com.hx.example, pid=7994 success
     06-10 19:41:43.783  7994  7994 I C02D0B/com.hx.example/HICHECKER: hichecker param is empty.
     06-10 19:41:43.784   663   663 I C02C11/appspawn/APPSPAWN: [appspawn_service.c:293]SendMessageComplete connectionId: 1 result 0 app com.hx.example pid 7994
     06-10 19:41:43.784  7994  7994 I C01317/com.hx.example/AppKit: [main_thread.cpp:2781]App main thread create, pid:7994
     ```

     进程创建成功后，下一步需要确认AMS生命周期是否正常。
   * AMS生命周期分析，通过日志确认应用UIAbility正常启动，窗口创建成功，首页成功绘制：

     ```txt
     06-10 19:41:43.920  7994  7994 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onCreate
     06-10 19:41:43.926  7994  7994 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1613]end, name: onCreate, time: 5
     06-10 19:41:43.926  7994  7994 E C01332/com.hx.example/UIAbility: [ui_ability_impl.cpp:301]hasSaveData_: false
     06-10 19:41:43.926  7994  7994 W C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:922]formatRegex: []
     06-10 19:41:43.932  7994  7994 E C01332/com.hx.example/UIAbility: [ui_ability.cpp:323]appRecovery not recovery restart
     06-10 19:41:43.932  7994  7994 I C01332/com.hx.example/UIAbility: [js_ui_ability.cpp:1568]JsUIAbility call js, name: onWindowStageCreate
     ```

     至此，系统侧启动流程已完成，下一步进入应用业务流程，本案例中应用下一步的业务流程为隐私弹框。
   * 分析应用侧隐私弹窗代码流程，应用隐私弹窗关键代码片段如下：

     ```ts
     async aboutToAppear(): Promise<void> {
       const startupTask = await DI_CONTAINER.getAsync(AppStartupTask)
       // 此处会一直阻塞，直到弹窗同意
       await startupTask.run({
         readPrivacyHandler: (callback) => {
           this.agreeCallback = () => callback(true)
           this.showPrivacyDialog(this.agreeCallback)
         },
       })
     }
     ```

     从代码上看StartupTask任务执行完成回调后才会执行隐私弹窗流程，StartupTask负责一系列冷启动任务的初始化动作，初步分析是StartupTask中的某项任务执行异常导致未执行隐私弹窗代码。对StartupTask中的任务排查分析，确认是其中的wasm初始化任务失败，导致StartupTask未回调，中断了后续隐私弹窗弹出流程。

     此处关键思路是找到业务卡住的代码，梳理分析出业务执行的前置条件，重点排查引起前置条件不满足的异常因素。
   * 根因确认，查阅5.1(API18)变更说明，涉及wasm功能的关键变更：[JIT功能默认关闭，需申请权限证书并通过审核后启用](../harmonyos-releases/changelogs-for-all-apps-5101.md#section398)。JIT关闭wasm接口将无法执行，导致StartupTask中wasm初始化任务失败。

## 分析结论

应用启动页卡死，是应用业务初始化流程中某项任务因系统变更导致失败，中断了业务初始化流程。本案例中是JSVM增加系统变更，默认禁止JIT功能，导致业务初始化流程中的wasm任务失败，中断了业务流程。

## 修改建议

参考[JSVM 申请JIT权限指导](../harmonyos-guides/jsvm-apply-jit-profile.md)申请权限证书后使用JIT功能。
