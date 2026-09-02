---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-936
title: 列表选择弹窗ActionSheet的sheets属性无法实时更新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 列表选择弹窗ActionSheet的sheets属性无法实时更新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:77fb14550b73ece5f1170d654818b10d85f9a34e34e18d72130034f4f5bdf172
---

## 问题现象

动态改变列表选择弹窗ActionSheet的sheets属性，弹窗内容无法实时更新。问题代码示例参考如下：

```ts
@Entry
@Component
struct showActionSheetExample {
  @State sheets: Array<SheetInfo> = [{
    title: 'apples',
    action: () => {
    }
  }];
  @State count: number = 0;

  build() {
    Column() {
      Button('showActionSheet')
        .margin(30)
        .onClick(() => {
          setInterval(() => {
            this.count++;
            this.sheets.push({
              title: 'bananas' + this.count,
              action: () => {
              }
            });
          }, 1000);

          this.getUIContext().showActionSheet({
            title: 'ActionSheet title',
            message: 'message',
            confirm: {
              value: 'Confirm button',
              action: () => {
                console.info('Get Alert Dialog handled');
              }
            },
            alignment: DialogAlignment.Center,
            sheets: this.sheets
          });
        });
    }.width('100%');
  }
}
```

## 背景知识

* [列表选择弹窗 (ActionSheet)](../harmonyos-guides/arkts-fixes-style-dialog.md#列表选择弹出框-actionsheet)是一个列表选择器弹窗适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时。固定样式，当用户需要关注或确认的信息存在列表选择时使用。
* 当用户需要自定义弹出框内动态更新弹出框属性和内容时，使用[不依赖UI组件的自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)。存在两种入参方式创建自定义弹出框：
  + openCustomDialog（传参为ComponentContent形式）：通过ComponentContent封装内容可以与UI界面解耦，调用更加灵活，可以满足开发者的封装诉求。具有较高的灵活性，弹出框样式完全自定义，并且在弹出框打开后可以使用updateCustomDialog方法动态更新弹出框的参数。
  + openCustomDialog（传builder的形式）：相对于ComponentContent，builder必须要与上下文做绑定，与UI存在一定耦合。此方法有默认的弹出框样式，适合于开发者想要实现与系统弹窗默认风格一致的效果。

## 问题定位

在showActionSheet打开列表选择弹窗后，对sheets属性进行动态修改，弹窗UI未变化。

## 分析结论

ActionSheet列表选择弹窗不支持动态更新属性，需要通过自定义弹出框实现。

## 修改建议

下面通过openCustomDialog实现，并且以传builder的形式为例，实现动态更新自定义弹出框的内容。

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private customDialogComponentId: number = 0;
  @State count: number = 0;
  intervalId?: number;

  @Builder
  customDialogComponent() {
    Column() {
      Text('充电详情').fontSize(25);
      Text(`已充电时间：${this.count}秒`);
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          clearInterval(this.intervalId);
        });
        Button('取消').onClick(() => {
          this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          clearInterval(this.intervalId);
        });
      };
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceAround);
  }

  build() {
    Row() {
      Column({ space: 20 }) {
        Text('组件内弹窗')
          .fontSize(30)
          .onClick(() => {
            this.getUIContext()
              .getPromptAction()
              .openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                }
              })
              .then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              })
              .catch((error: BusinessError) => {
                console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
              });

            this.intervalId = setInterval(() => {
              this.count++;
            }, 1 * 1000);
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
