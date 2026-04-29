---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-popup
title: popup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > popup
category: harmonyos-references
scraped_at: 2026-04-29T13:53:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f5e1a3f313bb82fecf3442fbe668aed9acc3824e15bf49bfc505158f045950eb
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

气泡指示。给控件绑定气泡弹窗，并在点击控件或者调用气泡弹窗显示方法后弹出相应的气泡提示来引导用户进行操作。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件节点5+。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| target | string | - | 是 | popup绑定目标元素的id属性值，不支持动态切换。 |
| placement | string | bottom | 否 | popup相对于目标元素的位置。可选值为：  - left：位于目标元素左边；  - right：位于目标元素右边；  - top：位于目标元素上边；  - bottom：位于目标元素下边；  - topLeft：位于目标元素左上角；  - topRight：位于目标元素右上角；  - bottomLeft：位于目标元素左下角；  - bottomRight：位于目标元素右下角。 |
| keepalive5+ | boolean | false | 否 | 设置当前popup是否需要保留。设置为true时，点击屏幕区域或者页面切换气泡不会消失，需调用气泡组件的hide方法才可让气泡消失；设置为false时，点击屏幕区域或者页面切换气泡会自动消失。 |
| clickable5+ | boolean | true | 否 | popup是否支持点击目标元素弹窗，当设置为false时，只支持方法调用显示弹窗。 |
| arrowoffset5+ | <length> | 0 | 否 | popup箭头在弹窗处的偏移，默认居中，正值按照语言方向进行偏移，负值相反。 |

说明

* 不支持focusable属性。

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| mask-color | <color> | - | 否 | 遮罩层的颜色，默认值为全透明。 |

说明

* 不支持position相关样式。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| visibilitychange | { visibility: boolean } | 当气泡弹出和消失时会触发该回调函数。 |

## 方法

PhonePC/2in1TabletTVWearable

仅支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| show5+ | - | 弹出气泡提示。 |
| hide5+ | - | 隐藏气泡提示。 |

说明

1. popup气泡弹窗属性、样式均不支持动态更新。
2. popup气泡弹窗的margin样式是相对于target元素进行生效的，如popup在target元素下方，此时只生效margin-top样式，popup在target元素左上方，此时只生效margin-bottom和margin-right样式。
3. popup的border四边样式需一致，若四边设置不一致且圆角为零，则按左、上、右、下的顺序取第一个被设置的样式，否则border不生效。
4. popup的target组件的click事件不生效。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text id="text">Click to show the pop-up</text>
4. <!-- popup supports single child of any type5+ -->
5. <popup id="popup" class="popup" target="text" placement="top" keepalive="true" clickable="true"
6. arrowoffset="100px" onvisibilitychange="visibilitychange" onclick="hidepopup">
7. <text class="text">Text content of the pop-up</text>
8. </popup>
9. <button class="button" onclick="showpopup">Click to show the pop-up</button>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. padding-top: 200px;
6. padding-left: 200px;
7. }
8. .popup {
9. mask-color: gray;
10. }
11. .text {
12. color: white;
13. }
14. .button {
15. width: 220px;
16. height: 100px;
17. margin-top: 50px;
18. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction'
3. export default {
4. visibilitychange(e) {
5. promptAction.showToast({
6. message: 'visibility change visibility: ' + e.visibility,
7. duration: 3000
8. });
9. },
10. showpopup() {
11. this.$element("popup").show();
12. },
13. hidepopup() {
14. this.$element("popup").hide();
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/2egw9wKRTBiPdFEO5Rz-ow/zh-cn_image_0000002558766710.png?HW-CC-KV=V1&HW-CC-Date=20260429T055319Z&HW-CC-Expire=86400&HW-CC-Sign=2B2EF92492E105498FEEBFAC641FE13532245AC28D9F022C38DE45CF746FD26E)
