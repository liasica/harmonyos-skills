---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-piece
title: piece
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > piece
category: harmonyos-references
scraped_at: 2026-04-29T13:53:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b0b9cfd39e1db5692afa2c0a99622da81fa00b8c35b3b8e039f91be589161b9a
---

一种块状的入口，可包含图片和文本，常用于展示收件人。例如，邮件收件人或信息收件人。

说明

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| content | string | 是 | 操作块文本内容。 |
| closable | boolean | 否 | 设置当前操作块是否显示删除图标，当显示删除图标时，点击删除图标会触发close事件。  true表示显示删除图标，false表示不显示删除图标。默认为false。 |
| icon | string | 否 | 操作块删除图标的url，支持本地路径。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

说明

文本和图片默认在整个piece组件中居中。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| close | - | 当piece组件点击删除图标触发，此时可以通过渲染属性if删除该组件。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml-->
2. <div class="container" >
3. <piece if="{{first}}" content="example"></piece>
4. <piece if="{{second}}" content="example" closable="true" onclose="closeSecond"></piece>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. align-items: center;
6. justify-content: center;
7. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. first: true,
5. second: true
6. },
7. closeSecond(e) {
8. this.second = false;
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7liC6qOeSuOmHMpp72C9Vw/zh-cn_image_0000002589246531.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055324Z&HW-CC-Expire=86400&HW-CC-Sign=4387EB6D7D124271DC8C9A810CDEB82423AB78312B35E596B10D063F20F7619A)
