---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-225
title: Canvas绘制内容如何动态更新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Canvas绘制内容如何动态更新
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:373fb378d180befb0ca212cd94563862a33299d77da0d484789f3498564e9c0d
---

在声明式语法中，Canvas使用数据驱动UI刷新。可以将变化的数据通过@Watch监听，并绑定自定义的draw()方法。当数据刷新时，@Watch绑定的方法会执行绘制逻辑。

参考代码如下：

```
1. @Entry
2. @Component
3. struct CanvasContentUpdate {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
6. @State @Watch('draw')content: string = '';

8. draw() {
9. this.context.clearRect(0, 0, 200, 200); // Clean up canvas content
10. this.context.fillText(this.content, 50, 50); // Refill
11. }

13. build() {
14. Column() {
15. Canvas(this.context)
16. .width('100%')
17. .height('25%')
18. .backgroundColor('#F5DC62')
19. .onReady(() => {
20. //You can draw content here.
21. this.context.font = '55px sans-serif';
22. this.context.fillText(this.content, 50, 50);
23. })
24. TextInput({
25. text:$$this.content
26. })
27. }
28. .borderColor('#31525B')
29. .borderWidth(12)
30. .width('100%')
31. .height('100%')
32. }
33. }
```

[CanvasDrawingContentDynamicallyUpdates.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CanvasDrawingContentDynamicallyUpdates.ets#L21-L53)

参考链接

[使用画布绘制自定义图形 (Canvas)](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)
