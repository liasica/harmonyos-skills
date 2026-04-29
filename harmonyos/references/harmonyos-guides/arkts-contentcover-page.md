---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-contentcover-page
title: 绑定全模态页面（bindContentCover）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 绑定模态页面 > 绑定全模态页面（bindContentCover）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:885006cd55b824919bf17af599fa63f54802ad8b82420230b42186404f2ee80c
---

[全模态页面（bindContentCover）](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)是全屏模态形式的弹窗交互页面，完全覆盖底层父视图。适用于查看大图，全屏查看文稿等场景。

## 使用约束

全模态页面本质上是弹窗类组件，其交互层级默认为应用内顶层。

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)导航转场时，新push的页面层级无法超出全模态，其效果仍然显示在模态页面之下。针对此类场景，建议将模态页面的内容迁移至转场页面中实现。例如，在上述情况下，可以使用NavDestination来替代拉起的模态页面，新push的页面层级低于全模态。

## 生命周期

全模态页面提供了生命周期函数，用于通知应用程序该弹窗的生命周期状态。生命周期的触发顺序依次为：onWillAppear -> onAppear -> onWillDisappear -> onDisappear。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onWillAppear | () => void | 全模态页面显示（动画开始前）回调函数。 |
| onAppear | () => void | 全模态页面显示（动画结束后）回调函数。 |
| onWillDisappear | () => void | 全模态页面回退（动画开始前）回调函数。 |
| onDisappear | () => void | 全模态页面回退（动画结束后）回调函数。 |

## 使用bindContentCover构建全屏模态内容覆盖半模态

全模态与半模态之间存在弹窗式的层级交互。后拉起的模态页面能够覆盖先前的模态页面。若开发者期望实现全屏转场，以覆盖半模态，并在全屏页面侧滑退出后，半模态页面仍保持显示，使用bindSheet结合bindContentCover将满足这一场景诉求。

详见[模态转场](arkts-modal-transition.md#使用bindcontentcover构建全屏模态转场效果)章节，了解使用bindContentCover构建全屏模态转场效果。

```
1. import { curves } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. interface PersonList {
5. name: string,
6. cardNum: string
7. }

9. @Entry
10. @Component
11. struct BindContentCoverDemo {
12. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. private manager = this.context.resourceManager;
14. private personList: Array<PersonList> = [
15. // 'Person_example1'资源文件中的value值为'王**'
16. { name: this.manager.getStringByNameSync('Person_example1'), cardNum: '1234***********789' },
17. // 'Person_example2'资源文件中的value值为'宋*'
18. { name: this.manager.getStringByNameSync('Person_example2'), cardNum: '2345***********789' },
19. // 'Person_example3'资源文件中的value值为'许**'
20. { name: this.manager.getStringByNameSync('Person_example3'), cardNum: '3456***********789' },
21. // 'Person_example4'资源文件中的value值为'唐*'
22. { name: this.manager.getStringByNameSync('Person_example4'), cardNum: '4567***********789' }
23. ];
24. // 半模态转场控制变量
25. @State isSheetShow: boolean = false;
26. // 全模态转场控制变量
27. @State isPresent: boolean = false;

29. @Builder
30. MyContentCoverBuilder() {
31. Column() {
32. Row() {
33. // 请将$r('app.string.Text_choose_person')替换为实际资源文件，在本示例中该资源文件的value值为"选择乘车人"
34. Text($r('app.string.Text_choose_person'))
35. .fontSize(20)
36. .fontColor(Color.White)
37. .width('100%')
38. .textAlign(TextAlign.Center)
39. .padding({ top: 30, bottom: 15 })
40. }
41. .backgroundColor(0x007dfe)

43. Row() {
44. // 请将$r('app.string.Text_add_person')替换为实际资源文件，在本示例中该资源文件的value值为"+ 添加乘车人"
45. Text($r('app.string.Text_add_person'))
46. .fontSize(16)
47. .fontColor(0x333333)
48. .margin({ top: 10 })
49. .padding({ top: 20, bottom: 20 })
50. .width('92%')
51. .borderRadius(10)
52. .textAlign(TextAlign.Center)
53. .backgroundColor(Color.White)
54. }

56. Column() {
57. ForEach(this.personList, (item: PersonList, index: number) => {
58. Row() {
59. Column() {
60. if (index % 2 == 0) {
61. Column()
62. .width(20)
63. .height(20)
64. .border({ width: 1, color: 0x007dfe })
65. .backgroundColor(0x007dfe)
66. } else {
67. Column()
68. .width(20)
69. .height(20)
70. .border({ width: 1, color: 0x007dfe })
71. }
72. }
73. .width('20%')

75. Column() {
76. Text(item.name)
77. .fontColor(0x333333)
78. .fontSize(18)
79. Text(item.cardNum)
80. .fontColor(0x666666)
81. .fontSize(14)
82. }
83. .width('60%')
84. .alignItems(HorizontalAlign.Start)

86. Column() {
87. // 请将$r('app.string.Text_edit')替换为实际资源文件，在本示例中该资源文件的value值为"编辑"
88. Text($r('app.string.Text_edit'))
89. .fontColor(0x007dfe)
90. .fontSize(16)
91. }
92. .width('20%')
93. }
94. .padding({ top: 10, bottom: 10 })
95. .border({ width: { bottom: 1 }, color: 0xf1f1f1 })
96. .width('92%')
97. .backgroundColor(Color.White)
98. })
99. }
100. .padding({ top: 20, bottom: 20 })

102. // 请将$r('app.string.Text_confirm')替换为实际资源文件，在本示例中该资源文件的value值为"确认"
103. Text($r('app.string.Text_confirm'))
104. .width('90%')
105. .height(40)
106. .textAlign(TextAlign.Center)
107. .borderRadius(10)
108. .fontColor(Color.White)
109. .backgroundColor(0x007dfe)
110. .onClick(() => {
111. this.isPresent = !this.isPresent;
112. })
113. }
114. .size({ width: '100%', height: '100%' })
115. .backgroundColor(0xf5f5f5)
116. }

118. @Builder
119. TripInfo() {
120. Row() {
121. Column() {
122. Text('00:25')
123. // 请将$r('app.string.Label_origin_station')替换为实际资源文件，在本示例中该资源文件的value值为"始发站"
124. Text($r('app.string.Label_origin_station'))
125. }
126. .width('25%')

128. Column() {
129. Text('G1234')
130. // 请将$r('app.string.Label_start_time')替换为实际资源文件，在本示例中该资源文件的value值为"8时1分"
131. Text($r('app.string.Label_start_time'))
132. }
133. .width('25%')

135. Column() {
136. Text('08:26')
137. // 请将$r('app.string.Label_destination_station')替换为实际资源文件，在本示例中该资源文件的value值为"终点站"
138. Text($r('app.string.Label_destination_station'))
139. }
140. .width('25%')
141. }
142. }

144. // 第二步：定义半模态展示界面
145. // 通过@Builder构建模态展示界面
146. @Builder
147. MySheetBuilder() {
148. Column() {
149. Column() {
150. this.TripInfo()
151. }
152. .width('92%')
153. .margin(15)
154. .backgroundColor(Color.White)
155. .shadow({ radius: 30, color: '#aaaaaa' })
156. .borderRadius(10)

158. Column() {
159. // 请将$r('app.string.Sheet_choose_person')替换为实际资源文件，在本示例中该资源文件的value值为"+ 选择乘车人"
160. Text($r('app.string.Sheet_choose_person'))
161. .fontSize(18)
162. .fontColor(Color.Orange)
163. .fontWeight(FontWeight.Bold)
164. .padding({ top: 10, bottom: 10 })
165. .width('60%')
166. .textAlign(TextAlign.Center)
167. .borderRadius(15)
168. .onClick(() => {
169. // 第三步：通过全模态接口调起全模态展示界面，新拉起的模态面板默认显示在最上层
170. this.isPresent = !this.isPresent;
171. })
172. // 通过全模态接口，绑定模态展示界面MyContentCoverBuilder。transition属性支持自定义转场效果，此处定义了x轴横向入场
173. .bindContentCover($$this.isPresent, this.MyContentCoverBuilder(), {
174. transition: TransitionEffect.translate({ x: 500 }).animation({ curve: curves.springMotion(0.6, 0.8) })
175. })
176. }
177. .padding({ top: 60 })
178. }
179. }

181. build() {
182. Column() {
183. Row() {
184. this.TripInfo()
185. // 请将$r('app.string.Sheet_tickets_available')替换为实际资源文件，在本示例中该资源文件的value值为"有票"
186. Text($r('app.string.Sheet_tickets_available'))
187. .fontColor(Color.Blue)
188. .width('25%')
189. }
190. .width('100%')
191. .margin({top: 200, bottom: 30})
192. .borderRadius(10)
193. .backgroundColor(Color.White)
194. .onClick(()=>{
195. this.isSheetShow = !this.isSheetShow;
196. })
197. // 第一步：定义半模态转场效果
198. .bindSheet($$this.isSheetShow, this.MySheetBuilder(), {
199. height: SheetSize.MEDIUM,
200. // 请将$r('app.string.Text_confirm_order')替换为实际资源文件，在本示例中该资源文件的value值为"确认订单"
201. title: {title: $r('app.string.Text_confirm_order')},
202. })
203. }
204. .width('100%')
205. .height('100%')
206. .backgroundColor('#30aaaaaa')
207. }
208. }
```

[BindContentCoverDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BindSheet/entry/src/main/ets/pages/bindContentCover/template6/BindContentCoverDemo.ets#L15-L224)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/kE-tOomYSHifM7xULqHdIQ/zh-cn_image_0000002589324283.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052758Z&HW-CC-Expire=86400&HW-CC-Sign=1307CFE2BC048943F9B54C2FB7393F78163505C52F80CDE89C315BD1E8F17175)
