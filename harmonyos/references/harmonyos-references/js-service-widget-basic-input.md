---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-input
title: input
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 基础组件 > input
category: harmonyos-references
scraped_at: 2026-04-29T13:54:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:34111a24b742092030b95698834f38bce84bd6e5a675fe11886631081326fd2c
---

交互式组件，提供单选框功能。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | radio | 是 | input组件类型，当前仅支持radio类型：  - "radio"：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个。 |
| checked | boolean | false | 否 | 当前组件是否选中，true表示选中，false表示未选中。 |
| name | string | - | 否 | input组件的名称。 |
| value | string | - | 否 | input组件的value值，类型为radio时必填且相同name值的选项该值唯一。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-service-widget-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | $event.checkedItem | radio单选框的checked状态发生变化时触发该事件，返回选中的组件value值。 |
| click | - | 点击动作触发该事件。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="content">
3. <input type="radio" checked='true' name="radioSample" value="radio1" onchange="onRadioChange"></input>
4. <input type="radio" checked='false' name="radioSample" value="radio2" onchange="onRadioChange"></input>
5. <input type="radio" checked='false' name="radioSample" value="radio3" onchange="onRadioChange"></input>
6. </div>
```

```
1. /* xxx.css */
2. .content{
3. width: 100%;
4. height: 200px;
5. justify-content: center;
6. align-items: center;
7. }
```

```
1. {
2. "actions": {
3. "onRadioChange":{
4. "action": "message",
5. "params": {
6. "checkedRadio": "$event.checkedItem"
7. }
8. }
9. }
10. }
```

**4\*4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/eKA_Ef-rQbKQqR-waITvqA/zh-cn_image_0000002558766958.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055402Z&HW-CC-Expire=86400&HW-CC-Sign=A246E58989727B731824838254388ADD5BC02126682244BD8167E6E12DD2FF1E)
