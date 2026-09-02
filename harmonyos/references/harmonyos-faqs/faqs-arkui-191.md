---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191
title: 通用属性width是否支持设置变量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 通用属性width是否支持设置变量
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:174aec30801ba52211a311759b1a539fd42542f69cb55d80948398140338c929
---

通用属性width支持设置变量。

```
1. @Entry
2. @Component
3. struct Page1 {
4. @State message: string = 'Hello';
5. @State widthNum: number = 300;

7. build() {
8. Row() {
9. Column() {
10. Text(this.message)
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. .width(this.widthNum)
14. .backgroundColor(Color.Blue)
15. }
16. .width('100%')
17. }
18. .height('100%')
19. }
20. }
```

[DoesWidthSupportSettingVariables.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DoesWidthSupportSettingVariables.ets#L21-L40)

效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/cGH94RmlRKWkVGAFYk2AHg/zh-cn_image_0000002194158632.png "点击放大")
