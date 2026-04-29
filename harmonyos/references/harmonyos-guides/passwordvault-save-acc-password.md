---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-save-acc-password
title: 账号密码保存
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用接入密码保险箱 > 自动保存 > 账号密码保存
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:38+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:8a60adebdcb07cd5ed2d3ad7e9b2fd2e1bace3ab927a5b9c03859be7cd20a046
---

密码保险箱在应用的登录、注册、修改密码等场景中具备自动保存用户名和密码的能力。

保存后的用户名和密码可以在下次登录、修改密码时自动填充到界面上的对应输入框，用户可以在密码保险箱内对已保存的用户名和密码进行查看，修改，添加备注，删除。

当应用界面触发账号密码自动保存时，若密码保险箱中不存在同应用下的相同账号，系统将弹出账号密码保存提示框，用户点击“保存密码”按钮后，本次使用的账号和密码将被保存至密码保险箱。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/cOdAdGGqRNiOqrWycE7z5w/zh-cn_image_0000002589244665.png?HW-CC-KV=V1&HW-CC-Date=20260429T053037Z&HW-CC-Expire=86400&HW-CC-Sign=E42112FFC11A81CD1BB499A7BD430D5F68D3511A11BCEFE21F20F404EBA34CA5)

当应用触发账号登录或注册时，均可触发保存功能，以下分别介绍两种布局的标准适配场景。

**触发条件及注意事项：**

1. **已设置锁屏密码**，并且开启密码保险箱中“自动填充和保存”开关。
2. 界面中TextInput输入框组件的enableAutoFill属性的值应为true（默认为true）。
3. 密码保险箱的自动保存功能只适用于用户名和密码保存场景，在界面中必须同时存在用户名和密码的TextInput输入框组件。具体类型请参考[输入框类型说明](passwordvault-quick-adaptation.md#约束与限制)。

   用户名输入框应设置type属性为InputType.USER\_NAME。

   密码输入框应设置type属性为InputType.Password或InputType.NEW\_PASSWORD。

   其中，InputType.Password表示普通密码输入框，适用于登录界面的密码和修改密码界面的旧密码。

   InputType.NEW\_PASSWORD表示新密码输入框，适用于注册界面和修改密码界面的新密码。
4. 用户名和密码输入框中需要输入内容，不能为空也不能超长。用户名长度不能超过128字符，密码长度不能超过256字符。
5. 页面跳转时触发保存功能。
6. 在只有type为InputType.USER\_NAME和InputType.Password的两个TextInput组件时，如果使用[账号密码填充-修改密码](passwordvault-autofill-acc-password.md#修改密码)自动填充了用户名和密码并没有修改，则不会触发保存和更新功能。

## 账号密码登录

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/pVdAtr6_RhqhSv1Ucjwycw/zh-cn_image_0000002558764860.png?HW-CC-KV=V1&HW-CC-Date=20260429T053037Z&HW-CC-Expire=86400&HW-CC-Sign=E1D960B8DF56C04568A55A06F83C532DFBAE5401D0EF6F04F0738EC5469E3CAD)

示例代码如下：

```
1. @Entry
2. @Component
3. struct LoginExample {
4. pathInfos: NavPathStack = new NavPathStack();
5. @State ReserveAccount: string = '';
6. @State ReservePassword: string = '';

8. @Builder
9. PageMap(name: string) {
10. if (name === 'home_page') {
11. HomePage()
12. }
13. }

15. build() {
16. Navigation(this.pathInfos) {
17. Column({ space: 16 }) {
18. Text("账户登录").commonTitleStyles()

20. TextInput({ placeholder: '用户名' })
21. .commonInputStyles()
22. .type(InputType.USER_NAME) // 账号框使用USER_NAME属性
23. .onChange((value: string) => {
24. this.ReserveAccount = value;
25. })

27. TextInput({ placeholder: '密码' })
28. .showPasswordIcon(true)
29. .commonInputStyles()
30. .type(InputType.Password) // 密码框使用Password属性
31. .onChange((value: string) => {
32. this.ReservePassword = value;
33. })

35. Button('登录')
36. .width('100%')
37. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
38. .onClick(() => {
39. this.pathInfos.pushPathByName('home_page', null)
40. })
41. }
42. .padding(16)
43. }
44. .navDestination(this.PageMap)
45. .height('100%')
46. .width('100%')
47. }
48. }

50. @Component
51. struct HomePage {
52. pathInfos: NavPathStack = new NavPathStack();

54. build() {
55. NavDestination() {
56. Column() {
57. Text("Home Page").commonTitleStyles()
58. }.width('100%').height('100%')
59. }.title("Home Page")
60. .onReady((context: NavDestinationContext) => {
61. this.pathInfos = context.pathStack;
62. })
63. }
64. }

66. @Extend(Text)
67. function commonTitleStyles() {
68. .fontSize(24)
69. .fontColor('#000000')
70. .fontWeight(FontWeight.Medium)
71. .margin({ top: 24, bottom: 16 })
72. }

74. @Extend(TextInput)
75. function commonInputStyles() {
76. .placeholderColor(0x182431)
77. .width('100%')
78. .opacity(0.6)
79. .placeholderFont({ size: 16, weight: FontWeight.Regular })
80. .margin({ top: 16 })
81. }

83. @Extend(Button)
84. function commonButtonStyles() {
85. .width('100%')
86. .height(40)
87. .borderRadius(20)
88. .margin({ top: 24 })
89. }
```

## 账号密码注册

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/qoor2vIcRJOf42KWsbM5Cw/zh-cn_image_0000002558605204.png?HW-CC-KV=V1&HW-CC-Date=20260429T053037Z&HW-CC-Expire=86400&HW-CC-Sign=2FA444D27DF491DB55A4CAF52DBF0B25AB6060ABBE689A8BB0BA5EF5FFDCEDF6)

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
