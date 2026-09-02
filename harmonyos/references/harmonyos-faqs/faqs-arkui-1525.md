---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1525
title: 无法通过点击在画板上画出点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 无法通过点击在画板上画出点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ecaa59d3d79474b07ac7f14f6b71e6d0c6e03898278e8be6db324da7071b736c
---

## 问题现象

在绘画类应用上，单指按住滑动可以画出线条，但是单次点击操作无法绘制点状图形。

## 背景知识

* [TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)：支持单击、双击和多次点击的识别。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发。

## 问题定位

点击画布，查看hilog检查是否缺少了点击手势的响应能力，相关日志如下：

```screen
touch test hitted recognizer type info: recognizer type PanRecognizer node info: { tag: Canvas };recognizer type PinchRecognizer node info: { tag: Canvas };recognizer type RotationRecognizer node info: { tag: Canvas };
```

从日志可知，日志中存在PanRecognizer相关信息，能够响应手指拖动操作。但是缺少了ClickRecognizer相关信息，表明组件未实现对点击事件的响应功能。

## 分析结论

画布组件未实现点击反馈功能，需要添加点击反馈。

## 修改建议

为画布组件添加TapGesture属性来响应点击事件。

```ts
@Entry
@Component
struct TapGestureExample {
  private x: number|undefined = 0; // 触摸点x坐标
  private y: number|undefined = 0; // 触摸点y坐标
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private tempPath: Path2D = new Path2D(); // 临时绘画路径

  build() {
    Row() {
      Canvas(this.context)
        .gesture(
          // 添加点击回调
          TapGesture({ count: 1, fingers: 1 })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                // 点击后在位置画点
                this.x = event.tapLocation?.x;
                this.y = event.tapLocation?.y;
                // 设置线宽
                this.context.lineWidth = 4;
                this.tempPath = new Path2D();
                this.tempPath.lineTo(this.x, this.y);
                this.context.lineCap = 'round';
                this.context.stroke(this.tempPath);
              };
            })
        );
      // 根据需求添加画线等其余回调
    }
    .height('100%');
  };
};
```

对应日志如下：

```screen
touch test hitted recognizer type info: recognizer type ClickRecognizer node info: { tag: Stack };
```
