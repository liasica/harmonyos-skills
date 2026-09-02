---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-855
title: 侧滑退出应用后再次打开，会有提示是否退出登录的弹框
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 侧滑退出应用后再次打开，会有提示是否退出登录的弹框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5dca62d681a6db66484bd80c4fdc592df3f09b7dcfaa03cb0feed249d1f920cd
---

## 问题现象

用户侧滑退出应用后，此时应用进入到后台。当用户再次访问该应用时，系统会显示一个提示用户是否退出登录的对话框：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/rsEtiLFVT4K4_ZBe2AJI4g/zh-cn_image_0000002658797927.png "点击放大")

## 背景知识

[自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

onWillDismiss：交互式关闭回调函数。当用户执行点击遮罩层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。

[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：当用户点击返回按钮时触发（仅router路由页面生效）。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。

## 问题定位

根据HiLog日志进行定位。

1. 在日志中检索关键字onBackPress，如下日志信息：

   ```shell
   06-30 17:46:01.290   13720-13840   C0420C/应用包名/WMSEvent       应用包名  I     [] HandleBackEvent(3975): called
   06-30 17:46:01.290   13720-13840   C03900/应用包名/Ace            应用包名  I     [(-1:100000:singleton)] [com.zhuawa.form.harm][entry][100000]: OnBackPressed called
   06-30 17:46:01.290   13720-13720   C03903/应用包名/AceSubWindow   应用包名  W     [(-2:100000:singleton)] Fail to find subwindow in subwindowMap_, instanceId is 100000.
   06-30 17:46:01.290   13720-13720   C03953/应用包名/SelectOverlay  应用包名  I     [(100000:100000:scope)] isDestroyed:0,isClosed:0
   06-30 17:46:01.291   13720-13720   C03900/应用包名/Ace            应用包名  E     [(100000:100000:scope)] Error calling onBackPress
   ```

   根据日志信息，发现有OnBackPressed called则说明侧滑事件被触发。但是，在后续日志中，根据关键字“onBackPress return true”未检索到相关信息，表明开发者未在代码中重写onBackPress方法。
2. 继续观察后续日志，发现有如下的日志信息：

   ```shell
   06-30 17:46:01.326   13720-13840   C03900/应用包名/Ace        应用包名  I     [(-1:100000:singleton)] [com.zhuawa.form.harm][entry][100000]: window unfocus
   06-30 17:46:01.326   13720-13822   C01332/应用包名/UIAbility  应用包名  I     [ui_ability_thread.cpp:323]name:EntryAbility,targeState:6,isNewWant:0
   06-30 17:46:01.326   13720-13720   C03900/应用包名/Ace        应用包名  I     [(100000:100000:scope)] Update application state , state: ON_INACTIVE
   06-30 17:46:01.326   13720-13720   C0391C/应用包名/AceFocus   应用包名  I     [(100000:100000:scope)] Window id: 197 lost focus.
   06-30 17:46:01.333   13720-13720   C03900/应用包名/Ace        应用包名  I     [(-2:100000:singleton)] [com.zhuawa.form.harm][entry][100000]: window background
   ```

   日志显示window unfocus和window background的相关信息，说明此时应用已经退出到后台。
3. 继续观察日志，发现有如下日志信息：

   ```shell
   10-25 09:51:12.580   43822-43822   C01332/com.hua...ion/UIAbility  com.huawe...lication  I     [ui_ability_impl.cpp:434]Lifecycle:Call
   10-25 09:51:12.580   43822-43822   C03900/com.hua...plication/Ace  com.huawe...lication  I     [(-2:100000:singleton)] [com.huawei.dota2.myapplication][entry][100000]: window foreground
   10-25 09:51:12.580   43822-43822   C03900/com.hua...plication/Ace  com.huawe...lication  I     [(100000:100000:scope)] Update application state , state: ON_SHOW
   10-25 09:51:12.580   43822-43822   C03922/com.hua...AceNavigation  com.huawe...lication  I     [(100000:100000:scope)] custom dialog onShow
   ```

   可以看到有window foreground、Update application state , state: ON\_SHOW、ability state: foreground，说明此时应用被拉起到前台。同时，根据日志custom dialog onShow，表明当前展示了一个自定义弹窗页面。

## 分析结论

应用在onBackPress侧滑退出过程中，系统显示了一个自定义弹窗。该自定义弹窗未处理侧滑事件，当应用再次被拉起至前台时，该弹窗会被展示。

## 修改建议

根据应用当前表现的现象，其期望实现的效果是当用户进行侧滑操作时，弹出确认退出的弹窗。用户点击确认，应用退出，当用户点击取消或进行侧滑时，关闭弹窗，应用不退出。

参考如下的示例代码：

```ts
import { common } from '@kit.AbilityKit';

// 自定义弹窗，确认用户是否退出应用
@CustomDialog
struct CustomDialogExample {
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('确认退出')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .margin({
          top: 25,
          bottom: 10
        })
      Row() {
        Button('取消')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
            }
          })
          .backgroundColor(0xffffff)
          .fontColor(0x0A59F7)
          .margin({left:50})
        Text('|').fontColor(0xc1c2c4).fontWeight(FontWeight.Lighter)
        Button('确认')
          .fontColor(0x0A59F7)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            context.terminateSelf();
          })
          .backgroundColor(0xffffff)
          .margin({right:50})
          // .backgroundColor(0x0A59F7)
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround)
      .margin(20)
    }
    .backgroundColor(0xffffff)
    .height('20%')
  }
}

@Entry
@Component
struct S2CFK20250630191612363971 {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4];

  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      }
    }),
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      // 1、PRESS_BACK    点击三键back、侧滑（左滑/右滑）、键盘ESC。
      // 2、TOUCH_OUTSIDE    点击遮障层时
      // 3、CLOSE_BUTTON    点击关闭按钮
      if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
        // ...
        // 处理业务逻辑后通过dismiss主动关闭对话框
      }
      if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
        // ...
        // 处理业务逻辑后通过dismiss主动关闭对话框
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: 0 }
  });

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  onBackPress() {
    this.dialogController.open();
    return true;
  }

  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item?:number|undefined) => {
          if (item) {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xDCDCDC)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }
        }, (item:number) => item.toString())
      }.width('100%')
    }
    .backgroundColor(0xFFFFFF)
    .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}
```
