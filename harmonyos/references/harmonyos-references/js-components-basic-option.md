---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option
title: option
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > option
category: harmonyos-references
scraped_at: 2026-04-28T08:03:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:65b99dea8641326babdac8c874b9dbb633fbce42471abc45a550c5d6f6a2c94e
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当作为<[select](js-components-basic-select.md)>的子组件时用来展示下拉选择的具体项目。

当作为<[menu](js-components-basic-menu.md)>的子组件时用来展示弹出菜单的具体项目。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| selected | boolean | - | 否 | 选择项是否为下拉列表的默认项，仅在父组件是select时生效。true表示该选项是下拉列表的默认项，false表示该选项不是下拉列表的默认项。 |
| value | string | - | 是 | 该属性定义选项值，将作为父组件select/menu的selected事件回调参数。  option选项的UI展示值需要放在标签内，如：  <option value="10">十月</option> |
| icon | string | - | 否 | 图标资源路径，该图标展示在选项文本前，图标格式为jpg，png和svg。 |

## 样式

PhonePC/2in1TabletTVWearable

支持如下样式。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #e6000000 | 否 | 选择项的文本颜色。 |
| font-size | <length> | 16px | 否 | 选择项的文本尺寸。 |
| allow-scale | boolean | true | 否 | 选择项的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-weight | number | string | normal | 否 | 选择项的字体粗细，见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| text-decoration | string | none | 否 | 选择项的文本修饰，见[text组件text-decoration的样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 选择项的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持。

## 方法

PhonePC/2in1TabletTVWearable

不支持。

## 示例

PhonePC/2in1TabletTVWearable

详见[menu示例](js-components-basic-menu.md#示例)。
