---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas
title: Canvas对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Canvas对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:03845e2e0ff5f1894005446760441b1dc2073ae3d45b5a4e110267e0db35019f
---

Canvas组件提供画布，用于自定义绘制图形。具体用法请参考[CanvasRenderingContext2D对象](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md)。

## 创建Canvas组件

在pages/index目录下的hml文件中创建一个Canvas组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas></canvas>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. background-color: #00ff73;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/nT-SxY4uQWqp5gC7GxbjKQ/zh-cn_image_0000002583478131.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=59E42526B06B9E842F0657BD49E682263428D69776F69C0119495880D862D8DE)

说明

* Canvas组件默认背景色与父组件的背景色一致。
* Canvas默认宽高为width: 300px，height: 150px。

## 添加样式

Canvas组件设置宽（width）、高（height）、背景色（background-color）及边框样式（border）。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas></canvas>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. background-color: #F1F3F5;
7. width: 100%;
8. height: 100%;
9. }

11. canvas {
12. width: 500px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/gtVJ7gaUSJqYEWjgmEtbIw/zh-cn_image_0000002552798482.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=A2E56378578662FEA79586778DDEBBEC646EF1EA6BB6B44CA1DB06FE182486C5)

## 添加事件

Canvas添加长按事件，长按后可获取Canvas组件的dataUrl值（toDataURL方法返回的图片信息），打印在下方文本区域内。

说明

promptAction相关接口参考[弹窗](../harmonyos-references/js-apis-promptaction.md)。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <canvas ref="canvas1" onlongpress="getUrl"></canvas>
4. <text>dataURL</text>
5. <text class="content">{{ dataURL }}</text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }

11. canvas {
12. width: 500px;
13. height: 500px;
14. background-color: #fdfdfd;
15. border: 5px solid red;
16. margin-bottom: 50px;
17. }

19. .content {
20. border: 5px solid blue;
21. padding: 10px;
22. width: 90%;
23. height: 400px;
24. overflow: scroll;
25. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';

4. export default {
5. data: {
6. dataURL: null,
7. },
8. onShow() {
9. let el = this.$refs.canvas1;
10. let ctx = el.getContext("2d");
11. ctx.strokeRect(100, 100, 300, 300);
12. },
13. getUrl() {
14. let el = this.$refs.canvas1
15. let dataUrl = el.toDataURL()
16. this.dataURL = dataUrl;
17. promptAction.showToast({ duration: 2000, message: "long press,get dataURL" })
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/63TUvLi7SkyVU41C1GkC1A/zh-cn_image_0000002583438177.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=30B21B7E2355D9E3475DAEE5D7EF3EBCD004D4E8BEF43A3A602C7AE6FB882177)

说明

画布不支持在onInit和onReady中进行创建。
