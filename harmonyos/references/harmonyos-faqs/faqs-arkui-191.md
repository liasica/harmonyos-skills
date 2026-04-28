---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191
title: 通用属性width是否支持设置变量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 通用属性width是否支持设置变量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c3121cea9c951c0fbb67016266cac73a9592b6f88106c7628ace01cc666ff61
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/cGH94RmlRKWkVGAFYk2AHg/zh-cn_image_0000002194158632.png?HW-CC-KV=V1&HW-CC-Date=20260428T002547Z&HW-CC-Expire=86400&HW-CC-Sign=201FFEC9E572247B879E8383F996315D3A03726595B1D0E6EC1F1744E73C91AC "点击放大")
