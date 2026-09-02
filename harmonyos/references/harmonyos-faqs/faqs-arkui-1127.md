---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1127
title: 多个弹窗链式调用时失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 多个弹窗链式调用时失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0456dab4b65cfc4326f2b260fa5ea63c36e7be545f3c64bf965009eaa19a3e5c
---

## 问题现象

使用CustomDialog实现多个弹窗链式调用时，当在第一个弹窗中打开第二个弹窗时，第二个弹窗未能正确显示，实际显示的还是第一个弹窗的内容。

错误代码如下：

```ts
@CustomDialog
struct MyDialog1 {
  controller1: CustomDialogController
  controller2: CustomDialogController
  title: string=''
  build() {
    Row() {
      Column({ space: 10 }) {
        Text(this.title)
          .fontSize(30)
          .fontColor(Color.Blue)
        Button('点击打开弹窗2')
          .onClick(() => {
            this.controller2.open()
          }).backgroundColor(0xffffff).fontColor(Color.Red)
        Flex({ justifyContent: FlexAlign.SpaceAround }) {
          Button('cancel')
            .onClick(() => {
              this.controller1.close()
            }).backgroundColor(0xffffff).fontColor(Color.Black)
        }.width('100%')
      }.width('50%')
    }.height('50%')
  }
}
// 弹窗组件
@CustomDialog
struct MyDialog2 {
  controller: CustomDialogController
  title: string=''
  build() {
    Row() {
      Column({ space: 10 }) {
        Text(this.title)
          .fontSize(30)
          .fontColor(Color.Blue)
        Flex({ justifyContent: FlexAlign.SpaceAround }) {
          Button('cancel')
            .onClick(() => {
              this.controller.close()
            }).backgroundColor(0xffffff).fontColor(Color.Black)
          Button('confirm')
            .onClick(() => {
              this.controller.close()
            }).backgroundColor(0xffffff).fontColor(Color.Red)
        }.width('100%')
      }.margin({ bottom: 10 })
    }.height('50%')
  }
}
@Entry
@Component
struct DialogTest {
  @State dialogTitle: string = ''
  @State dialogData: string = ''
  dialogController2: CustomDialogController = new CustomDialogController({
    builder: MyDialog2({
      title: '弹窗2',
    }),
    customStyle: false
  })
  dialogController1: CustomDialogController = new CustomDialogController({
    builder: MyDialog1({
      controller2: this.dialogController2,
      title: '弹窗1',
    }),
    customStyle: false
  })
  build() {
    Row() {
      Column({ space: 10 }) {
        Button('点击打开弹窗1')
          .onClick(() => {
            this.dialogController1.open()
          })
      }.width('100%')
    }.height('100%')
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/umaikSFoTFGIavqJEX1Eow/zh-cn_image_0000002658808785.png "点击放大")

## 背景知识

* HarmonyOS使用[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)类显示自定义弹窗，可通过[open](../harmonyos-references/ts-methods-custom-dialog-box.md#open)方法显示自定义弹窗内容，[close](../harmonyos-references/ts-methods-custom-dialog-box.md#close)方法关闭显示的自定义弹窗。
* [@ohos.promptAction](../harmonyos-references/js-apis-promptaction.md)是用于创建和管理弹窗（如提示、确认、输入框等）的模块，支持用户交互操作，常用于弹出提示信息、确认操作或收集用户输入。

## 问题定位

CustomDialog的打开与关闭都与CustomDialog的CustomDialogController有关，当多个弹窗链式调用时会存在多个CustomDialogController，会出现上述问题的原因可能是由于使用了错误的CustomDialogController，或未将指向自己的controller置于最后导致打开了错误的弹窗。根据上述错误代码中：

```ts
controller1: CustomDialogController
controller2: CustomDialogController
```

错误的弹窗是由于未将自身的controller放置于其它controller之后。

## 分析结论

在CustomDialog中传入多个其他的controller，以实现在CustomDialog中打开另一个或另一些CustomDialog，那么此处需要将指向自己的controller放在所有controller的后面。

## 修改建议

为了正确的实现弹窗的嵌套使用，可以通过以下方式实现：

* 使用CustomDialog，将被嵌套的弹窗的CustomDialogController放置于上一层弹窗中实现嵌套使用，需要注意的是要将指向自己的controller放在其它所有controller的后面。具体可参考示例：[弹出嵌套弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#示例1弹出嵌套弹窗)。
* 实现弹窗链式调用也可使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)实例，再通过此实例调用方法[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)，通过builder参数传入不同弹窗页面，使用示例如下：

  ```ts
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    private customDialogComponentId: number = 0;
    private customDialogComponentTwoId: number = 0;
    private promptAction: PromptAction = this.getUIContext().getPromptAction();

    @Builder
    customDialogComponentTwo() {
      Column() {
        Text('第二个弹窗');
        Button('关闭弹窗').onClick(() => {
          // 记录当前弹窗ID
          this.promptAction.closeCustomDialog(this.customDialogComponentTwoId);
        });
      };
    }

    @Builder
    customDialogComponent() {
      Column() {
        Text('第一个弹窗').fontSize(30);
        Text('打开第二个弹窗')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              width: '70%',
              builder: () => {
                this.customDialogComponentTwo();
              }
            })
              .then((dialogId: number) => {
                // 记录当前弹窗ID
                this.customDialogComponentTwoId = dialogId;
              });
          });
        Row({ space: 50 }) {
          Button('关闭弹窗').onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          });
        };
      }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween);
    }

    build() {
      Row() {
        Column({ space: 20 }) {
          Text('打开第一个弹窗')
            .fontSize(30)
            .onClick(() => {
              this.promptAction.openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
              }).then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              });
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

## 总结

上述两种方案都可实现弹窗链式调用，具体如何选用，可根据下表结合自身需求进行选择：

| 方式 | CustomDialog | promptAction |
| --- | --- | --- |
| 注意点 | 通过CustomDialog实现嵌套弹窗，需要注意将指向自己的controller放在其它所有controller的后面。 | promptAction实现嵌套弹窗无需注册controller，在使用弹窗时只需要在需要弹出的事件中使用PromptAction对象的openCustomDialog函数。 |
| 优点 | CustomDialog具有更高的自定义控制能力。 | promptAction使用更加方便。 |
