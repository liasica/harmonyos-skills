---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-image-layout
title: 图文混排
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 图文混排
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4739a7ad260ff97057ee53dd150b8f7fc8494229942982f6380a9908dcd0d3c9
---

图文混排是指图片与文字混合排列，文字可展示于图片四周。此排列方式能够直观呈现页面信息，增强视觉冲击力，使页面展示效果更加多样化。

## 使用Span和ImageSpan实现图文混排

通过设置[Text](../harmonyos-references/ts-basic-components-text.md)组件[textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)属性和设置[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)组件[verticalAlign](../harmonyos-references/ts-basic-components-imagespan.md#verticalalign)为ImageSpanAlignment.FOLLOW\_PARAGRAPH，实现商品价格优惠信息展示的应用场景。

```
1. Text() {
2. // 请将$r('app.media.hot_sale')替换为实际资源文件
3. ImageSpan($r('app.media.hot_sale'))
4. .width(50)
5. .height(30)
6. .borderRadius(5)
7. .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)
8. // 请将$r('app.string.surprise_price')替换为实际资源文件，在本示例中该资源文件的value值为"惊喜价 ￥1299"
9. Span($r('app.string.surprise_price'))
10. .fontSize(25)
11. .fontColor(Color.Red)
12. Span('1599')
13. .decoration({
14. type: TextDecorationType.LineThrough,
15. color: Color.Grey,
16. style: TextDecorationStyle.SOLID
17. })
18. .fontSize(16)
19. }.textVerticalAlign(TextVerticalAlign.CENTER)
```

[TextImageComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textImageMixedLayout/TextImageComponent.ets#L21-L41)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/SAek9WewT3C4n045BdmO9A/zh-cn_image_0000002583437895.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=7CE501010FD79958934F438966E3920EDE1AE5E82BF76C9B4B0939B5DA0EB749)

## 使用属性字符串实现图文混排

通过[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)添加图片，[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)设置多种文本样式，实现商品详情信息展示的应用场景。

```
1. // resourceGetString封装工具，从资源中获取字符串
2. import resourceGetString from '../../common/resource';
3. import { image } from '@kit.ImageKit';
4. import { LengthMetrics } from '@kit.ArkUI';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const TAG = '[Sample_Textcomponent]';
8. const DOMAIN = 0xF811;
9. const BUNDLE = 'Textcomponent_';

11. @Entry
12. @Component
13. struct styled_string_demo {
14. @State message: string = 'Hello World';
15. imagePixelMap: image.PixelMap | undefined = undefined;
16. @State imagePixelMap3: image.PixelMap | undefined = undefined;
17. mutableStr: MutableStyledString = new MutableStyledString('123');
18. controller: TextController = new TextController();
19. mutableStr2: MutableStyledString = new MutableStyledString('This is set decoration line style to the mutableStr2', [{
20. start: 0,
21. length: 15,
22. styledKey: StyledStringKey.DECORATION,
23. styledValue: new DecorationStyle({
24. type: TextDecorationType.Overline,
25. color: Color.Orange,
26. style: TextDecorationStyle.DOUBLE
27. })
28. }]);

30. async aboutToAppear() {
31. hilog.info(DOMAIN, TAG, BUNDLE + 'aboutToAppear initial imagePixelMap');
32. // $r('app.media.sky')需要替换为开发者所需的资源文件。
33. this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.sky'));
34. }

36. private async getPixmapFromMedia(resource: Resource) {
37. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
38. let imageSource = image.createImageSource(unit8Array?.buffer?.slice(0, unit8Array?.buffer?.byteLength));
39. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
40. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
41. });
42. await imageSource.release();
43. return createPixelMap;
44. }

46. leadingMarginValue: ParagraphStyle = new ParagraphStyle({
47. leadingMargin: LengthMetrics.vp(5),
48. maxLines: 2,
49. overflow: TextOverflow.Ellipsis,
50. textVerticalAlign: TextVerticalAlign.BASELINE
51. });
52. //行高样式对象
53. lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
54. //Bold样式
55. boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
56. //创建含段落样式的对象paragraphStyledString1
57. paragraphStyledString1: MutableStyledString =
58. // 请将$r('app.string.print_photo')替换为实际资源文件，在本示例中该资源文件的value值为"\n高质量冲洗照片，高清冲印3/4/5/6寸包邮塑封，品质保证，"
59. new MutableStyledString(resourceGetString.resourceToString($r('app.string.print_photo')), [
60. {
61. start: 0,
62. length: 28,
63. styledKey: StyledStringKey.PARAGRAPH_STYLE,
64. styledValue: this.leadingMarginValue
65. },
66. {
67. start: 11,
68. length: 4,
69. styledKey: StyledStringKey.LINE_HEIGHT,
70. styledValue: this.lineHeightStyle1
71. }
72. ]);
73. // 请将$r('app.string.limited_time_discount')替换为实际资源文件，在本示例中该资源文件的value值为"\n限时直降5.15元 限量增送"
74. paragraphStyledString2: MutableStyledString = new MutableStyledString(resourceGetString.resourceToString($r('app.string.limited_time_discount')), [
75. {
76. start: 0,
77. length: 5,
78. styledKey: StyledStringKey.PARAGRAPH_STYLE,
79. styledValue: this.leadingMarginValue
80. },
81. {
82. start: 0,
83. length: 4,
84. styledKey: StyledStringKey.LINE_HEIGHT,
85. styledValue: new LineHeightStyle(new LengthMetrics(40))
86. },
87. {
88. start: 0,
89. length: 9,
90. styledKey: StyledStringKey.FONT,
91. styledValue: this.boldTextStyle
92. },
93. {
94. start: 1,
95. length: 9,
96. styledKey: StyledStringKey.FONT,
97. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20), fontColor: Color.Red })
98. },
99. {
100. start: 11,
101. length: 4,
102. styledKey: StyledStringKey.FONT,
103. styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
104. }
105. ]);
106. // 请将$r('app.string.sales_volume')替换为实际资源文件，在本示例中该资源文件的value值为"\n￥22.50 销量400万+"
107. paragraphStyledString3: MutableStyledString = new MutableStyledString(resourceGetString.resourceToString($r('app.string.sales_volume')), [
108. {
109. start: 0,
110. length: 15,
111. styledKey: StyledStringKey.PARAGRAPH_STYLE,
112. styledValue: this.leadingMarginValue
113. },
114. {
115. start: 0,
116. length: 7,
117. styledKey: StyledStringKey.LINE_HEIGHT,
118. styledValue: new LineHeightStyle(new LengthMetrics(40))
119. },
120. {
121. start: 0,
122. length: 7,
123. styledKey: StyledStringKey.FONT,
124. styledValue: this.boldTextStyle
125. },
126. {
127. start: 1,
128. length: 1,
129. styledKey: StyledStringKey.FONT,
130. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18), fontColor: Color.Red })
131. },
132. {
133. start: 2,
134. length: 2,
135. styledKey: StyledStringKey.FONT,
136. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(36), fontColor: Color.Red })
137. },
138. {
139. start: 4,
140. length: 3,
141. styledKey: StyledStringKey.FONT,
142. styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20), fontColor: Color.Red })
143. },
144. {
145. start: 7,
146. length: 9,
147. styledKey: StyledStringKey.FONT,
148. styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
149. }
150. ]);

152. build() {
153. Row() {
154. Column({ space: 10 }) {
155. Text(undefined, { controller: this.controller })
156. .copyOption(CopyOptions.InApp)
157. .draggable(true)
158. .backgroundColor('#FFFFFF')
159. .borderRadius(5)
160. .width(210)
161. // 请将$r('app.string.textImageMixedLayout_content')替换为实际资源文件，在本示例中该资源文件的value值为"点击查看商品详情"
162. Button($r('app.string.textImageMixedLayout_content'))
163. .onClick(() => {
164. if (this.imagePixelMap !== undefined) {
165. this.mutableStr = new MutableStyledString(new ImageAttachment({
166. value: this.imagePixelMap,
167. size: { width: 210, height: 190 },
168. verticalAlign: ImageSpanAlignment.BASELINE,
169. objectFit: ImageFit.Fill,
170. layoutStyle: {
171. borderRadius: LengthMetrics.vp(5)
172. }
173. }));
174. this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
175. this.paragraphStyledString1.appendStyledString(this.paragraphStyledString3);
176. this.mutableStr.appendStyledString(this.paragraphStyledString1);
177. this.controller.setStyledString(this.mutableStr);
178. }
179. })
180. }
181. .width('100%')
182. }
183. .height('100%')
184. .backgroundColor('#F8F8FF')
185. }
186. }
```

[TextImageAttribute.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/textImageMixedLayout/TextImageAttribute.ets#L16-L203)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/w6coeOaARSqCkm7r_2NC-A/zh-cn_image_0000002552957850.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=142A6B93A4AD71087445C74ADC4C9550B7A2C89195F005F24BBE94FBD8F7013D)
