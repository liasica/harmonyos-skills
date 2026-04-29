---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/smart-photopicker
title: 使用PhotoPicker推荐图片
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用PhotoPicker推荐图片
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ca273a3f1cc382c749eaff63218ee76e2c248ab2ae61ea4f918c754dcf4fa52a
---

应用在调用PhotoPicker接口时，如果配置了PhotoPicker图片推荐参数，当设备中有满足图片推荐参数的图片，且设备中的图片已经分析完成时，PhotoPicker界面除了展示全量的图片外，还会展示符合条件的推荐图片供用户参考选择，从而缩短用户筛选图片的时间。

* 选择特定类型（[RecommendationType](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#recommendationtype11)）的图片，如身份证、银行卡、驾驶证、行驶证、二维码等。当有符合应用指定类型的图片传入时，将显示对应的图片推荐页。

  以指定图片类型为二维码为例，PhotoPicker界面上将出现“二维码”的Tab页，展示图库中的二维码图片。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/fzWRUosnQjiihpkwlgfZQA/zh-cn_image_0000002589244913.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053534Z&HW-CC-Expire=86400&HW-CC-Sign=24E89AFED210F2F9A40ACD6E437A50E2C68ABB125610D3E02C6EF6A1A1034E58)
* 在图文编辑时选择图片，系统可以根据应用传入的文本信息，提取出时间、地点、事物或活动，并根据提取的信息，推荐对应的图片展示在PhotoPicker中。

  举例说明，如设置的推荐参数文本是“国庆节，带着女儿去了上海野生动物园，看到了凶猛的大象，漂亮的火烈鸟，还有她心心念念的大熊猫，小家伙可开心了。”

  而且手机中有相应的图片，图片分析完成时，会在“推荐”的Tab页中展示出时间是国庆节，地点是上海野生动物园的大熊猫、火烈鸟、大象的图片。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/xMvzinTSQ2KMY0CiDWC8dQ/zh-cn_image_0000002558765108.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053534Z&HW-CC-Expire=86400&HW-CC-Sign=920DC1E3AF5DC903404D355FEB6557B1E0E1ABA949671CA46DEA000A6DE3BF8F)

## 约束与限制

* PhotoPicker推荐图片的功能依赖于图片分析的结果，只有在媒体库中的图片分析完成后，系统才会进行推荐。

  当设备在灭屏充电时，在电量充足、温度正常的情况下，系统将自动进行图片分析。

  如果图片带有地理位置信息，设备需要联网才可以正常解析图片中的位置信息。
* 当前仅支持推荐图片类型的文件。

## 开发方式

**前提条件**

开发者可以通过两种方式实现PhotoPicker，拉起系统图库。请选择其中一种方式，实现PhotoPicker。

* 参考[使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)，实现PhotoPicker。

  在配置参数**photoAccessHelper.PhotoSelectOptions**时，媒体文件类型MIMEType（[PhotoViewMIMETypes](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photoviewmimetypes)）需要配置为IMAGE\_TYPE或IMAGE\_VIDEO\_TYPE。
* 参考[使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)，实现PhotoPicker。

  在配置PhotoPickerComponent的属性**pickerOptions**时，媒体文件类型MIMEType（[PhotoViewMIMETypes](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#photoviewmimetypes)）需要配置为IMAGE\_TYPE或IMAGE\_VIDEO\_TYPE。

说明

* 当MIMEType配置为IMAGE\_TYPE或IMAGE\_VIDEO\_TYPE，并在后续步骤中配置了推荐参数，将根据参数推荐**图片类型**的文件。页签“全部”下展示的文件类型与MIMEType配置项一致。
* 当MIMEType配置为其他类型，推荐不生效。正常展示PhotoPicker筛选的全部照片。

接下来将以通过PhotoPickerComponent为例，指导开发者如何配置PhotoPicker推荐参数，从而实现PhotoPicker推荐图片。

### 根据特定类型推荐图片

当需要推荐特定类型的图片，如身份证、银行卡、驾驶证、行驶证、二维码等，可通过配置[RecommendationOptions](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#recommendationoptions11).recommendationType，指定推荐的图片类型。支持的图片类型可参考[RecommendationType](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#recommendationtype11)。

```
1. let recommendationOptions: photoAccessHelper.RecommendationOptions = {
2. recommendationType: photoAccessHelper.RecommendationType.QR_CODE // 配置枚举类型，不同的枚举值，推荐不同种类的图片
3. };
4. this.pickerOptions.recommendationOptions = recommendationOptions;// 将推荐参数赋值给 pickerOptions.recommendationOptions
```

说明

当前示例以通过Picker组件实现推荐图片为例。

如果使用Picker接口，需要将推荐参数赋值给 photoSelectOptions.recommendationOptions。

### 根据文本信息推荐图片

当需要在图文编辑时，根据文本信息推荐图片，可通过配置[RecommendationOptions](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#recommendationoptions11).textContextInfo。

说明

如果RecommendationOptions同时配置了recommendationType和textContextInfo，仅textContextInfo生效。

```
1. let textInfo: photoAccessHelper.TextContextInfo = {
2. text: '国庆节，带着女儿去了上海野生动物园，看到了凶猛的大象，漂亮的火烈鸟，还有她心心念念的大熊猫，小家伙可开心了。'
3. };
4. let recommendationOptions: photoAccessHelper.RecommendationOptions = {
5. textContextInfo: textInfo
6. };
7. this.pickerOptions.recommendationOptions = recommendationOptions;// 将推荐参数赋值给 pickerOptions.recommendationOptions
```

说明

当前示例以通过Picker组件实现推荐图片为例。

如果使用Picker接口，需要将推荐参数赋值给 photoSelectOptions.recommendationOptions。

## 示例代码

* [基于PhotoPicker实现图片推荐功能](https://gitcode.com/HarmonyOS_Samples/SmartPhotoPicker)
