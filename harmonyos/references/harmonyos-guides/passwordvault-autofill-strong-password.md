---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-autofill-strong-password
title: 强密码填充
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 自动填充 > 强密码填充
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:09+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:16b45765937e6e62533dd1a582b7a4dea5c3f03a3d19090b88ac82e1a3f509e9
---

密码保险箱可以在用户需要输入一个新密码时，自动生成一个高强度的密码。用户选择使用生成的强密码时可以将这个密码填充到新密码输入框。

**触发条件及注意事项：**

* **已设置锁屏密码**并且开启密码保险箱中“自动填充和保存”开关。
* 界面中必须同时存在type为InputType.USER\_NAME（表示用户名输入框）和InputType.NEW\_PASSWORD（表示新密码输入框）的TextInput输入框组件。

  具体类型请参考[输入框类型说明](passwordvault-quick-adaptation.md#约束与限制)。
* TextInput组件的enableAutoFill属性的值为true（默认true）。
* 用户在界面中首次点击新密码输入框时触发强密码弹窗，用户点击使用密码按钮可以将弹窗中显示的强密码自动填充到新密码输入框。
* 开发者可以根据[一定的规则和建议](passwordvault-custom-strong-password-rules.md)指定强密码生成规则。

## 注册

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/elHIqf9bQbWi4Fx9-14UiA/zh-cn_image_0000002552958364.png?HW-CC-KV=V1&HW-CC-Date=20260427T234207Z&HW-CC-Expire=86400&HW-CC-Sign=0A9682A9D2E49639BFECC745D7CB832951F4F4B53087324E49BF6E49FAA05659)

示例代码如下：

```
1. @Entry
2. @Component
3. struct RegisterExample {
4. pathInfos: NavPathStack = new NavPathStack();
5. @State ReserveAccount: string = '';
6. @State ReservePassword: string = '';
7. @State enableAutoFill: boolean = true;

9. onBackPress() {
10. // 当非成功登录、返回等页面跳转时，将enableAutoFill设置为false，密码保险箱将不启用自动填充功能
11. this.enableAutoFill = false;
12. return false;
13. }

15. @Builder
16. PageMap(name: string) {
17. if (name === 'register_result_page') {
18. RegisterResultPage()
19. }
20. }

22. build() {
23. Navigation(this.pathInfos) {
24. Column() {
25. Text("注册账号")
26. .commonTitleStyles()

28. TextInput({ placeholder: '用户名' })
29. .commonInputStyles()
30. .type(InputType.USER_NAME) // 账号框使用USER_NAME属性
31. .onChange((value: string) => {
32. this.ReserveAccount = value;
33. })

35. TextInput({ placeholder: '新密码' })
36. .showPasswordIcon(true)
37. .commonInputStyles()
38. .type(InputType.NEW_PASSWORD) // 密码框使用NEW_PASSWORD属性，可以触发生成强密码。
39. .enableAutoFill(this.enableAutoFill)
40. .passwordRules('begin:[upper],special:[yes],len:[maxlen:32,minlen:12]')
41. .onChange((value: string) => {
42. this.ReservePassword = value;
43. })

45. Button('页面跳转')
46. .commonButtonStyles()
47. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
48. .onClick(() => {
49. this.pathInfos.pushPathByName('register_result_page', null)
50. })

52. Button('页面跳转（跳转前关闭autofill）')
53. .commonButtonStyles()
54. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
55. .onClick(() => {
56. this.enableAutoFill = false;
57. this.pathInfos.pushPathByName('register_result_page', null)
58. })
59. }
60. }
61. .navDestination(this.PageMap)
62. .height('100%')
63. .width('100%')
64. }
65. }

67. @Component
68. struct RegisterResultPage {
69. pathInfos: NavPathStack = new NavPathStack();

71. build() {
72. NavDestination() {
73. Column() {
74. Text("Result Page").commonTitleStyles()
75. }.width('100%').height('100%')
76. }.title("Result Page")
77. .onReady((context: NavDestinationContext) => {
78. this.pathInfos = context.pathStack;
79. })
80. }
81. }

83. @Extend(Text)
84. function commonTitleStyles() {
85. .fontSize(24)
86. .fontColor('#000000')
87. .fontWeight(FontWeight.Medium)
88. .margin({ top: 24, bottom: 16 })
89. }

91. @Extend(TextInput)
92. function commonInputStyles() {
93. .placeholderColor(0x182431)
94. .width('100%')
95. .opacity(0.6)
96. .placeholderFont({ size: 16, weight: FontWeight.Regular })
97. .margin({ top: 16 })
98. }

100. @Extend(Button)
101. function commonButtonStyles() {
102. .width('100%')
103. .height(40)
104. .borderRadius(20)
105. .margin({ top: 24 })
106. }
```

## 修改密码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/QcPBw1ciTjCSD8CHsy2PgA/zh-cn_image_0000002583478365.png?HW-CC-KV=V1&HW-CC-Date=20260427T234207Z&HW-CC-Expire=86400&HW-CC-Sign=9EBC75F3B17CB3A3F1A1DEBBA5E41723120EDD8A2E0423E31E66FB1E92627A61)

示例代码如下：

```
1. @Component
2. struct RegisterExample {
3. pathInfos: NavPathStack = new NavPathStack();
4. @State ReserveAccount: string = '';
5. @State ReservePassword: string = '';
6. @State enableAutoFill: boolean = true;

8. onBackPress() {
9. // 当非成功登录、返回等页面跳转时，将enableAutoFill设置为false，密码保险箱将不启用自动填充功能
10. this.enableAutoFill = false;
11. return false;
12. }

14. @Builder
15. PageMap(name: string) {
16. if (name === 'register_result_page') {
17. RegisterResultPage()
18. }
19. }

21. build() {
22. Navigation(this.pathInfos) {
23. Column() {
24. Text("修改密码")
25. .commonTitleStyles()

27. TextInput({ placeholder: '用户名' })
28. .commonInputStyles()
29. .type(InputType.USER_NAME) // 账号框使用USER_NAME属性
30. .onChange((value: string) => {
31. this.ReserveAccount = value;
32. })

34. TextInput({ placeholder: '密码' })
35. .showPasswordIcon(true)
36. .commonInputStyles()
37. .type(InputType.Password)
38. .onChange((value: string) => {
39. this.ReservePassword = value;
40. })

42. TextInput({ placeholder: '新密码' })
43. .showPasswordIcon(true)
44. .commonInputStyles()
45. .type(InputType.NEW_PASSWORD) // 密码框使用NEW_PASSWORD属性，可以触发生成强密码。
46. .enableAutoFill(this.enableAutoFill)
47. .passwordRules('begin:[upper],special:[yes],len:[maxlen:32,minlen:12]')
48. .onChange((value: string) => {
49. this.ReservePassword = value;
50. })

52. Button('页面跳转')
53. .commonButtonStyles()
54. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
55. .onClick(() => {
56. this.pathInfos.pushPathByName('register_result_page', null)
57. })

59. Button('页面跳转（跳转前关闭autofill）')
60. .commonButtonStyles()
61. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
62. .onClick(() => {
63. this.enableAutoFill = false;
64. this.pathInfos.pushPathByName('register_result_page', null)
65. })
66. }
67. }
68. .navDestination(this.PageMap)
69. .height('100%')
70. .width('100%')
71. }
72. }

74. @Component
75. struct RegisterResultPage {
76. pathInfos: NavPathStack = new NavPathStack();

78. build() {
79. NavDestination() {
80. Column() {
81. Text("Result Page").commonTitleStyles()
82. }.width('100%').height('100%')
83. }.title("Result Page")
84. .onReady((context: NavDestinationContext) => {
85. this.pathInfos = context.pathStack;
86. })
87. }
88. }

90. @Extend(Text)
91. function commonTitleStyles() {
92. .fontSize(24)
93. .fontColor('#000000')
94. .fontWeight(FontWeight.Medium)
95. .margin({ top: 24, bottom: 16 })
96. }

98. @Extend(TextInput)
99. function commonInputStyles() {
100. .placeholderColor(0x182431)
101. .width('100%')
102. .opacity(0.6)
103. .placeholderFont({ size: 16, weight: FontWeight.Regular })
104. .margin({ top: 16 })
105. }

107. @Extend(Button)
108. function commonButtonStyles() {
109. .width('100%')
110. .height(40)
111. .borderRadius(20)
112. .margin({ top: 24 })
113. }
```
