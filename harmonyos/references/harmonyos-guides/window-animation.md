---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-animation
title: 设置窗口动效 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 其他开发场景 > 设置窗口动效 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7eaed1599d0cfa5f799adf94dc8b7a7bbc8b8fb9fcc1bb75fc4d8c688d161b21
---

## 场景介绍

窗口动效是指窗口在显示、隐藏、切换过程中的过渡动画效果。为了让这些过程更加自然流畅，避免界面切换过于突兀，系统提供了过渡动画支持。同时，为满足开发者的自定义需求，系统还提供了自定义设置窗口动效的能力。

以下为支持设置自定义窗口动效的几种典型场景：

* [设置应用内UIAbility组件启动淡入淡出动效](window-animation.md#设置应用内uiability组件启动淡入淡出动效)
* [设置主窗口销毁时的转场动画](window-animation.md#设置主窗口销毁时的转场动画)

## 设置应用内UIAbility组件启动淡入淡出动效

在使用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-2)接口拉起同一应用内其他UIAbility组件时，可以通过[StartOptions](../harmonyos-references/js-apis-app-ability-startoptions.md)中[WindowCreateParams](../harmonyos-references/arkts-apis-window-i.md#windowcreateparams20)配置窗口的启动动画。

目前支持将窗口启动动画配置为淡入淡出动效[FADE\_IN\_OUT](../harmonyos-references/arkts-apis-window-e.md#animationtype20)。

示例代码如下：

```typescript
import { Want, StartOptions, common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private context = AppStorage.get('context') as common.UIAbilityContext;

  openAbility():void {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.startabilitywithfadeinout',
      abilityName: 'FadeInOutAbility',
      moduleName: 'entry'
    };
    let options: StartOptions = {
      // 传入启动动效参数
      windowCreateParams: {
        animationParams : { type: window.AnimationType.FADE_IN_OUT },
      }
    }
    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbility succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
  build() {
    RelativeContainer() {
      Column() {
        Button('startAbility').onClick(() => this.openAbility())
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/5uO2PifWS4iOeQyyiwAd7Q/zh-cn_image_0000002742003233.gif)

## 设置主窗口销毁时的转场动画

在[自由窗口](window-terminology.md#freeform-window自由窗口)状态下，应用使用[getWindowTransitionAnimation()](../harmonyos-references/arkts-apis-window-window.md#getwindowtransitionanimation20)获取主窗口转场的动画配置，当前转场动画配置不符合业务诉求时，可以使用[setWindowTransitionAnimation()](../harmonyos-references/arkts-apis-window-window.md#setwindowtransitionanimation20)接口配置窗口转场时的动画，当前仅支持配置窗口销毁时的转场动画。

示例代码如下：

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    try {
      // 获取主窗口
      const windowClass = await windowStage.getMainWindow();

      // 配置窗口销毁动画
      this.setupWindowDestroyAnimation(windowClass);

      // 加载页面
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });
    } catch (err) {
      console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
    }
  }

  private setupWindowDestroyAnimation(windowClass: window.Window): void {
    try {
      // 检查是否已存在销毁动画配置
      const existingAnimation = windowClass.getWindowTransitionAnimation(
        window.WindowTransitionType.DESTROY
      );

      if (existingAnimation) {
        return;
      }

      // 配置动画
      const animationConfig: window.WindowAnimationConfig = {
        duration: 1000,
        curve: window.WindowAnimationCurve.LINEAR,
      };

      const transitionAnimation: window.TransitionAnimation = {
        opacity: 0.0,
        config: animationConfig
      };

      // 设置动画
      windowClass.setWindowTransitionAnimation(
        window.WindowTransitionType.DESTROY,
        transitionAnimation
      ).then(() => {
        console.info('Succeeded in setting window transition animation');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set window transition animation. Cause: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to setup window animation. Cause: ${exception.message}`);
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/JNaps2Z4QnOfqj5SxNmHhA/zh-cn_image_0000002712404246.gif)
