---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-346
title: 使用Canvas如何实现部分区域镂空的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用Canvas如何实现部分区域镂空的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d477cc87ec25f120e8e79a728571658612ccb0bf50c4824b6173d34b7dc419ef
---

1. 利用[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)绘制镂空圆形；
2. 使用Stack组件在需要透明展示的区域上叠加。

**参考代码**

```
1. @Entry
2. @Component
3. struct HollowOutWithCanvas {
4. @State circleCenterX: number = 0;
5. @State circleCenterY: number = 0;
6. @State circleRadius: number = 1000;
7. private contextSettings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.contextSettings);

10. build() {
11. Row() {
12. Column() {
13. Stack() {
14. Image($r('app.media.startIcon'))
15. .height(300)
16. // Use Canvas to draw masks to cover images, cameras, etc
17. Canvas(this.context)
18. .width('100%')
19. .height('100%')
20. .backgroundColor('#00000000')
21. .onReady(() => {
22. this.circleCenterX = this.context.width / 2;
23. this.circleCenterY = this.context.height / 2;
24. this.context.fillStyle = 'rgba(0,0,0,0.67)';
25. if (this.circleRadius > this.circleCenterX) {
26. this.circleRadius = this.circleCenterX / 2;
27. }
28. // Draw a circular path for semi transparent filling
29. this.context.beginPath();
30. this.context.moveTo(0, 0);
31. this.context.lineTo(0, this.context.height);
32. this.context.lineTo(this.context.width, this.context.height);
33. this.context.lineTo(this.context.width, 0);
34. this.context.lineTo(0, 0);
35. this.context.arc(this.circleCenterX, this.circleCenterY, this.circleRadius, 0, Math.PI * 2);
36. this.context.fill();
37. this.context.closePath();
38. })
39. }
40. .width('1456px')
41. .height('1456px')
42. }
43. .width('100%')
44. }
45. .height('100%')
46. }
47. }
```

[CanvasRealizesRegionHollowingOut.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CanvasRealizesRegionHollowingOut.ets#L21-L68)
