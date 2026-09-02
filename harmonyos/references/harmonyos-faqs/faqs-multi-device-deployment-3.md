---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-3
title: 弹窗页面文本重叠
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 常见问题 > 弹窗页面文本重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:52b76f21442f9b3428b63368cd6cae8d5f16b1cdfd5779e50e04dbe66c453ff1
---

## 问题现象

进入应用后，弹窗页面内文本有重叠。问题效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/H9Rptdp8QCaOMR5A7bpu-g/zh-cn_image_0000002658911719.png "点击放大")

## 背景知识

* [Text组件](../harmonyos-references/ts-basic-components-text.md)用于一段文本的显示。可以通过设置[fontSize](../harmonyos-references/ts-basic-components-text.md#fontsize)和[lineHeight](../harmonyos-references/ts-basic-components-text.md#lineheight)等属性，调整文本的样式。
* [断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)：将窗口宽度划分为不同的范围（即断点），监听窗口尺寸变化，当断点改变时同步调整页面布局。

## 问题定位

1. 检查是否有对不同的窗口尺寸设置断点。
2. 排查文本是否设置了组件换行、宽高、裁剪显示等属性，避免互相影响。

## 分析结论

应用没有针对窗口尺寸设置断点，且由于Text组件设置了固定的lineHeight，在窗口尺寸和字体大小发生变化时，超出lineHeight高度，导致文本重叠。

## 修改建议

1. 通过工具类BreakpointType为属性赋值。
2. 根据窗口尺寸大小，设置不同的lineHeight。

   ```ts
   export class BreakpointType<T> {
     sm: T;
     md: T;
     lg: T;

     constructor(sm: T, md: T, lg: T) {
       this.sm = sm;
       this.md = md;
       this.lg = lg;
     }

     getValue(currentHeightBreakpoint: HeightBreakpoint): T {
       if (currentHeightBreakpoint === HeightBreakpoint.HEIGHT_LG) {
         return this.lg;
       } else if (currentHeightBreakpoint === HeightBreakpoint.HEIGHT_MD) {
         return this.md;
       } else {
         return this.sm;
       }
     }
   }

   @CustomDialog
   @Component
   struct CustomDialogExample {
     controller?: CustomDialogController;
     breakpoint: BreakpointType<number> = new BreakpointType(28, 36, 36);
     @Prop currentWidthBreakpoint: HeightBreakpoint;

     build() {
       Scroll() {
         Flex({ direction: FlexDirection.Column }) {
           Text() {
             Span('Customer Dialog Content. \n');
             Span('Customer Dialog Content. Customer Dialog Content. \n');
             Span('Customer Dialog Content. Customer Dialog Content. Customer Dialog Content. ');
           }
           .textAlign(TextAlign.Center)
           .fontSize('25fp')
           .lineHeight(this.breakpoint.getValue(this.currentWidthBreakpoint))
           .margin(24);
         };
       }
       .height('40%');
     }
   }

   @Entry
   @Component
   struct CustomDialogUser {
     @State currentHeightBreakpoint: HeightBreakpoint = this.getUIContext().getWindowHeightBreakpoint();
     dialogController: CustomDialogController | null = new CustomDialogController({
       builder: CustomDialogExample({ currentWidthBreakpoint: this.currentHeightBreakpoint }),
       cancel: this.exitApp,
       autoCancel: true,
       onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
         console.info('reason=' + JSON.stringify(dismissDialogAction.reason));
         console.log('dialog onWillDismiss');
         if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
           dismissDialogAction.dismiss();
         }
         if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
           dismissDialogAction.dismiss();
         }
       },
       alignment: DialogAlignment.Center,
       gridCount: 4,
       customStyle: false,
       cornerRadius: 10
     });

     // 在自定义组件即将析构销毁时将dialogController置空
     aboutToDisappear() {
       this.dialogController = null; // 将dialogController置空
     }

     exitApp() {
       console.info('Click the callback in the blank area');
     }

     aboutToAppear(): void {
       this.dialogController?.open();
     }

     build() {
     }
   }
   ```
