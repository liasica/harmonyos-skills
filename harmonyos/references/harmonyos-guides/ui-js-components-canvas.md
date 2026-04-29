---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas
title: Canvas对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > Canvas开发指导 > Canvas对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b640f6f183f46b31d4249f2992a957b85ca9737d0a6854466a792b6a679702ad
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/LfARArMFQqK-EtFORxrTXg/zh-cn_image_0000002589244429.png?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=DE3022FD9A3AAA3D8D5A667EFD3B2CB8FFF3EC0965CFADCB7815948BEE4FF10B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/yiqBJtB6SC6Yoyu-iVv-Ug/zh-cn_image_0000002558764622.png?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=D64BA846A9AA7A1037BE8BB1D976B830D11D8E9E1B8CDDD6D80A565700F44F0F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/v62KX6NBRFqya11VPgt2ww/zh-cn_image_0000002558604966.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=F57D6AB1E9283BF5141F86E87F31418FC12500B379579FA01BDC2AE5A5ED9CB4)

说明

画布不支持在onInit和onReady中进行创建。
