---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29ff2808dcb6dc8750f38251f6a138385b1e7491ee77e2701319e574d88cee98
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能debug调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下（模块）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/QrFDz29ETMmuQihyWnd2MQ/zh-cn_image_0000002530752694.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=FF65513CC5C1D2361CBF7D157C6EFA92AA2D6919127669705A975E4ECBB36268)

## 工程级build-profile.json5示例

```
1. {
2. "app": {
3. "signingConfigs": [],
4. "products": [
5. {
6. "name": "default",
7. "signingConfig": "default",
8. "compatibleSdkVersion": "6.1.0(23)",
9. "runtimeOS": "HarmonyOS",
10. "buildOption": {
11. "strictMode": {
12. "caseSensitiveCheck": true,
13. "useNormalizedOHMUrl": true
14. }
15. }
16. }
17. ],
18. "buildModeSet": [
19. {
20. "name": "debug"
21. },
22. {
23. "name": "release"
24. }
25. ]
26. },
27. "modules": [
28. {
29. "name": "entry",
30. "srcPath": "./entry",
31. "targets": [
32. {
33. "name": "default",
34. "applyToProducts": [
35. "default"
36. ]
37. }
38. ]
39. }
40. ]
41. }
```

## 模块级build-profile.json5示例

### entry模块

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. },
5. "buildOptionSet": [
6. {
7. "name": "release",
8. "arkOptions": {
9. "obfuscation": {
10. "ruleOptions": {
11. "enable": true,
12. "files": [
13. "./obfuscation-rules.txt"
14. ]
15. }
16. }
17. }
18. },
19. {
20. "name": "debug",
21. "debuggable": true,
22. "arkOptions": {
23. "obfuscation": {
24. "ruleOptions": {
25. "enable": false
26. }
27. }
28. }
29. }
30. ],
31. "buildModeBinder": [
32. {
33. "buildModeName": "release",
34. "mappings": [
35. {
36. "buildOptionName": "release",
37. "targetName": "default"
38. }
39. ]
40. },
41. {
42. "buildModeName": "debug",
43. "mappings": [
44. {
45. "buildOptionName": "debug",
46. "targetName": "default"
47. }
48. ]
49. }
50. ],
51. "targets": [
52. {
53. "name": "default",
54. },
55. {
56. "name": "ohosTest",
57. }
58. ]
59. }
```

## 指定构建模式

### 命令行

示例1：构建APP时，构建产物为default，指定构建模式为debug，可执行如下命令：

```
1. hvigorw --mode project -p product=default -p buildMode=debug assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/cOxHGwKPRDqXMULyjtuXxQ/zh-cn_image_0000002561752631.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=EAFF4088B7A403E937F6D644B1973B8872458F37F4BF46EC7F874999CC31DB47)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```
1. hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/1VajZ-u7TLWxhxhpzu--Tg/zh-cn_image_0000002530912684.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=EAD79CB304723C020C72D2EA1D8BDFEB34A35FFE6651855152F707EAB7EE8786)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Build Mode下拉选择对应配置选项debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，构建编译模式为debug，构建产物为default的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/1uCfMf5wTQqF0msTxZ7hyQ/zh-cn_image_0000002530752690.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=2201C0C1EE4495B59FB0A3381791CFA140004CCFF9225C6E60CB9818AF2AEF72)
