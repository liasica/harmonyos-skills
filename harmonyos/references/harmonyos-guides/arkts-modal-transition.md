---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-transition
title: 模态转场
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 模态转场
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e63e6fd76ed71dc37b4858efd1d4deb976d43f96e8d641becdd5b2c27038fa05
---

模态转场是新的界面覆盖在旧的界面上，旧的界面不消失的一种转场方式。

**表1** 模态转场接口

| 接口 | 说明 | 使用场景 |
| --- | --- | --- |
| [bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover) | 弹出全屏的模态组件。 | 用于自定义全屏的模态展示界面，结合转场动画和共享元素动画可实现复杂转场动画效果，如缩略图片点击后查看大图。 |
| [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet) | 弹出半模态组件。 | 用于半模态展示界面，如分享框。 |
| [bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11) | 弹出菜单，点击组件后弹出。 | 需要Menu菜单的场景，如一般应用的“+”号键。 |
| [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12) | 弹出菜单，长按或者右键点击后弹出。 | 长按浮起效果，一般结合拖拽框架使用，如桌面图标长按浮起。 |
| [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup) | 弹出Popup弹框。 | Popup弹框场景，如点击后对某个组件进行临时说明。 |
| [if](arkts-rendering-control-ifelse.md) | 通过if新增或删除组件。 | 用来在某个状态下临时显示一个界面，这种方式的返回导航需要由开发者监听接口实现。 |

## 使用bindContentCover构建全屏模态转场效果

[bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)接口用于为组件绑定全屏模态页面，在组件出现和消失时可通过设置转场参数ModalTransition添加过渡动效。

1. 定义全屏模态转场效果[bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)。
2. 定义模态展示界面。

   ```
   1. // 通过@Builder构建模态展示界面
   2. @Builder MyBuilder() {
   3. Column() {
   4. Text('my model view')
   5. }
   6. // 通过转场动画实现出现消失转场动画效果，transition需要加在builder下的第一个组件
   7. .transition(TransitionEffect.translate({ y: 1000 }).animation({ curve: curves.springMotion(0.6, 0.8) }))
   8. }
   ```
3. 通过模态接口调起模态展示界面，通过转场动画或者共享元素动画去实现对应的动画效果。

   ```
   1. // 模态转场控制变量
   2. @State isPresent: boolean = false;

   4. Button('Click to present model view')
   5. // 通过选定的模态接口，绑定模态展示界面，ModalTransition是内置的ContentCover转场动画类型，这里选择None代表系统不加默认动画，通过onDisappear控制状态变量变换
   6. .bindContentCover(this.isPresent, this.MyBuilder(), {
   7. modalTransition: ModalTransition.NONE,
   8. onDisappear: () => {
   9. if (this.isPresent) {
   10. this.isPresent = !this.isPresent;
   11. }
   12. }
   13. })
   14. .onClick(() => {
   15. // 改变状态变量，显示模态界面
   16. this.isPresent = !this.isPresent;
   17. })
   ```

完整示例代码和效果如下。

```
1. import { curves } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. interface PersonList {
5. name: Resource,
6. cardNum: string
7. }

9. @Entry
10. @Component
11. struct BindContentCoverDemo {
12. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. private personList: Array<PersonList> = [
14. // 请将$r('app.string.modal_transition_text1')替换为实际资源文件，在本示例中该资源文件的value值为"王**"
15. { name: $r('app.string.modal_transition_text1'), cardNum: '1234***********789' },
16. // 请将$r('app.string.modal_transition_text2')替换为实际资源文件，在本示例中该资源文件的value值为"宋*"
17. { name: $r('app.string.modal_transition_text2'), cardNum: '2345***********789' },
18. // 请将$r('app.string.modal_transition_text3')替换为实际资源文件，在本示例中该资源文件的value值为"许**"
19. { name: $r('app.string.modal_transition_text3'), cardNum: '3456***********789' },
20. // 请将$r('app.string.modal_transition_text4')替换为实际资源文件，在本示例中该资源文件的value值为"唐*"
21. { name: $r('app.string.modal_transition_text4'), cardNum: '4567***********789' }
22. ];
23. // 第一步：定义全屏模态转场效果bindContentCover
24. // 模态转场控制变量
25. @State isPresent: boolean = false;

27. // 第二步：定义模态展示界面
28. // 通过@Builder构建模态展示界面
29. @Builder
30. MyBuilder() {
31. Column() {
32. Row() {
33. // 请将$r('app.string.modal_transition_text5')替换为实际资源文件，在本示例中该资源文件的value值为"选择乘车人"
34. Text($r('app.string.modal_transition_text5'))
35. .fontSize(20)
36. .fontColor(Color.White)
37. .width('100%')
38. .textAlign(TextAlign.Center)
39. .padding({ top: 30, bottom: 15 })
40. }
41. .backgroundColor(0x007dfe)

43. Row() {
44. // 请将$r('app.string.modal_transition_text6')替换为实际资源文件，在本示例中该资源文件的value值为"+ 添加乘车人"
45. Text($r('app.string.modal_transition_text6'))
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
60. if (index % 2 === 0) {
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
87. // 请将$r('app.string.modal_transition_text7')替换为实际资源文件，在本示例中该资源文件的value值为"编辑"
88. Text($r('app.string.modal_transition_text7'))
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
101. // 请将$r('app.string.modal_transition_text8')替换为实际资源文件，在本示例中该资源文件的value值为“确认”
102. Text($r('app.string.modal_transition_text8'))
103. .width('90%')
104. .height(40)
105. .textAlign(TextAlign.Center)
106. .borderRadius(10)
107. .fontColor(Color.White)
108. .backgroundColor(0x007dfe)
109. .onClick(() => {
110. this.isPresent = !this.isPresent;
111. })
112. }
113. .size({ width: '100%', height: '100%' })
114. .backgroundColor(0xf5f5f5)
115. // 通过转场动画实现出现消失转场动画效果
116. .transition(TransitionEffect.translate({ y: 1000 }).animation({ curve: curves.springMotion(0.6, 0.8) }))
117. }

119. build() {
120. Column() {
121. Row() {
122. // 请将$r('app.string.modal_transition_text9')替换为实际资源文件，在本示例中该资源文件的value值为"确认订单"
123. Text($r('app.string.modal_transition_text9'))
124. .fontSize(20)
125. .fontColor(Color.White)
126. .width('100%')
127. .textAlign(TextAlign.Center)
128. .padding({ top: 30, bottom: 60 })
129. }
130. .backgroundColor(0x007dfe)

132. Column() {
133. Row() {
134. Column() {
135. Text('00:25')
136. // 请将$r('app.string.modal_transition_text10')替换为实际资源文件，在本示例中该资源文件的value值为"始发站"
137. Text($r('app.string.modal_transition_text10'))
138. }
139. .width('30%')

141. Column() {
142. Text('G1234')
143. // 请将$r('app.string.modal_transition_text11')替换为实际资源文件，在本示例中该资源文件的value值为"8时1分"
144. Text($r('app.string.modal_transition_text11'))
145. }
146. .width('30%')

148. Column() {
149. Text('08:26')
150. // 请将$r('app.string.modal_transition_text12')替换为实际资源文件，在本示例中该资源文件的value值为"终点站"
151. Text($r('app.string.modal_transition_text12'))
152. }
153. .width('30%')
154. }
155. }
156. .width('92%')
157. .padding(15)
158. .margin({ top: -30 })
159. .backgroundColor(Color.White)
160. .shadow({ radius: 30, color: '#aaaaaa' })
161. .borderRadius(10)

163. Column() {
164. // 请将$r('app.string.modal_transition_text13')替换为实际资源文件，在本示例中该资源文件的value值为"+ 选择乘车人"
165. Text($r('app.string.modal_transition_text13'))
166. .fontSize(18)
167. .fontColor(Color.Orange)
168. .fontWeight(FontWeight.Bold)
169. .padding({ top: 10, bottom: 10 })
170. .width('60%')
171. .textAlign(TextAlign.Center)
172. .borderRadius(15)
173. // 通过选定的模态接口，绑定模态展示界面，ModalTransition是内置的ContentCover转场动画类型，
174. // 这里选择DEFAULT代表设置上下切换动画效果，通过onDisappear控制状态变量变换。
175. .bindContentCover(this.isPresent, this.MyBuilder(), {
176. modalTransition: ModalTransition.DEFAULT,
177. onDisappear: () => {
178. if (this.isPresent) {
179. this.isPresent = !this.isPresent;
180. }
181. }
182. })
183. .onClick(() => {
184. // 第三步：通过模态接口调起模态展示界面，通过转场动画或者共享元素动画去实现对应的动画效果
185. // 改变状态变量，显示模态界面
186. this.isPresent = !this.isPresent;
187. })
188. }
189. .padding({ top: 60 })
190. }
191. }
192. }
```

[BindContentCoverDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template1/BindContentCoverDemo.ets#L16-L209)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/65IjgJuYRmeDTVCg2hto9w/zh-cn_image_0000002558604818.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=F15D881ED8E5653D8145A462E34D5AAD3E1F3B14E8D8E00BA3A79432FBE65A9E)

## 使用bindSheet构建半模态转场效果

[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性可为组件绑定半模态页面，在组件出现时可通过设置自定义或默认的内置高度确定半模态大小。构建半模态转场动效的步骤基本与使用[bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)构建全屏模态转场动效相同。

完整示例和效果如下。

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct BindSheetDemo {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 半模态转场显示隐藏控制
8. @State isShowSheet: boolean = false;
9. // 请将$r('app.string.modal_transition_text14')替换为实际资源文件，在本示例中该资源文件的value值为"不要辣"
10. private menuList: Resource[] = [$r('app.string.modal_transition_text14'),
11. // 请将$r('app.string.modal_transition_text15')替换为实际资源文件，在本示例中该资源文件的value值为"少放辣"
12. $r('app.string.modal_transition_text15'),
13. // 请将$r('app.string.modal_transition_text16')替换为实际资源文件，在本示例中该资源文件的value值为"多放辣"
14. $r('app.string.modal_transition_text16'),
15. // 请将$r('app.string.modal_transition_text17')替换为实际资源文件，在本示例中该资源文件的value值为"不要香菜"
16. $r('app.string.modal_transition_text17'),
17. // 请将$r('app.string.modal_transition_text18')替换为实际资源文件，在本示例中该资源文件的value值为"不要香葱"
18. $r('app.string.modal_transition_text18'),
19. // 请将$r('app.string.modal_transition_text19')替换为实际资源文件，在本示例中该资源文件的value值为"不要一次性餐具"
20. $r('app.string.modal_transition_text19'),
21. // 请将$r('app.string.modal_transition_text20')替换为实际资源文件，在本示例中该资源文件的value值为"需要一次性餐具"
22. $r('app.string.modal_transition_text20')];

24. // 通过@Builder构建半模态展示界面
25. @Builder
26. mySheet() {
27. Column() {
28. Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
29. ForEach(this.menuList, (item: string) => {
30. Text(item)
31. .fontSize(16)
32. .fontColor(0x333333)
33. .backgroundColor(0xf1f1f1)
34. .borderRadius(8)
35. .margin(10)
36. .padding(15)
37. })
38. }
39. .padding({ top: 18 })
40. }
41. .width('100%')
42. .height('100%')
43. .backgroundColor(Color.White)
44. }

46. build() {
47. Column() {
48. // 请将$r('app.string.modal_transition_text21')替换为实际资源文件，在本示例中该资源文件的value值为"口味与餐具"
49. Text($r('app.string.modal_transition_text21'))
50. .fontSize(28)
51. .padding({ top: 30, bottom: 30 })
52. Column() {
53. Row() {
54. Row()
55. .width(10)
56. .height(10)
57. .backgroundColor('#a8a8a8')
58. .margin({ right: 12 })
59. .borderRadius(20)

61. Column() {
62. // 请将$r('app.string.modal_transition_text22')替换为实际资源文件，在本示例中该资源文件的value值为"选择点餐口味和餐具"
63. Text($r('app.string.modal_transition_text22'))
64. .fontSize(16)
65. .fontWeight(FontWeight.Medium)
66. }
67. .alignItems(HorizontalAlign.Start)

69. Blank()

71. Row()
72. .width(12)
73. .height(12)
74. .margin({ right: 15 })
75. .border({
76. width: { top: 2, right: 2 },
77. color: 0xcccccc
78. })
79. .rotate({ angle: 45 })
80. }
81. .borderRadius(15)
82. .shadow({ radius: 100, color: '#ededed' })
83. .width('90%')
84. .alignItems(VerticalAlign.Center)
85. .padding({ left: 15, top: 15, bottom: 15 })
86. .backgroundColor(Color.White)
87. // 通过选定的半模态接口，绑定模态展示界面，style中包含两个参数，一个是设置半模态的高度，不设置时默认高度是Large，
88. // 一个是是否显示控制条DragBar，默认是true显示控制条，通过onDisappear控制状态变量变换。
89. .bindSheet(this.isShowSheet, this.mySheet(), {
90. height: 300,
91. dragBar: false,
92. onDisappear: () => {
93. this.isShowSheet = !this.isShowSheet;
94. }
95. })
96. .onClick(() => {
97. this.isShowSheet = !this.isShowSheet;
98. })
99. }
100. .width('100%')
101. }
102. .width('100%')
103. .height('100%')
104. .backgroundColor(0xf1f1f1)
105. }
106. }
```

[BindSheetDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template2/BindSheetDemo.ets#L16-L124)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/UWuooijPRYGPEX6pj6kWfQ/zh-cn_image_0000002589324343.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=37D7E804AD7F0EEB2395B5D7603558039B1C3515B1B317F2AA8EBE5310A6D304)

## 使用bindMenu实现菜单弹出效果

[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)为组件绑定弹出式菜单，通过点击触发。完整示例和效果如下。

```
1. import { common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0xF811;
5. const TAG = '[Sample_Animation]';

7. class BMD {
8. public value: ResourceStr = '';
9. public action: () => void = () => {
10. };
11. }

13. @Entry
14. @Component
15. struct BindMenuDemo {
16. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

18. // 第一步: 定义一组数据用来表示菜单按钮项
19. @State items: BMD[] = [
20. {
21. // 请将$r('app.string.modal_transition_text23')替换为实际资源文件，在本示例中该资源文件的value值为"菜单项1"
22. value: $r('app.string.modal_transition_text23'),
23. action: () => {
24. hilog.info(DOMAIN, TAG, 'handle Menu1 select');
25. }
26. },
27. {
28. // 请将$r('app.string.modal_transition_text24')替换为实际资源文件，在本示例中该资源文件的value值为"菜单项2"
29. value: $r('app.string.modal_transition_text24'),
30. action: () => {
31. hilog.info(DOMAIN, TAG, 'handle Menu2 select');
32. }
33. },
34. ]

36. build() {
37. Column() {
38. Button('click')
39. .backgroundColor(0x409eff)
40. // 第二步: 通过bindMenu接口将菜单数据绑定给元素
41. .bindMenu(this.items)
42. }
43. .justifyContent(FlexAlign.Center)
44. .width('100%')
45. .height(437)
46. }
47. }
```

[BindMenuDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template3/BindMenuDemo.ets#L16-L65)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/BCi2PWGLRiqCtEPsAHmjhQ/zh-cn_image_0000002589244283.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=4512BACDA2B3877CA476ACFF20E410F1C339681E5A2E26637FF211A5A25D9F74)

## 使用bindContextMenu实现菜单弹出效果

[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)为组件绑定弹出式菜单，通过长按或右键点击触发。

完整示例和效果如下。

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct BindContextMenuDemo {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 请将$r('app.string.modal_transition_text25')替换为实际资源文件，在本示例中该资源文件的value值为"保存图片"
8. private menu: Resource[] = [$r('app.string.modal_transition_text25'),
9. // 请将$r('app.string.modal_transition_text26')替换为实际资源文件，在本示例中该资源文件的value值为"收藏"
10. $r('app.string.modal_transition_text26'),
11. // 请将$r('app.string.modal_transition_text27')替换为实际资源文件，在本示例中该资源文件的value值为"搜一搜"
12. $r('app.string.modal_transition_text27')];
13. // 请将$r('app.media.icon_2')替换为实际资源文件
14. private pics: Resource[] = [$r('app.media.icon_1'), $r('app.media.icon_2')];

16. // 通过@Builder构建自定义菜单项
17. @Builder
18. myMenu() {
19. Column() {
20. ForEach(this.menu, (item: string) => {
21. Row() {
22. Text(item)
23. .fontSize(18)
24. .width('100%')
25. .textAlign(TextAlign.Center)
26. }
27. .padding(15)
28. .border({ width: { bottom: 1 }, color: 0xcccccc })
29. })
30. }
31. .width(140)
32. .borderRadius(15)
33. .shadow({ radius: 15, color: 0xf1f1f1 })
34. .backgroundColor(0xf1f1f1)
35. }

37. build() {
38. Column() {
39. Row() {
40. // 请将$r('app.string.modal_transition_text28')替换为实际资源文件，在本示例中该资源文件的value值为"查看图片"
41. Text($r('app.string.modal_transition_text28'))
42. .fontSize(20)
43. .fontColor(Color.White)
44. .width('100%')
45. .textAlign(TextAlign.Center)
46. .padding({ top: 20, bottom: 20 })
47. }
48. .backgroundColor(0x007dfe)

50. Column() {
51. ForEach(this.pics, (item: Resource) => {
52. Row() {
53. Image(item)
54. .width('100%')
55. .draggable(false)
56. }
57. .padding({
58. top: 20,
59. bottom: 20,
60. left: 10,
61. right: 10
62. })
63. .bindContextMenu(this.myMenu, ResponseType.LongPress)
64. })
65. }
66. }
67. .width('100%')
68. .alignItems(HorizontalAlign.Center)
69. }
70. }
```

[BindContextMenuDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template4/BindContextMenuDemo.ets#L16-L88)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/526mFTneSA6PkvU_1G_C8g/zh-cn_image_0000002558764476.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=C2AF996F11CF8215E150FC98B9CCDF7668809FFF2051D530A10F9C969BFDD6A7)

## 使用bindPopup实现气泡弹窗效果

[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)属性可为组件绑定弹窗，并设置弹窗内容，交互逻辑和显示状态。

完整示例和代码如下。

```
1. @Entry
2. @Component
3. struct BindPopupDemo {
4. // 第一步：定义变量控制弹窗显示
5. @State customPopup: boolean = false;

7. // 第二步：popup构造器定义弹框内容
8. @Builder
9. popupBuilder() {
10. Column({ space: 2 }) {
11. Row().width(64)
12. .height(64)
13. .backgroundColor(0x409eff)
14. Text('Popup')
15. .fontSize(10)
16. .fontColor(Color.White)
17. }
18. .justifyContent(FlexAlign.SpaceAround)
19. .width(100)
20. .height(100)
21. .padding(5)
22. }

24. build() {
25. Column() {

27. Button('click')
28. // 第四步：创建点击事件，控制弹窗显隐
29. .onClick(() => {
30. this.customPopup = !this.customPopup;
31. })
32. .backgroundColor(0xf56c6c)
33. // 第三步：使用bindPopup接口将弹窗内容绑定给元素
34. .bindPopup(this.customPopup, {
35. builder: this.popupBuilder,
36. placement: Placement.Top,
37. maskColor: 0x33000000,
38. popupColor: 0xf56c6c,
39. enableArrow: true,
40. onStateChange: (e) => {
41. if (!e.isVisible) {
42. this.customPopup = false;
43. }
44. }
45. })
46. }
47. .justifyContent(FlexAlign.Center)
48. .width('100%')
49. .height(437)
50. }
51. }
```

[BindPopupDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template5/BindPopupDemo.ets#L16-L69)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/DqfRUFfATKmbXco5fd64uA/zh-cn_image_0000002558604820.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=31148AB7E1500B16FDD40AAE4AB18DD1543CDEB636E34F827A8C623015F47ABA)

## 使用if实现模态转场

上述模态转场接口需要绑定到其他组件上，通过监听状态变量改变调起模态界面。同时，也可以通过if范式，通过新增/删除组件实现模态转场效果。

完整示例和代码如下。

```
1. import { common } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct ModalTransitionWithIf {
6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text29'，value为非空字符串的资源
8. private listArr: ResourceStr[] = ['WLAN', this.context.resourceManager.getStringByNameSync('modal_transition_text29'),
9. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text30'，value为非空字符串的资源
10. this.context.resourceManager.getStringByNameSync('modal_transition_text30'),
11. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text31'，value为非空字符串的资源
12. this.context.resourceManager.getStringByNameSync('modal_transition_text31')];
13. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text32'，value为非空字符串的资源
14. private shareArr: ResourceStr[] = [this.context.resourceManager.getStringByNameSync('modal_transition_text32'),
15. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text33'，value为非空字符串的资源
16. this.context.resourceManager.getStringByNameSync('modal_transition_text33'), 'VPN',
17. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text34'，value为非空字符串的资源
18. this.context.resourceManager.getStringByNameSync('modal_transition_text34'), 'NFC'];
19. // 第一步：定义状态变量控制页面显示
20. @State isShowShare: boolean = false;

22. private shareFunc(): void {
23. this.getUIContext()?.animateTo({ duration: 500 }, () => {
24. this.isShowShare = !this.isShowShare;
25. })
26. }

28. build() {
29. // 第二步：定义Stack布局显示当前页面和模态页面
30. Stack() {
31. Column() {
32. Column() {
33. // 请将$r('app.string.modal_transition_text35')替换为实际资源文件，在本示例中该资源文件的value值为“设置”
34. Text($r('app.string.modal_transition_text35'))
35. .fontSize(28)
36. .fontColor(0x333333)
37. }
38. .width('90%')
39. .padding({ top: 30, bottom: 15 })
40. .alignItems(HorizontalAlign.Start)
41. // 请将$r('app.string.modal_transition_text36')替换为实际资源文件，在本示例中该资源文件的value值为“输入关键字搜索”
42. TextInput({ placeholder: $r('app.string.modal_transition_text36') })
43. .width('90%')
44. .height(40)
45. .margin({ bottom: 10 })
46. .focusable(false)

48. List({ space: 12, initialIndex: 0 }) {
49. ForEach(this.listArr, (item: string, index: number) => {
50. ListItem() {
51. Row() {
52. Row() {
53. Text(`${item.slice(0, 1)}`)
54. .fontColor(Color.White)
55. .fontSize(14)
56. .fontWeight(FontWeight.Bold)
57. }
58. .width(30)
59. .height(30)
60. .backgroundColor('#a8a8a8')
61. .margin({ right: 12 })
62. .borderRadius(20)
63. .justifyContent(FlexAlign.Center)

65. Column() {
66. Text(item)
67. .fontSize(16)
68. .fontWeight(FontWeight.Medium)
69. }
70. .alignItems(HorizontalAlign.Start)

72. Blank()

74. Row()
75. .width(12)
76. .height(12)
77. .margin({ right: 15 })
78. .border({
79. width: { top: 2, right: 2 },
80. color: 0xcccccc
81. })
82. .rotate({ angle: 45 })
83. }
84. .borderRadius(15)
85. .shadow({ radius: 100, color: '#ededed' })
86. .width('90%')
87. .alignItems(VerticalAlign.Center)
88. .padding({ left: 15, top: 15, bottom: 15 })
89. .backgroundColor(Color.White)
90. }
91. .width('100%')
92. .onClick(() => {
93. // 第五步：改变状态变量，显示模态页面
94. // 请在resources\base\element\string.json文件中配置name为'modal_transition_text37'，value为非空字符串的资源
95. if (item.slice(-2) === this.context.resourceManager.getStringByNameSync('modal_transition_text37')) {
96. this.shareFunc();
97. }
98. })
99. }, (item: string): string => item)
100. }
101. .width('100%')
102. }
103. .width('100%')
104. .height('100%')
105. .backgroundColor(0xfefefe)

107. // 第三步：在if中定义模态页面，显示在最上层，通过if控制模态页面出现消失
108. if (this.isShowShare) {
109. Column() {
110. Column() {
111. Row() {
112. Row() {
113. Row()
114. .width(16)
115. .height(16)
116. .border({
117. width: { left: 2, top: 2 },
118. color: 0x333333
119. })
120. .rotate({ angle: -45 })
121. }
122. .padding({ left: 15, right: 10 })
123. .onClick(() => {
124. this.shareFunc();
125. })
126. // 请将$r('app.string.modal_transition_text31')替换为实际资源文件，在本示例中该资源文件的value值为“连接与共享”
127. Text($r('app.string.modal_transition_text31'))
128. .fontSize(28)
129. .fontColor(0x333333)
130. }
131. .padding({ top: 30 })
132. }
133. .width('90%')
134. .padding({ bottom: 15 })
135. .alignItems(HorizontalAlign.Start)

137. List({ space: 12, initialIndex: 0 }) {
138. ForEach(this.shareArr, (item: string) => {
139. ListItem() {
140. Row() {
141. Row() {
142. Text(`${item.slice(0, 1)}`)
143. .fontColor(Color.White)
144. .fontSize(14)
145. .fontWeight(FontWeight.Bold)
146. }
147. .width(30)
148. .height(30)
149. .backgroundColor('#a8a8a8')
150. .margin({ right: 12 })
151. .borderRadius(20)
152. .justifyContent(FlexAlign.Center)

154. Column() {
155. Text(item)
156. .fontSize(16)
157. .fontWeight(FontWeight.Medium)
158. }
159. .alignItems(HorizontalAlign.Start)

161. Blank()

163. Row()
164. .width(12)
165. .height(12)
166. .margin({ right: 15 })
167. .border({
168. width: { top: 2, right: 2 },
169. color: 0xcccccc
170. })
171. .rotate({ angle: 45 })
172. }
173. .borderRadius(15)
174. .shadow({ radius: 100, color: '#ededed' })
175. .width('90%')
176. .alignItems(VerticalAlign.Center)
177. .padding({ left: 15, top: 15, bottom: 15 })
178. .backgroundColor(Color.White)
179. }
180. .width('100%')
181. }, (item: string): string => item)
182. }
183. .width('100%')
184. }
185. .width('100%')
186. .height('100%')
187. .backgroundColor(0xffffff)
188. // 第四步：定义模态页面出现消失转场方式
189. .transition(TransitionEffect.OPACITY
190. .combine(TransitionEffect.translate({ x: '100%' }))
191. .combine(TransitionEffect.scale({ x: 0.95, y: 0.95 })))
192. }
193. }
194. }
195. }
```

[ModalTransitionWithIf.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/modalTransition/template6/ModalTransitionWithIf.ets#L16-L213)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/AU8iR0czTfi3cXWRhvRRpQ/zh-cn_image_0000002589324345.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=6F30FEF96ED69A7B2EDD0313876259C7789FF078095C4F62BFE960A8E13A809C)
