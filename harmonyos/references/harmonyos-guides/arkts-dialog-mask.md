---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-mask
title: 弹出框蒙层控制
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框蒙层控制
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e1cbb3771ce122992f467ff800b60c76b05a23cef280dac07b658d2f0abcbeba
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/hANBiWUCTNCrPkfkEHaYsA/zh-cn_image_0000002793036742.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=E43DCEA9C94141AC0BD4B8EBC295473B7BAD069E65DAB51D4283F6224669A115)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/VFhqqac9Q1KdgbkexiwfQA/zh-cn_image_0000002792876774.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A195EA7AF01385ABC27B32BE98B59B735C504A713D0E3466BAA23FAD5E2B4F3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/eUIXa9DZSDmorsxuESR3Bw/zh-cn_image_0000002821836679.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=99BA304BBA85E7DA1039C873B80FEF2EBD97930E89C896E0358F70680D402AC4)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/twSwDhkjRyu_41R2OPMM_w/zh-cn_image_0000002821756681.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1ACC1DFFC10F505F007A8258758D6E09B8CA1BD29A2B7C0A6EDDB4BBCED903E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/TN7DzlTsSvSo0d4KULu-Cw/zh-cn_image_0000002793036744.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0932C785840962A09198234624191D63781EAE865392D591BBDF732ED8FA0F1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/pkHi5rHlRey9XCg1jYb0Iw/zh-cn_image_0000002792876776.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=E685B51DCA22B8014D56C7F95BDBB62406AD640AAE016A43EA65D1F727890F47)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/giWvTdb8RQexlCUtEZpKBw/zh-cn_image_0000002821836681.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB88AF6B1A1097AFB9E5F3FFBC158CE944D6B9F6A35D4378DB5C631422F8A29E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/nS9A3fExTiO8vC_0qMKOzA/zh-cn_image_0000002821756683.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3A3996389A38A1671C9549F5F09D7CFEFCBDC173DC46ADA251D2B818E907C19)
