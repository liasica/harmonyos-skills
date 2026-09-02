---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-546
title: 应用退到后台后重新打开，会弹出相同的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用退到后台后重新打开，会弹出相同的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05b892831f16ea49d139ac3f6a98fcd5ae0157ac637a8208bf96bc78c2746691
---

## 问题现象

弹出弹窗后，应用每次退到后台后重新打开，都会再次生成弹窗，并堆叠在之前的弹窗上，导致需要多次点击相同弹窗。

## 背景知识

* [Tabs](../harmonyos-guides/arkts-navigation-tabs.md)：Tabs组件的页面组成包含两个部分，分别是TabContent和TabBar。TabContent是内容页，TabBar是导航页签栏。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)：aboutToAppear函数在创建自定义组件的新实例后，在执行其build()函数之前执行。
* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)：每次显示页面时触发一次，包括路由跳转、应用进入前台等场景。
* [onWillShow](../harmonyos-references/ts-container-tabcontent.md#onwillshow12)：TabContent将要显示的时候触发该回调。场景包括TabContent首次显示，TabContent切换，页面切换，窗口前后台切换。

## 问题定位

1. 首先排查弹出弹窗的逻辑是否写在页面的onPageShow()生命周期中，如：

   ```ts
   onPageShow(){
     dialogController.open();
   }
   ```
2. 若未在onPageShow()中实现弹出弹窗逻辑，且页面定义在TabContent组件中，可进一步排查开启弹窗的逻辑是否写在TabContent组件的onWillShow()方法中，如：

   ```ts
   Tabs(){
     TabContent(){
       // 页面内容
     }
     .onWillShow(() => {
       dialogController.open();
     })
   }
   ```

## 分析结论

1. 弹出弹窗逻辑实现在页面的onPageShow()生命周期中，导致每次打开应用都会重新生成弹窗。
2. 弹出弹窗逻辑实现在页面所在TabContent的onWillShow()方法中，导致每次打开应用都会重新生成弹窗。

## 修改建议

以上两个结论均可以通过将弹出弹窗逻辑实现在页面的aboutToAppear()生命周期中得到解决。

示例代码如下：

```ts
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Text('这是弹窗')
        .fontSize(20)
        .height(100)
      Button('点我关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct S2CFK20250709111725583112 {
  @State message: string = '弹窗';
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      }
    }),
    cancel: this.existApp,
    autoCancel: true,
    alignment: DialogAlignment.Center,
    width: 300,
    height: 200,
    backgroundColor: Color.White,
    shadow: ({
      radius: 20,
      color: Color.Grey,
      offsetX: 50,
      offsetY: 0
    }),
  });

  aboutToAppear(): void {
    if (this.dialogController != null) {
      this.dialogController.open();
    }
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Text(this.message)
        .id('S2CFK20250709111725583112HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
