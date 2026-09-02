---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1111
title: Toast弹窗使用常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Toast弹窗使用常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:442667c31c74dce4d16669d04013167672fa2fb71897f8959dced277499b85ee
---

## 问题现象

Toast弹窗使用常见场景如下：

场景一：如何使用Toast弹窗并设置其显示层级最高？

场景二：如何自定义Toast弹窗的阴影效果？

场景三：如何自定义Toast弹窗显示时间？

场景四：设置Toast的背板颜色backgroundColor为指定颜色后，发现显示颜色不符合预期。

## 背景知识

* [即时反馈（Toast）](../harmonyos-guides/arkts-create-toast.md)是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。它通常在屏幕的底部或顶部短暂弹出，随后在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，避免干扰用户当前的操作流程。
* 可以通过使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)创建并显示文本提示框。
* Toast弹窗相关使用限制参考[使用建议](../harmonyos-guides/arkts-create-toast.md#使用建议)。

## 解决方案

* **场景一**：使用UIContext中的getPromptAction方法获取当前UI上下文关联的PromptAction对象，再通过该对象调用showToast创建并显示文本提示框。通过设置[ShowToastOptions](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)中的属性showMode来控制Toast弹窗的显示层级，其中TOP\_MOST表示显示在应用之上。
* **场景二**：自定义Toast弹窗的阴影效果可以通过设置[ShowToastOptions](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)中的属性shadow来控制。
* **场景三**：自定义Toast弹窗的显示时间可以通过设置ShowToastOptions中的属性duration来控制，默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。
* **场景四**：设置Toast的背板颜色backgroundColor为指定颜色后，发现显示颜色不符合预期，是因为backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

示例代码如下：

```ts
import { PromptAction, promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct Index {
  private uiContext: UIContext = this.getUIContext();
  private promptAction: PromptAction = this.uiContext.getPromptAction();

  build() {
    Column({ space: 20 }) {
      Button('场景一')
        .fontSize(20)
        .onClick(() => {
          try {
            this.promptAction.showToast({
              message: 'I am TOP_MOST toast',
              duration: 2000,
              showMode: promptAction.ToastShowMode.TOP_MOST,
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`scene1:showToast args error code is ${code}, message is ${message}`);
          }
        })
      Button('场景二')
        .fontSize(20)
        .onClick(() => {
          try {
            this.promptAction.showToast({
              message: 'I am shadow toast',
              duration: 2000,
              shadow: ShadowStyle.OUTER_FLOATING_MD,
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`scene2:showToast args error code is ${code}, message is ${message}`);
          }
        })
      Button('场景三')
        .fontSize(20)
        .onClick(() => {
          try {
            this.promptAction.showToast({
              message: 'I am duration toast',
              duration: 3000,
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`scene3:showToast args error code is ${code}, message is ${message}`);
          }
        })
      Button('场景四')
        .fontSize(20)
        .onClick(() => {
          try {
            this.promptAction.showToast({
              message: 'I am color toast',
              duration: 3000,
              backgroundColor: Color.Gray,
              backgroundBlurStyle:BlurStyle.NONE,
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`scene4:showToast args error code is ${code}, message is ${message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 常见FAQ

Q：Toast弹窗无法显示的可能原因及排查方向有哪些？

A：主要排查方向包括：

* 排查调用Toast弹窗的位置是否有准确的UIContext，不支持在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的生命周期中调用，需要在创建组件实例后使用。不可在UI上下文不明确的地方使用。
* 排查是否将showToast封装在自定义class中（非UI实例）、异步中使用等。
* 若在子窗中显示Toast弹窗，排查子窗是否正常展示，是否Toast的子窗层级低导致被覆盖等。

Q：如何设置Toast弹窗的样式，包括圆角、宽高、字体大小、图片等？

A：Toast弹窗是一种固定样式的提示框，不支持自定义Toast弹窗的样式，可以使用自定义弹窗实现，参考[通过自定义弹窗实现自定义样式的Toast](faqs-arkui-736.md)。

Q：如何实现全局的Toast函数，并且可以显示和隐藏？

A：可以参考[自定义一个全局调用的Toast函数组件](https://developer.huawei.com/consumer/cn/forum/topic/0201169227598684144?fid=0109140870620153026)。

Q：使用Toast弹窗时报错Error: Internal error. UI execution context not found.如何解决？

A：根据报错信息，初步推断是在调用[promptAction.showToast](../harmonyos-references/js-apis-promptaction.md#promptactionshowtoastdeprecated)接口时，识别到场景下UI实例缺失主动抛出的。请尝试绑定UI实例来调用接口，同时进行合理的try catch异常捕捉。
