---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:037e7db2cab7c1c2fa7319ab2ee506cbeca7bd869fda5a5e15cc9928d4e23b9e
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/A0fOE7ZqQt--z2bOUhcuag/zh-cn_image_0000002530753414.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=B886AB51812B7CBE281660F274D72294DD3196FC6BB266EC661DB6398C2574C9)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WKKUAaCSTUi-y6ERoJjrgA/zh-cn_image_0000002561833325.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=C95CF4BF778CE2CC47BD1916CB566098A73A6AE025A2AAE37D503E13DAE30075)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/Tm9u-tZjSjyD47wQqlEEcA/zh-cn_image_0000002530753410.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=11514C76BCEF98C523056448FA94DB706D3DE04D455D68AAE754A28E08FB8F6A)

通过切换不同的product可以使用不同的自定义参数用来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/y_lIWVpWQ9SpUg3mmhO6FQ/zh-cn_image_0000002530913396.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=17E0C9D118159D266329C642971D57AF766D8D55A20C240A68BA86F8E37F7676)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Sg0nnW2hQHGL3ZaTnR_Aqg/zh-cn_image_0000002530913400.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=7C7321B01A2EE5EB131BE83960555A57A45AC82ADCC09B2E207E953A52C5BD42)

点击不同的Button可以改变message为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/gNALixuKRgGvFv8xfgSzUg/zh-cn_image_0000002530913398.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=8BD51657530D583701464CDF5160A307173F118F3DF45BB58FA939DE7A673150)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/tUYI0lGsS9Kf9ouTeq8Rsw/zh-cn_image_0000002561753351.png?HW-CC-KV=V1&HW-CC-Date=20260429T054716Z&HW-CC-Expire=86400&HW-CC-Sign=E4F3AE700390D070519E53DD54B698503224CD666C1E4559B71885365DDCA14F)
