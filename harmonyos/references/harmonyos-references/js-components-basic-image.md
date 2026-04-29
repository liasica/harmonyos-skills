---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image
title: image
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > image
category: harmonyos-references
scraped_at: 2026-04-29T13:53:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2217e6211df29775fcf094f7569be47a17c130fede94c4cb2a9b89f5442ad1b0
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

图片组件，用来渲染展示图片。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | string | - | 否 | 图片的路径，支持本地路径，图片格式包括png、jpg、bmp、svg和gif。  - 支持Base64字符串6+。格式为data:image/[png | jpeg | bmp | webp];base64, [base64 data], 其中[base64 data]为Base64字符串数据。  - 支持dataability://的路径前缀，用于访问通过data ability提供的图片路径6+。 |
| alt | string | - | 否 | 占位图，当指定图片在加载中时显示。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| object-fit | string | cover | 否 | 设置图片的缩放类型，不支持svg格式。可选值类型说明请见object-fit类型说明。 |
| match-text-direction | boolean | false | 否 | 图片是否跟随文字方向，不支持svg格式。  默认值：false，表示图片不跟随文字方向。 |
| fit-original-size | boolean | false | 否 | [image](js-components-basic-image.md)组件在未设置宽高的情况下是否适应图源尺寸，该属性为true时object-fit属性不生效，svg类型图源不支持该属性。  默认值：false，表示[image](js-components-basic-image.md)组件在未设置宽高的情况下不适应图源尺寸。 |
| object-position7+ | string | 0px 0px | 否 | 设置图片在组件内展示的位置。  设置类型有两种：  1. 像素，单位px，示例 15px 15px 代表X轴或者Y轴移动的位置。  2. 字符，可选值：  - left 图片显示在组件左侧。  - top 图片显示在组件顶部位置。  - right 图片显示在组件右侧位置。  - bottom 图片显示在组件底部位置。 |

**表1** object-fit 类型说明

| 类型 | 描述 |
| --- | --- |
| cover | 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界，居中显示。 |
| contain | 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内，居中显示。 |
| fill | 不保持宽高比进行放大缩小，使得图片填充满显示边界。 |
| none | 保持原有尺寸进行居中显示。 |
| scale-down | 保持宽高比居中显示，图片缩小或者保持不变。 |

说明

使用svg图片资源时：

* 建议设置image组件的长宽，否则在父组件的长或宽为无穷大的场景下，svg资源将不会绘制。
* 如果svg描述中未指定相应的长宽，则svg将会填满image组件区域。
* 如果svg描述中指定了相应的长宽，和image组件本身的长宽效果如下：

  1. 如果image组件本身的长宽小于svg中的长宽，svg会被裁切，仅显示左上角部分。
  2. 如果image组件本身的长宽大于svg中的长宽，svg会被放置在image组件的左上角，image组件其他部分显示空白。
* 图片设置svg图源时，支持的标签范围有限，目前支持的svg标签包括svg、rect、circle、ellipse、path、line、polyline、polygon、animate、animateMotion、animateTransform。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| complete | {  width：width，  height：height  } | 图片成功加载时触发该回调，返回成功加载的图源尺寸。 |
| error | {  width：width，  height：height  } | 图片加载出现异常时触发该回调，异常时长宽为零。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image src="common/images/example.png" style="width: 300px; height: 300px; object-fit:{{fit}}; object-position: center center; border: 1px solid red;">
4. </image>
5. <select class="selects" onchange="change_fit"><option for="{{fits}}" value="{{$item}}">{{$item}}</option></select>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. justify-content: center;
4. align-items: center;
5. flex-direction: column;
6. }
7. .selects{
8. margin-top: 20px;
9. width:300px;
10. border:1px solid #808080;
11. border-radius: 10px;
12. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. fit:"cover",
5. fits: ["cover", "contain", "fill", "none", "scale-down"],
6. },
7. change_fit(e) {
8. this.fit = e.newValue;
9. },
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/GF_Nn243TPG4aI8mynEJhQ/zh-cn_image_0000002558766716.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055322Z&HW-CC-Expire=86400&HW-CC-Sign=91FBE344B2D3E7FCB17ADA2200C07D2A584FFFEE2E3DFB1FC2C62E09EC9DBBC0)
