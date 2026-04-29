---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-button
title: button
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > button
category: harmonyos-references
scraped_at: 2026-04-29T13:53:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:361c1640b44b5a1bc4686a2df02a6586956b0eeb8ba5a62145f79dc70867df65
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

按钮组件，包括胶囊按钮、圆形按钮、文本按钮、弧形按钮、下载按钮。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | - | 否 | 不支持动态修改。默认展示为胶囊型按钮，不同于胶囊类型，四边圆角可以通过border-radius分别指定。该属性可选值包括：  - capsule：胶囊型按钮，带圆角按钮，有背景色和文本。  - circle：圆形按钮，支持放置图标。  - text：文本按钮，仅包含文本显示。  - arc：弧形按钮，仅支持智能穿戴。  - download：下载按钮，额外增加下载进度条功能。 |
| value | string | - | 否 | button的文本值。 |
| icon | string | - | 否 | button的图标路径，图标格式为jpg，png和svg。 |
| placement5+ | string | end | 否 | 仅在type属性为缺省时生效，设置图标位于文本的位置，可选值为：  - start：图标位于文本起始处。  - end：图标位于文本结束处。  - top：图标位于文本上方。  - bottom：图标位于文本下方。 |
| waiting | boolean | false | 否 | waiting状态，waiting为true时展现等待中转圈效果，位于文本左侧。值为false时，不展示等待中效果。类型为download时不生效。 |

## 样式

PhonePC/2in1TabletTVWearable

### type设置为非arc

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | #007dff | 否 | 按钮的文本颜色。 |
| font-size | <length> | 16px | 否 | 按钮的文本尺寸。 |
| allow-scale | boolean | true | 否 | 按钮的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | string | normal | 否 | 按钮的字体样式。 |
| font-weight | number | string | normal | 否 | 按钮的字体粗细。见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | <string> | sans-serif | 否 | 按钮的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |
| icon-width | <length> | - | 否 | 设置圆形按钮内部图标的宽，默认填满整个圆形按钮。  icon使用svg图源时必须设置该样式。 |
| icon-height | <length> | - | 否 | 设置圆形按钮内部图标的高，默认填满整个圆形按钮。  icon使用svg图源时必须设置该样式。 |
| radius | <length> | - | 否 | 按钮圆角半径。在圆形按钮类型下该样式优先于通用样式的width和height样式。 |

### type设置为arc

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)中background-color、opacity、display、visibility、position、[left|top|right|bottom]外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| text-color | <color> | #de0000 | 否 | 弧形按钮的文本颜色。 |
| font-size | <length> | 37.5px | 否 | 弧形按钮的文本尺寸。 |
| allow-scale | boolean | true | 否 | 弧形按钮的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。 |
| font-style | string | normal | 否 | 弧形按钮的字体样式。 |
| font-weight | number | string | normal | 否 | 弧形按钮的字体粗细。见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | <string> | sans-serif | 否 | 按钮的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-components-common-events.md)。

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

类型为download时，支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| setProgress | { progress:percent } | 设定下载按钮进度条进度，取值位于0-100区间内，当设置的值大于0时，下载按钮展现进度条。当设置的值大于等于100时，取消进度条显示。  浮在进度条上的文字通过value值进行变更。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="div-button">
3. <button class="first" type="capsule" value="Capsule button"></button>
4. <button class="button circle" type="circle" icon="common/ic_add_default.png"></button>
5. <button class="button text" type="text">Text button</button>
6. <button class="button download" type="download" id="download-btn"
7. onclick="progress">{{downloadText}}</button>
8. <button class="last" type="capsule" waiting="true">Loading</button>
9. </div>
```

```
1. /* xxx.css */
2. .div-button {
3. flex-direction: column;
4. align-items: center;
5. }
6. .first{
7. background-color: #F2F2F2;
8. text-color: #0D81F2;
9. }
10. .button {
11. margin-top: 15px;
12. }
13. .last{
14. background-color: #F2F2F2;
15. text-color: #969696;
16. margin-top: 15px;
17. width: 280px;
18. height:72px;
19. }
20. .button:waiting {
21. width: 280px;
22. }
23. .circle {
24. background-color: #007dff;
25. radius: 72px;
26. icon-width: 72px;
27. icon-height: 72px;
28. }
29. .text {
30. text-color: red;
31. font-size: 40px;
32. font-weight: 900;
33. font-family: sans-serif;
34. font-style: normal;
35. }
36. .download {
37. width: 280px;
38. text-color: white;
39. background-color: #007dff;
40. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. count: 5,
5. downloadText: "Download"
6. },
7. progress(e) {
8. this.count += 10;
9. this.downloadText = this.count + "%";
10. this.$element('download-btn').setProgress({ progress: this.count});
11. if (this.count >= 100) {
12. this.downloadText = "Done";
13. }
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/JRpMGvt3QTiDPMPp5SMe0Q/zh-cn_image_0000002589326579.png?HW-CC-KV=V1&HW-CC-Date=20260429T055321Z&HW-CC-Expire=86400&HW-CC-Sign=919CF88A8937D3B13E577D226A59D43328AE4B4D43BC156ADBDF37011AC0B340)
