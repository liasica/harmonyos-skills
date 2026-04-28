---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select
title: select
category: harmonyos-references
scraped_at: 2026-04-28T08:03:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:445c47455b2da29bb7b04b6980ed476486938fdb80eb1ba2ffa61c992ba1ee3c
---

下拉选择按钮，可使用下拉菜单展示并选择内容。

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

支持<[option](js-components-basic-option.md)>。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-components-common-attributes.md)。

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| font-family | string | 否 | 字体样式列表，用逗号分隔。列表中第一个系统中存在的字体样式或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体样式，会被选中作为当前文本的字体样式。  默认值：sans-serif |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | {newValue: newValue} | 选择下拉选项后触发该事件，返回值为一个对象，其中newValue为选中项option的value值。 |

说明

select组件不支持click事件。

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <select>
4. <option for="{{ array }}" value="{{ $item.value }}">
5. {{ $item.name }}
6. </option>
7. </select>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. height: 100%;
8. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. array: [
5. {
6. "value": "下拉选项0", "name": "选项0"
7. },
8. {
9. "value": "下拉选项1", "name": "选项1"
10. },
11. {
12. "value": "下拉选项2", "name": "选项2"
13. },
14. {
15. "value": "下拉选项3", "name": "选项3"
16. },
17. ]
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/R6Gwm0T0R7y3lZE2Twer-A/zh-cn_image_0000002583440245.png?HW-CC-KV=V1&HW-CC-Date=20260428T000304Z&HW-CC-Expire=86400&HW-CC-Sign=52F5C33B3834E20E987770D5E519956DC9670370AD0C45A6BF03A24EC4057838)
