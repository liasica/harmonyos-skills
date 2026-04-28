---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-adaptation-in-custom-layout
title: 自定义布局下的适配建议
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 自定义布局下的适配建议
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:08+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:a31dec57562e6cb75188a0ee050639f8bf6fc242f428390102150a67bdd7d3d5
---

## 登录

应用在设置“登录”页面时，需要“用户名/账号名”、“密码”在同一个界面，具体可参照[账号密码保存-登录](passwordvault-save-acc-password.md#账号密码登录)、[账号密码填充-登录](passwordvault-autofill-acc-password.md#登录)中的介绍。

## 注册

应用在设置“注册”页面时，需要“用户名/账号名”、“新密码”在同一个界面，具体可参照[账号密码保存-注册](passwordvault-save-acc-password.md#账号密码注册)、[强密码填充-注册](passwordvault-autofill-strong-password.md#注册)中的介绍。

## 修改密码

应用在设置“修改密码”页面时，需要“用户名/账号名”、“旧密码”、“新密码”在同一个界面，具体可参照[账号密码更新-修改账号密码](passwordvault-update-acc-password.md#修改账号密码)、[账号密码填充-修改密码](passwordvault-autofill-acc-password.md#修改密码)中的介绍。

## 登录、注册失败

当应用成功登录或注册后，应将账号密码保存至密码保险箱。若登录或注册未成功，通过页面路由（router）跳转返回时，建议应用将enableAutofill属性设置为false，以避免保存错误信息。

示例代码如下：

```
1. @Entry
2. @Component
3. struct LoginExample {
4. pathInfos: NavPathStack = new NavPathStack();
5. @State ReserveAccount: string = '';
6. @State ReservePassword: string = '';
7. // 保存填充功能初始值：true
8. @State enableAutoFill: boolean = true;

10. onBackPress() {
11. // 当非成功登录、返回等页面跳转时，将enableAutoFill设置为false，密码保险箱将不启用自动填充功能
12. this.enableAutoFill = false;
13. return false;
14. }

16. @Builder
17. PageMap(name: string) {
18. if (name === 'home_page') {
19. HomePage()
20. }
21. }

23. build() {
24. Navigation(this.pathInfos) {
25. Column({ space: 16 }) {
26. Text("账户登录")
27. .commonTitleStyles()

29. TextInput({ placeholder: '账号' })
30. .commonInputStyles()
31. .type(InputType.USER_NAME)// 账号框使用USER_NAME属性
32. .enableAutoFill(this.enableAutoFill)// 保存填充功能属性
33. .onChange((value: string) => {
34. this.ReserveAccount = value;
35. })

37. TextInput({ placeholder: '密码' })
38. .commonInputStyles()
39. .showPasswordIcon(true)
40. .type(InputType.Password)// 密码框使用Password属性
41. .enableAutoFill(this.enableAutoFill)// 保存填充功能属性
42. .onChange((value: string) => {
43. this.ReservePassword = value;
44. })

46. Button('登录', { type: ButtonType.Capsule, stateEffect: false })
47. .borderRadius(20)
48. .width('100%')
49. .height(40)
50. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
51. .onClick(() => {
52. // 成功登录时页面跳转将enableAutoFill设置为true，密码保险箱使能
53. this.enableAutoFill = true;
54. this.pathInfos.pushPathByName('home_page', null)
55. })
56. }
57. .padding(16)
58. }
59. .navDestination(this.PageMap)
60. .height('100%')
61. .width('100%')
62. }
63. }

65. @Component
66. struct HomePage {
67. pathInfos: NavPathStack = new NavPathStack();

69. build() {
70. NavDestination() {
71. Column() {
72. Text("Home Page").commonTitleStyles()
73. }.width('100%').height('100%')
74. }.title("Home Page")
75. .onReady((context: NavDestinationContext) => {
76. this.pathInfos = context.pathStack;
77. })
78. }
79. }

81. @Extend(Text)
82. function commonTitleStyles() {
83. .fontSize(24)
84. .fontColor('#000000')
85. .fontWeight(FontWeight.Medium)
86. .margin({ top: 18 })
87. }

89. @Extend(TextInput)
90. function commonInputStyles() {
91. .placeholderColor(0x182431)
92. .width('100%')
93. .opacity(0.6)
94. .placeholderFont({ size: 16, weight: FontWeight.Regular })
95. }
```

## 将导致功能受限的布局

除上述典型场景外，以下界面布局对密码保险箱功能的使用存在限制：

| 实现场景 | 布局情况 | 账号密码填充 | 强密码填充 | 自动保存 |
| --- | --- | --- | --- | --- |
| 登录 | 用户名、密码不在同一界面 | 不支持 | 不支持 | 不支持 |
| 登录 | 验证码登录 | 不支持 | 不支持 | 不支持 |
| 注册 | 用户名、密码不在同一界面 | 不支持 | 不支持 | 不支持 |
| 修改密码 | 界面只有用户名、新密码 | 不支持 | 支持 | 支持 |
| 修改密码 | 界面只有旧密码、新密码 | 不支持 | 不支持 | 不支持 |
| 修改密码 | 界面只有新密码 | 不支持 | 不支持 | 不支持 |
