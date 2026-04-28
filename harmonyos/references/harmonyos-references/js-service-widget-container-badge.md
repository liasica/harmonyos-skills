---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-badge
title: badge
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 容器组件 > badge
category: harmonyos-references
scraped_at: 2026-04-28T08:03:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:958a507f4c08db99cd3b4c26c8ee30236e129094c7f838cb3a76bfdd82c27ade
---

应用中如果有需用户关注的新事件提醒，可以采用新事件标记来标识。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持单个子组件。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| placement | string | rightTop | 否 | 事件提醒的数字标记或者圆点标记的位置，可选值为：  - right：位于组件右边框。  - rightTop：位于组件边框右上角。  - left：位于组件左边框。 |
| count | number | 0 | 否 | 设置提醒的消息数，默认为0。当设置相应的提醒消息数大于0时，消息提醒会变成数字标记类型，未设置消息数或者消息数不大于0时，消息提醒将采用圆点标记。  说明：当数字设置为大于maxcount时，将使用maxcount显示。count属性最大支持整数值为2147483647。 |
| visible | boolean | false | 否 | 是否显示消息提醒，当收到新信息提醒时可以设置该属性为true，显示相应的消息提醒，如果需要使用数字标记类型，同时需要设置相应的count属性。 |
| maxcount | number | 99 | 否 | 最大消息数限制，当收到新信息提醒大于该限制时，标识数字会进行省略，仅显示maxcount+。  说明：maxcount属性最大支持整数值为2147483647。 |
| config | BadgeConfig | - | 否 | 设置新事件标记相关配置属性。 |
| label | string | - | 否 | 设置新事件提醒的文本值。  说明：使用该属性时，count和maxcount属性不生效。 |

### BadgeConfig

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| badgeColor | <color> | #fa2a2d | 否 | 新事件标记背景色。 |
| textColor | <color> | #ffffff | 否 | 数字标记的数字文本颜色。 |
| textSize | <length> | 10px | 否 | 数字标记的数字文本大小。 |
| badgeSize | <length> | 6px | 否 | 圆点标记的大小。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-service-widget-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-service-widget-common-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <badge class="badge" config="{{ badgeConfig }}" visible="true" count="100" maxcount="99">
4. <text class="text1">example</text>
5. </badge>
6. <badge class="badge" visible="true" count="1">
7. <text class="text2">example</text>
8. </badge>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. width: 100%;
5. align-items: center;
6. }

8. .badge {
9. width: 160px;
10. height: 60px;
11. margin-top: 30px;
12. }

14. .text1 {
15. background-color: #f9a01e;
16. font-size: 19fp;
17. }

19. .text2 {
20. background-color: #46b1e3;
21. font-size: 19fp;
22. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. badgeConfig: {
5. badgeColor: "#0a59f7",
6. textColor: "#ffffff",
7. }
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/eP_f00TRRVe1WR8nzA0JkA/zh-cn_image_0000002552960424.png?HW-CC-KV=V1&HW-CC-Date=20260428T000335Z&HW-CC-Expire=86400&HW-CC-Sign=BF74C5116089C6FB620B725ECD5437C3DE0F85616CE1A83D6F75C00907046CA2)
