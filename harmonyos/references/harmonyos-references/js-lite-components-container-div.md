---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-div
title: div
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 容器组件 > div
category: harmonyos-references
scraped_at: 2026-09-05T06:17:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7041ad21ef2e4de279b2f35859534d22fd8a39ae560beddfca47cc10e290c6cf
---

基础容器，用作页面结构的根节点或将内容进行分组。

**说明** 

该组件从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持。

## 属性

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

## 事件

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | [SwipeEvent](js-lite-common-events.md#swipeevent) | 组件上快速滑动后触发。 |

## 样式

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | string | row | 否 | flex容器主轴方向。可选项有：  - column：垂直方向从上到下  - row：水平方向从左到右 |
| flex-wrap | string | nowrap | 否 | flex容器是单行还是多行显示，此属性暂不支持动态修改。可选项有：  - nowrap：不换行，单行显示。  - wrap：换行，多行显示。 |
| justify-content | string | flex-start | 否 | flex容器当前行的主轴对齐格式。可选项有：  - flex-start：项目位于容器的开头。  - flex-end：项目位于容器的结尾。  - center：项目位于容器的中心。  - space-between：项目位于各行之间留有空白的容器内。  - space-around：项目位于各行之前、之间、之后都留有空白的容器内。 |
| align-items | string | stretch5+  flex-start1-4 | 否 | flex容器当前行的交叉轴对齐格式，可选值为：  - stretch5+：弹性元素在交叉轴方向被拉伸到与容器相同的高度或宽度。  - flex-start：元素向交叉轴起点对齐。  - flex-end：元素向交叉轴终点对齐。  - center：元素沿交叉轴方向居中。 |
| display | string | flex | 否 | 确定该元素视图框的类型，此属性暂不支持动态修改。可选值为：  - flex：弹性布局  - none：不渲染此元素 |
| width | <length> | <percentage>5+ | - | 否 | 设置组件自身的宽度。  未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | - | 否 | 设置组件自身的高度。  未设置时组件高度默认为0。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有内边距。  该属性可以有1到4个值：  - 指定一个值时，该值指定四个边的内边距。  - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。  - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。  - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有外边距，该属性可以有1到4个值。  - 只有一个值时，这个值会被指定给全部的四个边。  - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。  - 三个值时，第一个值被匹配给上，第二个值被匹配给左和右，第三个值被匹配给下。  - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| background-color | <color> | - | 否 | 设置背景颜色。 |
| opacity5+ | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

## 示例

1. Flex样式

   ```html
   <!-- xxx.hml -->
   <div class="container">
     <div class="flex-box">
       <div class="flex-item color-primary"></div>
       <div class="flex-item color-warning"></div>
       <div class="flex-item color-success"></div>
     </div>
   </div>
   ```

   ```css
   /* xxx.css */
   .container {
     flex-direction: column;
     justify-content: center;
     align-items: center;
     width: 454px;
     height: 454px;
   }
   .flex-box {
     justify-content: space-around;
     align-items: center;
     width: 400px;
     height: 140px;
     background-color: #ffffff;
   }
   .flex-item {
     width: 120px;
     height: 120px;
     border-radius: 16px;
   }
   .color-primary {
     background-color: #007dff;
   }
   .color-warning {
     background-color: #ff7500;
   }
   .color-success {
     background-color: #41ba41;
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/nIz7MB47QHidREmTrF_ngg/zh-cn_image_0000002712406866.png)
2. Flex Wrap样式

   ```html
   <!-- xxx.hml -->
   <div class="container">
     <div class="flex-box">
       <div class="flex-item color-primary"></div>
       <div class="flex-item color-warning"></div>
       <div class="flex-item color-success"></div>
     </div>
   </div>
   ```

   ```css
   /* xxx.css */
   .container {
     flex-direction: column;
     justify-content: center;
     align-items: center;
     width: 454px;
     height: 454px;
   }
   .flex-box {
     justify-content: space-around;
     align-items: center;
     flex-wrap: wrap;
     width: 300px;
     height: 250px;
     background-color: #ffffff;
   }
   .flex-item {
     width: 120px;
     height: 120px;
     border-radius: 16px;
   }
   .color-primary {
     background-color: #007dff;
   }
   .color-warning {
     background-color: #ff7500;
   }
   .color-success {
     background-color: #41ba41;
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/cJyCmBiyTDK_hnGYBhNYYw/zh-cn_image_0000002742125815.png)
