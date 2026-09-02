---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-form
title: form
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > form
category: harmonyos-references
scraped_at: 2026-09-02T15:01:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7f3780b3f8bf3b680b6f14f37fdd15c6e9a0e4fe7c6d8645c62515fa8b291559
---

**说明** 

从API version 6开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

表单容器，支持容器内input元素的内容提交和重置。

## 权限列表

无

## 子组件

支持。

## 属性

支持[通用属性](js-components-common-attributes.md)。

## 样式

支持[组件通用样式](js-components-common-styles.md)。

## 事件

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

支持[通用方法](js-components-common-methods.md)。

## 示例

```html
<!-- xxx.hml -->
<form onsubmit='onSubmit' onreset='onReset'>
  <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
    <label>选项一</label>
    <input type='radio' name='radioGroup' value='radio1'></input>
    <label>选项二</label>
    <input type='radio' name='radioGroup' value='radio2'></input>
  </div>
  <text style="margin-left: 50px;margin-bottom: 50px;">输入文本</text>
  <input type='text' name='user'></input>
  <div style="width: 600px;height: 150px;margin-top: 50px;flex-direction: row;justify-content: space-around;">
    <input type='submit'>Submit</input>
    <input type='reset'>Reset</input>
  </div>
</form>
```

```js
// xxx.js
export default{
  onSubmit(result) {
    console.info(result.value.radioGroup) // radio1 or radio2
    console.info(result.value.user) // text input value
  },
  onReset() {
    console.info('reset all value')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KlaQ_33AQRC6hk7XGlczaw/zh-cn_image_0000002736315477.gif)
