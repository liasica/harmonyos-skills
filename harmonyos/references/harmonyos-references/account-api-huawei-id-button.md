---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-huawei-id-button
title: LoginWithHuaweiIDButton (华为账号Button登录组件)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS组件 > LoginWithHuaweiIDButton (华为账号Button登录组件)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:45+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1220160d8108dc87072918b3f36be0c58cd53e62ed17b913acbe1794d565aab5
---

本模块提供LoginWithHuaweiIDButton组件，应用通过集成该组件完成华为账号登录功能。

LoginWithHuaweiIDButton需要配合[loginComponentManager](account-api-component-manager.md)一起使用，用于实现华为账号登录功能。LoginWithHuaweiIDButton组件文本内容默认支持多语言。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { LoginWithHuaweiIDButton, loginComponentManager } from '@kit.AccountKit';
```

## LoginWithHuaweiIDButton

PhonePC/2in1TabletTV

该类为用来展示登录华为账号按钮的UI组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| params | [LoginWithHuaweiIDButtonParams](account-api-component-manager.md#loginwithhuaweiidbuttonparams) | 是 | - | LoginWithHuaweiIDButton组件参数。 |
| controller | [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 是 | - | LoginWithHuaweiIDButton组件控制器用来接收组件的点击事件。 |

### build

PhonePC/2in1TabletTV

build(): void

用于创建[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct QuickLoginButtonComponent {
8. logTag: string = 'QuickLoginButtonComponent';
9. domainId: number = 0x0000;
10. // 参考华为账号开发指南获取匿名手机号
11. @State quickLoginAnonymousPhone: string = '';
12. // 展示用户服务协议、隐私协议和华为账号用户认证协议
13. privacyText: loginComponentManager.PrivacyText[] = [{
14. text: '已阅读并同意',
15. type: loginComponentManager.TextType.PLAIN_TEXT
16. }, {
17. text: '《用户服务协议》 ',
18. tag: '用户服务协议',
19. type: loginComponentManager.TextType.RICH_TEXT
20. }, {
21. text: '《隐私协议》',
22. tag: '隐私协议',
23. type: loginComponentManager.TextType.RICH_TEXT
24. }, {
25. text: '和',
26. type: loginComponentManager.TextType.PLAIN_TEXT
27. }, {
28. text: '《华为账号用户认证协议》',
29. tag: '华为账号用户认证协议',
30. type: loginComponentManager.TextType.RICH_TEXT
31. }];
32. // 构造LoginWithHuaweiIDButton组件的控制器
33. controller: loginComponentManager.LoginWithHuaweiIDButtonController =
34. new loginComponentManager.LoginWithHuaweiIDButtonController()
35. /**
36. * 当应用使用自定义的登录页时，如果用户未同意协议，需要设置协议状态为NOT_ACCEPTED，当用户同意协议后再设置
37. * 协议状态为ACCEPTED，才可以使用华为账号一键登录功能
38. */
39. .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
40. .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
41. if (error) {
42. this.dealAllError(error);
43. return;
44. }
45. if (response) {
46. // 获取到Authorization Code
47. const authorizationCode = response.authorizationCode;
48. hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
49. return;
50. }
51. })
52. .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
53. if (error) {
54. this.dealAllError(error);
55. return;
56. }
57. hilog.info(0x0000, 'testTag', `onClickEvent clickEvent: ${clickEvent}`);
58. });

60. // 错误处理
61. dealAllError(error: BusinessError): void {
62. hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
63. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
64. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
65. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
66. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
67. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
68. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
69. // 登录失败，请尝试使用其他方式登录
70. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
71. // 用户取消授权
72. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
73. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
74. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
75. // 重复请求，应用无需处理
76. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
77. // 用户未同意协议
78. } else {
79. // 应用登录失败，请尝试使用其他方式登录
80. }
81. }

83. build() {
84. Scroll() {
85. Column() {
86. Column() {
87. Column() {
88. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
89. Image($r('app.media.app_icon'))
90. .width(48)
91. .height(48)
92. .draggable(false)
93. .copyOption(CopyOptions.None)
94. .onComplete(() => {
95. hilog.info(0x0000, 'testTag', 'appIcon loading success');
96. })
97. .onError(() => {
98. hilog.error(0x0000, 'testTag', 'appIcon loading fail');
99. })

101. Text($r('app.string.app_name'))
102. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
103. .fontWeight(FontWeight.Medium)
104. .fontWeight(FontWeight.Bold)
105. .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
106. .minFontSize($r('sys.float.ohos_id_text_size_body1'))
107. .maxLines(1)
108. .fontColor($r('sys.color.ohos_id_color_text_primary'))
109. .constraintSize({ maxWidth: '100%' })
110. .margin({
111. top: 12
112. })

114. Text('应用描述')
115. .fontSize($r('sys.float.ohos_id_text_size_body2'))
116. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
117. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
118. .fontWeight(FontWeight.Regular)
119. .constraintSize({ maxWidth: '100%' })
120. .margin({
121. top: 8
122. })
123. }.margin({
124. top: 100
125. })

127. Column() {
128. Text(this.quickLoginAnonymousPhone)
129. .fontSize(36)
130. .fontColor($r('sys.color.ohos_id_color_text_primary'))
131. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
132. .fontWeight(FontWeight.Bold)
133. .lineHeight(48)
134. .textAlign(TextAlign.Center)
135. .maxLines(1)
136. .constraintSize({ maxWidth: '100%', minHeight: 48 })

138. Text('华为账号绑定号码')
139. .fontSize($r('sys.float.ohos_id_text_size_body2'))
140. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
141. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
142. .fontWeight(FontWeight.Regular)
143. .lineHeight(19)
144. .textAlign(TextAlign.Center)
145. .maxLines(1)
146. .constraintSize({ maxWidth: '100%' })
147. .margin({
148. top: 8
149. })
150. }.margin({
151. top: 64
152. })

154. Column() {
155. LoginWithHuaweiIDButton({
156. params: {
157. // LoginWithHuaweiIDButton支持的样式
158. style: loginComponentManager.Style.BUTTON_RED,
159. // 账号登录按钮在登录过程中展示加载态
160. extraStyle: {
161. buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
162. show: true
163. })
164. },
165. // LoginWithHuaweiIDButton的边框圆角半径
166. borderRadius: 24,
167. // LoginWithHuaweiIDButton支持的登录类型
168. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
169. // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
170. supportDarkMode: true
171. },
172. controller: this.controller
173. })
174. }
175. .height(40)
176. .width('100%')
177. .margin({
178. top: 56
179. })

181. Column() {
182. Button({
183. type: ButtonType.Capsule,
184. stateEffect: true
185. }) {
186. Text('其他方式登录')
187. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
188. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
189. .fontWeight(FontWeight.Medium)
190. .fontSize($r('sys.float.ohos_id_text_size_button1'))
191. .focusable(true)
192. .focusOnTouch(true)
193. .textOverflow({ overflow: TextOverflow.Ellipsis })
194. .maxLines(1)
195. .padding({ left: 8, right: 8 })
196. }
197. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
198. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
199. .fontWeight(FontWeight.Medium)
200. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
201. .focusable(true)
202. .focusOnTouch(true)
203. .constraintSize({ minHeight: 40 })
204. .width('100%')
205. .onClick(() => {
206. hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
207. })
208. }.margin({ top: 16 })
209. }.width('100%')

211. Row() {
212. Row() {
213. Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
214. .width(24)
215. .height(24)
216. .focusable(true)
217. .focusOnTouch(true)
218. .margin({ top: 0 })
219. .onChange((value: boolean) => {
220. if (value) {
221. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
222. } else {
223. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
224. }
225. hilog.info(0x0000, 'testTag', `agreementChecked: ${value}`);
226. })
227. }

229. Row() {
230. Text() {
231. ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
232. if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
233. Span(item?.text)
234. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
235. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
236. .fontWeight(FontWeight.Regular)
237. .fontSize($r('sys.float.ohos_id_text_size_body3'))
238. } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
239. Span(item?.text)
240. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
241. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
242. .fontWeight(FontWeight.Medium)
243. .fontSize($r('sys.float.ohos_id_text_size_body3'))
244. .onClick(() => {
245. // 应用需要根据item.tag实现协议页面的跳转逻辑
246. hilog.info(0x0000, 'testTag', `click privacy text tag: ${item.tag}`);
247. })
248. }
249. }, (item: loginComponentManager.PrivacyText) => item.text.toString())
250. }
251. .width('100%')
252. }
253. .margin({ left: 12 })
254. .layoutWeight(1)
255. .constraintSize({ minHeight: 24 })
256. }
257. .alignItems(VerticalAlign.Top)
258. .margin({
259. top: 16,
260. bottom: 16
261. })
262. }
263. .justifyContent(FlexAlign.SpaceBetween)
264. .constraintSize({ minHeight: '100%' })
265. .margin({
266. left: 16,
267. right: 16
268. })
269. }
270. .width('100%')
271. .height('100%')
272. }
273. }

275. export enum ErrorCode {
276. // 账号未登录
277. ERROR_CODE_LOGIN_OUT = 1001502001,
278. // 网络错误
279. ERROR_CODE_NETWORK_ERROR = 1001502005,
280. // 内部错误
281. ERROR_CODE_INTERNAL_ERROR = 1001502009,
282. // 用户取消授权
283. ERROR_CODE_USER_CANCEL = 1001502012,
284. // 系统服务异常
285. ERROR_CODE_SYSTEM_SERVICE = 12300001,
286. // 用户未同意用户协议
287. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
288. // 重复请求
289. ERROR_CODE_REQUEST_REFUSE = 1001500002
290. }
```
