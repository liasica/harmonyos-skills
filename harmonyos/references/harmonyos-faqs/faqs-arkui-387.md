---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-387
title: 使用Text嵌套Span或者使用属性字符串渲染文本，部分文本颜色显示异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用Text嵌套Span或者使用属性字符串渲染文本，部分文本颜色显示异常
category: harmonyos-faqs
scraped_at: 2026-04-29T14:17:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:63458f7880f2e6b5025c8b3a3b4aa757b1267b42e3f6234324a6ed40a2ab9133
---

**问题现象**

1、使用Text嵌套Span时，文本组合会导致后续文字的颜色无法正常渲染。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Text() {
7. Span('r')
8. .fontColor(Color.Blue)
9. Span('f')
10. .fontColor(Color.Red)
11. }
12. .fontSize(50)
13. }
14. .width('100%')
15. .height('100%')
16. }
17. }
```

[RenderText\_1.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/src/main/ets/pages/RenderText_1.ets#L6-L23)

预期效果应为r显示蓝色、f显示红色，但实际rf都显示为蓝色：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/l5NAIuciTu2IxyJj2_8ceQ/zh-cn_image_0000002371388781.png?HW-CC-KV=V1&HW-CC-Date=20260429T061738Z&HW-CC-Expire=86400&HW-CC-Sign=F8426B727C2182522D62DDDBCD9F44B3C496C4F6D63E9B4C8FB45F8C1C076634)

2、使用属性字符串，同段文本设置不同样式后，与预期渲染结果不符。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. textController: TextController = new TextController();

8. async onPageShow() {
9. let style1: MutableStyledString = new MutableStyledString('');
10. style1.appendStyledString(new StyledString('sr', [{
11. start: 0,
12. length: 2,
13. styledKey: StyledStringKey.FONT,
14. styledValue: new TextStyle({ fontColor: Color.Blue, fontSize: LengthMetrics.px(150) })
15. }]));
16. style1.appendStyledString(new StyledString('fff', [{
17. start: 0,
18. length: 5,
19. styledKey: StyledStringKey.FONT,
20. styledValue: new TextStyle({ fontColor: Color.Orange, fontSize: LengthMetrics.px(150) })
21. }]));
22. this.textController.setStyledString(style1);
23. }

25. build() {
26. Row() {
27. Column() {
28. Text(undefined, { controller: this.textController })
29. .fontSize(30)
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[RenderText\_2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RenderText_2.ets#L6-L41)

预期结果应该是sr为蓝色，fff为黄色，实际srf结合为蓝色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/-u9kv5qfT2mR_s18BUisNg/zh-cn_image_0000002337590428.png?HW-CC-KV=V1&HW-CC-Date=20260429T061738Z&HW-CC-Expire=86400&HW-CC-Sign=333C7D20DE99E3F7B66A393191A3E8CB4A91E53891791EFF82A71EE88C44447C)

**解决措施**

此问题与[fontFeature](../harmonyos-references/ts-basic-components-text.md#fontfeature12)有关，fontFeature 中的 "liga" 属性默认开启, 导致部分字符发生连接, 两个码点匹配到一个glyph，因此颜色展示异常，可禁用 "liga": "\"liga\" 0"。

系统默认字体支持的liga连字：Th fb ff fb ffb ffh ffi ffk ffl fh fi fk fl rf rt rv rx ry。

在对应的Text组件上添加如下代码，即可取消连字：

```
1. Text()
2. // ...
3. .fontFeature("\"liga\" 0")
```

[RenderText\_2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/src/main/ets/pages/RenderText_2.ets#L48-L50)
