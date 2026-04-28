---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-xcomponent
title: xcomponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > xcomponent
category: harmonyos-references
scraped_at: 2026-04-28T08:03:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9bd508c61135d8dad540ec6dddca77c49210c5e40423d882810304ebc35c2e05
---

说明

该组件从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

用于显示写入了EGL/OpenGLES或媒体数据的组件。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | string | 是 | 用于指定xcomponent组件类型，可选值为：  - surface：组件内容单独送显，直接合成到屏幕。  - component：组件内容与其他组件合成后统一送显。 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 功能描述 |
| --- | --- |
| onLoad(context?: object) => void | 插件加载完成时回调事件。  context：开发者扩展的xcomponent方法的实例对象，context对象的接口由开发者自定义。 |
| onDestroy() => void | 插件卸载完成时回调事件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 返回值类型 | 描述 |
| --- | --- | --- | --- |
| getXComponentSurfaceId | - | string | 获取xcomponent对应Surface的ID，供@ohos接口使用，比如camera相关接口。 |
| setXComponentSurfaceSize | {  surfaceWidth: number,  surfaceHeight: number  } | - | 设置xcomponent持有Surface的宽度和高度。 |
| getXComponentContext | - | object | 获取开发者扩展的xcomponent方法的实例对象。 |

## 示例

PhonePC/2in1TabletTVWearable

提供surface类型xcomponent，支持相机预览等能力。

```
1. <!-- xxx.hml -->
2. <div style="height: 500px; width: 500px; flex-direction: column; justify-content: center; align-items: center;">
3. <text id = 'camera' class = 'title'>camera_display</text>
4. <xcomponent id = 'xcomponent' type = 'surface' onload = 'onload' ondestroy = 'ondestroy'></xcomponent>
5. </div>
```

```
1. // xxx.js
2. import camera from '@ohos.multimedia.camera';
3. export default {
4. onload() {
5. var surfaceId = this.$element('xcomponent').getXComponentSurfaceId();
6. camera.createPreviewOutput(surfaceId).then((previewOutput) => {
7. console.info('Promise returned with the PreviewOutput instance');
8. })
9. }
10. }
```
