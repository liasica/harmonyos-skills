---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tabs
title: tabs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > tabs
category: harmonyos-references
scraped_at: 2026-11-21T09:14:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0dd2f4dd55ab35366cdd561fa06a3ef9446e67be15a1b18b8005eae11797ec7b
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

tab页签容器。

## 权限列表

无

## 子组件

仅支持<[tab-bar](js-components-container-tab-bar.md)>和<[tab-content](js-components-container-tab-content.md)>。

## 属性

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | number | 0 | 否 | 当前处于激活态的tab索引。 |
| vertical | boolean | false | 否 | 是否为纵向的tab，默认为false，可选值为：  - false：tabbar和tabcontent上下排列。  - true：tabbar和tabcontent左右排列。 |

## 样式

支持[通用样式](js-components-common-styles.md)。

## 事件

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { index: indexValue } | tab页签切换后触发，动态修改index值不会触发该回调。 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <tabs class = "tabs" index="0" vertical="false" onchange="change">
    <tab-bar class="tab-bar" mode="fixed">
      <text class="tab-text">Home</text>
      <text class="tab-text">Index</text>
      <text class="tab-text">Detail</text>
    </tab-bar>
    <tab-content class="tabcontent" scrollable="true">
      <div class="item-content" >
        <text class="item-title">First screen</text>
      </div>
      <div class="item-content" >
        <text class="item-title">Second screen</text>
      </div>
      <div class="item-content" >
        <text class="item-title">Third screen</text>
      </div>
    </tab-content>
  </tabs>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
.tabs {
  width: 100%;
}
.tabcontent {
  width: 100%;
  height: 80%;
  justify-content: center;
}
.item-content {
  height: 100%;
  justify-content: center;
}
.item-title {
  font-size: 60px;
}
.tab-bar {
  margin: 10px;
  height: 60px;
  border-color: #007dff;
  border-width: 1px;
}
.tab-text {
  width: 300px;
  text-align: center;
}
```

```js
// xxx.js
export default {
  change: function(e) {
    console.info("Tab index: " + e.index);
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/th5YPaeBScC7GzzV-jBY2w/zh-cn_image_0000002821759393.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011320Z&HW-CC-Expire=31536000000&HW-CC-Sign=0244B8634B93713A74903E1240EE111F5C9C9E26A8B131B6DBA7DC28618455BE)
