---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/passwordvault-update-acc-password
title: 账号密码更新
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:08+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:899077439b0dd458f17a42e723d5d15246ccf61e1a913a969afbe5b09c916c5a
---

应用界面触发账号密码自动保存时，若密码保险箱中已存在同应用下与本次使用账号相同的账号，则弹出密码更新提示框，用户点击更新按钮，即可更新密码保险箱内对应账号的密码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/fMO1aXNXQ-KcKWDD14qrKQ/zh-cn_image_0000002552958362.png?HW-CC-KV=V1&HW-CC-Date=20260427T234206Z&HW-CC-Expire=86400&HW-CC-Sign=97953BCD82E9B01F86497FD6D61A84719DDFB2E8178FD1B9D82A980C51E8172A)

应用触发修改密码或使用已经保存过的账号手动登录时，均会触发密码更新功能。

登录的布局介绍请参考[账号密码登录](passwordvault-save-acc-password.md#账号密码登录)，以下仅介绍修改账号密码的标准适配场景。

**触发条件及注意事项同[账号密码保存](passwordvault-save-acc-password.md)功能。**

## 修改账号密码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jhLmpyhNSo-janty80VP2A/zh-cn_image_0000002583478363.png?HW-CC-KV=V1&HW-CC-Date=20260427T234206Z&HW-CC-Expire=86400&HW-CC-Sign=5037E55164782E6D3B024990947147848ADA0E66D4A1C88E481B0B937916A26B)

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
