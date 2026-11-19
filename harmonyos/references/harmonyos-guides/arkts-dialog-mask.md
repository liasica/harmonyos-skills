---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-mask
title: 弹出框蒙层控制
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框蒙层控制
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a44f6035ec8d934e0d3989c73e548db4f66430fcd6a659ab1d3ad3801878d82b
---

开发者对弹出框的定制不仅限于弹出框里的内容，对弹出框蒙层的定制需求也逐渐增加。本文介绍ArkUI弹出框的蒙层控制，包括点击蒙层时是否消失、蒙层区域、蒙层颜色和蒙层动画等特性。

## 使用约束

ArkUI提供多种弹出框，不同类型的弹出框具备不同的蒙层定制能力。详情请参阅下表：

| 接口&组件 | autoCancel | maskRect | isModal | immersiveMode |
| --- | --- | --- | --- | --- |
| [openCustomDialog](arkts-uicontext-custom-dialog.md) | 支持 | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 | 支持 |
| [presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18) | 支持 | 支持 | 支持 | 支持 |
| [updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12) | 支持 | 不支持 | 不支持 | 不支持 |
| [CustomDialog](arkts-common-components-custom-dialog.md) | 支持 | 支持 | 支持 | 支持 |
| [showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog) | 不支持 | 支持 | 支持 | 支持 |
| [showAlertDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showalertdialog) | 支持 | 支持 | 支持 | 支持 |
| [showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet) | 支持 | 支持 | 支持 | 支持 |
| [showActionMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu11) | 不支持 | 不支持 | 支持 | 支持 |
| [showDatePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showdatepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md) | 不支持 | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtimepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [showTextPickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtextpickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |

**说明** 

* 设置autoCancel参数，可控制弹出框蒙层被点击时是否消失。
* 设置maskRect参数，可定制弹出框的蒙层的大小和位置。此外，蒙层范围内的事件无法透传，而蒙层范围外的事件可以透传。
* 设置isModal参数，可定制弹出框的模态状态：非模态弹出框无蒙层，支持与周围组件交互；模态弹出框有蒙层，禁止与周围组件交互。
* 从API version 15开始，当levelMode属性设置为LevelMode.EMBEDDED时，设置immersiveMode参数，可定制弹出框蒙层是否延伸至状态栏及导航栏。

| 接口&组件 | maskColor | transition | maskTransition |
| --- | --- | --- | --- |
| [openCustomDialog](arkts-uicontext-custom-dialog.md) | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 |
| [presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18) | 支持 | 支持 | 支持 |
| [updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12) | 支持 | 不支持 | 不支持 |
| [CustomDialog](arkts-common-components-custom-dialog.md) | 支持 | 不支持（可由openAnimation和closeAnimation替代） | 不支持 |
| [showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog) | 不支持 | 不支持 | 不支持 |
| [showAlertDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showalertdialog) | 不支持 | 支持 | 不支持 |
| [showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet) | 不支持 | 支持 | 不支持 |
| [showActionMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu11) | 不支持 | 不支持 | 不支持 |
| [showDatePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showdatepickerdialog) | 不支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md) | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtimepickerdialog) | 不支持 | 不支持 | 不支持 |
| [showTextPickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtextpickerdialog) | 不支持 | 不支持 | 不支持 |

**说明** 

* 设置maskColor参数，可定制弹出框蒙层的颜色。
* 设置openAnimation参数，可定制弹出框的进入动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
* 设置closeAnimation参数，可定制弹出框的退出动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
* 设置transition参数，可定制弹出框的进入和退出动画，同时影响蒙层动画。
* 从API version 19开始，设置maskTransition参数，可定制弹出框的蒙层动画。

## 弹出框蒙层显隐控制

通过autoCancel和isModal属性控制弹出框的蒙层显隐。

设置autoCancel为false，取消默认点击蒙层时弹窗消失。

```typescript
autoCancelOpt: promptAction.CustomDialogOptions = {
  builder: () => {
    this.myBuilder();
  },
  autoCancel: false,
} as promptAction.CustomDialogOptions;
// ...
build() {
  NavDestination() {
    Column() {
      Button('openCustomDialog autoCancel:false')
        .width('100%')
        .margin({ top: 10 })
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt);
        })

      // ...
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/dsPK-6oQT0qo9C1StNWXGQ/zh-cn_image_0000002820525075.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=77C4D5AB183E993E4DC351716B06B2FAF681BF53A9A93CEF8FF171A44D711039)

设置isModal为false，将默认的模态弹出框变为非模态弹出框。

```typescript
modalOpt: promptAction.CustomDialogOptions = {
  builder: () => {
    this.myBuilder();
  },
  isModal: false,
} as promptAction.CustomDialogOptions;
// ...
build() {
  NavDestination() {
    Column() {
      // ...
      Button('openCustomDialog isModal:false')
        .width('100%')
        .margin({ top: 10 })
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt);
        })

      // ...
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/iMTVGMJVSLS1yaWX0Yiq9Q/zh-cn_image_0000002820405075.png?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B76939092F0F5A9A6255A33775A1A365831269BB13B3F8E6D4B4E60B86B9243)

## 弹出框蒙层样式控制

该示例通过maskRect、immersiveMode和maskColor展示弹出框在蒙层样式控制方面的能力。

设置maskRect和maskColor，实现蒙层区域和蒙层颜色的设置。

```typescript
maskOpt: promptAction.CustomDialogOptions = {
  builder: () => {
    this.myBuilder();
  },
  maskRect: {
    x: 0,
    y: 10,
    width: '100%',
    height: '90%'
  },
  maskColor: '#33AA0000'
} as promptAction.CustomDialogOptions;
// ...
build() {
  NavDestination() {
    Column() {
      // ...
      Button('openCustomDialog maskOpt')
        .width('100%')
        .margin({ top: 10 })
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt);
        })

      // ...
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/oqUK4CD3TY6Mdj-PMxaJVQ/zh-cn_image_0000002791725096.png?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F7DFD1E41F57FC78350D4AEC3B1F0628E88751F92F47CB2F27AFBFA2DF762F7)

在levelMode为LevelMode.EMBEDDED下，展示不同immersiveMode对蒙层在导航栏和状态栏的延伸效果。

```typescript
  @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;
  // ···
  build() {
    NavDestination() {
      Column() {
        // ···
        Button('openCustomDialog immersiveMode')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.immersiveMode =
              this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              levelMode: LevelMode.EMBEDDED,
              immersiveMode: this.immersiveMode,
            })
          })

        // ···
      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/LhaidJp0TaqX0m6Ptct-UA/zh-cn_image_0000002791565124.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=678EFF6EE456AE01760B05AEC73C7505FD5C38D919BCA8C1FDCAA4CC5024491B)

## 弹出框蒙层动画控制

该示例通过transition和maskTransition分别展示弹出框在蒙层动画方面的能力。

设置transition，实现弹出框与蒙层整体的动画。

```typescript
  transitionOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
  } as promptAction.CustomDialogOptions;
  // ···
  build() {
    NavDestination() {
      Column() {
        // ···
        Button('openCustomDialog transition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
          })

        // ···
      }
      .width('100%')
      .height('100%')
    }
  }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/bfpUpHHvRUiyXlUcXgJAMw/zh-cn_image_0000002820525077.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=19C4C6A5653281FAE9F730EA80CB9AF49A5195D60D1CBBE9CA264171F4893C9C)

设置maskTransition，实现弹出框中蒙层单独的动画定制能力。

```typescript
Button('openCustomDialog maskTransition')
  .width('100%')
  .margin({ top: 10 })
  .onClick(() => {
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.myBuilder();
      },
      maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
        .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
    });
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/3hiT00cwTmaXpdMaL4cXPg/zh-cn_image_0000002820405077.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B296E6C78EDFA1FB99E7CF563E9CF5CC747820BB66D25664E79E62E685D2F26)

[CustomDialog](arkts-common-components-custom-dialog.md)虽然不支持transition接口，但与之对应的openAnimation和closeAnimation接口在动画的打开和关闭时可进行定制，示例代码如下：

```typescript
// xxx.ets

@CustomDialog
@Component
struct CustomDialogAnimationBuilder {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('title')
        .margin(10)
        .fontSize(20)
      Button('button1')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.controller?.close();
        })
      Button('button2')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.controller?.close();
        })
    }.width('100%')
    .height('50%')
  }
}

@Entry
@Component
export struct CustomDialogAnimation {
  animationController: CustomDialogController | null =
    new CustomDialogController({
      builder: CustomDialogAnimationBuilder(),
      closeAnimation: { duration: 2000 },
      openAnimation: { duration: 2000 }
    });

  aboutToDisappear(): void {
    this.animationController = null;
  }

  build() {
    NavDestination() {
      Column() {
        Button('CustomDialogController animate')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.animationController?.open();
          })
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/TyNTM-q6TXiWdeCnCsSdgg/zh-cn_image_0000002791725098.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F94576BE830A4B6B250831F38AAD66774F11E5452D754A67722A0D7F77525C7)

## 完整示例

```typescript
// xxx.ets
import { ImmersiveMode, LevelMode, promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct CustomDialogControl {
  @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;

  autoCancelOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    autoCancel: false,
  } as promptAction.CustomDialogOptions;

  modalOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    isModal: false,
  } as promptAction.CustomDialogOptions;

  maskOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    maskRect: {
      x: 0,
      y: 10,
      width: '100%',
      height: '90%'
    },
    maskColor: '#33AA0000'
  } as promptAction.CustomDialogOptions;

  transitionOpt: promptAction.CustomDialogOptions = {
    builder: () => {
      this.myBuilder();
    },
    transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
  } as promptAction.CustomDialogOptions;

  @Builder
  myBuilder() {
    Column() {
      Text('title').margin(10).fontSize(20)
      Button('button1').margin(10).fontSize(20)
      Button('button2').margin(10).fontSize(20)
    }.width('100%').height('50%')
  }

  build() {
    NavDestination() {
      Column() {
        Button('openCustomDialog autoCancel:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt);
          })

        Button('openCustomDialog isModal:false')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt);
          })

        Button('openCustomDialog maskOpt')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt);
          })

        Button('openCustomDialog transition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
          })

        Button('openCustomDialog immersiveMode')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.immersiveMode =
              this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              levelMode: LevelMode.EMBEDDED,
              immersiveMode: this.immersiveMode,
            })
          })

        Button('openCustomDialog maskTransition')
          .width('100%')
          .margin({ top: 10 })
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.myBuilder();
              },
              maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
                .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
            });
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/BGQ3LSPPRoC4E8IQf5ohPg/zh-cn_image_0000002791565126.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014651Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBF36E18C9DF8528F0367A414365B39946E2485195EC6EA64C1BC405A944BD31)
