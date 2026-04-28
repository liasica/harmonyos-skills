---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-form
title: form
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > form
category: harmonyos-references
scraped_at: 2026-04-28T08:02:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a0110cc2a8340077a8b88758bd90166fa4842eccf219c20b8e3bf9c9b9ab579a
---

说明

从API version 6开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

表单容器，支持容器内input元素的内容提交和重置。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-components-common-attributes.md)。

## 样式

PhonePC/2in1TabletTVWearable

支持[组件通用样式](js-components-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| submit | FormResult | 点击提交按钮，进行表单提交时，触发该事件。 |
| reset | - | 点击重置按钮后，触发该事件。 |

**表1** FormResult

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| value | Object | input元素的name和value的值。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <form onsubmit='onSubmit' onreset='onReset'>
3. <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
4. <label>选项一</label>
5. <input type='radio' name='radioGroup' value='radio1'></input>
6. <label>选项二</label>
7. <input type='radio' name='radioGroup' value='radio2'></input>
8. </div>
9. <text style="margin-left: 50px;margin-bottom: 50px;">输入文本</text>
10. <input type='text' name='user'></input>
11. <div style="width: 600px;height: 150px;margin-top: 50px;flex-direction: row;justify-content: space-around;">
12. <input type='submit'>Submit</input>
13. <input type='reset'>Reset</input>
14. </div>
15. </form>
```

```
1. // xxx.js
2. export default{
3. onSubmit(result) {
4. console.info(result.value.radioGroup) // radio1 or radio2
5. console.info(result.value.user) // text input value
6. },
7. onReset() {
8. console.info('reset all value')
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/89i3o3p9S5yweZk14kJI0w/zh-cn_image_0000002583440227.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=CDC70B6DCE55F7E2A09212442B96EC6FEBFBA586EABB7B6120597F4D9599A992)
