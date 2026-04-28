---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-313
title: 如何使用canvas绘制圆角矩形
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何使用canvas绘制圆角矩形
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e224aa078ac6556beb87200a25014565443cffa67b55d32841a29b99dfb65831
---

利用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象的arc绘制弧形路径，结合lineTo方法绘制直线，参考代码如下：

```
1. @Entry
2. @Component
3. struct CanvasDrawRoundedRectangle {
4. private readonly settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private readonly ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

7. drawRoundRect(x: number, y: number, width: number, height: number, radius: number, strokeColor?: string,
8. fillColor?: string, lineDash?: Array<number>) {
9. if (width < 2 * radius || height < 2 * radius) {
10. radius = Math.min(width, height) / 2;
11. }
12. strokeColor = strokeColor || '#333';
13. lineDash = lineDash || [];
14. this.ctx.beginPath();
15. this.ctx.setLineDash(lineDash);
16. // Draw the first arc path
17. this.ctx.arc(x + radius, y + radius, radius, Math.PI, Math.PI * 3 / 2);
18. // Draw the first straight path
19. this.ctx.lineTo(width - radius + x, y);
20. // Draw the second arc path
21. this.ctx.arc(width - radius + x, radius + y, radius, Math.PI * 3 / 2, Math.PI * 2);
22. // Draw the second straight path
23. this.ctx.lineTo(width + x, height + y - radius);
24. // Draw the third arc path
25. this.ctx.arc(width - radius + x, height - radius + y, radius, 0, Math.PI / 2);
26. // Draw the third straight path
27. this.ctx.lineTo(radius + x, height + y);
28. // Draw the fourth arc path
29. this.ctx.arc(radius + x, height - radius + y, radius, Math.PI / 2, Math.PI);
30. // Draw the fourth straight path
31. this.ctx.lineTo(x, y + radius);
32. // Set brush color
33. this.ctx.strokeStyle = strokeColor;
34. // Stroke drawing
35. this.ctx.stroke();
36. if (fillColor) {
37. this.ctx.fillStyle = fillColor;
38. this.ctx.fill();
39. }
40. this.ctx.closePath();
41. }

43. build() {
44. Row() {
45. Column() {
46. Canvas(this.ctx)
47. .width('100%')
48. .height('100%')
49. .onReady(() => {
50. this.drawRoundRect(50, 50, 100, 100, 10);
51. })
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

[DrawRoundedRectanglesUsingCanvas.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DrawRoundedRectanglesUsingCanvas.ets#L21-L78)

实现效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Xw_riQDsQQmEzHOElDKNZQ/zh-cn_image_0000002229758593.png?HW-CC-KV=V1&HW-CC-Date=20260428T002617Z&HW-CC-Expire=86400&HW-CC-Sign=A2CB5727AACEBDD93F93286AA5D8E61A7A9B758E7610AFBB3EF76BE6711BBD5D)
