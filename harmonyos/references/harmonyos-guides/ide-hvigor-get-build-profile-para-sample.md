---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6512840b8217aeced3ef9b696b5455fb75eabfddb4020afc91025210d2f9fb9f
---

示例：配置工程级和模块级的自定义参数并通过切换product来展示不同的message。

## 新建工程并创建一个har模块

在工程级别的build-profile.json5使用以下配置，目的是为了实现在所有模块中都可以使用到productMessage自定义参数。

通过切换不同的product从而使用到对应的productMessage值。

```
1. {
2. "app": {
3. "products": [
4. {
5. "name": "default",
6. "signingConfig": "default",
7. "compatibleSdkVersion": "6.1.0(23)",
8. "runtimeOS": "HarmonyOS",
9. "buildOption": {
10. "arkOptions": {
11. // 工程级自定义参数
12. "buildProfileFields": {
13. "productMessage": 'defaultMessage'
14. }
15. }
16. }
17. },
18. {
19. "name": "mirror",
20. "signingConfig": "default",
21. "compatibleSdkVersion": "6.1.0(23)",
22. "runtimeOS": "HarmonyOS",
23. "buildOption": {
24. "arkOptions": {
25. // 工程级自定义参数
26. "buildProfileFields": {
27. "productMessage": 'mirrorMessage'
28. }
29. }
30. }
31. },
32. {
33. "name": "product",
34. "signingConfig": "default",
35. "compatibleSdkVersion": "6.1.0(23)",
36. "runtimeOS": "HarmonyOS",
37. "buildOption": {
38. "arkOptions": {
39. // 工程级自定义参数
40. "buildProfileFields": {
41. "productMessage": 'productMessage'
42. }
43. }
44. }
45. }
46. ],
47. "buildModeSet": [
48. {
49. "name": "debug",
50. },
51. {
52. "name": "release"
53. }
54. ]
55. },
56. "modules": [
57. {
58. "name": "entry",
59. "srcPath": "./entry",
60. "targets": [
61. {
62. "name": "default",
63. "applyToProducts": [
64. // 关联到多个product
65. "default",
66. "product",
67. "mirror"
68. ]
69. }
70. ]
71. },
72. {
73. "name": "har",
74. "srcPath": "./har"
75. }
76. ]
77. }
```

在har模块的build-profile.json5使用以下配置。

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. "arkOptions": {
5. // har模块的自定义参数
6. "buildProfileFields": {
7. "targetMessage1": 'this is target buildProfileValue1',
8. "targetMessage2": 'this is target buildProfileValue2'
9. }
10. }
11. },
12. "buildOptionSet": [
13. {
14. "name": "release",
15. "arkOptions": {
16. "obfuscation": {
17. "ruleOptions": {
18. "enable": true,
19. "files": [
20. "./obfuscation-rules.txt"
21. ]
22. },
23. "consumerFiles": [
24. "./consumer-rules.txt"
25. ]
26. }
27. },
28. },
29. ],
30. "targets": [
31. {
32. "name": "default"
33. }
34. ]
35. }
```

在har模块的MainPage.ets中添加以下代码。

```
1. import BuildProfile from "../../../../BuildProfile"

3. @Preview
4. @Component
5. export struct MainPage {
6. // 默认赋值为工程级别BuildProfile自定义参数配置的productMessage
7. @State message: string = BuildProfile.productMessage
8. build() {
9. Row() {
10. Column() {
11. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceAround }) {
12. Button("Button 1").width("40%")
13. .onClick(() => {
14. // 点击展示自定义字段targetMessage1
15. this.message = BuildProfile.targetMessage1;
16. })
17. Button("Button 2").width("40%")
18. .onClick(() => {
19. // 点击展示自定义字段targetMessage2
20. this.message = BuildProfile.targetMessage2;
21. })
22. }.margin(20)
23. .width(315)
24. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
25. Text(this.message)
26. .textAlign(TextAlign.Start)
27. .fontSize(12)
28. .border({ width: 1 })
29. .padding(10)
30. .width('100%')
31. }.height(600).width(350).padding({ left: 35, right: 35})
32. }
33. }
34. }
35. }
```

在hap的oh-package.json5中引用本地的har模块。

```
1. {
2. "name": "entry",
3. "version": "1.0.0",
4. "description": "Please describe the basic information.",
5. "main": "",
6. "author": "",
7. "license": "",
8. "dependencies": {
9. "har": "file:../har"
10. }
11. }
```

在hap的Index.ets文件中引用该har包并且使用MainPage方法。

```
1. import { MainPage } from "har"

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. MainPage()
9. }
10. }
11. }
```

## 执行预览或签名后推包到设备调试

点击har模块执行以下按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/eX-CKX5KSXOa561f3FShCw/zh-cn_image_0000002530753414.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=C858C16263FCBCD25163D72DA7C5BE330E5D5C796D73E15E621E4D08B799F7AB)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/A6RxCtQLSymt0hipZlHsVw/zh-cn_image_0000002561833325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=A23934AABF016A78731429C0EA10151216B5607B6560E92C99DBFA256EEA0F9B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/I9nLRDukRM6fVhT-19XK9g/zh-cn_image_0000002530753410.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=E21F4E925C5AC21C7B7D680E17D98B9786479FCE6B400F06C320ABD05B9BB86B)

通过切换不同的product可以使用不同的自定义参数用来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/1vQofxoISA6ibgpXHU-kCQ/zh-cn_image_0000002530913396.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=01207FE3D327668874C0E5198E6023EFF045D7131F5E0BD36996AF5DDAC15D6E)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/py9TJBidTc6yOsTNVFB3tQ/zh-cn_image_0000002530913400.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=140A0308A08B5B0C7388EE45D37905636A9DFA4FD0F8D108189A83E5127301EB)

点击不同的Button可以改变message为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/T9-GQb_LQm6F94x_OTL6iw/zh-cn_image_0000002530913398.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=5E8C9CCB7D705F1F68826E27F4943F3D52D3CDDE9E9A445A7E7EECBE80FEEA94)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Cys9BL6VTKqdX40_iLfmKg/zh-cn_image_0000002561753351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=871E6752078861CB38988A26663852AA5AB9A390FC437CB49B6C2D7471DEDAB1)
