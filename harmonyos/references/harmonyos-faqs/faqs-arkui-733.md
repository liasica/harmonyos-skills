---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-733
title: 波纹动效实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 波纹动效实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:55974270df35aeea600f7c08a8d428d6d31160f1c1ebb513d21877496d7c8cec
---

## 问题现象

动画可以使应用界面过渡自然流畅，并且增强用户从界面获得的反馈感和互动感。如何实现组件的水波纹效果？

## 背景知识

* [实现属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md)：通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供两种属性动画接口animateTo和animation驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。
* [组件内转场](../harmonyos-references/ts-transition-animation-component.md)：组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

## 解决方案

**场景一**：点击后实现波纹动效。

通过onClick回调获取手指点击的位置用于为圆形组件的位置赋值，然后通过组件内转场实现圆形出现并逐渐透明的效果。

```screen
@Entry
@Component
struct WaterPageDemo {
  @State flag: boolean = false;
  @State ballX: number = 0;
  @State ballY: number = 0;
  build() {
    Column() {
      Column() {
      }.layoutWeight(1).backgroundColor(Color.Pink).width('100%');

      Stack() {
        // 根据flag判断是否显示动画效果
        if (this.flag) {
          Row()
            .width(5)
            .height(5)
            .position({
              x: this.ballX,
              y: this.ballY
            })
            .backgroundColor('rgba(0,0,0,0.7)')
              // 组件转场动画
            .transition(TransitionEffect.asymmetric(
              TransitionEffect.IDENTITY,
              TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.EaseInOut }).combine(
                TransitionEffect.scale({ x: 100, y: 100 })
              )
            ))
            .borderRadius(15)
        }
      }.width('100%').height('100%').clip(true)
      .onClick((e) => {
        this.ballX = e.x - 3;
        this.ballY = e.y - 3;
        this.flag = !this.flag;
        // 延时改变状态变量
        setTimeout(() => {
          this.flag = !this.flag;
        }, 100);
      });
    }
    .width('100%')
    .height('100%')
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/LKL7J4ieQy2nOhj-2UoG1g/zh-cn_image_0000002658914545.gif "点击放大")

**场景二**：控件自主产生动效。

```screen
@Entry
@Component
struct WaterPageDemo2 {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  waveSpeed: number = 0.03;
  phase: number = 0;
  // 绘制波纹动效
  drawWave() {
    this.context?.clearRect(0, 0, this.context.width, this.context.height); // 清除画布上在该矩形区域内的内容
    this.context?.beginPath();  // 开始创建路径
    for (let x = 0; x <= this.context.width; x += 10) {
      const y = this.context.height / 2 + Math.sin(x * 0.01 + this.phase) * 20;
      this.context?.lineTo(x, y); // 连接路径点
    }
    this.context?.lineTo(this.context.width, this.context.height);
    this.context?.lineTo(0, this.context.height);
    this.context?.closePath();    // 关闭一个路径
    this.context.fillStyle = '#30007bff'; // 设置填充色
    this.context?.fill();
    this.context?.beginPath();
    for (let x = 0; x <= this.context.width; x += 10) {
      const y = this.context.height / 2 + Math.sin(x * 0.02 + this.phase) * 10;
      this.context?.lineTo(x, y);
    }
    this.context?.lineTo(this.context.width, this.context.height);
    this.context?.lineTo(0, this.context.height);
    this.context?.closePath();
    this.context.fillStyle = '#50007bff';
    this.context?.fill();
    this.context?.beginPath();
    for (let x = 0; x <= this.context.width; x += 10) {
      const y = this.context.height / 2 + Math.sin(x * 0.015 + this.phase) * 30;
      this.context?.lineTo(x, y);
    }
    this.context?.lineTo(this.context.width, this.context.height);
    this.context?.lineTo(0, this.context.height);
    this.context?.closePath();
    this.context.fillStyle = '#20007bff';
    this.context?.fill();
    this.phase += this.waveSpeed;
  }

  build() {
    Column() {
      Canvas(this.context)
        .width(200)
        .height(100)
        .backgroundColor(Color.Pink)
          // Canvas初始化完成回调
        .onReady(() => {
          setInterval(this.drawWave.bind(this), 20);
        })
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/iv9nYIV_RSyGX_3ASWIOsQ/zh-cn_image_0000002628395320.gif "点击放大")
