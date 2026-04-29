---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-switch
title: switch
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > switch
category: harmonyos-references
scraped_at: 2026-04-29T13:53:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f3e98957c24914a9fb88e97afe12f35ba252832ef8243b326ab9f0776b884435
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

开关选择器，通过开关，开启或关闭某个功能。

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
| checked | boolean | false | 否 | 是否选中。 true表示选中，false表示未选中。 |
| showtext | boolean | false | 否 | 是否显示文本。true表示显示文本，false表示不显示文本。 |
| texton | string | "On" | 否 | 选中时显示的文本。 |
| textoff | string | "Off" | 否 | 未选中时显示的文本。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| texton-color | <color> | #000000 | 否 | 选中时显示的文本颜色，仅设置texton和textoff生效。 |
| textoff-color | <color> | #000000 | 否 | 未选中时显示的文本颜色，仅设置texton和textoff生效。 |
| text-padding | number | 0px | 否 | texton/textoff中最长文本两侧距离滑块边界的距离。 |
| font-size | <length> | - | 否 | 文本尺寸，仅设置texton和textoff生效。 |
| allow-scale | boolean | true | 否 | 文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-style | string | normal | 否 | 字体样式，仅设置texton和textoff生效。见text组件[font-style的样式属性](js-components-basic-text.md#样式)。 |
| font-weight | number | string | normal | 否 | 字体粗细，仅设置texton和textoff生效。见text组件的[font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。仅设置texton和textoff生效。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { checked: checkedValue } | 选中状态改变时触发该事件。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <switch @change="normalSwitchChange">
4. </switch>
5. <switch class="switch" showtext="true" texton="开启" textoff="关闭" @change="switchChange">
6. </switch>
7. <switch class="switch text" showtext="true" texton="开启" textoff="关闭" checked="true" @change="switchChange">
8. </switch>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. }
7. .switch {
8. texton-color: red;
9. textoff-color: forestgreen;
10. }
11. .text {
12. text-padding: 20px;
13. font-size: 30px;
14. font-weight: 700;
15. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. title: 'World'
6. },
7. switchChange(e) {
8. if (e.checked) {
9. promptAction.showToast({
10. message: "打开开关"
11. });
12. } else {
13. promptAction.showToast({
14. message: "关闭开关"
15. });
16. }
17. },
18. normalSwitchChange(e) {
19. if (e.checked) {
20. promptAction.showToast({
21. message: "switch on"
22. });
23. } else {
24. promptAction.showToast({
25. message: "switch off"
26. });
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/aYnp-O_qQ-qeHUSW_sOZ6Q/zh-cn_image_0000002589246535.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055326Z&HW-CC-Expire=86400&HW-CC-Sign=707AF8E3E05276E1D3F6CA2835449A7188F573ED2C1CE951816D7ED24795A1DA)
