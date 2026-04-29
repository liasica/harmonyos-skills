---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-blur-effect
title: 模糊
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画效果 > 模糊
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c02fe11732f202e247a095a98562c4aa09b4a3728a54fce894a415285d87548
---

动画效果可以丰富界面的细节，提升UI界面的真实感和品质感。例如，模糊和阴影效果可以让物体看起来更加立体，使得动画更加生动。ArkUI提供了丰富的效果接口，开发者可快速打造出精致、个性化的效果。本章主要介绍常用的模糊、阴影和色彩效果等接口。

模糊效果可以体现界面空间的纵深感，区分前后元素的层级关系。

| 接口 | 说明 |
| --- | --- |
| [backdropBlur](../harmonyos-references/ts-universal-attributes-background.md#backdropblur) | 为当前组件添加背景模糊效果，入参为模糊半径。 |
| [blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur) | 为当前组件添加内容模糊效果，入参为模糊半径。 |
| [backgroundBlurStyle](../harmonyos-references/ts-universal-attributes-background.md#backgroundblurstyle9) | 为当前组件添加背景模糊效果，入参为模糊样式。 |
| [foregroundBlurStyle](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle) | 为当前组件添加内容模糊效果，入参为模糊样式。 |
| [motionBlur](../harmonyos-references/ts-universal-attributes-motionblur.md#motionblur) | 为当前组件添加由缩放大小或位移变化引起的运动过程中的动态模糊效果，入参为模糊半径和锚点坐标。 |

说明

以上接口均为实时模糊接口，每帧执行实时渲染，性能负载较大。当模糊内容与模糊半径均无需变动时，推荐采用静态模糊接口[blur](../harmonyos-references/js-apis-effectkit.md#blur)。最佳实践请参考：[图像模糊动效优化-使用场景](../best-practices/bpta-fuzzy-scene-performance-optimization.md#section4945532519)。

## 使用backdropBlur为组件添加背景模糊

```
1. @Entry
2. @Component
3. struct BlurEffectsExample {
4. build() {
5. Column({ space: 10 }) {
6. Text('backdropBlur')
7. .width('90%')
8. .height('90%')
9. .fontSize(20)
10. .fontColor(Color.White)
11. .textAlign(TextAlign.Center)
12. .backdropBlur(10)// 对背景进行模糊
13. // 请将$r('app.media.bg')替换为实际资源文件
14. .backgroundImage($r('app.media.bg'))
15. .backgroundImageSize({ width: 400, height: 300 })
16. }
17. .width('100%')
18. .height('50%')
19. .margin({ top: 20 })
20. }
21. }
```

[BlurEffectsExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animationBlur/template1/BlurEffectsExample.ets#L15-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/YYrLmNjvSGiz4gvo99kwpQ/zh-cn_image_0000002589244297.png?HW-CC-KV=V1&HW-CC-Date=20260429T052814Z&HW-CC-Expire=86400&HW-CC-Sign=955050F6DE2F51845CDD9803CFFAC49A61D845467D264F93EECDF7F81DDB97E0)

## 使用blur为组件添加内容模糊

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. @State radius: number = 0;
8. @State text: string = '';
9. @State y: Resource | string = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text1').id);// 请在resources\base\element\string.json文件中配置name为'animation_blur_text1'，value为非空字符串的资源

11. aboutToAppear() {
12. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text2'，value为非空字符串的资源
13. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text3'，value为非空字符串的资源
14. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text4'，value为非空字符串的资源
15. this.text = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text2').id) +
16. "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text3').id) + this.y +
17. "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text4').id) + this.radius;
18. }

20. build() {
21. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
22. Text(this.text)
23. .height(200)
24. .fontSize(20)
25. .fontWeight(FontWeight.Bold)
26. .fontFamily("cursive")
27. .fontStyle(FontStyle.Italic)
28. // 请将$r('app.media.bg')替换为实际资源文件
29. Image($r("app.media.bg"))
30. .blur(this.radius)// 使用blur接口为照片组件添加内容模糊效果
31. .height('100%')
32. .width("100%")
33. .objectFit(ImageFit.Cover)
34. }.height('100%')
35. .width("100%")
36. .onTouch((event?: TouchEvent) => {
37. if (event) {
38. if (event.type === TouchType.Move) {
39. this.y = Number(event.touches[0].y.toString()).toString();
40. this.radius = Number(this.y) / 10; // 根据跟手过程中的滑动距离修改模糊半径，配合模糊接口，形成跟手模糊效果
41. }
42. if (event.type === TouchType.Up) {
43. this.radius = 0;
44. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text1'，value为非空字符串的资源
45. this.y = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text1').id);
46. }
47. }
48. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text2'，value为非空字符串的资源
49. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text3'，value为非空字符串的资源
50. // 请在resources\base\element\string.json文件中配置name为'animation_blur_text4'，value为非空字符串的资源
51. this.text = this.context.resourceManager.getStringSync($r('app.string.animation_blur_text2').id) + "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text3').id) + this.y +
52. "\n" + this.context.resourceManager.getStringSync($r('app.string.animation_blur_text4').id) + this.radius;
53. })
54. }
55. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animationBlur/template2/Index.ets#L15-L71)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/qRauI5DHRr-YPgkvV4u_BA/zh-cn_image_0000002558764490.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052814Z&HW-CC-Expire=86400&HW-CC-Sign=7E34CA64537670BCA5602EB6E7F1F51522C7DC6068FD88586886705AA2A09BCB)

## 使用backgroundBlurStyle为组件添加背景模糊效果

```
1. @Entry
2. @Component
3. struct BackDropBlurStyleDemo {
4. build() {
5. Grid() {
6. GridItem() {
7. Column() {
8. Column() {
9. // 请将$r('app.string.originalImage')替换为实际资源文件，在本示例中该资源文件的value值为"原图"
10. Text($r('app.string.originalImage'))
11. .fontSize(20)
12. .fontColor(Color.White)
13. .textAlign(TextAlign.Center)
14. .width('100%')
15. .height('100%')
16. }
17. .height(100)
18. .aspectRatio(1)
19. .borderRadius(10)
20. // 请将$r('app.media.bg')替换为实际资源文件
21. .backgroundImage($r('app.media.bg'))

23. // 请将$r('app.string.originalImage')替换为实际资源文件，在本示例中该资源文件的value值为"原图"
24. Text($r('app.string.originalImage'))
25. .fontSize(12)
26. .fontColor(Color.Black)
27. }
28. .height('100%')
29. .margin({ top: 20 })
30. .justifyContent(FlexAlign.Start)
31. }
32. .width(200)
33. .height(200)

35. GridItem() {
36. Column() {
37. Column() {
38. Text('Thin')
39. .fontSize(20)
40. .fontColor(Color.White)
41. .textAlign(TextAlign.Center)
42. .width('100%')
43. .height('100%')
44. }
45. .height(100)
46. .aspectRatio(1)
47. .borderRadius(10)
48. // 请将$r('app.media.bg')替换为实际资源文件
49. .backgroundImage($r('app.media.bg'))
50. // BlurStyle.Thin: 为组件添加轻薄材质模糊效果
51. // ThemeColorMode.LIGHT: 固定使用浅色模式效果
52. // AdaptiveColor.DEFAULT: 不使用取色模糊，使用默认的颜色作为蒙版颜色
53. // scale: 背景材质模糊效果程度，默认值是1
54. .backgroundBlurStyle(BlurStyle.Thin, {
55. colorMode: ThemeColorMode.LIGHT,
56. adaptiveColor: AdaptiveColor.DEFAULT,
57. scale: 0.1
58. })

60. Text('Thin')
61. .fontSize(12)
62. .fontColor(Color.Black)
63. }
64. .height('100%')
65. .margin({ top: 20 })
66. .justifyContent(FlexAlign.Start)
67. }
68. .width(200)
69. .height(200)

71. GridItem() {
72. Column() {
73. Column() {
74. Text('Regular')
75. .fontSize(20)
76. .fontColor(Color.White)
77. .textAlign(TextAlign.Center)
78. .width('100%')
79. .height('100%')
80. }
81. .height(100)
82. .aspectRatio(1)
83. .borderRadius(10)
84. // 请将$r('app.media.bg')替换为实际资源文件
85. .backgroundImage($r('app.media.bg'))
86. .backgroundBlurStyle(BlurStyle.Regular, {
87. colorMode: ThemeColorMode.LIGHT,
88. adaptiveColor: AdaptiveColor.DEFAULT,
89. scale: 0.1
90. })

92. Text('Regular')
93. .fontSize(12)
94. .fontColor(Color.Black)
95. }
96. .height('100%')
97. .justifyContent(FlexAlign.Start)
98. }
99. .width(200)
100. .height(200)

102. GridItem() {
103. Column() {
104. Column() {
105. Text('Thick')
106. .fontSize(20)
107. .fontColor(Color.White)
108. .textAlign(TextAlign.Center)
109. .width('100%')
110. .height('100%')
111. }
112. .height(100)
113. .aspectRatio(1)
114. .borderRadius(10)
115. // 请将$r('app.media.bg')替换为实际资源文件
116. .backgroundImage($r('app.media.bg'))
117. .backgroundBlurStyle(BlurStyle.Thick, {
118. colorMode: ThemeColorMode.LIGHT,
119. adaptiveColor: AdaptiveColor.DEFAULT,
120. scale: 0.1
121. })

123. Text('Thick')
124. .fontSize(12)
125. .fontColor(Color.Black)
126. }
127. .height('100%')
128. .justifyContent(FlexAlign.Start)
129. }
130. .width(200)
131. .height(200)

133. GridItem() {
134. Column() {
135. Column() {
136. Text('BACKGROUND_THIN')
137. .fontSize(12)
138. .fontColor(Color.White)
139. .textAlign(TextAlign.Center)
140. .width('100%')
141. .height('100%')
142. }
143. .height(100)
144. .aspectRatio(1)
145. .borderRadius(10)
146. // 请将$r('app.media.bg')替换为实际资源文件
147. .backgroundImage($r('app.media.bg'))
148. .backgroundBlurStyle(BlurStyle.BACKGROUND_THIN, {
149. colorMode: ThemeColorMode.LIGHT,
150. adaptiveColor: AdaptiveColor.DEFAULT,
151. scale: 0.1
152. })

154. Text('BACKGROUND_THIN')
155. .fontSize(12)
156. .fontColor(Color.Black)
157. }
158. .height('100%')
159. .justifyContent(FlexAlign.Start)
160. }
161. .width(200)
162. .height(200)

164. GridItem() {
165. Column() {
166. Column() {
167. Text('BACKGROUND_REGULAR')
168. .fontSize(12)
169. .fontColor(Color.White)
170. .textAlign(TextAlign.Center)
171. .width('100%')
172. .height('100%')
173. }
174. .height(100)
175. .aspectRatio(1)
176. .borderRadius(10)
177. // 请将$r('app.media.bg')替换为实际资源文件
178. .backgroundImage($r('app.media.bg'))
179. .backgroundBlurStyle(BlurStyle.BACKGROUND_REGULAR, {
180. colorMode: ThemeColorMode.LIGHT,
181. adaptiveColor: AdaptiveColor.DEFAULT,
182. scale: 0.1
183. })

185. Text('BACKGROUND_REGULAR')
186. .fontSize(12)
187. .fontColor(Color.Black)
188. }
189. .height('100%')
190. .justifyContent(FlexAlign.Start)
191. }
192. .width(200)
193. .height(200)

195. GridItem() {
196. Column() {
197. Column() {
198. Text('BACKGROUND_THICK')
199. .fontSize(12)
200. .fontColor(Color.White)
201. .textAlign(TextAlign.Center)
202. .width('100%')
203. .height('100%')
204. }
205. .height(100)
206. .aspectRatio(1)
207. .borderRadius(10)
208. // 请将$r('app.media.bg')替换为实际资源文件
209. .backgroundImage($r('app.media.bg'))
210. .backgroundBlurStyle(BlurStyle.BACKGROUND_THICK, {
211. colorMode: ThemeColorMode.LIGHT,
212. adaptiveColor: AdaptiveColor.DEFAULT,
213. scale: 0.1
214. })

216. Text('BACKGROUND_THICK')
217. .fontSize(12)
218. .fontColor(Color.Black)
219. }
220. .height('100%')
221. .justifyContent(FlexAlign.Start)
222. }
223. .width(200)
224. .height(200)

226. GridItem() {
227. Column() {
228. Column() {
229. Text('BACKGROUND_ULTRA_THICK')
230. .fontSize(12)
231. .fontColor(Color.White)
232. .textAlign(TextAlign.Center)
233. .width('100%')
234. .height('100%')
235. }
236. .height(100)
237. .aspectRatio(1)
238. .borderRadius(10)
239. // 请将$r('app.media.bg')替换为实际资源文件
240. .backgroundImage($r('app.media.bg'))
241. .backgroundBlurStyle(BlurStyle.BACKGROUND_ULTRA_THICK, {
242. colorMode: ThemeColorMode.LIGHT,
243. adaptiveColor: AdaptiveColor.DEFAULT,
244. scale: 0.1
245. })

247. Text('BACKGROUND_ULTRA_THICK')
248. .fontSize(12)
249. .fontColor(Color.Black)
250. }
251. .height('100%')
252. .justifyContent(FlexAlign.Start)
253. }
254. .width(200)
255. .height(200)
256. }
257. .columnsTemplate('1fr 1fr')
258. .rowsTemplate('1fr 1fr 1fr 1fr')
259. .width('100%')
260. .height('100%')
261. .margin({ top: 40 })
262. }
263. }
```

[BackDropBlurStyleDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animationBlur/template3/BackDropBlurStyleDemo.ets#L15-L279)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/90koVDljRk2HOySyn9FNHQ/zh-cn_image_0000002558604834.png?HW-CC-KV=V1&HW-CC-Date=20260429T052814Z&HW-CC-Expire=86400&HW-CC-Sign=6D79308251A3603746FE0CE9069D5B5DC366AB80F9D0C908CABA4FEC51394D3A)

## 使用foregroundBlurStyle为组件添加内容模糊效果

```
1. @Entry
2. @Component
3. struct ForegroundBlurStyleDemo {
4. build() {
5. Grid() {
6. GridItem() {
7. Column() {
8. Column() {
9. // 请将$r('app.string.originalImage')替换为实际资源文件，在本示例中该资源文件的value值为"原图"
10. Text($r('app.string.originalImage'))
11. .fontSize(20)
12. .fontColor(Color.White)
13. .textAlign(TextAlign.Center)
14. .width('100%')
15. .height('100%')
16. }
17. .height(100)
18. .aspectRatio(1)
19. .borderRadius(10)
20. // 请将$r('app.media.bg')替换为实际资源文件
21. .backgroundImage($r('app.media.bg'))

23. // 请将$r('app.string.originalImage')替换为实际资源文件，在本示例中该资源文件的value值为"原图"
24. Text($r('app.string.originalImage'))
25. .fontSize(12)
26. .fontColor(Color.Black)
27. }
28. .height('100%')
29. .justifyContent(FlexAlign.Start)
30. }
31. .width(200)
32. .height(200)

34. GridItem() {
35. Column() {
36. Column() {
37. Text('Thin')
38. .fontSize(20)
39. .fontColor(Color.White)
40. .textAlign(TextAlign.Center)
41. .width('100%')
42. .height('100%')
43. }
44. .height(100)
45. .aspectRatio(1)
46. .borderRadius(10)
47. // 请将$r('app.media.bg')替换为实际资源文件
48. .backgroundImage($r('app.media.bg'))
49. // BlurStyle.Thin: 为组件添加轻薄材质模糊效果
50. // ThemeColorMode.LIGHT: 固定使用浅色模式效果
51. // AdaptiveColor.DEFAULT: 不使用取色模糊，使用默认的颜色作为蒙版颜色
52. // scale: 背景材质模糊效果程度，默认值是1
53. .foregroundBlurStyle(BlurStyle.Thin, {
54. colorMode: ThemeColorMode.LIGHT,
55. adaptiveColor: AdaptiveColor.DEFAULT,
56. scale: 0.1
57. })

59. Text('Thin')
60. .fontSize(12)
61. .fontColor(Color.Black)
62. }
63. .height('100%')
64. .justifyContent(FlexAlign.Start)
65. }
66. .width(200)
67. .height(200)

69. GridItem() {
70. Column() {
71. Column() {
72. Text('Regular')
73. .fontSize(20)
74. .fontColor(Color.White)
75. .textAlign(TextAlign.Center)
76. .width('100%')
77. .height('100%')
78. }
79. .height(100)
80. .aspectRatio(1)
81. .borderRadius(10)
82. // 请将$r('app.media.bg')替换为实际资源文件
83. .backgroundImage($r('app.media.bg'))
84. .foregroundBlurStyle(BlurStyle.Regular, {
85. colorMode: ThemeColorMode.LIGHT,
86. adaptiveColor: AdaptiveColor.DEFAULT,
87. scale: 0.1
88. })

90. Text('Regular')
91. .fontSize(12)
92. .fontColor(Color.Black)
93. }
94. .height('100%')
95. .justifyContent(FlexAlign.Start)
96. }
97. .width(200)
98. .height(200)

100. GridItem() {
101. Column() {
102. Column() {
103. Text('Thick')
104. .fontSize(20)
105. .fontColor(Color.White)
106. .textAlign(TextAlign.Center)
107. .width('100%')
108. .height('100%')
109. }
110. .height(100)
111. .aspectRatio(1)
112. .borderRadius(10)
113. // 请将$r('app.media.bg')替换为实际资源文件
114. .backgroundImage($r('app.media.bg'))
115. .foregroundBlurStyle(BlurStyle.Thick, {
116. colorMode: ThemeColorMode.LIGHT,
117. adaptiveColor: AdaptiveColor.DEFAULT,
118. scale: 0.1
119. })

121. Text('Thick')
122. .fontSize(12)
123. .fontColor(Color.Black)
124. }
125. .height('100%')
126. .justifyContent(FlexAlign.Start)
127. }
128. .width(200)
129. .height(200)

131. GridItem() {
132. Column() {
133. Column() {
134. Text('BACKGROUND_THIN')
135. .fontSize(12)
136. .fontColor(Color.White)
137. .textAlign(TextAlign.Center)
138. .width('100%')
139. .height('100%')
140. }
141. .height(100)
142. .aspectRatio(1)
143. .borderRadius(10)
144. // 请将$r('app.media.bg')替换为实际资源文件
145. .backgroundImage($r('app.media.bg'))
146. .foregroundBlurStyle(BlurStyle.BACKGROUND_THIN, {
147. colorMode: ThemeColorMode.LIGHT,
148. adaptiveColor: AdaptiveColor.DEFAULT,
149. scale: 0.1
150. })

152. Text('BACKGROUND_THIN')
153. .fontSize(12)
154. .fontColor(Color.Black)
155. }
156. .height('100%')
157. .justifyContent(FlexAlign.Start)
158. }
159. .width(200)
160. .height(200)

162. GridItem() {
163. Column() {
164. Column() {
165. Text('BACKGROUND_REGULAR')
166. .fontSize(12)
167. .fontColor(Color.White)
168. .textAlign(TextAlign.Center)
169. .width('100%')
170. .height('100%')
171. }
172. .height(100)
173. .aspectRatio(1)
174. .borderRadius(10)
175. // 请将$r('app.media.bg')替换为实际资源文件
176. .backgroundImage($r('app.media.bg'))
177. .foregroundBlurStyle(BlurStyle.BACKGROUND_REGULAR, {
178. colorMode: ThemeColorMode.LIGHT,
179. adaptiveColor: AdaptiveColor.DEFAULT,
180. scale: 0.1
181. })

183. Text('BACKGROUND_REGULAR')
184. .fontSize(12)
185. .fontColor(Color.Black)
186. }
187. .height('100%')
188. .justifyContent(FlexAlign.Start)
189. }
190. .width(200)
191. .height(200)

193. GridItem() {
194. Column() {
195. Column() {
196. Text('BACKGROUND_THICK')
197. .fontSize(12)
198. .fontColor(Color.White)
199. .textAlign(TextAlign.Center)
200. .width('100%')
201. .height('100%')
202. }
203. .height(100)
204. .aspectRatio(1)
205. .borderRadius(10)
206. // 请将$r('app.media.bg')替换为实际资源文件
207. .backgroundImage($r('app.media.bg'))
208. .foregroundBlurStyle(BlurStyle.BACKGROUND_THICK, {
209. colorMode: ThemeColorMode.LIGHT,
210. adaptiveColor: AdaptiveColor.DEFAULT,
211. scale: 0.1
212. })

214. Text('BACKGROUND_THICK')
215. .fontSize(12)
216. .fontColor(Color.Black)
217. }
218. .height('100%')
219. .justifyContent(FlexAlign.Start)
220. }
221. .width(200)
222. .height(200)

224. GridItem() {
225. Column() {
226. Column() {
227. Text('BACKGROUND_ULTRA_THICK')
228. .fontSize(12)
229. .fontColor(Color.White)
230. .textAlign(TextAlign.Center)
231. .width('100%')
232. .height('100%')
233. }
234. .height(100)
235. .aspectRatio(1)
236. .borderRadius(10)
237. // 请将$r('app.media.bg')替换为实际资源文件
238. .backgroundImage($r('app.media.bg'))
239. .foregroundBlurStyle(BlurStyle.BACKGROUND_ULTRA_THICK, {
240. colorMode: ThemeColorMode.LIGHT,
241. adaptiveColor: AdaptiveColor.DEFAULT,
242. scale: 0.1
243. })

245. Text('BACKGROUND_ULTRA_THICK')
246. .fontSize(12)
247. .fontColor(Color.Black)
248. }
249. .height('100%')
250. .justifyContent(FlexAlign.Start)
251. }
252. .width(200)
253. .height(200)
254. }
255. .columnsTemplate('1fr 1fr')
256. .rowsTemplate('1fr 1fr 1fr 1fr')
257. .width('100%')
258. .height('100%')
259. .margin({ top: 40 })
260. }
261. }
```

[ForegroundBlurStyleDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animationBlur/template4/ForegroundBlurStyleDemo.ets#L15-L277)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/mAwoeLXaSuK4OOeTwHY05g/zh-cn_image_0000002589324359.png?HW-CC-KV=V1&HW-CC-Date=20260429T052814Z&HW-CC-Expire=86400&HW-CC-Sign=9B3A6AD67D6FBB8D6E171D35A703E511E3DFBAEAC0707F781818711387D38D3F)

## 使用motionBlur为组件添加运动模糊效果

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct motionBlurTest {
6. @State widthSize: number = 300;
7. @State heightSize: number = 240;
8. @State flag: boolean = true;
9. @State radius: number = 0;
10. @State x: number = 0.5;
11. @State y: number = 0.5;

13. build() {
14. Column() {
15. Column() {
16. // 请将$r('app.media.testImg')替换为实际资源文件
17. Image($r('app.media.testImg'))
18. .width(this.widthSize)
19. .height(this.heightSize)
20. .scale({ x: this.flag ? 1 : 0.8,y: this.flag ? 1 : 0.8 ,centerX: '50%', centerY: '50%' })
21. .onClick(() => {
22. this.radius = 50;
23. this.x = 0.5;
24. this.y = 0.5;
25. this.flag = !this.flag;
26. })
27. .animation({
28. duration: 2000,
29. iterations: 1,
30. playMode: PlayMode.Alternate,
31. onFinish: () => {
32. this.radius = 0;
33. }
34. })
35. .motionBlur({ radius: this.radius, anchor: { x: this.x, y: this.y } })
36. }
37. }.width('100%').margin({ top: 50 })
38. }
39. }
```

[MotionBlurTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/animationBlur/template5/MotionBlurTest.ets#L15-L55)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/bEKT_1HkQEmQ8LfxaEevHg/zh-cn_image_0000002589244299.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052814Z&HW-CC-Expire=86400&HW-CC-Sign=5B99587226F15314BAB1B8E558844FDB4591667E67A73A9244640F3B9BFC28DC)
