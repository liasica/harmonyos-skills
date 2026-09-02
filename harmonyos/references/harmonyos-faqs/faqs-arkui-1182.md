---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1182
title: 如何结合关键帧动画和路径动画绘制
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何结合关键帧动画和路径动画绘制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7400fb0eb0eaad068ee576da7f3c6beced0bf98ebc812aa709fc88131f75ecf5
---

## 问题现象

在关键帧动画中的不同步骤如何使用不同motionPath路径？

## 背景知识

* 使用[keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)可以指定若干个关键帧状态，实现分段的动画。
* 使用[motionPath](../harmonyos-references/ts-motion-path-animation.md)可以设置组件进行位移动画时的运动路径。
* [绘制路径](../harmonyos-guides/ui-js-components-svg-path.md)格式要求：必须符合SVG路径规范，使用M（移动）、L（直线）、C（贝塞尔曲线）等指令。

## 解决方案

在keyframeAnimateTo中分段设置motionPath会导致路径移动异常，可以使用显示动画配合onFinish回调方法实现分段路径，具体实现如下：

```ts
@Entry
@Component
struct MotionPathDemo {
  @State toggle: boolean = true;
  @State myColor: Color = Color.Pink;
  @State pathParams: MotionPathOptions = {
    path: 'Mstart.x start.y L10 100 L0 0 Lend.x end.y',
    from: 0,
    to: 1,
    rotatable: false
  };
  @State x: number = 10;
  @State y: number = 10;

  setPosition() {
    this.x = 200;
    this.y = 200;
    this.myColor = Color.Blue;
  }

  setPosition2() {
    this.x = 400;
    this.y = 400;
    this.myColor = Color.Green;
  }

  private runPath() {
    this.getUIContext().animateTo({
      duration: 1000,
      onFinish: () => {
        this.getUIContext().animateTo({
          duration: 1000,
        }, () => {
          this.pathParams = {
            path: 'M200 200 L200 400 L400 400',
            from: 0,
            to: 1,
            rotatable: false
          };
          this.setPosition2();
        });
      }
    }, () => {
      this.toggle = !this.toggle;
      this.pathParams = {
        path: 'M10 10 L10 200 L200 200',
        from: 0,
        to: 1,
        rotatable: false
      };
      this.setPosition();
    });
  }

  build() {
    Column() {
      Button('点击')
        .onClick(() => {
          this.runPath();
        });

      Text('Hello')
        .margin({ top: 50 })
        .width(50)
        .height(50)
        .backgroundColor(this.myColor)
        .motionPath(this.pathParams) // 设置路径动画
        .position({ top: this.toggle ? 10 : this.y, left: this.toggle ? 10 : this.x }); // 根据toggle状态设置位置
    }
    .width('100%')
    .height('100%'); // 设置列的宽度和高度为100%
  }
}
```
