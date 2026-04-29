---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-loginpanel
title: LoginPanel (华为账号Panel登录组件)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS组件 > LoginPanel (华为账号Panel登录组件)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:44+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:40aa22a7276e46de5dfb18be1b2383c08ee8aefe2c7dc4efc99d695a3b7c86f3
---

本模块提供LoginPanel组件，应用通过集成该组件完成华为账号登录功能。

LoginPanel需要配合[loginComponentManager](account-api-component-manager.md)一起使用，用于实现华为账号登录功能。LoginPanel内的按钮文本默认支持多语言。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
```

## LoginPanel

PhonePC/2in1TabletTV

该类为用来展示登录面板的UI组件。

**模型约束：** 此接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| show | boolean | 是 | @Link | 该参数用于控制LoginPanel组件是否展示。  false表示不展示该组件。  true表示展示该组件，当业务需要使用LoginPanel组件时设置值为true。  **说明：**  - 该参数必须是@State装饰的局部变量。  - LoginPanel仅支持在页面中使用，弹框、子窗口等场景暂不支持。 |
| params | [LoginPanelParams](account-api-component-manager.md#loginpanelparams) | 是 | - | LoginPanel组件参数。 |
| controller | [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | 是 | - | LoginPanel组件控制器用来接收组件的点击事件。 |

### build

PhonePC/2in1TabletTV

build(): void

用于创建[LoginPanel](account-api-loginpanel.md#loginpanel)对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct PreviewLoginPanelPage {
8. // 是否展示LoginPanel组件
9. @State show: boolean = true;
10. // 定义LoginPanel展示的隐私文本，展示用户服务协议、隐私协议和华为账号用户认证协议
11. privacyText: loginComponentManager.PrivacyText[] = [{
12. text: '已阅读并同意',
13. type: loginComponentManager.TextType.PLAIN_TEXT
14. }, {
15. text: '《用户服务协议》',
16. tag: '用户服务协议',
17. type: loginComponentManager.TextType.RICH_TEXT
18. }, {
19. text: '《隐私协议》',
20. tag: '隐私协议',
21. type: loginComponentManager.TextType.RICH_TEXT
22. }, {
23. text: '和',
24. type: loginComponentManager.TextType.PLAIN_TEXT
25. }, {
26. text: '《华为账号用户认证协议》',
27. tag: '华为账号用户认证协议',
28. type: loginComponentManager.TextType.RICH_TEXT
29. }];
30. // 定义LoginPanel展示的其他方式登录Icon
31. iconArray: loginComponentManager.LoginIcon[] = [{
32. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
33. icon: $r('app.media.app_icon'),
34. tag: '其他方式登录'
35. }];
36. // 构造LoginPanel组件的控制器
37. controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
38. // 当登录类型不是QUICK_LOGIN且未设置协议时，如果需要展示自定义协议弹框，需要设置协议状态为NOT_ACCEPTED
39. .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
40. // 用户点击其他方式登录展示隐私协议弹框
41. .setShowAgreementForOptionalLogin()
42. .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
43. hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
44. if (error) {
45. this.dealAllError(error);
46. return;
47. }
48. if (response) {
49. // 获取到Authorization Code后，传给应用服务端
50. const authorizationCode = response.authorizationCode;
51. hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
52. this.show = false;
53. return;
54. }
55. })
56. .onClickOptionalLoginButton(() => {
57. hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
58. this.show = false;
59. })
60. .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
61. if (error) {
62. this.dealAllError(error);
63. return;
64. }
65. hilog.info(0x0000, 'testTag', `onClickOptionalLoginIcon tag: ${tag}`);
66. this.show = false;
67. })
68. .onClickPrivacyText((error: BusinessError, tag: string) => {
69. if (error) {
70. this.dealAllError(error);
71. return;
72. }
73. // 应用需要根据tag实现协议页面的跳转逻辑
74. hilog.info(0x0000, 'testTag', `onClickPrivacyText tag: ${tag}`);
75. })
76. .onClickCloseButton(() => {
77. hilog.info(0x0000, 'testTag', 'onClickCloseButton');
78. this.show = false;
79. })
80. .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
81. if (error) {
82. this.dealAllError(error);
83. return;
84. }
85. hilog.info(0x0000, 'testTag', `onChangeAgreementStatus agreementStatus: ${agreementStatus}`);
86. })
87. .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
88. if (error) {
89. this.dealAllError(error);
90. return;
91. }
92. hilog.info(0x0000, 'testTag', `onClickEvent clickEvent: ${clickEvent}`);
93. });

95. // 错误处理
96. dealAllError(error: BusinessError): void {
97. hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
98. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
99. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
100. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
101. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
102. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
103. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
104. // 登录失败，请尝试使用其他方式登录
105. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
106. // 用户取消授权
107. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
108. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
109. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
110. // 重复请求，应用无需处理
111. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
112. // 用户未同意协议
113. } else {
114. // 应用登录失败，请尝试使用其他方式登录
115. }
116. }

118. build() {
119. if (this.show) {
120. Stack() {
121. LoginPanel({
122. show: this.show,
123. params: {
124. appInfo: {
125. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
126. appIcon: $r('app.media.app_icon'),
127. appName: '应用名称'
128. },
129. privacyText: this.privacyText,
130. // 参考华为账号开发指南获取匿名手机号
131. anonymousPhoneNumber: '139******99',
132. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
133. // optionalLoginAreaAttr和optionalLoginButtonAttr同时存在时优先展示optionalLoginAreaAttr
134. optionalLoginAreaAttr: { iconArray: this.iconArray },
135. optionalLoginButtonAttr: { text: '其他方式登录' }
136. },
137. controller: this.controller
138. })
139. }
140. .height('100%')
141. .width('100%')
142. }
143. }
144. }

146. export enum ErrorCode {
147. // 账号未登录
148. ERROR_CODE_LOGIN_OUT = 1001502001,
149. // 网络错误
150. ERROR_CODE_NETWORK_ERROR = 1001502005,
151. // 内部错误
152. ERROR_CODE_INTERNAL_ERROR = 1001502009,
153. // 用户取消授权
154. ERROR_CODE_USER_CANCEL = 1001502012,
155. // 系统服务异常
156. ERROR_CODE_SYSTEM_SERVICE = 12300001,
157. // 用户未同意用户协议
158. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
159. // 重复请求
160. ERROR_CODE_REQUEST_REFUSE = 1001500002
161. }
```
