---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-678
title: 如何在横屏时从右边弹出半模态页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在横屏时从右边弹出半模态页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7028f923e561cd56672df40c07ec470537f9bd4f2652ce469e9636a22d114a1d
---

## 问题现象

组件使用bindSheet属性绑定半模态页面，竖屏时，半模态页面从底部弹出，期望应用在横屏时，从右边弹出半模态页面。

## 背景知识

通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。点击后默认从底部弹出模态页面。

## 解决方案

1. 半模态在竖屏时可以满足要求，但在横屏时不能从右边弹出，需要和自定义弹窗互相搭配使用。
2. 使用媒体查询接口监听屏幕旋转。在竖屏时弹窗弹出的是半模态弹窗，横屏后弹出的是自定义弹窗。代码运行前需要将[module.json5的orientation字段](../best-practices/bpta-landscape-and-portrait-development.md#section1188593118171)配置成auto\_rotation,让屏幕随传感器旋转。

完整示例参考如下：

```ts
import { mediaquery } from '@kit.ArkUI';

@Component
struct MenuExample {
  @State list: string[] = ['共享屏幕', '聊天', '举手'];

  build() {
    Column() {
      Column() {
        ForEach(this.list, (item: string) => {
          Text(item).fontSize(16).margin({ bottom: 30 });
        });
      }
      .alignItems(HorizontalAlign.Center);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}

// 自定义弹窗
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    MenuExample();
  }
}

@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false; // 控制半模态弹窗
  @State showType: number = 0; // 0没有弹窗，1竖屏弹窗打开，2横屏弹窗打开
  @State matches: boolean = false; // false竖屏
  // 监听横屏事件，mediaquery.matchMediaSync接口已废弃，建议使用this.getUIContext().getMediaQuery().matchMediaSync()来获取
  listener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample(),
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
        this.showType = 0;
      }
      dismissDialogAction.dismiss(); // 注册dismiss行为
    },
    autoCancel: true,
    alignment: DialogAlignment.CenterEnd,
    cornerRadius: 20,
    width: '30%',
    height: '100%',
  });

  ChangeWindow() {
    if (this.showType !== 0) {
      if (this.matches) {
        // 横屏时，关闭竖屏弹窗，打开横屏弹窗
        this.isShow = false;
        if (this.dialogController != null) {
          this.dialogController.open();
        }
      } else {
        // 竖屏时，关闭横屏弹窗，打开竖屏弹窗
        this.isShow = true;
        if (this.dialogController != null) {
          this.dialogController.close();
        }
      }
    }
  }

  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
    this.matches = mediaQueryResult.matches;
    this.ChangeWindow();
  }

  aboutToAppear(): void {
    // 注册回调
    let portraitFunc = (mediaQueryResult: mediaquery.MediaQueryResult): void =>
    this.onPortrait(mediaQueryResult);
    // 绑定回调函数
    this.listener.on('change', portraitFunc);
  }

  aboutToDisappear(): void {
    this.listener.off('change'); // 取消注册回调
    this.dialogController = null; // 将dialogController置空
  }

  @Builder
  myBuilder() {
    MenuExample();
  }

  build() {
    Column() {
      Button('显示弹窗')
        .onClick(() => {
          this.showType = this.matches ? 2 : 1;
          this.ChangeWindow();
        })
        .fontSize(20);
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .bindSheet($$this.isShow, this.myBuilder(), {
      height: 300,
      onWillDismiss: ((dismissSheetAction: DismissSheetAction) => {
        if (dismissSheetAction.reason === DismissReason.SLIDE_DOWN) {
          this.showType = 0;
        }
        dismissSheetAction.dismiss(); // 注册dismiss行为
      }),
    });
  }
}
```
