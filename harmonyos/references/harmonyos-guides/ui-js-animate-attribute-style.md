---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-attribute-style
title: 属性样式动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > CSS动画 > 属性样式动画
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:07+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b39a564df73b01280eb31aa9a5975707c1c359a9932b9adca73811f39239087e
---

在关键帧（Keyframes）中动态设置父组件的width和height，实现组件变大缩小。子组件设置scale属性使父子组件同时缩放，再设置opacity实现父子组件的显示与隐藏。

```html
<!-- xxx.hml -->
<div class="container">
  <div class="fade">
    <text>fading away</text>
  </div>
  <div class="bigger">
    <text>getting bigger</text>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  background-color:#F1F3F5;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.fade {
  width: 30%;
  height: 200px;
  left: 35%;
  top: 25%;
  position: absolute;
  animation: 2s change infinite friction;
}
.bigger {
  width: 20%;
  height: 100px;
  background-color: blue;
  animation: 2s change1 infinite linear-out-slow-in;
}
text {
  width: 100%;
  height: 100%;
  text-align: center;
  color: white;
  font-size: 35px;
  animation: 2s change2 infinite linear-out-slow-in;
}
/* 颜色与不透明度变化 */
@keyframes change{
  from {
    background-color: #f76160;
    opacity: 1;
  }
  to {
    background-color: #09ba07;
    opacity: 0;
  }
}
/* 父组件大小变化 */
@keyframes change1 {
  0% {
    width: 20%;
    height: 100px;
  }
  100% {
    width: 80%;
    height: 200px;
  }
}
/* 子组件文字缩放 */
@keyframes change2 {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1.5);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/RgDHlHaMQ8q4vNO0Hykfzg/zh-cn_image_0000002712244212.gif)

**说明** 

* animation取值不区分先后，duration （动画执行时间）/ delay （动画延迟执行时间）按照出现的先后顺序解析。
* 必须设置animation-duration样式，否则时长为0则不会有动画效果。当设置animation-fill-mode属性为forwards时，组件直接展示最后一帧的样式。
