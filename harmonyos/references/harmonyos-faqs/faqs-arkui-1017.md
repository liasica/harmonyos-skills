---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1017
title: 自定义嵌套弹窗统一关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义嵌套弹窗统一关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e8eb359ae06c62a65859774acb8c423598431dd30f32ea5d3ca7b3485000af0c
---

## 问题现象

多个自定义嵌套弹窗，如何实现一键全部关闭。

## 背景知识

* [自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
* [onCreate](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)：当UIExtensionAbility组件实例完成创建时，系统会触发该回调。开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。

## 解决方案

通过HarmonyOS中的一个UIAbility类实现，使用AppStorage存储全局的弹窗控制器数组DialogList，实现跨页面、跨组件数据共享。并通过事件总线实现“添加弹窗”和“关闭所有弹窗”的跨组件通信。

代码示例如下：

```ts
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  console.info(`want:${want}`);
  console.info(`launchParam:${launchParam}`);
  let eventhub = this.context.eventHub;
  AppStorage.setOrCreate('dialogList', []);
  eventhub.on('addDiaLog', (data: CustomDialogController) => {
    let dialogList: SubscribedAbstractProperty<CustomDialogController[]> = AppStorage.link('dialogList');
    let dialoginfo: CustomDialogController[] = dialogList.get();
    dialoginfo.push(data);
    dialogList.set(dialoginfo);
  });
  eventhub.on('closeAllDiaLog', () => {
    let dialogList: SubscribedAbstractProperty<CustomDialogController[]> = AppStorage.link('dialogList');
    let dialoginfo: CustomDialogController[] = dialogList.get();
    for (let elem of dialoginfo.values()) {
      elem.close();
    }
  });
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
}
```

通过实现两个可交互的自定义弹窗，并通过按钮触发弹窗的打开与关闭、事件监听及数据传递。完整示例代码如下：

```ts
// Index.ets文件
import common from '@ohos.app.ability.common';

@CustomDialog
struct CustomDialogExampleTwo {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  controllerTwo?: CustomDialogController;

  build() {
    Column() {
      Text('我是第二个弹窗')
        .fontSize(30);
      Button('点我关闭所有弹窗')
        .onClick(() => {
          this.context.eventHub.emit('closeAllDiaLog');
        })
        .margin(20);
    };
  }
}

@CustomDialog
struct CustomDialogExample {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @Link textValue: string;
  @Link inputValue: string;
  dialogControllerTwo: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExampleTwo(),
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -25 }
  });
  controller?: CustomDialogController;
  // 若尝试在CustomDialog中传入多个其他的Controller，以实现在CustomDialog中打开另一个或另一些CustomDialog，那么此处需要将指向自己的controller放在所有controller的后面
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  aboutToAppear() {
    this.context.eventHub.emit('addDiaLog', this.dialogControllerTwo);
  }

  build() {
    Column() {
      Text('Change text').fontSize(20).margin({ top: 10, bottom: 10 });
      TextInput({ placeholder: '', text: this.textValue }).height(60).width('90%')
        .onChange((value: string) => {
          this.textValue = value;
        });
      Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 });
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('cancel')
          .onClick(() => {
            if (this.controller != undefined) {
              this.controller.close();
              this.cancel();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Black);
        Button('confirm')
          .onClick(() => {
            if (this.controller != undefined) {
              this.inputValue = this.textValue;
              this.controller.close();
              this.confirm();
            }
          }).backgroundColor(0xffffff).fontColor(Color.Red);
      }.margin({ bottom: 10 });

      Button('点我打开第二个弹窗')
        .onClick(() => {
          if (this.dialogControllerTwo != null) {
            this.dialogControllerTwo.open();
          }
        })
        .margin(20);
    }.borderRadius(10);

    // 如果需要使用border属性或cornerRadius属性，请和borderRadius属性一起使用。
  }
}

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private textValue: string = '';
  private inputValue: string = 'click me';
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      },
      textValue: $textValue,
      inputValue: $inputValue
    }),
    cancel: this.exitApp,
    autoCancel: true,
    alignment: DialogAlignment.Bottom,
    offset: { dx: 0, dy: -20 },
    gridCount: 4,
    customStyle: false,
    cornerRadius: 10,
  });

  aboutToAppear() {
    this.context.eventHub.emit('addDiaLog', this.dialogController);
  }

  // 在自定义组件即将析构销毁时将dialogControlle置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  exitApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button(this.inputValue)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff);
    }.width('100%').margin({ top: 5 });
  }
}
```
