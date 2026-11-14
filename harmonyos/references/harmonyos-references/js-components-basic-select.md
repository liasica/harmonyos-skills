---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select
title: select
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > select
category: harmonyos-references
scraped_at: 2026-11-14T08:50:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:277a7468405076e144df8c4a91da9650b62363917ac0ce8c1faf9db896e6be90
---

下拉选择按钮，可使用下拉菜单展示并选择内容。

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持<[option](js-components-basic-option.md)>。

## 属性

支持[通用属性](js-components-common-attributes.md)。

## 样式

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| font-family | string | 否 | 字体系列列表，用逗号分隔。列表中第一个系统中存在的字体样式或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体样式，会被选中作为当前文本的字体样式。  默认值：sans-serif |

## 事件

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {newValue: newValue} | 选择下拉选项后触发该事件，返回值为一个对象，其中newValue为选中项option的value值。 |

**说明** 

select组件不支持click事件。

## 方法

支持[通用方法](js-components-common-methods.md)。

## 示例

```html
<!-- xxx.hml -->
<div class="container">
    <select>
        <option for="{{ array }}" value="{{ $item.value }}">
            {{ $item.name }}
        </option>
    </select>
</div>
```

```css
/* xxx.css */
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
```

```js
// xxx.js
export default {
    data: {
        array: [
            {
                "value": "下拉选项0", "name": "选项0"
            },
            {
                "value": "下拉选项1", "name": "选项1"
            },
            {
                "value": "下拉选项2", "name": "选项2"
            },
            {
                "value": "下拉选项3", "name": "选项3"
            },
        ]
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/r3NT3oK7QOyJ3V878KZnqQ/zh-cn_image_0000002788469436.png?HW-CC-KV=V1&HW-CC-Date=20261114T005031Z&HW-CC-Expire=31536000000&HW-CC-Sign=9160DB5BB91EC37711AE6B64FC09F6F2595009BB94EB6ACBD3317376665048BF)
