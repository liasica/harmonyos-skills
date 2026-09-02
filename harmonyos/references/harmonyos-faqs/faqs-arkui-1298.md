---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1298
title: 输入框输入时键盘异常收回又弹出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 输入框输入时键盘异常收回又弹出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9ed4c7d0435ebf61b31730777f62123662556a2d8152fc095fe691fb8023b5b1
---

## 问题现象

Loading自定义弹窗弹起时，输入框失去焦点，会导致键盘自动隐藏。

如何实现Loading自定义弹窗弹起时，输入框不会失去焦点，键盘也不会自动收起。

```ts
// LoadingManager.ets
import { ComponentContent, PromptAction } from "@kit.ArkUI";

class LoadingManager {
  contentNode: ComponentContent<Object> | undefined = undefined;
  promptAction: PromptAction | undefined = undefined;

  show(uiContext: UIContext) {
    if (this.contentNode && this.promptAction) {
      this.promptAction.closeCustomDialog(this.contentNode)
    }
    this.contentNode = new ComponentContent(uiContext, wrapBuilder(Loading));
    this.promptAction = uiContext.getPromptAction();
    this.promptAction.openCustomDialog(this.contentNode, {
      alignment: DialogAlignment.Center
    })
  }

  hide() {
    if (this.promptAction) {
      this.promptAction.closeCustomDialog(this.contentNode)
    }
  }
}

@Builder
function Loading() {
  Column() {
    LoadingProgress()
      .width(50).height(50)
      .color(Color.White)
  }
  .width('100%')
  .height('100%')
  .backgroundColor('rgba(0,0,0,0.5)')
  .justifyContent(FlexAlign.Center)
}

export default new LoadingManager()
```

```ts
// Index.ets
import LoadingManager from './LoadingManager';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  uiContext?: UIContext
  @State phoneNumber: string = ''

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  // 模拟接口loading
  mockRequest() {
    LoadingManager.show(this.uiContext!)

    setTimeout(() => {
      LoadingManager.hide()
    }, 2000)
  }

  build() {
    RelativeContainer() {
      TextInput({ placeholder: '请输入手机号', text: this.phoneNumber })
        .type(InputType.Number)
        .onChange((value: string) => {
          this.phoneNumber = value
          if (this.phoneNumber.length === 11) {
            this.mockRequest()
          }
        })
        .onFocus(() => {
          this.phoneNumber = ''
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/-xcPGI11SzqeWYrC9iT4RQ/zh-cn_image_0000002628599010.png "点击放大")

## 背景知识

* 被动走焦是指组件焦点因系统或其他操作而自动转移，无需开发者直接干预，这是焦点系统的默认行为，参考链接：[走焦规范](../harmonyos-guides/arkts-common-events-focus-event.md#走焦规范)。
* 设置组件不能获取焦点focusable(false)，焦点就不会被转移此组件上，参考链接：[focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)。
* 通过requestFocus(true)可以主动让焦点转移至参数指定的组件，参考链接：[requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)。
* [自定义弹窗(CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)：基础的自定义弹窗，可用于广告、中奖、警告、软件更新等与用户交互响应操作。Dialog类型弹窗在弹出时会抢占焦点。

## 问题定位

输入框TextInput在获焦时，会默认拉起系统软键盘。出现键盘的反复拉起收回，通常是因为焦点反复切换到输入框上。

Dialog弹窗默认会抢占焦点，问题中每次加载出现的loading弹窗是由自定义弹窗CustomDialog实现的，因此出现了反复抢占输入框焦点的问题。

## 分析结论

loading自定义弹窗没有弹起时，此时输入框获取了焦点，但是loading自定义弹窗弹起时，输入框的焦点就会被动走焦到loading自定义弹窗上。

## 修改建议

* 刷新list要加载的数据量很小，加载时间很短，将loading弹窗直接移除不影响用户体验，若希望保留弹窗，可以更改openCustomDialog传参形式，从ComponentContent形式改为builder形式。
* 在loading自定义弹窗的最外层的组件添加focusable(false)，设置loading自定义弹窗组件不可以获焦，键盘也不会自动收起。但输入框还是会失焦，导致光标消失，使用onBlur事件监听失焦事件，触发失焦则执行requestFocus方法，使输入框重新获焦。

  代码示例如下:

1. LoadingManager.ets，定义loading工具类。

   ```ts
   import { promptAction, window } from "@kit.ArkUI";

   let windowClass: window.Window | undefined = AppStorage.get('windowClass');
   let dialogHeight: number = 0;

   class LoadingManager {
     customDialogId: number | undefined = undefined;

     public static createOption(builder: CustomBuilder) {
       const option: promptAction.CustomDialogOptions = {
         builder: builder,
         alignment: DialogAlignment.Center,
         cornerRadius: 0,
         width: "110%",
         height: dialogHeight,
         backgroundBlurStyle: BlurStyle.NONE,

       };
       return option;
     }

     show(context: Object, uiContext: UIContext, height: number) {
       dialogHeight = height;
       uiContext.getPromptAction().showToast({ message: "用户名或密码错误" });
       if (windowClass) {
         windowClass.setSpecificSystemBarEnabled('status', false)
           .then(() => {
             console.info('Succeeded in setting the status bar to be invisible.');
           })
           .catch(() => {
           });
       }
       uiContext.getPromptAction()
         .openCustomDialog(LoadingManager.createOption(Loading.bind(context)))
         .then((dialogId: number) => {
           this.customDialogId = dialogId;
         });
     }

     hide(uiContext: UIContext) {
       if (this.customDialogId) {
         uiContext.getPromptAction().closeCustomDialog(this.customDialogId);
         if (windowClass) {
           windowClass.setSpecificSystemBarEnabled('status', true)
             .then(() => {
               console.info('Succeeded in setting the status bar to be invisible.');
             })
             .catch(() => {
             });
         }
       }
     }
   }

   @Builder
   function Loading() {
     Column() {
       LoadingProgress()
         .width(50).height(50)
         .color(Color.White);
     }
     .focusable(false) // 设置当前组件不可以获焦
     .width('100%')
     .height('100%')
     .backgroundColor('rgba(0,0,0,0.5)')
     .justifyContent(FlexAlign.Center);
   }

   export default new LoadingManager();
   ```
2. Index.ets中调用。

   ```ts
   import LoadingManager from './LoadingManager';
   import { display } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State phoneNumber: string = '';
     @State displayHeight: number = 0;

     // 模拟接口loading
     mockRequest() {
       LoadingManager.show(this, this.getUIContext(), this.displayHeight);

       setTimeout(() => {
         LoadingManager.hide(this.getUIContext());
       }, 2000);
     }

     aboutToAppear() {
       this.displayHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
     }

     build() {
       RelativeContainer() {
         TextInput({ placeholder: '请输入手机号', text: this.phoneNumber })
           .margin({ top: 55,left:16,right:16 })
           .id("key2")
           .type(InputType.Number)
           .onChange((value: string) => {
             this.phoneNumber = value;
             if (this.phoneNumber.length === 11) {
               this.mockRequest();
             }
           })
           .onFocus(() => {
             setTimeout(() => {
               this.phoneNumber = '';
             }, 2100); // 模拟loading后删除号码
           })
           .onBlur(() => { // 失焦触发
             focusControl.requestFocus('key2'); // 重新获焦
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

   效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/kt72BPZDSAStkSONEqJKWw/zh-cn_image_0000002628758908.png "点击放大")

## 总结

设置组件的focusable属性为false，避免不必要的焦点抢占。

## 常见FAQ

Q：H5页面中，在输入框获焦、失焦时分别打开不同的自定义弹窗，键盘弹出又收回导致无法正常输入，该如何解决？

A：由于弹窗打开后会抢占焦点，导致键盘弹出异常。从API version 19开始，可以通过设置[focusable](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来管理弹出框是否获取焦点，设置为false后弹窗不会抢占焦点，键盘可以正常弹出。
