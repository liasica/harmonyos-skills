---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-badge
title: badge
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > badge
category: harmonyos-references
scraped_at: 2026-09-05T06:17:34+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:cfc3b2b708e554994881a62f104913c8a0f7a04f909dfc7bfa2c7a26b8d7671f
---

**说明** 

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

应用中如果有需用户关注的新事件提醒，可以采用新事件标记来标识。

## 权限列表

无

## 子组件

支持单个子组件。

**说明** 

仅支持单子组件节点，如果使用多子组件节点，默认使用第一个子组件节点。

## 属性

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| placement | string | rightTop | 否 | 事件提醒的数字标记或者圆点标记的位置，可选值为：  - right：位于组件右边框。  - rightTop：位于组件边框右上角。  - left：位于组件左边框。 |
| count | number | 0 | 否 | 设置提醒的消息数，默认为0，为0时不显示。当设置相应的提醒消息数大于0时，消息提醒会变成数字标记类型。  当数字设置大于maxcount时，将显示maxcount+。count属性最大支持整数值为2147483647。 |
| visible | boolean | false | 否 | 是否显示事件提醒，当收到新事件提醒时可以设置该属性为true，显示相应的事件提醒，如果需要使用数字标记类型，同时需要设置相应的count属性。 |
| maxcount | number | 99 | 否 | 最大事件数限制，当收到新事件提醒大于该限制时，标识数字会进行省略，仅显示maxcount+。  maxcount属性支持的最大整数值为2147483647。 |
| config | BadgeConfig | - | 否 | 设置新事件标记相关配置属性。 |
| label6+ | string | - | 否 | 设置新事件提醒的文本值。  使用该属性时，count和maxcount属性不生效。 |

**表1** BadgeConfig

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| badgeColor | <color> | #fa2a2d | 否 | 新事件标记背景色。 |
| textColor | <color> | #ffffff | 否 | 数字标记的数字文本颜色。 |
| textSize | <length> | 10px | 否 | 数字标记的文本大小。 |
| badgeSize | <length> | 6px | 否 | 圆点标记大小。 |

## 样式

支持[通用样式](js-components-common-styles.md)。

**说明** 

badge组件的子组件大小不能超过badge组件本身的大小，否则子组件不会绘制。

## 事件

支持[通用事件](js-components-common-events.md)。

## 方法

支持[通用方法](js-components-common-methods.md)。

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <badge class="badge" config="{{badgeconfig}}" visible="true" count="100" maxcount="99">
    <text class="text1">example</text>
  </badge>
  <badge class="badge" visible="true" count="0">
    <text class="text2">example</text>
  </badge>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  width: 100%;
  align-items: center;
}
.badge {
  width: 50%;
  margin-top: 100px;
}
.text1 {
  background-color: #f9a01e;
  font-size: 50px;
}
.text2 {
  background-color: #46b1e3;
  font-size: 50px;
}
```

```js
// xxx.js
export default {
  data:{
    badgeconfig:{
      badgeColor:"#0a59f7",
      textColor:"#ffffff",
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ZQFCpux5RKmxa0J8ZROdcQ/zh-cn_image_0000002742005627.png)
