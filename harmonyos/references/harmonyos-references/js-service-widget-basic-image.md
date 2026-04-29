---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-image
title: image
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 基础组件 > image
category: harmonyos-references
scraped_at: 2026-04-29T13:54:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:610ec5e5625ecb78099ea716b3bd3876ef187664b2fb46e9d66a0b1e6648e442
---

图片组件，用来渲染展示图片。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| src | string | - | 否 | 图片的路径。  - 支持本地路径，图片格式包括png， jpg， bmp， svg和gif。  - 支持内存图片读取，scheme格式为memory://。  **说明：**  如需显示网络图片，应自行下载后使用内存图片方式刷新，禁止使用网络URL地址。 |
| alt | string | - | 否 | 占位图，当指定图片在加载中时显示。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-service-widget-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| object-fit | string | cover | 否 | 设置图片的缩放类型，可选值类型说明请见object-fit 类型说明，svg格式不支持。 |
| match-text-direction | boolean | false | 否 | 图片是否跟随文字方向，svg格式不支持。  默认值：false，表示图片不跟随文字方向。 |
| fit-original-size | boolean | false | 否 | [image](js-service-widget-basic-image.md)组件在未设置宽高的情况下是否适应图源尺寸，该属性为true时object-fit属性不生效，svg类型图源不支持该属性。  默认值：false，表示[image](js-service-widget-basic-image.md)组件在未设置宽高的情况下不适应图源尺寸。 |

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

  + 如果image组件本身的长宽小于svg中的长宽，svg会被裁切，仅显示左上角部分。
  + 如果image组件本身的长宽大于svg中的长宽，svg会被放置在image组件的左上角，image组件其他部分显示空白。

## 事件

PhonePC/2in1TabletTVWearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| complete | - | 图片成功加载时触发该回调。 |
| error | - | 图片加载出现异常时触发该回调。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <stack class="content">
3. <image src="/common/bg3.jpg" class="img"></image>
4. </stack>
```

```
1. /* xxx.css */
2. .img{
3. object-fit: contain
4. }
```

**4\*4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/xGlB3wykQNCOchoUZRqvdQ/zh-cn_image_0000002589246765.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055401Z&HW-CC-Expire=86400&HW-CC-Sign=04171E9E9303C15380207F4ADCB41BDD75225C48E9DBAA2587E6FAF9687B865C)
