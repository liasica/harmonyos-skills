---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-svg
title: svg动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > CSS动画 > svg动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c8e4f7d6c43496cda026bd5e733b803fc9d1a590f55cb07b0488674bf29b5345
---

为svg组件添加动画效果。

## 属性样式动画

在svg的子组件[animate](../harmonyos-references/js-components-svg-animate.md)中，通过attributeName设置需要进行动效的属性，from设置开始值，to设置结束值。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg>
4. <text x="300" y="300" fill="blue">
5. Hello
6. <animate attributeName="font-size" from="30" to="60" dur="3s" repeatCount="indefinite">
7. </animate>
8. <animate attributeName="fill" from="red" to="blue" dur="3s" repeatCount="indefinite">
9. </animate>
10. <animate attributeName="opacity" from="1" to="0.3" dur="3s" repeatCount="indefinite">
11. </animate>
12. </text>
13. <text x="300" y="600" fill="blue">
14. World
15. <animate attributeName="font-size" from="30" to="60" values="30;80" dur="3s" repeatCount="indefinite">
16. </animate>
17. <animate attributeName="fill" from="red" to="blue"  dur="3s" repeatCount="indefinite">
18. </animate>
19. <animate attributeName="opacity" from="0.3" to="1" dur="3s" repeatCount="indefinite">
20. </animate>
21. </text>
22. </svg>
23. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/e1SEKYt8ScqH-X5YvYGTCg/zh-cn_image_0000002589324507.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052854Z&HW-CC-Expire=86400&HW-CC-Sign=074B4D651A6813014DC724B633966722BC0F171F3B1649860CD74643304B98AB)

说明

在设置动画变化值时，如果已经设置了values属性，则from和to都失效。

## 路径动画

在svg的子组件[animateMotion](../harmonyos-references/js-components-svg-animatemotion.md)中，通过path设置动画变化的路径。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" width="800" height="900">
4. <path d="M300,200 h-150 a150 150 0 1 0 150 -150 z" fill="white" stroke="blue" stroke-width="5" >
5. </path>
6. <path fill="red" d="M-5,-5 L10,0 L-5,5 L0,0 Z"  >
7. <animateMotion dur="2000" repeatCount="indefinite" rotate="auto-reverse"path="M300,200 h-150 a150 150 0 1 0 150 -150 z">
8. </animateMotion>
9. </path>
10. </svg>
11. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/nRkl1l3EQRe5uEdjtVS7DA/zh-cn_image_0000002589244445.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052854Z&HW-CC-Expire=86400&HW-CC-Sign=D330629E5025C7FE7E4B2AAF8676A0CD46EF3F5553BCC037EB11D65AA3E7205B)

## animateTransform动画

在svg的子组件[animateTransform](../harmonyos-references/js-components-svg-animatetransform.md)中，通过attributeName绑定transform属性，type设置动画类型，from设置开始值，to设置结束值。

```
1. <!-- xxx.hml -->
2. <div class="container" style="">
3. <svg>
4. <line x1="90" y1="300" x2="90" y2="730" stroke-width="10" stroke="black" stroke-linecap="round">
5. <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="3s" values="0;30;10;30;20;30;25;30" keyTimes="0;0.3;0.5;0.7;0.8;0.9;1.0;1.1"
6. fill="freeze">
7. </animateTransform>
8. </line>
9. <circle cx="500" cy="500" r="50" stroke-width="15" fill="red" stroke="#e70d0d">
10. <animateTransform attributeName="transform" attributeType="XML" type="rotate"  dur="3s" values="0;30;10;30;20;30;25;30" keyTimes="0;0.3;0.5;0.7;0.8;0.9;1.0;1.1" fill="freeze">
11. </animateTransform>
12. <animateTransform attributeName="transform" attributeType="XML" type="scale"  dur="6s" values="1;1;1.3" keyTimes="0;0.5;1" fill="freeze"></animateTransform>
13. <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="9s" values="0;0;300 7" keyTimes="0;0.6;0.9" fill="freeze"></animateTransform>
14. </circle>
15. <rect width="500" height="200" x="90" y="840">
16. <animateTransform attributeName="transform" attributeType="XML" type="skewY"  dur="6s" values="0;0;30" keyTimes="0;0.5;1" fill="freeze"></animateTransform>
17. </rect>
18. <line x1="650" y1="300" x2="650" y2="600" stroke-width="20" stroke="blue" stroke-linecap="round">
19. <animateTransform attributeName="transform" attributeType="XML" type="translate"  dur="9s" values="0;0;0 800" keyTimes="0;0.6;1" fill="freeze"></animateTransform>
20. </line>
21. </svg>
22. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. width: 100%;
6. height: 100%;
7. background-color: #F1F3F5;
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/VT4b4iNZS7ORpM4bqVpQyQ/zh-cn_image_0000002558764638.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052854Z&HW-CC-Expire=86400&HW-CC-Sign=813ED9995BEACD18983D0AFC58ABAF4142753813FD4ADA8C23068D5112948549)
