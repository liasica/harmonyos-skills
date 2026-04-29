---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image
title: Image对象
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 画布组件 > Image对象
category: harmonyos-references
scraped_at: 2026-04-29T13:53:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4f126bdb39dcbbee849c616d9a12ba6247e5f2fadb12643271b439fbaa3600ae
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

图片对象。

## 属性

PhonePC/2in1TabletTVWearable

| 属性 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | string | - | 是 | 图片资源的路径。 |
| width | <length> | 0px | 否 | 图片的宽度。 |
| height | <length> | 0px | 否 | 图片的高度。 |
| onload | Function | - | 否 | 图片加载成功后触发该事件，无参数。 |
| onerror | Function | - | 否 | 图片加载失败后触发该事件，无参数。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div>
3. <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
4. </div>
```

```
1. // xxx.js
2. export default {
3. onShow() {
4. const el = this.$refs.canvas;
5. var ctx = el.getContext('2d');
6. var img = new Image();
7. // 图片路径建议放在common目录下
8. img.src = 'common/images/example.jpg';
9. img.onload = function () {
10. console.log('Image load success');
11. ctx.drawImage(img, 0, 0, 360, 250);
12. };
13. img.onerror = function () {
14. console.error('Image load fail');
15. };
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/x-Fq1XwYRU2fqxjEkugRYQ/zh-cn_image_0000002589326623.png?HW-CC-KV=V1&HW-CC-Date=20260429T055329Z&HW-CC-Expire=86400&HW-CC-Sign=AD1D952D7406EB1C27E046171CF7CAC17AC99FB7530852F076D045B7A10AC895)
