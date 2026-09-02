---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1599
title: 图案锁功能实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 图案锁功能实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c74d186d3700680f5ee2ac3fba2f9103a7e4a2f910d27e8737c14edf8fb6bfe0
---

## 问题现象

在手机的锁屏界面，如何实现设置图案密码锁的功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ZlUftpkHT2SDWZqwQXxjWQ/zh-cn_image_0000002628613330.gif "点击放大")

## 背景知识

* [PatternLock](../harmonyos-references/ts-basic-components-patternlock.md)是一种图案密码锁组件，以九宫格图案的方式输入密码，常用于密码验证场景。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是一种画布组件，用于自定义绘制图形。
* [Grid](../harmonyos-references/ts-container-grid.md)组件为网格容器，通过指定项目所在的单元格做出各种各样的布局，其中容器内各条目对应一个[GridItem](../harmonyos-references/ts-container-griditem.md)组件。

## 解决方案

* 方案一：使用PatternLock组件实现密码锁的绘制，详情可参考官网：[创建图案密码锁](../harmonyos-references/ts-basic-components-patternlock.md#示例1创建图案密码锁)。
* 方案二：通过在Stack组件内嵌套Canvas画布和Grid网格的方式，实现图案密码锁的功能。
  1. 在Stack中创建Canvas和Grid组件，用于展示图案界面。
  2. 给Canvas组件添加handleTouch方法，该方法是整段代码的核心部分，当手指在屏幕上滑动时，记录经过的每个数字并把它存入数组，当TouchType为Up时，使用validatePassword方法来判断输入的密码是否正确并展示对应的文字提示信息。

  完整示例参考如下：

  ```ts
  import { promptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct GestureLock {
    @State points: number[][] = [
      [50, 50], [150, 50], [250, 50],
      [50, 150], [150, 150], [250, 150],
      [50, 250], [150, 250], [250, 250]
    ];
    @State path: number[] = [];
    @State isDrawing: boolean = false;
    @State isError: boolean = false;
    @State shakeOffset: number = 0;
    @State lineColor: string = '#CCCCCC';
    @State currentX: number = 0;
    @State currentY: number = 0;
    // 设置默认密码
    private presetPassword: number[] = [1, 2, 5, 8, 9];
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Stack() {
        Column() {
          // 提示文字
          Text(this.getHintText())
            .fontSize(20)
            .fontColor(Color.Black)
            .margin({ top: 20, bottom: 20 });
          // 层叠布局
          Stack() {
            // 画布组件
            Canvas(this.canvasContext)
              .width(300)
              .height(300)
              .backgroundColor(Color.Transparent)
              .hitTestBehavior(HitTestMode.Transparent)
              .onTouch((event: TouchEvent) => {
                this.handleTouch(event);
              })
              .onReady(() => {
                this.drawPath();
              });
            // 密码锁的网格组件
            Grid() {
              ForEach(this.points, (point: number[], index: number) => {
                // 循环渲染出每个数字
                GridItem() {
                  Column() {
                    Column()
                      .width(16)
                      .height(16)
                      .borderRadius(8)
                      .backgroundColor(this.getCircleColor(index))
                      .animation({ duration: 300, curve: Curve.EaseInOut })
                  }
                  .width(20)
                  .height(20)
                  .justifyContent(FlexAlign.Center)
                  .alignItems(HorizontalAlign.Center)
                  .borderRadius(40)
                  .backgroundColor(this.getCircleBorderColor(index))
                  .animation({ duration: 300, curve: Curve.EaseInOut })
                  .onAppear(() => {
                    console.info(`${index}: [${point[0]}, ${point[1]}]`);
                  });
                }
              });
            }
            .columnsTemplate('1fr 1fr 1fr')
            .rowsTemplate('1fr 1fr 1fr')
            .width(300)
            .height(300)
            .hitTestBehavior(HitTestMode.Transparent)
          }
          .translate({ x: this.shakeOffset, y: 0 })
          .animation({ duration: 50, curve: Curve.EaseInOut })
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.White)
      .zIndex(200)
      .position({ x: 0, y: 0 })
    }

    // 绘制密码时，修改数字圆圈的颜色
    getCircleColor(index: number): string {
      if (!this.path.includes(index) || this.isDrawing) {
        return '#000000';
      }
      return this.isError ? '#ffff0000' : '#0A59F7';
    }

    // 绘制密码时，修改数字圆圈边界的颜色
    getCircleBorderColor(index: number): ResourceColor {
      console.info(`cicle border color select: ${index} black`);
      return this.path.includes(index) ? '#CCCCCC' : Color.Transparent;
    }

    // 修改提示文字
    getHintText(): string {
      if (this.isError) {
        return '密码错误，请重试';
      } else {
        return '请绘制手势密码';
      }
    }

    // 绘制路径
    drawPath() {
      const context = this.canvasContext;
      context.clearRect(0, 0, 300, 300);
      context.strokeStyle = this.lineColor;
      context.lineWidth = 16;
      context.lineCap = 'round';
      context.lineJoin = 'round';
      if (this.path.length > 0) {
        context.beginPath();
        const start = this.points[this.path[0]];
        context.moveTo(start[0], start[1]);
        for (let i = 1; i < this.path.length; i++) {
          const end = this.points[this.path[i]];
          context.lineTo(end[0], end[1]);
        }
        if (this.isDrawing) {
          context.lineTo(this.currentX, this.currentY);
        }
        context.stroke();
      }
    }

    // 当手指在屏幕上滑动时，记录经过的每个数字并把它存入数组
    handleTouch(event: TouchEvent) {
      const touch = event.touches[0];
      const x = touch.x;
      const y = touch.y;
      if (event.type === TouchType.Down) {
        this.isDrawing = true;
        this.path = [];
        this.isError = false;
        this.lineColor = '#CCCCCC';
        this.drawPath();
      }
      if (this.isDrawing) {
        this.currentX = x;
        this.currentY = y;
        this.points.forEach((point: number[], index: number) => {
          const centerX = point[0];
          const centerY = point[1];
          const distance = Math.sqrt(Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2));
          if (distance <= 20 && !this.path.includes(index)) {
            this.path.push(index);
          }
        });
        this.drawPath();
      }

      if (event.type === TouchType.Up) {
        this.isDrawing = false;
        this.validatePassword();
      }
    }

    // 验证输入的手势密码是否正确
    validatePassword() {
      if (this.path.length === this.presetPassword.length &&
      this.path.every((value: number, index: number) => value + 1 === this.presetPassword[index])) {
        promptAction.openToast({ message: '密码正确' });
        setTimeout(() => {
          this.reset();
        }, 1000);
      } else {
        this.isError = true;
        this.shake();
        setTimeout(() => {
          this.reset();
        }, 1000);
        promptAction.openToast({ message: '密码错误，请重试' });
      }
    }

    // 实现输入密码出错时的抖动效果
    shake() {
      const shakeDistance = 10;
      const shakeDuration = 50;
      const shakeCount = 4;
      let direction = 1;
      for (let i = 0; i < shakeCount; i++) {
        setTimeout(() => {
          this.shakeOffset = direction * shakeDistance;
          direction *= -1;
        }, i * shakeDuration);
      }
      setTimeout(() => {
        this.shakeOffset = 0;
      }, shakeCount * shakeDuration);
    }

    // 复位，将路径数组设置为空
    reset() {
      this.path = [];
      this.isError = false;
      this.lineColor = '#CCCCCC';
      this.drawPath();
    }
  }
  ```

## 总结

对方案一来说，PatternLock是HarmonyOS官方提供用于实现图案密码锁功能的组件，其优点是健壮性和适用性可以得到保证；而对方案二来说，使用Canvas和Grid组件实现时，开发者可以自定义图案锁的样式和功能，其灵活性和可扩展性比方案一要更好。
