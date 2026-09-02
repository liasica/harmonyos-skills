---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-225
title: Canvas绘制内容如何动态更新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Canvas绘制内容如何动态更新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6e938611cab2d154b4ac00769451835c8a9f2bcee3a0384be9e349d584e0bd70
---

在声明式语法中，Canvas使用数据驱动UI刷新。可以将变化的数据通过@Watch监听，并绑定自定义的draw()方法。当数据刷新时，@Watch绑定的方法会执行绘制逻辑。

参考代码如下：

```ts
@Entry
@Component
struct CanvasContentUpdate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State @Watch('draw')content: string = '';

  draw() {
    this.context.clearRect(0, 0, 200, 200); // Clean up canvas content
    this.context.fillText(this.content, 50, 50); // Refill
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('25%')
        .backgroundColor('#F5DC62')
        .onReady(() => {
          //You can draw content here.
          this.context.font = '55px sans-serif';
          this.context.fillText(this.content, 50, 50);
        })
      TextInput({
        text:$$this.content
      })
    }
    .borderColor('#31525B')
    .borderWidth(12)
    .width('100%')
    .height('100%')
  }
}
```

参考链接

[使用画布绘制自定义图形 (Canvas)](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)
