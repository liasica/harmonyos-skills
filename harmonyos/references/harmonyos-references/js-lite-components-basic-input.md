---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-input
title: input
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 基础组件 > input
category: harmonyos-references
scraped_at: 2026-04-28T08:03:28+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:2d5e98fd8e9326b8fceaafca4943ecddcd4894e2b28d9af276af05b63e179498
---

交互式组件，包括单选框，多选框，按钮。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

不支持。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | button | 否 | input组件类型，可选值为button，checkbox，radio，text。  button，checkbox，radio，text不支持动态修改。可选值定义如下：  - button：定义可点击的按钮。  - checkbox：定义多选框。  - radio：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个。  - text：定义用于文字输入的文本框，仅在支持输入法功能的真机设备上，支持点击拉起文字输入界面，[UI预览](../harmonyos-guides/ui-ide-previewer.md)无效果。 |
| checked | boolean | false | 否 | 当前组件是否选中，true表示选中，false表示未选中。仅type为checkbox和radio生效。 |
| name | string | - | 否 | input组件的名称。 |
| value | string | - | 否 | input组件的value值，当类型为radio时必填且相同name值的选项该值唯一。 |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

## 事件

PhonePC/2in1TabletTVWearableLite Wearable

* 当input类型为checkbox、radio时，支持如下事件：

  | 名称 | 参数 | 描述 |
  | --- | --- | --- |
  | change | { checked:true | false } | checkbox多选框或radio单选框的checked状态发生变化时触发该事件。 |
  | click | - | 点击动作触发该事件。 |
  | longpress | - | 长按动作触发该事件。 |
  | swipe5+ | [SwipeEvent](js-lite-common-events.md) | 组件上快速滑动后触发。 |
* 当input类型为button时，支持如下事件：

  | 名称 | 参数 | 描述 |
  | --- | --- | --- |
  | click | - | 点击动作触发该事件。 |
  | longpress | - | 长按动作触发该事件。 |
  | swipe5+ | [SwipeEvent](js-lite-common-events.md) | 组件上快速滑动后触发。 |

## 样式

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #ffffff | 否 | 按钮的文本颜色。 |
| font-size | <length> | 30px | 否 | 按钮的文本尺寸。 |
| width | <length> | - | 否 | type为button时，默认值为100px。 |
| height | <length> | - | 否 | type为button时，默认值为50px。 |
| font-family | string | SourceHanSansSC-Regular | 否 | 字体。目前仅支持SourceHanSansSC-Regular 字体。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有的内边距属性。  该属性可以有1到4个值：  - 指定一个值时，该值指定四个边的内边距。  - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。  - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。  - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。  - 只有一个值时，这个值会被指定给全部的四个边。  - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。  - 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。  - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| background-color | <color> | - | 否 | 设置背景颜色。 |
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为：  - flex：弹性布局。  - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

1. type为button

   ```
   1. <!-- xxx.hml -->
   2. <div class="div-button">
   3. <input class="button" type="button" value="Input-Button"></input>
   4. </div>
   ```

   ```
   1. /* xxx.css */
   2. .div-button {
   3. flex-direction: column;
   4. align-items: center;
   5. width: 100%;
   6. height: 100%;
   7. }
   8. .button {
   9. margin-top: 30px;
   10. width: 280px;
   11. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/b6112IzzRsSFvgXOXKJmmw/zh-cn_image_0000002552800760.png?HW-CC-KV=V1&HW-CC-Date=20260428T000327Z&HW-CC-Expire=86400&HW-CC-Sign=457869C8235CF781307F999658C73216DEBEB8B48351FFDA6B3E0ADE94DD0D3C)
2. type为checkbox

   ```
   1. <!-- xxx.hml -->
   2. <div class="content">
   3. <input onchange="checkboxOnChange" checked="true" type="checkbox"></input>
   4. <text class="text">{{text}}</text>
   5. </div>
   ```

   ```
   1. /* xxx.css */
   2. .content{
   3. width: 100%;
   4. height: 100%;
   5. flex-direction: column;
   6. align-items: center;
   7. justify-content: center;
   8. }
   9. .text{
   10. font-size: 30px;
   11. text-align: center;
   12. width: 200px;
   13. margin-top: 20px;
   14. height: 100px;
   15. }
   ```

   ```
   1. // xxx.js
   2. export default {
   3. data: {
   4. text: "text"
   5. },
   6. checkboxOnChange(e) {
   7. this.text = e.checked;
   8. }
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/DTf8jC_xSKmrqoB-eMTcJg/zh-cn_image_0000002583440455.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000327Z&HW-CC-Expire=86400&HW-CC-Sign=3037AB26587011DCD8BD756B764FC737349552F1A0C6D116C48DABBB73D1E25E)
3. type为radio

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="item">
   4. <input type="radio" checked="true" name="radioSample" value="radio1" onchange="onRadioChange"></input>
   5. <text class="text">radio1</text>
   6. </div>
   7. <div class="item">
   8. <input type="radio" checked="false" name="radioSample" value="radio2" onchange="onRadioChange"></input>
   9. <text class="text">radio2</text>
   10. </div>
   11. <div class="item">
   12. <input type="radio" checked="false" name="radioSample" value="radio3" onchange="onRadioChange"></input>
   13. <text class="text">radio3</text>
   14. </div>
   15. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. width: 100%;
   4. height: 100%;
   5. justify-content: center;
   6. align-items: center;
   7. flex-direction: column;
   8. }
   9. .item {
   10. width: 50%;
   11. height: 30%;
   12. justify-content: center;
   13. }
   14. .text {
   15. margin-top: 25%;
   16. font-size: 30px;
   17. text-align: center;
   18. width: 200px;
   19. height: 100px;
   20. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_x0x5rVfRg-kSMeR-246lg/zh-cn_image_0000002552960410.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000327Z&HW-CC-Expire=86400&HW-CC-Sign=5AD854B9D0AF4192FE44BA813806FE3BD57B0EEEA447B652744B79E04789559B)
