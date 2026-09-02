---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-554
title: 自定义弹窗键盘避让问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义弹窗键盘避让问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b39a0e354fa5af43bb17a4972ea14dd51a25e0402a0bc9f6e592aa7fb6d12692
---

## 问题现象

在CustomDialog弹框中存在输入框，系统软键盘弹出后，CustomDialog会进行安全区域避让。

1. 预期效果：系统软键盘弹出后，弹框进行安全避让，但仍然紧贴软键盘边缘。
2. 实际效果：系统软键盘弹出后，出现键盘与输入框分离的情况。

预期效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/WyCKadshTSeqEhlJ0PXNDg/zh-cn_image_0000002658910905.png "点击放大")

实际效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/EAaxGdpkR4mhjItopPjK5w/zh-cn_image_0000002658790957.png "点击放大")

## 背景知识

[自定义弹出框 (CustomDialog)](../harmonyos-guides/arkts-common-components-custom-dialog.md)：CustomDialog是自定义弹窗，可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹窗。具体用法请参考[自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)。

[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)：安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠，默认情况下开发者开发的界面都被布局在安全区域内，通过设置[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)来配置软键盘抬起时页面的避让模式。

## 问题定位

弹窗与软键盘始终有间隙：自定义弹窗仅适用于简单提示场景，不能替代页面使用。为了避免组件覆盖，系统规格设计软键盘的安全间距为16vp，导致键盘抬起时弹窗与键盘之间有高度为16vp的空白区域。

## 分析结论

根据上述分析出的问题可知，若想实现弹窗避让键盘且紧贴键盘的效果，可以给组件设置position、offset等属性，将高度/偏移量完全固定，若输入文字的过程中模块高度发生变化，弹窗模块仍然会被短暂顶起，可根据键盘高度和内容变化实时调整弹窗位置，动态适配键盘高度。

## 修改建议

* 方法一、用[offset](../harmonyos-references/js-apis-arkui-componentutils.md#offset)属性设置弹窗整体向下偏移16vp。

  **说明** 

  弹窗高度加上键盘高度大于屏幕高度时，弹窗会被压缩导致显示异常，不适用此方案，请选择方案二、方案三。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct CustomDialogPage {
    private message: string = 'CustomDialogPage';
    customDialogController: CustomDialogController = new CustomDialogController({
      builder: CustomEditDialogWidget({
        inputType: InputType.Normal,
        textInputConString: () => {
        }
      }),
      alignment: DialogAlignment.Bottom,
      maskColor: Color.White,
      customStyle: true
    });

    build() {
      Row() {
        Column() {
          Button(this.message).onClick(() => {
            this.customDialogController.open();
          });
        }
        .width('100%');
      }
      .height('100%');
    }
  }

  @CustomDialog
  @Component
  export struct CustomEditDialogWidget {
    controller?: CustomDialogController;
    @State textInputString: string = '';
    textInputConString = () => {
    };
    inputType: InputType = InputType.Normal;

    build() {
      Column() {
        Column() {
          Text('顶部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');

        TextArea({ placeholder: `请输入您的详细信息` })
          .margin({ left: 18, right: 18 })
          .defaultFocus(true)
          .onChange((value: string) => {
            this.textInputString = value;
          });
        Column() {
          Text('底部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Start)
      .width('calc(100% - 32vp)')
      .height(400)
      .borderRadius(10)
      .backgroundColor('#f1f3f5')
      .offset({ x: 0, y: 16 });
    }
  }
  ```
* 方法二、动态判断软键盘高度，并基于软键盘高度调整自定义弹窗的外边距尺寸。

  在自定义弹窗的aboutToAppear生命周期接口中，监听键盘的拉起和隐藏，获取键盘的高度，并将高度动态赋值给弹窗根容器的底部外边距，实现弹窗避让软键盘。

  **说明** 

  **注意：必须设置自定义弹窗不自动避让软键盘（KeyboardAvoidMode.NONE），否则弹窗会出现不符合预期的顶起。**

  示例代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct CustomDialogPage {
    private message: string = 'CustomDialogPage';
    customDialogController: CustomDialogController = new CustomDialogController({
      builder: CustomEditDialogWidget({
        textInputConString: () => {
        }
      }),
      alignment: DialogAlignment.Bottom,
      // 自定义弹窗偏移量设为0
      offset: { dx: 0, dy: 0 },
      autoCancel: true,
      maskColor: Color.White,
      customStyle: true,
      // 必须设置自定义弹窗不自动避让软键盘，否则弹窗会出现不符合预期的顶起
      keyboardAvoidMode: KeyboardAvoidMode.NONE
    });

    build() {
      Row() {
        Column() {
          Button(this.message).onClick(() => {
            this.customDialogController.open();
          });
        }
        .width('100%');
      }
      .backgroundColor(Color.White)
      .height('100%');
    }
  }

  @CustomDialog
  @Component
  export struct CustomEditDialogWidget {
    controller?: CustomDialogController;
    textInputConString = () => {
    };
    @State private keyboardHeight: number = 0;
    private context: Context = this.getUIContext().getHostContext() as Context;

    aboutToAppear(): void {
      window.getLastWindow(this.context).then(currentWindow => {
        currentWindow.on('avoidAreaChange', data => {
          if (data.type === window.AvoidAreaType.TYPE_KEYBOARD) {
            // 获取软键盘高度
            this.keyboardHeight = this.getUIContext().px2vp(data.area.bottomRect.height);
          }
        });
      });
    }

    build() {
      Column() {
        Column() {
          Text('顶部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');

        TextArea({ placeholder: `请输入您的详细信息` })
          .margin({ left: 18, right: 18 })
          .defaultFocus(true);
        Column() {
          Text('底部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Start)
      .width('calc(100% - 32vp)')
      .height(400)
      .margin({ bottom: this.keyboardHeight })
      .borderRadius(10)
      .backgroundColor('#f1f3f5');
    }
  }
  ```
* 方法三：从API version 15开始，可通过[keyboardAvoidDistance](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)设置弹窗避让键盘后，和键盘之间的距离。

  示例代码如下：

  ```ts
  import { LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct CustomDialogPage {
    private message: string = 'CustomDialogPage';
    customDialogController: CustomDialogController = new CustomDialogController({
      builder: CustomEditDialogWidget({
        textInputConString: () => {
        }
      }),
      alignment: DialogAlignment.Bottom,
      // 自定义弹窗偏移量设为0
      offset: { dx: 0, dy: 0 },
      autoCancel: true,
      maskColor: Color.White,
      customStyle: true,
      keyboardAvoidDistance: LengthMetrics.px(0)
    });

    build() {
      Row() {
        Column() {
          Button(this.message).onClick(() => {
            this.customDialogController.open();
          });
        }
        .width('100%');
      }
      .backgroundColor(Color.White)
      .height('100%');
    }
  }

  @CustomDialog
  @Component
  export struct CustomEditDialogWidget {
    controller?: CustomDialogController;
    textInputConString = () => {
    };

    build() {
      Column() {
        Column() {
          Text('顶部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');

        TextArea({ placeholder: `请输入您的详细信息` })
          .margin({ left: 18, right: 18 })
          .defaultFocus(true);
        Column() {
          Text('底部内容');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('45%');
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Start)
      .width('calc(100% - 32vp)')
      .height(400)
      .borderRadius(10)
      .backgroundColor('#f1f3f5');
    }
  }
  ```

## 总结

| 方法 | 特性 | 适用场景 |
| --- | --- | --- |
| 方法一：使用offset设置固定间距 | 简单易用，固定间距，适配性差 | 键盘高度固定的场景 |
| 方法二：动态监听键盘高度调整外边距 | 精准适配键盘高度，需监听事件 | 多设备/动态键盘场景 |
| 方法三：API15+的keyboardAvoidDistance | 系统能力实现，最为简单高效 | 新版本设备 |
