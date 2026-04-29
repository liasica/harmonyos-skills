---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-span
title: span
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > span
category: harmonyos-references
scraped_at: 2026-04-29T13:53:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:12103f6e5e1e554b9b67f326673e9a20824212a15b987d98b69607a738e1bad1
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

作为<[text](js-components-basic-text.md)>子组件提供文本修饰能力。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-components-common-attributes.md)。

说明

不支持focusable和disabled属性。

## 样式

PhonePC/2in1TabletTVWearable

仅支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | - | 否 | 设置文本段落的文本颜色。 |
| font-size | <length> | 30px | 否 | 设置文本段落的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置文本段落的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | string | normal | 否 | 设置文本段落的字体样式，见[text组件font-style的样式属性](js-components-basic-text.md#样式)。 |
| font-weight | number | string | normal | 否 | 设置文本段落的字体粗细，见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| text-decoration | string | none | 否 | 设置文本段落的文本修饰，见[text组件text-decoration样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 设置文本段落的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

仅支持[通用事件](js-components-common-events.md)中的click事件。

## 方法

PhonePC/2in1TabletTVWearable

不支持。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. <span class="spanTxt">span</span>
5. </text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. }
7. .title {
8. font-size: 30px;
9. text-align: center;
10. width: 100%;
11. height: 100px;
12. }
13. .spanTxt{
14. color: chartreuse;
15. font-size: 80px;
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/tYnWDq6KRZKIUFeqj4lTyA/zh-cn_image_0000002589326593.png?HW-CC-KV=V1&HW-CC-Date=20260429T055326Z&HW-CC-Expire=86400&HW-CC-Sign=50A4D8994AC52F64F41E2198B906BCA7408B450F252DDCEC344CFF394D2FC48F)
