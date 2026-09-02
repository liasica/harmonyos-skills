---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1564
title: 按照提示再侧滑一次仍然退出失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 按照提示再侧滑一次仍然退出失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df51a560e7ac404478723131c71bb26d6c395a49ba19288845fba93ed0fef824
---

## 问题现象

打开应用，当侧滑退出应用时会有弹出提示“再侧滑一次退出应用”，再次侧滑还是无法退出。

## 背景知识

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出自定义弹窗。推荐使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口在相对应用复杂的场景来实现自定义弹出框，相较于[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)优势点在于页面解耦，支持动态刷新[update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)。
* [DialogOptions](../harmonyos-references/js-apis-promptaction.md#dialogoptions18)：自定义弹窗的内容，继承自[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)。
  + onWillDismiss：交互式关闭回调函数。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型（点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭），从而根据原因选择是否能关闭弹窗。
  + onWillAppear：弹窗显示动效前的事件回调。
* [showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)：创建并显示文本提示框。

## 问题定位

1. 查看hilog日志，搜索“HandleBackEvent”、“onBackPress return true”、“DialogWindow”等关键词，可以看到第一次侧滑手势触发了页面的onBackPress生命周期函数，并且创建了“再侧滑一次退出应用”提示弹窗。

   ```screen
   12-07 22:42:54.024 11211 11380 I C0420C/com.hm.example/WMSEvent: [] HandleBackEvent(3329): called
   12-07 22:42:54.024 11211 11380 I C03900/com.hm.example/Ace: [(-1:100000:singleton)] [com.hm.example][100000]: OnBackPressed called
   12-07 22:42:54.025 11211 11211 I C03925/com.hm.example/AceRouter: [(100000:100000:scope)] router user onBackPress return true
   12-07 22:42:54.032 11211 11211 I C0420A/com.hm.example/WMSLife: [] CreateAndConnectSpecificSession(373): name:pages/modal/Toast,id:645,parentId:642,type:1001,touchable:1
   12-07 22:42:54.032 11211 11211 I C0420A/com.hm.example/WMSLife: [] MakeSubOrDialogWindowDragableAndMoveble(224): Called 645.
   12-07 22:42:54.033 11211 11211 I C0420F/com.hm.example/WMSRecover: [] RegisterSessionRecoverCallbackFunc(320): persistentId = 645
   12-07 22:42:54.033 11211 11211 I C04200/com.hm.example/JsWindow: (5801)CreateJsWindow pages/modal/Toast
   12-07 22:42:54.034 11211 11211 I C04200/com.hm.example/JsWindowStage: (466)[NAPI]Create sub window pages/modal/Toast end
   12-07 22:42:54.034 11211 11211 I C04209/com.hm.example/WMSImms: [] SetLayoutFullScreen(1904): winId:645 pages/modal/Toast status:1
   12-07 22:42:54.034 11211 11211 I C04209/com.hm.example/WMSImms: [] SetLayoutFullScreenByApiVersion(1867): SetIgnoreViewSafeArea winId:645 status:1
   12-07 22:42:54.039 11211 11211 I C04200/com.hm.example/WMS: [] GetSurfaceNode(1473): name:pages/modal/Toast, id:645
   ```
2. 搜索“HandleBackEvent”、“Destroy”、“windowId”等关键词，发现第二次侧滑操作没有触发onBackPress函数，而是关闭了“再侧滑一次退出应用”的弹窗。

   ```screen
   12-07 22:42:55.247 11211 11380 I C0420C/com.hm.example/WMSEvent: [] HandleBackEvent(3329): called
   12-07 22:42:55.247 11211 11380 I C03900/com.hm.example/Ace: [(-1:100003:active)] [com.hm.example][100003]: OnBackPressed called
   12-07 22:42:55.535 11211 11211 I C04200/com.hm.example/JsWindow: (141)Destroy
   12-07 22:42:55.536 11211 11211 I C0420A/com.hm.example/WMSLife: [] Destroy(1364): Destroy start, id: 645, state_:2, needNotifyServer: 1, needClearListener: 1
   12-07 22:42:55.536 11211 11211 I C04200/com.hm.example/InputChannel: (145)Destroy WindowInputChannel, windowId:645
   12-07 22:42:55.536 11211 11211 I C04200/com.hm.example/InputChannel: (34)windowName: pages/modal/Toast, windowId: 645
   12-07 22:42:55.538   898  8485 I C01731/resource_schedule_service/SUSPEND_MSG: [(RecordWindowVisibleInfo):56] 20020440_com.hm.example_11211 visible window:1 windowId:645
   12-07 22:42:55.539  3195  3737 I C04207/com.ohos.sceneboard/WMSFocus: [] NotifyFocusStatus(5074): name: com.fbank.mobile.hm/EntryAbility/pages/modal/Toast, id: 645, isFocused: 0
   12-07 22:42:55.540  3195  3737 I C04207/com.ohos.sceneboard/WMSFocus: [] NotifyFocusStatus(5074): name: com.fbank.mobile.hm/EntryAbility/hm0, id: 642, isFocused: 1
   12-07 22:42:55.541 11211 11379 I C04207/com.hm.example/WMSFocus: [] UpdateFocus(959): Report update focus: 1, id: 642
   12-07 22:42:55.542 11211 11379 I C03900/com.hm.example/Ace: [(-1:100003:active)] [com.hm.example][fmBank][100000]: window focus
   12-07 22:42:55.544 11211 11380 I C04207/com.hm.example/WMSFocus: [] UpdateFocus(959): Report update focus: 0, id: 645
   12-07 22:42:55.545 11211 11380 I C03900/com.hm.example/Ace: [(-1:100000:active)] [com.hm.example][fmBank][100003]: window unfocus
   ```
3. 查看相关代码，发现侧滑页面使用了openCustomDialog来实现自定义弹窗（默认为模态窗口）。onBackPress函数中判断两次侧滑操作的时间间隔，间隔大于1秒则显示弹窗，间隔小于1秒则关闭应用。

   ```screen
   import { common } from "@kit.AbilityKit";
   import { ComponentContent, promptAction } from "@kit.ArkUI";
   import { BusinessError } from "@kit.BasicServicesKit";

   class Params {
     text: string = "";

     constructor(text: string) {
   	this.text = text
     }
   }

   @Builder
   function BuilderDialog(params: Params) {
     Column() {
       Text(params.text)
         .margin(30)
     }
     .backgroundColor(Color.Grey)
   }

   @Entry
   @Component
   struct Index {
     @State firstBackTimestamp: number = 0;
     uiContext = this.getUIContext();
     promptAction = this.uiContext.getPromptAction();
     contentNode: ComponentContent<Object> = new ComponentContent(this.uiContext, wrapBuilder(BuilderDialog), new Params('再侧滑一次退出应用'));

     onBackPress() {
       let now = Date.now();
       if (now - this.firstBackTimestamp < 1000) {
         let context = this.uiContext.getHostContext() as common.UIAbilityContext
         context.terminateSelf();
       } else {
         this.firstBackTimestamp = now;
         this.promptAction.openCustomDialog(this.contentNode).then(() => {
           console.info("OpenCustomDialog succeeded")
         }).catch((error: BusinessError) => {
           console.error(`OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
         })
       }
       return true
     }

     build() {
       Column() {
         Text("Hello World")
           .fontSize(30)
           .margin(30)
       }.width("100%")
     }
   }
   ```

## 分析结论

侧滑页面的onBackPress函数中实现了两次侧滑操作退出应用的逻辑，但是由于自定义弹窗默认为模态窗口，实际第二次侧滑不会触发onBackPress函数，而是关闭了弹窗，所以导致第二次侧滑无法退出应用。

## 修改建议

* 可以在自定义弹窗的生命周期函数onWillAppear、onWillDismiss进行两次侧滑退出应用的逻辑处理。
* 如果业务上不需要自定义弹窗，也可以使用showToast文本提示框提示用户二次侧滑。

  示例代码如下：

  ```screen
  import { common } from '@kit.AbilityKit';
  import { ComponentContent, promptAction } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  class Params {
    text: string = '';

    constructor(text: string) {
      this.text = text;
    }
  }

  @Builder
  function BuilderDialog(params: Params) {
    Column() {
      Text(params.text)
        .margin(30);
    }
    .backgroundColor(Color.Grey);
  }

  @Entry
  @Component
  struct SwipeTwiceToExitApp {
    arr: string[] = ['solution1', 'solution2'];
    count: number = 3;
    @State text: string = this.arr[0];
    @State firstBackTimestamp: number = 0;
    solution: () => void = () => {
    };

    aboutToAppear(): void {
      this.solution = () => {
        this.solution1();
      };
    }

    uiContext = this.getUIContext();
    promptAction = this.uiContext.getPromptAction();
    contentNode: ComponentContent<Object> =
      new ComponentContent(this.uiContext, wrapBuilder(BuilderDialog), new Params('再侧滑一次退出应用'));
    dialogOptions: promptAction.DialogOptions = {
      showInSubWindow: false,
      onWillAppear: () => {
        this.firstBackTimestamp = Date.now();
        setTimeout(() => {
          this.closeDialog();
        }, 2000);
      },
      onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
        if (dismissDialogAction.reason == 0) {
          this.closeDialog();
          let now = Date.now();
          if (now - this.firstBackTimestamp < 1000) {
            const context = this.uiContext.getHostContext() as common.UIAbilityContext;
            context.terminateSelf().catch(() => {
              console.error('terminateSelf failed');
            });
          }
        } else if (dismissDialogAction.reason == 1) {
          this.closeDialog();
        }
      },
    };

    closeDialog() {
      this.promptAction.closeCustomDialog(this.contentNode).then(() => {
        console.info('succeeded');
      }).catch((error: BusinessError) => {
        console.error(`CloseCustomDialog args error code is ${error.code}, message is ${error.message}`);
      });
    }

    openDialog() {
      this.promptAction.openCustomDialog(this.contentNode, this.dialogOptions).then(() => {
        console.info('succeeded');
      }).catch((error: BusinessError) => {
        console.error(`OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
      });
    }

    onBackPress() {
      this.solution();
      return true;
    }

    solution1() {
      this.openDialog();
    }

    solution2() {
      let now = Date.now();
      if (now - this.firstBackTimestamp < 1000) {
        const context = this.uiContext.getHostContext() as common.UIAbilityContext;
        context.terminateSelf().catch(() => {
          console.error('terminateSelf failed');
        });
      } else {
        this.firstBackTimestamp = now;
        try {
          this.promptAction.showToast({
            message: '再侧滑一次退出应用',
            duration: 1000
          });
        } catch (error) {
          console.error('showToast failed');
        }
      }
    }

    build() {
      Column() {
        Button(this.text)
          .fontSize(30)
          .margin(30)
          .onClick(() => {
            this.text = this.arr[this.count % 2];
            this.count++;
            if (this.text === 'solution1') {
              this.solution = () => {
                this.solution1();
              };
            } else {
              this.solution = () => {
                this.solution2();
              };
            }
          });
      }.width('100%');
    }
  }
  ```
