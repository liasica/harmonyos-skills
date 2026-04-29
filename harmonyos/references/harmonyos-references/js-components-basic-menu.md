---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu
title: menu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > menu
category: harmonyos-references
scraped_at: 2026-04-29T13:53:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bda38fbff8251a4c1748acad8b561e7d57a87f21d25ecd727e41f9b7ddea56ba
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

<[option](js-components-basic-option.md)>子组件。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| target | string | - | 否 | 目标元素选择器。当使用目标元素选择器后，点击目标元素会自动弹出menu菜单。弹出菜单位置优先为目标元素右下角，当右边可视空间不足时会适当左移，当下方空间不足时会适当上移。 |
| type | string | click | 否 | 目标元素触发弹窗的方式，可选值有：  - click：点击弹窗。  - longpress：长按弹窗。 |
| title | string | - | 否 | 菜单标题内容。 |

说明

不支持focusable、disabled属性。

## 样式

PhonePC/2in1TabletTVWearable

仅支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | - | 否 | 设置菜单的文本颜色。 |
| font-size | <length> | 30px | 否 | 设置菜单的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置菜单的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| letter-spacing | <length> | 0 | 否 | 设置菜单的字符间距。 |
| font-style | string | normal | 否 | 设置菜单的字体样式。见[text组件font-style的样式属性](js-components-basic-text.md#样式)。 |
| font-weight | number | string | normal | 否 | 设置菜单的字体粗细。见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 设置菜单的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

仅支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| selected | { value:value } | 菜单中某个值被点击选中时触发，返回的value值为option组件的value属性。 |
| cancel | - | 用户取消。 |

## 方法

PhonePC/2in1TabletTVWearable

仅支持如下方法。

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| show | { x:x, y:y } | 显示menu菜单。(x, y)指定菜单弹窗位置。其中x表示距离可见区域左边沿的 X 轴坐标，不包含任何滚动偏移，y表示距离可见区域上边沿的 Y 轴坐标，不包含任何滚动偏移以及状态栏。菜单优先显示在弹窗位置右下角，当右边可视空间不足时会适当左移，当下方空间不足时会适当上移。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text onclick="onTextClick" class="title-text">Show popup menu.</text>
4. <menu id="apiMenu">
5. <option value="Item 1">Item 1</option>
6. <option value="Item 2">Item 2</option>
7. <option value="Item 3">Item 3</option>
8. </menu>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. align-items: flex-start;
5. justify-content: center;
6. }
7. .title-text {
8. margin: 20px;
9. }
```

```
1. // xxx.js
2. export default {
3. onTextClick() {
4. this.$element("apiMenu").show({ x: 175, y: 50 });
5. }
6. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/nGYfaKkMS6GO_8K7gL66hw/zh-cn_image_0000002558766720.png?HW-CC-KV=V1&HW-CC-Date=20260429T055323Z&HW-CC-Expire=86400&HW-CC-Sign=7E3FE7755C7C2C0E93B4002DED4FF6CA66CECABAA4D603FFAB3D33CC28C67EE7)
