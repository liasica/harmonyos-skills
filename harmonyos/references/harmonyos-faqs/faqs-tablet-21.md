---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-21
title: 平板横竖屏切换，底部图标隐藏不见
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板横竖屏切换，底部图标隐藏不见
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6afe14aa64a9c6d90a1e0cb5ee44c5fafd9f688e2047b21a437deceff4e6757e
---

## 问题现象

应用在平板上打开，横竖屏切换后底部的图标隐藏不见了，再次点击图标区域又显示出来。

## 背景知识

[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。

[横竖屏切换](../best-practices/bpta-landscape-and-portrait-development.md)：横竖屏切换功能实现应用内既支持竖屏显示也支持横屏显示的效果。当传感器变化或用户手动设置窗口方向时，窗口显示和尺寸会发生变化。

## 问题定位

检查页面布局，页面底部图标使用Canvas绘制。根据官方文档，建议检查代码中Canvas绘制的时机，以及页面是否监听了平板横竖屏变化。页面横竖屏切换时，会触发Canvas的onReady事件将画布清空。

## 分析结论

横竖屏切换后，页面布局大小发生变化，此时Canvas组件大小发生变化，画布被清空，但点击后又能重新显示出来，表明绘制逻辑正常，但是没有强制重新渲染导致图标隐藏不见。

## 修改建议

监听屏幕方向变化，并重新渲染Canvas画布。简单示例：

```screen
import display from '@ohos.display';

@Entry
@Component
struct RotationCanvas {
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D();

  aboutToAppear() {
    // 同步获取屏幕信息
    this.updateCanvasByDisplay();
    this.registerRotationListener();
  }

  // 同步更新画布
  private updateCanvasByDisplay() {
    try {
      this.drawCanvas();
    } catch (err) {
      console.error(`获取屏幕信息失败: ${err}`);
    }
  }

  // 注册旋转监听
  private registerRotationListener() {
    display.on('change', () => {
      this.context.reset(); // 清空画布
      this.updateCanvasByDisplay(); // 同步更新
    });
  }

  // 绘制逻辑保持不变
  private drawCanvas() {
    this.context.fillStyle = '#D1D1D6';
    this.context.fillRect(50, 50, 200, 200);
    // 绘制Canvas的业务代码
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('80%')
        .onReady(() => this.updateCanvasByDisplay()); // 同步初始化
    };
  }

  aboutToDisappear() {
    display.off("change");
  }
}
```
