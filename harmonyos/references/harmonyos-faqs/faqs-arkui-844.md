---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-844
title: CustomDialog如何添加平移动画，实现从底部右侧平移进入/滑出
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > CustomDialog如何添加平移动画，实现从底部右侧平移进入/滑出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2a59b85fc4b903f995e865aa2bb8dc7caa85dc6554db886c7255679a06051926
---

## 问题现象

CustomDialog如何添加平移动画，从底部右侧平移进入和离开时平移从底部滑出？

## 背景知识

* [自定义弹窗（CustomDialog）](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
* [出现/消失转场](../harmonyos-guides/arkts-enter-exit-transition.md)：[transition](../harmonyos-references/ts-transition-animation-component.md)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect对象](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)的组合使用，定义出各式效果。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：显式动画是一个用于平滑过渡动画的方法，通常用于在UI元素中实现平滑的移动、缩放或其他变化效果。它允许你指定一个目标值，并以指定的时间和曲线进行动画过渡。

## 解决方案

* **方案一**：通过combine属性对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect，另外使用translate属性设置组件转场时的平移效果，其中设置的x值为横向的平移距离。

  完整示例参考如下：

  ```ts
  import { curves } from '@kit.ArkUI';

  @CustomDialog
  struct CustomDialogExample {
    controller: CustomDialogController;
    @State showFlag: Visibility = Visibility.Visible;
    private effect: TransitionEffect =
      TransitionEffect.OPACITY.animation({ curve: curves.springMotion(0, 1) })
      // 添加平移转场效果，这里的动画参数使用指定的springMotion()
        .combine(TransitionEffect.translate({ x: 150 }).animation({ curve: curves.springMotion() }));

    build() {
      Column() {
        Button('关闭弹窗');
      }
      .width('100%')
      .height(400)
      .backgroundColor(Color.Gray)
      .onClick(() => {
        this.cancel();
      })
      .visibility(this.showFlag)
      .transition(this.effect);
    }

    cancel() {
      this.showFlag = Visibility.Hidden;
      setTimeout(() => {
        this.controller.close();
      }, 400);
    }
  }

  @Entry
  @Component
  struct CustomDialogUser {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogExample(),
      alignment: DialogAlignment.Bottom,
      autoCancel: false,
      customStyle: true
    });

    build() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.dialogController.open();
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* **方案二**：定义状态变量translateX用于设置组件在x轴的平移距离；定义状态变量transparency用于设置组件的不透明度。

  打开和关闭弹窗的过程中，使用显式动画动态控制translateX和transparency，实现平移进入/滑出动画。

  完整示例参考如下：

  ```ts
  import { curves } from '@kit.ArkUI';

  @CustomDialog
  struct CustomDialogExampleTwo {
    controller: CustomDialogController;
    @State showFlag: Visibility = Visibility.Visible;
    @State translateX: number = 500; // 设置组件在x轴的平移距离
    @State transparency: number = 0; // 设置组件的不透明度
    duration: number = 400;

    build() {
      Column() {
        Button('关闭弹窗');
      }
      .width('100%')
      .height(400)
      .backgroundColor(Color.Gray)
      .onClick(() => {
        this.cancel();
      })
      .visibility(this.showFlag)
      .opacity(this.transparency)
      .translate({ x: this.translateX })
      .onAppear(() => {
        this.getUIContext().animateTo({
          duration: this.duration,
          iterations: 1,
          curve: curves.springMotion(0, 1)
        }, () => {
          this.translateX = 0;
          this.transparency = 1;
        });
      });
    }

    cancel() {
      this.getUIContext().animateTo({
        duration: this.duration,
        iterations: 1,
        curve: curves.springMotion(),
        onFinish: () => {
        }
      }, () => {
        this.transparency = 0;
        this.translateX = 500;
      });

      setTimeout(() => {
        this.controller.close();
      }, 200);
    }
  }

  @Entry
  @Component
  struct CustomDialogUserTwo {
    dialogController: CustomDialogController = new CustomDialogController({
      builder: CustomDialogExampleTwo(),
      alignment: DialogAlignment.Bottom,
      autoCancel: false,
      customStyle: true
    });

    build() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.dialogController.open();
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
