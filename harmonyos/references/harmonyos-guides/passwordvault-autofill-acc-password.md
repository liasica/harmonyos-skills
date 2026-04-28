---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-autofill-acc-password
title: 账号密码填充
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:08+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:5dcea5c54409add2c7bfbccebd5b79b4495c218c339d69f8b198561ea1ff5231
---

密码保险箱可以在登录或修改密码时，自动填充已保存的用户名和密码。

**触发条件及注意事项：**

* **已设置锁屏密码**并且开启密码保险箱中“自动填充和保存”开关。
* 界面中必须同时存在type为InputType.USER\_NAME（表示用户名输入框）和InputType.Password（表示普通密码输入框）的TextInput输入框组件。

  具体类型请参考[输入框类型说明](passwordvault-quick-adaptation.md#约束与限制)。
* TextInput组件的enableAutoFill属性的值为true（默认true）。
* 密码保险箱中已保存过当前应用的用户名和密码。
* 用户在界面中首次点击用户名输入框或密码输入框时触发自动填充弹窗。

## 登录

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/K0uTsBtuSs-FdsjGyHODRA/zh-cn_image_0000002552798714.png?HW-CC-KV=V1&HW-CC-Date=20260427T234206Z&HW-CC-Expire=86400&HW-CC-Sign=46C1D084EF11A363BDF7BEE523E3FD71CDCE73C614356FA7E6C5D9AE6DE7DC60)

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
17. Column() {
18. Text("账户登录")
19. .commonTitleStyles()

21. TextInput({ placeholder: '用户名' })
22. .commonInputStyles()
23. .type(InputType.USER_NAME)// 账号框使用USER_NAME属性
24. .onChange((value: string) => {
25. this.ReserveAccount = value;
26. })

28. TextInput({ placeholder: '密码' })
29. .showPasswordIcon(true)
30. .commonInputStyles()
31. .type(InputType.Password)// 密码框使用Password属性
32. .onChange((value: string) => {
33. this.ReservePassword = value;
34. })

36. Button('登录')
37. .commonButtonStyles()
38. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
39. .onClick(() => {
40. this.pathInfos.pushPathByName('home_page', null)
41. })
42. }
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

## 修改密码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/S77sRQOuSF6-oVtz09AeZg/zh-cn_image_0000002583438409.png?HW-CC-KV=V1&HW-CC-Date=20260427T234206Z&HW-CC-Expire=86400&HW-CC-Sign=F44C83F1EA171203CCC319B2DDABBA6DE10B46B7D189F90C3703C29C8D6236BD)

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
25. Text("修改密码")
26. .commonTitleStyles()

28. TextInput({ placeholder: '用户名' })
29. .commonInputStyles()
30. .type(InputType.USER_NAME) // 账号框使用USER_NAME属性
31. .onChange((value: string) => {
32. this.ReserveAccount = value;
33. })

35. TextInput({ placeholder: '密码' })
36. .showPasswordIcon(true)
37. .commonInputStyles()
38. .type(InputType.Password)
39. .onChange((value: string) => {
40. this.ReservePassword = value;
41. })

43. TextInput({ placeholder: '新密码' })
44. .showPasswordIcon(true)
45. .commonInputStyles()
46. .type(InputType.NEW_PASSWORD) // 密码框使用NEW_PASSWORD属性，可以触发生成强密码。
47. .enableAutoFill(this.enableAutoFill)
48. .passwordRules('begin:[upper],special:[yes],len:[maxlen:32,minlen:12]')
49. .onChange((value: string) => {
50. this.ReservePassword = value;
51. })

53. Button('页面跳转')
54. .commonButtonStyles()
55. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
56. .onClick(() => {
57. this.pathInfos.pushPathByName('register_result_page', null)
58. })

60. Button('页面跳转（跳转前关闭autofill）')
61. .commonButtonStyles()
62. .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
63. .onClick(() => {
64. this.enableAutoFill = false;
65. this.pathInfos.pushPathByName('register_result_page', null)
66. })
67. }
68. }
69. .navDestination(this.PageMap)
70. .height('100%')
71. .width('100%')
72. }
73. }

75. @Component
76. struct RegisterResultPage {
77. pathInfos: NavPathStack = new NavPathStack();

79. build() {
80. NavDestination() {
81. Column() {
82. Text("Result Page").commonTitleStyles()
83. }.width('100%').height('100%')
84. }.title("Result Page")
85. .onReady((context: NavDestinationContext) => {
86. this.pathInfos = context.pathStack;
87. })
88. }
89. }

91. @Extend(Text)
92. function commonTitleStyles() {
93. .fontSize(24)
94. .fontColor('#000000')
95. .fontWeight(FontWeight.Medium)
96. .margin({ top: 24, bottom: 16 })
97. }

99. @Extend(TextInput)
100. function commonInputStyles() {
101. .placeholderColor(0x182431)
102. .width('100%')
103. .opacity(0.6)
104. .placeholderFont({ size: 16, weight: FontWeight.Regular })
105. .margin({ top: 16 })
106. }

108. @Extend(Button)
109. function commonButtonStyles() {
110. .width('100%')
111. .height(40)
112. .borderRadius(20)
113. .margin({ top: 24 })
114. }
```
