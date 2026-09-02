---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1445
title: 使用属性动画和颜色渐变实现动态渐变色背景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用属性动画和颜色渐变实现动态渐变色背景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:629dd0fa27030a1f67f54063f91fccba051fd48fb996e1b86088cbdf2f27107b
---

## 问题现象

如何在HarmonyOS侧使用属性动画和颜色渐变实现动态渐变色背景？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/mk8U1KF4Qq66pUsV7I76hw/zh-cn_image_0000002658843527.gif "点击放大")

## 背景知识

动态背景主要由渐变色彩和动画来进行组合实现，linearGradient设计背景颜色，animateTo用来实现背景变化的动画效果。

* 使用[显式动画 (animateTo)](../harmonyos-references/ts-explicit-animation.md)来实现颜色变化效果。
* 使用[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)来设计整体背景颜色的渐变效果。

## 解决方案

* 实现思路
  + 使用linearGradient定义渐变色数组。
  + 定义animateTo属性动画方法并设置合理的动画持续时间。
  + 使用定时器合理切换不同的渐变色数组，实现动画变化效果。
  + 使用Stack堆叠组件将实现的动态效果设置背景。
* 完整示例参考如下：

  ```screen
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct LinearGradientBackgroundSample {
    @State bgPositionX: number = 0;
    @State gradientAngle: number = 135;
    @State currentColorIndex: number = 0;
    // 渐变色组（包含多个颜色方案）
    colorSchemes: Array<Array<[ResourceColor, number]>> = [
      [
        ['#e0f7ff', 0.0],
        ['#d9e5ff', 0.2],
        ['#e6e0ff', 0.4],
        ['#ffebfa', 0.8],
        ['#e0f7ff', 1.0]
      ],
      [
        ['#fff3e6', 0.0],
        ['#ffe6f0', 0.4],
        ['#e6ecff', 0.8],
        ['#f0fff4', 1.0]
      ],
    ];

    aboutToAppear() {
      this.startComplexAnimation();
    }

    onPageShow(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (_err, win) => {
        win.setWindowLayoutFullScreen(true);
      });
    }

    onPageHide(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (_err, win) => {
        win.setWindowLayoutFullScreen(false);
      });
    }

    startComplexAnimation() {
      // 背景滑动动画
      const animateSlide = () => {
        this.getUIContext().animateTo({
          duration: 15000,
          curve: Curve.EaseInOut
        }, () => {
          this.bgPositionX = 100;
        });

        this.getUIContext().animateTo({
          duration: 15000,
          delay: 15000,
          curve: Curve.EaseInOut
        }, () => {
          this.bgPositionX = 0;
        });
      };

      // 渐变角度动画
      const animateRotation = () => {
        this.getUIContext().animateTo({
          duration: 20000,
          curve: Curve.Linear
        }, () => {
          this.gradientAngle = 495;
        });

        this.getUIContext().animateTo({
          duration: 3000, // 动画时长
          delay: 1000,
          curve: Curve.Linear,
        }, () => {
          this.gradientAngle = 135;
        });
      };

      // 颜色方案切换
      setInterval(() => {
        this.currentColorIndex = (this.currentColorIndex + 1) % this.colorSchemes.length;
      }, 3000);

      // 启动复合动画
      animateSlide();
      animateRotation();
    }

    build() {
      Stack() {
        Column()
          .width('100%')
          .height('100%')
          .linearGradient({
            angle: this.gradientAngle,
            direction: GradientDirection.LeftTop,
            colors: this.colorSchemes[this.currentColorIndex],
            repeating: true
          })
          .backgroundImageSize(400) // 设置背景图尺寸
          .backgroundImagePosition({ x: `${this.bgPositionX}%`, y: '50%' }) // 设置背景图位置
          .transition({ type: TransitionType.All })
          .animation({ duration: 1000 })

        Column() {
          Text('动态渐变背景')
            .fontSize(24)
            .fontColor(Color.Black)
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
      }
      .onClick(() => {
        // 点击切换颜色方案
        this.currentColorIndex = (this.currentColorIndex + 1) % this.colorSchemes.length;
      })
    }
  }
  ```
