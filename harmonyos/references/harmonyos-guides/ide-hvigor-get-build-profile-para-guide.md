---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-guide
title: 能力说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 获取自定义编译参数 > 能力说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55ec96117de1f5eef056e17922354c69f9192e890df03de8880b4ddc33f756b6
---

在编译构建时，Hvigor会生成BuildProfile类，开发者可以通过该类在运行时获取编译构建参数，也可以在build-profile.json5中通过buildProfileFields增加自定义字段，从而在运行时获取自定义的参数。

## 使用说明

buildProfileFields的优先级：模块级target > 模块级buildOptionSet > 模块级buildOption > 工程级product > 工程级buildModeSet

## HAP/HSP运行时获取编译构建参数

### 生成BuildProfile类文件

当前有以下几种方式可以生成BuildProfile类文件：

* 选中需要编译的模块，在菜单栏选择“Build > Generate Build Profile ${moduleName}”。
* 在菜单栏选择“Build > Build Hap(s)/APP(s) > Build Hap(s)”或“Build > Build Hap(s)/APP(s) > Build APP(s)”。
* 在Terminal中执行如下命令：

  ```
  1. hvigorw GenerateBuildProfile
  ```

执行完上述操作后，将在“${moduleName} / build / ${productName} / generated / profile / ${targetName} ”目录下生成BuildProfile.ets文件。示例如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/YpR8XKL5QOOiDvhsn_2vGg/zh-cn_image_0000002561753361.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=1AB938A7381C42A1D4D4A4EDBC891620B29DB2CC5F5C0C9D9ED7A17E658BB901)

### 在代码中获取构建参数

生成BuildProfile类文件后，在代码中可以通过如下方式引入该文件，其中packageName是模块级oh-package.json5文件中name字段对应的值。

```
1. import BuildProfile from '${packageName}/BuildProfile';
```

说明

在HSP中使用import BuildProfile from 'BuildProfile'在跨包集成HSP的时候可能会产生编译错误，推荐使用import BuildProfile from '${packageName}/BuildProfile'。

通过如下方式获取到构建参数：

```
1. @State message: string = BuildProfile.BUNDLE_NAME;
```

### 默认参数

生成BuildProfile类文件时，Hvigor会根据当前工程构建的配置信息生成一部分默认参数，开发者可以在代码中直接使用。

**表1** 默认参数说明

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| BUNDLE\_NAME | string | 应用的Bundle名称。 |
| BUNDLE\_TYPE | string | 应用的Bundle类型。 |
| VERSION\_CODE | number | 应用的版本号。 |
| VERSION\_NAME | string | 应用版本号的文字描述。 |
| TARGET\_NAME | string | Target名称。 |
| PRODUCT\_NAME | string | Product名称。 |
| BUILD\_MODE\_NAME | string | 编译模式。 |
| DEBUG | boolean | 应用是否可调试。 |

### 自定义参数

开发者可以在模块级的build-profile.json5文件中增加自定义参数，在生成BuildProfile类文件后，在代码中使用自定义参数。

自定义参数可以在buildOption、buildOptionSet、targets节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。

配置示例如下所示：

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. "arkOptions": {
5. "buildProfileFields": {
6. "data": "Data",
7. }
8. }
9. },
10. "buildOptionSet": [
11. {
12. "name": "release",
13. "arkOptions": {
14. "buildProfileFields": {
15. "buildOptionSetData": "BuildOptionSetDataRelease",
16. "data": "DataRelease"
17. }
18. }
19. },
20. {
21. "name": "debug",
22. "arkOptions": {
23. "buildProfileFields": {
24. "buildOptionSetData": "BuildOptionSetDataDebug",
25. "data": "DataDebug"
26. }
27. }
28. }
29. ],
30. "targets": [
31. {
32. "name": "default",
33. "config": {
34. "buildOption": {
35. "arkOptions": {
36. "buildProfileFields": {
37. "targetData": "TargetData",
38. "data": "DataTargetDefault"
39. }
40. }
41. }
42. }
43. },
44. {
45. "name": "default1",
46. "config": {
47. "buildOption": {
48. "arkOptions": {
49. "buildProfileFields": {
50. "targetData": "TargetData1",
51. "data": "DataTargetDefault1"
52. }
53. }
54. }
55. }
56. },
57. {
58. "name": "ohosTest",
59. }
60. ]
61. }
```

## HAR运行时获取编译构建参数

### 生成BuildProfile类文件

当前有以下几种方式可以生成BuildProfile类文件：

* 选中需要编译的模块，在菜单栏选择“Build > Generate Build Profile ${moduleName}”。
* 选中需要编译的模块，在菜单栏选择“Build > Make Module ${moduleName}”。
* 在Terminal中执行如下命令：

  ```
  1. hvigorw GenerateBuildProfile
  ```

执行完上述操作后，将在模块根目录下生成BuildProfile.ets文件（该文件可放置在.gitignore文件中进行忽略）。示例如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/3QgtrBgkQGi1IF-wBYFVQg/zh-cn_image_0000002561833337.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=63C1785010205EF97007A589F34ECDE48290DD8D637E1FF01C894AB8319A8E01)

### 在代码中获取构建参数

生成BuildProfile类文件后，在代码中可以通过相对路径引入该文件，如在HAR模块的Index.ets文件中使用该文件：

```
1. import BuildProfile from './BuildProfile';
```

通过如下方式获取到构建参数：

```
1. const HAR_VERSION: string = BuildProfile.HAR_VERSION;
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/wJlrRzx1SZiMeobUnyS9DQ/zh-cn_image_0000002530753418.png?HW-CC-KV=V1&HW-CC-Date=20260427T235716Z&HW-CC-Expire=86400&HW-CC-Sign=AA7FC3B90A5B1E0A28349825B8992CB7288351E81AA96C426FC70AF74A5667B5)

### 默认参数

生成BuildProfile类文件时，Hvigor会根据当前工程构建的配置信息生成一部分默认参数，开发者可以在代码中直接使用。

**表2** 默认参数说明

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| HAR\_VERSION | string | HAR版本号。 |
| BUILD\_MODE\_NAME | string | 编译模式。 |
| DEBUG | boolean | 应用是否可调试。 |
| TARGET\_NAME | string | 目标名称。 |

### 自定义参数

开发者可以在模块级的build-profile.json5文件中增加自定义参数，在生成BuildProfile类文件后，在代码中使用自定义参数。

自定义参数可以在buildOption、buildOptionSet节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。

配置示例如下所示：

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. "arkOptions": {
5. "buildProfileFields": {
6. "data": "Data",
7. }
8. }
9. },
10. "buildOptionSet": [
11. {
12. "name": "release",
13. "arkOptions": {
14. "buildProfileFields": {
15. "buildOptionSetData": "BuildOptionSetDataRelease",
16. "data": "DataRelease"
17. }
18. }
19. },
20. {
21. "name": "debug",
22. "arkOptions": {
23. "buildProfileFields": {
24. "buildOptionSetData": "BuildOptionSetDataDebug",
25. "data": "DataDebug"
26. }
27. }
28. }
29. ],
30. "targets": [
31. {
32. "name": "default",
33. }
34. ]
35. }
```

## 工程级配置自定义构建参数

开发者可以在工程级的build-profile.json5文件中增加自定义参数，该自定义参数会生成到所有模块的BuildProfile类文件，在代码中使用自定义参数。

自定义参数可以在工程级products、buildModeSet中的buildOption节点下的arkOptions子节点中通过增加buildProfileFields字段实现，自定义参数通过key-value键值对的方式配置，其中value取值仅支持number、string、boolean类型。

配置示例如下所示：

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
11. "arkOptions": {
12. "buildProfileFields": {
13. "productValue": "defaultValue"
14. }
15. }
16. }
17. }
18. ],
19. "buildModeSet": [
20. {
21. "name": "debug",
22. "buildOption": {
23. "arkOptions": {
24. "buildProfileFields": {
25. "productBuildModeValue": "debugValue"
26. }
27. }
28. }
29. },
30. {
31. "name": "release"
32. }
33. ]
34. },
35. "modules": [
36. {
37. "name": "entry",
38. "srcPath": "./entry",
39. "targets": [
40. {
41. "name": "default",
42. "applyToProducts": [
43. "default"
44. ]
45. }
46. ]
47. }
48. ]
49. }
```
