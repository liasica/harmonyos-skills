---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-xcomponent
title: xcomponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > xcomponent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4528e8ae6bb175c94c825b65a93db1c28812a934584a4506ec7ab19b2623b2cd
---

**说明** 

该组件从API version 8 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

用于显示写入了EGL/OpenGLES或媒体数据的组件，支持surface（内容单独送显，直接合成到屏幕）和component（与其他组件合成后统一送显）两种类型，适用于相机预览等需要显示EGL/OpenGLES渲染内容或媒体数据的场景。

## 权限列表

无

## 子组件

不支持。

## 属性

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，最大字符串长度为128。 |
| type | string | 是 | 用于指定xcomponent组件类型，可选值为：  - surface：组件内容单独送显，直接合成到屏幕，适用于相机预览、视频播放等场景。  - component：组件内容与其他组件合成后统一送显，适用于需要与其他组件混合显示的场景。 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称。设置后组件加载该动态库，库中注册的方法可通过onLoad回调的context或getXComponentContext在JS侧调用；不设置时不加载动态库。 |

## 样式

支持[通用样式](js-components-common-styles.md)。

## 事件

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 功能描述 |
| --- | --- |
| onLoad(context?: object) => void | 插件（通过libraryname属性加载的Native动态库）加载完成时回调事件。  context：开发者扩展的xcomponent方法的实例对象，context对象的接口由开发者自定义。 |
| onDestroy() => void | 插件销毁完成时回调事件。 |

## 方法

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 返回值类型 | 描述 |
| --- | --- | --- | --- |
| getXComponentSurfaceId | - | string | 获取xcomponent对应Surface的ID，供@ohos接口使用，比如camera相关接口。需在onLoad回调后调用。 |
| setXComponentSurfaceSize | {  surfaceWidth: number,  surfaceHeight: number  } | - | 设置xcomponent持有Surface的宽度和高度，单位为px。需在onLoad回调后调用。 |
| getXComponentContext | - | object | 获取开发者扩展的xcomponent方法的实例对象，该对象的接口由开发者自定义。需先设置libraryname属性。 |

## 示例

提供surface类型xcomponent，支持相机预览等能力。

```html
<!-- xxx.hml -->
<div style="height: 500px; width: 500px; flex-direction: column; justify-content: center; align-items: center;">
    <text id = 'camera' class = 'title'>camera_display</text>
    <xcomponent id = 'xcomponent' type = 'surface' onload = 'onload' ondestroy = 'ondestroy'></xcomponent>
</div>
```

```js
// xxx.js
import camera from '@ohos.multimedia.camera';
export default {
    onload() {
        var surfaceId = this.$element('xcomponent').getXComponentSurfaceId();
        camera.createPreviewOutput(surfaceId).then((previewOutput) => {
            console.info('Promise returned with the PreviewOutput instance');
        });
    },
    ondestroy() {
    }
}
```
