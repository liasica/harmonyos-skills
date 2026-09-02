---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-147
title: 使用App Linking实现应用冷启动时应用闪退
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 使用App Linking实现应用冷启动时应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a1086d68da1366352dcbec3d969c114858ce16a44a2f2d9293ed1a9894e4617b
---

## 问题现象

在配置App Linking时，应用作为被拉起应用，冷启动情况下应用闪退，报错显示UIAbility未正常启动，涉及在EntryAbility的onCreate方法中有处理App Linking参数和跳转相关页面的操作。

问题代码的EntryAbility中参数配置如下：

```ts
// 冷启动
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.getRouterUri(want);
  console.info('Ability onCreate');
}
private getRouterUri(want: Want) {
  let uri: string | undefined = want?.uri;
  if (uri) {
    // 根据解析的uri跳转至相应页面，例如需要跳转页面为"pages/Access"
    let status: router.RouterState = router.getState();
    if (status && status.name !== 'Access' && uri) {
      // 根据uri参数做业务处理
      router.replaceUrl({
        url: 'pages/Page1',
        params: {
          uri: uri
        }
      })
    }
  }
}
```

## 背景知识

* App Linking与冷启动概念：[App Linking](../harmonyos-guides/app-linking-kit-guide.md)用于实现应用间的深度链接，[冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)是指应用从完全未运行状态启动。在此场景下，涉及到应用接收参数并正确跳转页面的处理机制。
* HarmonyOS相关代码环境：代码基于HarmonyOS，在EntryAbility中有对Want对象的处理，包括获取uri等参数，并尝试根据参数进行页面跳转。涉及到的相关API包括router相关操作、Ability的生命周期方法（如onCreate、onWindowStageCreate）以及相关的日志输出（hilog）功能。

## 问题定位

1. 用try-catch将问题代码包裹住，App确实没有再闪退，但首次启动时也无法跳转到二级页面。try-catch捕获到的异常信息如下：

   ```txt
    error:Error message:Internal error. UI execution context not found.
    Error code:100001
    Stacktrace:
      at onCreate (entry/src/main/ets/entryability/EntryAbility.ets:13:38)
   ```
2. 根据上述异常结合API特性分析可知，router.getState获取的是栈顶页面的状态信息，而在onCreate中获取调用时，它的生命周期尚未开始，所以会报错。

## 分析结论

分析当前问题出在冷启动时在onCreate方法中进行页面跳转（router操作）的处理方式上，导致UIAbility启动异常。需要重新审视这种在生命周期早期进行页面跳转的合理性，并考虑合适的处理参数和加载页面的时机。

## 修改建议

1. 避免在onCreate中使用跳转router操作，可以在onCreate里解析参数。在EntryAbility中定义参数（如funcAbilityWant）用于接收调用方UIAbility传过来的参数。
2. 在onWindowStageCreate中根据解析后的参数来加载页面。例如，根据funcAbilityWant中的parameters.router值来决定加载的页面（如值为'funcA'则加载'pages/Page\_ColdStartUp'，否则加载'pages/Index'），通过windowStage.loadContent方法加载页面，并处理可能的错误和数据。

   ```ts
   import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     funcAbilityWant: Want | undefined = undefined;
     uiContext: UIContext | undefined = undefined;

     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // 接收调用方UIAbility传过来的参数
       this.funcAbilityWant = want;

       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       hilog.info(DOMAIN, 'testTag', '%{public}s', JSON.stringify(launchParam));
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       console.info('Ability onWindowStageCreate');
       // Main window is created, set main page for this ability
       let url = 'pages/Index';
       if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') {
         url = 'pages/Page_ColdStartUp'; // 根据实际业务设置
       }
       windowStage.loadContent(url, (err, data) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         hilog.info(DOMAIN, 'testTag', 'data: %{public}s', JSON.stringify(data));
       });
     }

     // 示例省略其他生命周期函数
   };
   ```
3. 可参考官方文档链接：[目标UIAbility冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)，获取更多关于UIAbility设备内交互相关指导。

## 总结

* 应用冷启动的流程和几个重要的生命周期。应用冷启动的过程大致可分成以下四个阶段：应用进程创建&初始化、Application&Ability初始化、Ability/AbilityStage生命周期、加载绘制首页，如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/dp45E5CjSJaqA_6NRL5uwA/zh-cn_image_0000002628789246.png "点击放大")

  这个问题是在Ability/AbilityStage生命周期：该阶段主要是AbilityStage/Ability的启动生命周期，执行相应的生命周期回调。
* 此问题是HarmonyOS应用在处理App Linking冷启动时因在错误的生命周期方法（onCreate）中进行页面跳转操作导致UIAbility启动异常的问题。通过将参数解析和页面加载操作分别放在onCreate和onWindowStageCreate方法中，依据合适的参数判断来加载正确页面的方式解决。
* 在处理类似的应用启动和页面跳转逻辑时，应注意遵循HarmonyOS应用生命周期的规范，避免在不适当的时机执行可能影响启动流程的操作。
