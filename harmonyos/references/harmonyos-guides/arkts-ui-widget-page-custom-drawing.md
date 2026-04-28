---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-custom-drawing
title: ArkTS卡片使用画布组件绘制自定义图形
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片使用画布组件绘制自定义图形
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4b7fedc3263255941f8167bba397058bb438764c083a027b04a0519d96ed023
---

ArkTS卡片开放了自定义绘制的能力，在卡片上可以通过[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件创建一块画布，然后通过[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象在画布上进行自定义图形的绘制，如下示例代码实现了在画布的中心绘制了一个笑脸。

```
1. // entry/src/main/ets/customcanvasdrawing/pages/CustomCanvasDrawingCard.ets
2. @Entry
3. @Component
4. struct CustomCanvasDrawingCard {
5. private canvasWidth: number = 0;
6. private canvasHeight: number = 0;
7. // 初始化CanvasRenderingContext2D和RenderingContextSettings
8. private settings: RenderingContextSettings = new RenderingContextSettings(true);
9. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

11. build() {
12. Column() {
13. Row() {
14. Canvas(this.context)
15. .width('100%')
16. .height('100%')
17. .onReady(() => {
18. // 在onReady回调中获取画布的实际宽和高
19. this.canvasWidth = this.context.width;
20. this.canvasHeight = this.context.height;
21. // 绘制画布的背景
22. this.context.fillStyle = '#EEF0FF';
23. this.context.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
24. // 在画布的中心绘制一个圆
25. this.context.beginPath();
26. let radius = this.context.width / 3;
27. let circleX = this.context.width / 2;
28. let circleY = this.context.height / 2;
29. this.context.moveTo(circleX - radius, circleY);
30. this.context.arc(circleX, circleY, radius, 2 * Math.PI, 0, true);
31. this.context.closePath();
32. this.context.fillStyle = '#5A5FFF';
33. this.context.fill();
34. // 绘制笑脸的左眼
35. let leftR = radius / 13;
36. let leftX = circleX - (radius / 2.3);
37. let leftY = circleY - (radius / 4.5);
38. this.context.beginPath();
39. this.context.arc(leftX, leftY, leftR, 0, 2 * Math.PI, true);
40. this.context.closePath();
41. this.context.strokeStyle = '#FFFFFF';
42. this.context.lineWidth = 15;
43. this.context.stroke();
44. // 绘制笑脸的右眼
45. let rightR = radius / 13;
46. let rightX = circleX + (radius / 2.3);
47. let rightY = circleY - (radius / 4.5);
48. this.context.beginPath();
49. this.context.arc(rightX, rightY, rightR, 0, 2 * Math.PI, true);
50. this.context.closePath();
51. this.context.strokeStyle = '#FFFFFF';
52. this.context.lineWidth = 15;
53. this.context.stroke();
54. // 绘制笑脸的鼻子
55. let startX = circleX;
56. let startY = circleY - 20;
57. this.context.beginPath();
58. this.context.moveTo(startX, startY);
59. this.context.lineTo(startX - 8, startY + 40);
60. this.context.lineTo(startX + 8, startY + 40);
61. this.context.strokeStyle = '#FFFFFF';
62. this.context.lineWidth = 15;
63. this.context.lineCap = 'round';
64. this.context.lineJoin = 'round';
65. this.context.stroke();
66. // 绘制笑脸的嘴巴
67. let mouthR = radius / 2;
68. let mouthX = circleX;
69. let mouthY = circleY + 10;
70. this.context.beginPath();
71. this.context.arc(mouthX, mouthY, mouthR, Math.PI / 1.4, Math.PI / 3.4, true);
72. this.context.strokeStyle = '#FFFFFF';
73. this.context.lineWidth = 15;
74. this.context.stroke();
75. this.context.closePath();
76. })
77. }
78. }.height('100%').width('100%')
79. }
80. }
```

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/6ItrE2pTSZKWrE_l6cn4ug/zh-cn_image_0000002583478293.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234125Z&HW-CC-Expire=86400&HW-CC-Sign=CB83EE89E0C0D8501E7885CA477CDE9160D2DD04F555295BFB49B1B03EFD6CB3)
