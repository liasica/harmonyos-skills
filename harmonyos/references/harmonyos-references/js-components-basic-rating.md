---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-rating
title: rating
category: harmonyos-references
scraped_at: 2026-04-28T08:03:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:da6f698c473767ee8e4be42510297a7499ecffd559881ceb39f819cd56bb2ba6
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

评分条，表示用户使用感受的衡量标准条。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| numstars | number | 5 | 否 | 设置评分条的星级总数。 |
| rating | number | 0 | 否 | 设置评分条当前评星数。 |
| stepsize | number | 0.5 | 否 | 设置评分条的评星步长。 |
| indicator | boolean | false | 否 | 设置评分条是否为指示器。  true：作为指示器，用户不可操作。  false：非指示器，用户可操作。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| star-background | string | - | 否 | 设置单个星级未选中的背景图片，只支持本地路径图片，图片格式为png和jpg。 |
| star-foreground | string | - | 否 | 设置单个星级选中的前景图片，只支持本地路径图片，图片格式为png和jpg。 |
| star-secondary | string | - | 否 | 设置单个星级部分选中的次级背景图片，该图片会覆盖背景图片，只支持本地路径图片，图片格式为png和jpg。 |
| width | <length>|<percentage> | 120px  60px（不可操作） | 否 | 默认值是在未设置自定义资源和评分星数时，使用5个星和默认资源下的宽度值。 |
| height | <length>|<percentage> | 24px  12px（不可操作） | 否 | 默认值是在未设置自定义资源和评分星数时，使用5个星和默认资源下的高度值。 |
| rtl-flip | boolean | true | 否 | 在rtl文字方向下是否自动翻转图源。  true：在rtl文字方向下自动翻转图源。  false：在rtl文字方向下不自动翻转图源。 |

说明

star-background，star-secondary，star-foreground三个星级图源必须全部设置，否则默认的星级颜色为灰色，以此提示图源设置错误。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { rating: number } | 评分条的评星发生改变时触发该回调。 |

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating numstars="5" rating="5" @change="changeRating" id="rating">
4. </rating>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. }
7. .rating {
8. width: 200px;
9. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. changeRating(e){
5. promptAction.showToast({
6. message: e.rating
7. });
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/8B_FZY6qSQ-PWEB0utVVOg/zh-cn_image_0000002583480199.png?HW-CC-KV=V1&HW-CC-Date=20260428T000304Z&HW-CC-Expire=86400&HW-CC-Sign=B132AD692589B0FAF7CBFBFAF935BBCCEE566212A10AB5AEA871CE646C8A603F)
