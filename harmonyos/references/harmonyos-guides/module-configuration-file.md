---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file
title: module.json5配置文件
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用配置文件（Stage模型） > module.json5配置文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ca5166166c0a3f61f219a28a511d863ad81abd1c04cab98bdf94556088752908
---

模块级配置文件，包含模块的基本配置信息、UIAbility组件和ExtensionAbility组件信息，以及应用运行过程中需要的权限信息，用于向编译工具、操作系统和应用市场提供应用的基本信息。每个模块下必须包括一个module.json5配置文件，文件所在目录为工程名称/模块名称（例如entry）/src/main/module.json5。

说明

配置文件中的示例代码直接拷贝到工程中可能编译不通过，请开发者根据需求进行配置。例如：通过$符号引用的资源文件如果工程中不存在，需要开发者手动添加或替换为实际的资源文件。

配置文件中，字段可以重复，以最后一个配置为准。

## 配置文件示例

通过一个示例，整体了解module.json5配置文件。

```
1. {
2. "module": {
3. "name": "entry",
4. "type": "entry",
5. "description": "$string:module_desc",
6. "mainElement": "EntryAbility",
7. "deviceTypes": [
8. "tv",
9. "tablet"
10. ],
11. "deliveryWithInstall": true,
12. "pages": "$profile:main_pages", // 资源配置，指向profile下面定义的配置文件main_pages.json
13. "appStartup": "$profile:app_startup_config",
14. "metadata": [
15. {
16. "name": "string",
17. "value": "string",
18. "resource": "$profile:distributionFilter_config"
19. },
20. // ...
21. ],
22. "abilities": [
23. {
24. "name": "EntryAbility",
25. "srcEntry": "./ets/entryability/EntryAbility.ets",
26. "description": "$string:EntryAbility_desc",
27. "icon": "$media:layered_image",
28. "label": "$string:EntryAbility_label",
29. "startWindow": "$profile:start_window",
30. "startWindowIcon": "$media:icon",
31. "startWindowBackground": "$color:start_window_background",
32. "exported": true,
33. "skills": [
34. // ...
35. {
36. "entities": [
37. "entity.system.home"
38. ],
39. "actions": [
40. "ohos.want.action.home"
41. ]
42. }
43. ],
44. // ...
45. "continueType": [
46. "continueType1"
47. ],
48. "continueBundleName": [
49. "com.example.myapplication1",
50. "com.example.myapplication2"
51. ],
52. }
53. ],
54. "requestPermissions": [
55. {
56. "name": "ohos.permission.ACCESS_BLUETOOTH",
57. "reason": "$string:reason",
58. "usedScene": {
59. "abilities": [
60. "EntryAbility"
61. ],
62. "when": "inuse"
63. }
64. }
65. ],
66. "querySchemes": [
67. "app1Scheme",
68. "app2Scheme"
69. ],
70. "routerMap": "$profile:router_map",
71. "appEnvironments": [
72. {
73. "name": "name1",
74. "value": "value1"
75. }
76. ],
77. "fileContextMenu": "$profile:menu", // 资源配置，指向profile下面定义的配置文件menu.json
78. "crossAppSharedConfig": "$profile:shared_config",
79. // ...
80. }
81. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L16-L186)

## 配置文件标签

module.json5配置文件包含以下标签。

**表1** module.json5配置文件标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识当前Module的名称，确保该名称在整个应用中唯一。命名规则如下 ：  - 由字母、数字和下划线组成，且必须以字母开头。  - 最大长度128字节。  应用升级时允许修改该名称，但需要应用适配Module相关数据目录的迁移，详见[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)。  **说明：**  DevEco Studio新建模块时，限制模块名称的长度不能超过31。如果长度无法满足开发者需求，可以在配置文件修改该标签。 | 字符串 | 该标签不可缺省。 |
| type | 标识当前Module的类型。支持的取值如下：  - entry：应用的主模块。  - feature：应用的动态特性模块。  - har：静态共享包模块。  - shared：动态共享包模块。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 标识AbilityStage组件的代码路径，详情参考[AbilityStage组件容器](abilitystage.md)，取值为长度不超过127字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| description | 标识当前Module的描述信息，开发者可以通过该标签描述当前模块的功能与作用，取值为长度不超过255字节的字符串，可以采用字符串资源索引格式。 | 字符串 | 该标签可缺省，缺省值为空。 |
| mainElement | 标识当前Module的入口UIAbility名称，取值为长度不超过255字节的字符串，详情请参考配置应用图标和名称中的[配置优先级和生成策略](layered-image.md#配置优先级和生成策略)。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [deviceTypes](module-configuration-file.md#devicetypes标签) | 标识当前Module可以运行在哪类设备上。  **说明：**  当存在多个模块时，各模块的配置可以不同，但都必须包含将要安装的设备类型，以确保正常运行。 | 字符串数组 | 该标签不可缺省。 |
| deliveryWithInstall | 标识当前Module是否在用户主动安装的时候安装，即该Module对应的HAP/HSP是否跟随应用一起安装。  - true：跟随应用一起安装。  - false：不跟随应用一起安装。通过[按需分发](store-moduleinstall_arkts.md)的方式安装。 | 布尔值 | 当前Module类型为HAP或HSP时，该标签不可缺省。 |
| installationFree | 标识当前Module是否支持免安装特性。  - true：表示支持免安装特性，且符合免安装约束。  - false：表示不支持免安装特性。 | 布尔值 | 该标签可缺省。该标签在编译构建时自动生成，手动配置不生效。  **说明：**  当[bundleType](app-configuration-file.md#配置文件标签)为元服务时，该标签自动配置为true。反之，该标签自动配置为false。 |
| virtualMachine | 标识当前Module运行的目标虚拟机类型，供云端分发使用，如应用市场和分发中心。如果目标虚拟机类型为ArkTS引擎，则其值为“ark+版本号”。 | 字符串 | 该标签可缺省，手动配置不生效，由编译构建时自动生成。 |
| [pages](module-configuration-file.md#pages标签) | 标识当前Module的profile资源，用于列举每个页面信息，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [metadata](module-configuration-file.md#metadata标签) | 标识当前Module的自定义元信息，可通过资源引用的方式配置[distributionFilter](module-configuration-file.md#distributionfilter标签)、[shortcuts](module-configuration-file.md#shortcuts标签)等信息。只对当前Module、UIAbility、ExtensionAbility生效。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [abilities](module-configuration-file.md#abilities标签) | 标识当前Module中UIAbility的配置信息，只对当前UIAbility生效。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [extensionAbilities](module-configuration-file.md#extensionabilities标签) | 标识当前Module中ExtensionAbility的配置信息，只对当前ExtensionAbility生效。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [requestPermissions](declare-permissions.md#在配置文件中声明权限) | 标识当前应用运行时需向系统申请的权限集合。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [testRunner](module-configuration-file.md#testrunner标签) | 标识用于测试当前Module的测试框架的配置。详情请参考[启动测试框架命令](aa-tool.md#启动测试框架命令test)。 | 对象 | 该标签可缺省，缺省值为空。 |
| [atomicService](module-configuration-file.md#atomicservice标签) | 标识当前应用是元服务时，有关元服务的相关配置。 | 对象 | 该标签可缺省，缺省值为空。 |
| [dependencies](module-configuration-file.md#dependencies标签) | 标识当前模块运行时依赖的共享库列表。 | 对象数组 | 该标签可缺省，缺省值为空。手动配置不生效，由编译构建时自动生成。 |
| targetModuleName | 标识当前包所指定的目标Module。取值为长度不超过128字节的字符串，不支持中文。配置该标签的Module具有overlay特性。仅在动态共享包（HSP）中适用。 | 字符串 | 该标签可缺省，缺省值为空。 |
| targetPriority | 标识当前Module的优先级，取值范围为1~100。配置targetModuleName标签之后，才需要配置该标签。仅在动态共享包（HSP）中适用。 | 整型数值 | 该标签可缺省，缺省值为1。 |
| [proxyData](module-configuration-file.md#proxydata标签) | 标识当前Module提供的数据代理列表。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| isolationMode | 标识当前Module的多进程配置项。支持的取值如下：  - nonisolationFirst：优先在非独立进程中运行。  - isolationFirst：优先在独立进程中运行。  - isolationOnly：只在独立进程中运行。  - nonisolationOnly：只在非独立进程中运行。  **说明：**  1.仅2in1和tablet设备支持将当前Module设置为独立进程。  2.该标签仅对HAP生效。 | 字符串 | 该标签可缺省，缺省值为nonisolationFirst。 |
| generateBuildHash | 标识当前HAP/HSP是否由打包工具生成哈希值。当配置为true时，如果系统OTA升级时应用versionCode保持不变，可根据哈希值判断应用是否需要升级。  该标签仅在[app.json5文件](app-configuration-file.md)中的generateBuildHash标签为false时使能。  **说明：**  该标签仅对预置应用生效。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| compressNativeLibs | 在打包hap时，该标签标识libs库是否以压缩存储的方式打包到HAP。  - true：libs库以压缩方式存储。  - false：libs库以不压缩方式存储。 | 布尔值 | 该标签可缺省，在打包hap时缺省值为false。 |
| extractNativeLibs | 标识应用安装时，libs库是否解压到应用安装目录。当compressNativeLibs和extractNativeLibs都配置为false时，应用以不解压libs库的方式进行安装；其他场景，应用以解压libs库的方式进行安装。  **说明：**  从API version 20开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为true。 |
| libIsolation | 在libs目录下是否生成模块名称目录存储so，用于区分同一应用中不同HAP的.so文件，以防止.so文件冲突。  - true：当前HAP的.so文件会储存在libs目录中以Module名命名的路径下。  - false：当前HAP的.so文件会直接储存在libs目录中。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| [fileContextMenu](module-configuration-file.md#filecontextmenu标签) | 标识当前HAP的右键菜单配置项，是一个profile文件资源。取值为长度不超过255字节的字符串。  **说明：**  仅在PC/2in1设备上生效。  仅允许在entry类型模块中配置。 | 字符串 | 该标签可缺省，缺省值为空。 |
| querySchemes | 标识允许当前应用进行跳转查询的URL schemes，只允许entry类型模块配置，每个字符串取值不超过128字节。  **说明：**  从API version 21开始，最多允许配置200个URL scheme。API version 20及之前的版本，最多允许配置50个URL scheme。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| [routerMap](module-configuration-file.md#routermap标签) | 标识当前模块配置的路由表路径。取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [appEnvironments](module-configuration-file.md#appenvironments标签) | 标识当前模块配置的应用环境变量，只允许entry和feature模块配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| appStartup | 标识当前Module[启动框架](app-startup.md)配置路径，只允许entry类型模块配置。  从API version 18开始，新增支持在HSP、HAR中配置。  从API version 20开始，新增支持在feature类型的Module中配置。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [hnpPackages](module-configuration-file.md#hnppackages标签) | 标识当前应用包含的Native软件包信息。只允许entry类型模块配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [systemTheme](module-configuration-file.md#systemtheme标签) | 标识当前使用的系统主题配置项。只允许entry类型模块配置。取值为不超过255字节的字符串。  **说明：**  从API version 20开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| abilitySrcEntryDelegator | 标识当前Module需要重定向到的UIAbility的名称，与abilityStageSrcEntryDelegator标签组合使用，共同指定重定向的目标对象。  **说明：**  1.从API version 17开始，支持该标签。  2.当UIAbility是通过[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动时，该标签不生效。  3.不支持在HAR的配置文件中配置该标签，也不支持重定向到HAR的UIAbility。 | 字符串 | 该标签可缺省，缺省值为空。 |
| abilityStageSrcEntryDelegator | 标识当前Module需要重定向到的UIAbility对应的Module名称（不可为当前Module名称），与abilitySrcEntryDelegator标签组合使用，共同指定重定向的目标对象。  **说明：**  1.从API version 17开始，支持该标签。  2.当UIAbility是通过[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口启动时，该标签不生效。  3.不支持在HAR的配置文件中配置该标签，也不支持重定向到HAR的UIAbility。 | 字符串 | 该标签可缺省，缺省值为空。 |
| crossAppSharedConfig | 标识应用间共享配置的配置文件名。取值为不超过255字节的字符串。用于发布配置给其他应用读取，在应用安装时生效，应用卸载时失效。详细使用方式见[共享配置使用](share-config.md#配置发布方)。  **说明：**  从API version 20开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| formWidgetModule | 在[独立卡片包](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)中，应用包需要配置该标签，用来关联卡片包。取值为卡片包的模块名称，对应卡片包module.json5中的name标签。具体使用方式请参考[FormExtensionAbility配置](arkts-ui-widget-configuration.md#formextensionability配置)。  **说明：**  1. 从API version 20开始，支持该标签。  2. 仅在独立卡片包的应用包中，该标签配置生效，且要求对应的卡片包模块必须配置formExtensionModule标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| formExtensionModule | 在[独立卡片包](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)中，卡片包需要配置该标签，用来关联应用包。取值为应用包的模块名称，对应应用包module.json5中的name标签。具体使用方式请参考[独立卡片包配置](arkts-ui-widget-configuration.md#独立卡片包配置)。  **说明：**  1. 从API version 20开始，支持该标签。  2. 仅在独立卡片包的卡片包中，该标签配置生效，且要求对应的应用包模块必须配置formWidgetModule标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| shareFiles | 标识应用沙箱中分享目录的配置文件路径，用于为应用文件提供有安全保障的开放范围，保护应用资产。只允许entry类型模块配置，取值为长度不超过255字节的字符串。具体使用方式请参考[应用共享目录配置](share-app-file-configuration.md)。  **说明：**  从API version 23开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| uiSyntax(deprecated) | 标识当前Module syntax定义该JS Component的语法类型。  - hml：标识该JS Component使用hml/css/js进行开发。  - ets：标识该JS Component使用ArkTS声明式语法进行开发。  **说明：**  该标签从API version 9开始废弃。 | 字符串 | 该标签可缺省，缺省值为hml。 |
| srcEntrance(deprecated) | 标识当前Module所对应的代码路径，标签值为字符串（最长为127字节）。  **说明：**  该标签从API version 9开始废弃，请使用srcEntry字段替代。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [requiredDeviceFeatures](module-configuration-file.md#requireddevicefeatures标签) | 标识当前Module运行所需要的特定的设备特性，应用市场可以根据此配置，将应用分发给支持该特性的设备。  **说明：**  1.从API version 19开始，支持该字段。  2.不支持插件应用配置。 | 对象 | 该标签可缺省，缺省值为空。 |
| easyGo | 标识系统提供的一种兼容配置模式的配置文件路径，以满足不同产品的定制能力，当前仅支持平行视界分栏能力。只允许entry类型模块配置，取值为长度不超过255字节的字符串。  **说明：**  从API version 23开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |

## deviceTypes标签

**表2** deviceTypes标签说明

| 设备类型 | 枚举值 | 说明 |
| --- | --- | --- |
| 手机 | phone | - |
| 平板 | tablet | - |
| PC/2in1 | 2in1 | 即PC设备，主要交互方式以多窗口、多任务及键盘鼠标操作为主，充分发挥设备的生产力属性。在HarmonyOS文档中，所有“2in1”均代表“PC/2in1”。 |
| 智慧屏 | tv | - |
| 智能手表 | wearable | 系统能力较丰富的手表，具备电话功能。 |
| 车机 | car | - |
| 默认设备 | default | 配置为default类型的应用，虽然可以正常编译构建，但是不支持发布上架。建议使用phone替代。 |

deviceTypes示例：

```
1. {
2. "module": {
3. "name": "myHapName",
4. "type": "feature",
5. "deviceTypes": [
6. "tv",
7. "tablet"
8. ],
9. // ...
10. }
11. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L15-L169)

## pages标签

该标签是一个profile文件资源，用于指定描述页面信息的配置文件。

```
1. {
2. "module": {
3. // ...
4. "pages": "$profile:main_pages", // 资源配置，指向profile下面定义的配置文件main_pages.json
5. // ...
6. }
7. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L23-L179)

在开发视图的resources/base/profile下面定义配置文件main\_pages.json，其中文件名"main\_pages"可自定义，需要和pages标签指定的信息对应。配置文件中列举了当前应用组件中的页面信息，包含页面的路由信息和显示窗口相关的配置。

**表3** pages标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| src | 标识当前Module中所有页面的路由信息，包括页面路径和页面名称。其中，页面路径是以当前Module的src/main/ets为基准。该标签取值为一个字符串数组，其中每个元素表示一个页面。 | 字符串数组 | 该标签不可缺省。 |
| window | 标识用于定义与显示窗口相关的配置。 | 对象 | 该标签可缺省，缺省值为空。 |

**表4** window标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| designWidth | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。 | 数值 | 可缺省，缺省值为720px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。当配置为false时，设计基准宽度为designWidth。 | 布尔值 | 可缺省，缺省值为false。 |

```
1. {
2. "src": [
3. "pages/Index"
4. ],
5. "window": {
6. "designWidth": 720,
7. "autoDesignWidth": false
8. }
9. }
```

## metadata标签

该标签标识HAP的自定义元信息，标签值为数组类型，包含name、value、resource三个子标签。

**表5** metadata标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识数据项的名称，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| value | 标识数据项的值，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| resource | 标识了用户自定义数据，取值为长度不超过255字节的字符串，内容为该数据的资源索引，例如配置成$profile:shortcuts\_config，表示指向了/resources/base/profile/shortcuts\_config.json配置文件。 | 字符串 | 该标签可缺省，缺省值为空。 |

```
1. {
2. "module": {
3. // ...
4. "metadata": [
5. // ...
6. {
7. "name": "pageConfig",
8. "value": "main page config of application",
9. "resource": "$profile:main_pages" // 资源配置，指向profile下面定义的配置文件main_pages.json
10. }
11. ],
12. // ...
13. }
14. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L17-L185)

## abilities标签

abilities标签描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。

**表6** abilities标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识当前UIAbility组件的名称，确保该名称在整个应用中唯一。取值为长度不超过127字节的字符串，以字母开头，可包含字母、数字、下划线（\_）或点号（.）。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 标识当前UIAbility的代码路径，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| [launchType](uiability-launch-type.md) | 标识当前UIAbility组件的启动模式，支持的取值如下：  - multiton：多实例模式，每次启动创建一个新实例。  - singleton：单实例模式，仅第一次启动创建新实例。  - specified：指定实例模式，运行时由开发者决定是否创建新实例。  - standard：multiton的曾用名，效果与多实例模式一致。  **说明：**  元服务启动模式需要设置为单例模式，详情请参考[元服务规格](atomic-specifications.md)要求。 | 字符串 | 该标签可缺省，该标签缺省为“singleton”。 |
| description | 标识当前UIAbility组件的描述信息，开发者可以通过该标签描述当前组件的功能与作用，取值为长度不超过255字节的字符串。建议采用描述信息的资源索引，以支持多语言。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识当前UIAbility组件的[图标](layered-image.md)，取值为图标资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| label | 标识当前UIAbility组件对用户显示的[名称](layered-image.md)，取值为字符串资源的索引，以支持多语言，长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility组件的权限信息。其他应用访问该UIAbility时，需要申请相应的权限。  一个数组元素为一个权限名称，不超过255字节，取值请参考[应用权限列表](app-permissions.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| [metadata](module-configuration-file.md#metadata标签) | 标识当前UIAbility组件的元信息，典型使用场景详见[窗口元数据配置中的metadata标签](window-config-m.md#metadata标签)。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| exported | 标识当前UIAbility组件是否可以被其他应用拉起。  - true：表示可以被其他应用拉起（入口UIAbility建议配置为true）。  - false：只能由同应用或者具有ohos.permission.START\_INVISIBLE\_ABILITY权限（该权限仅系统应用支持申请）的应用拉起。  例如，配置为false时，桌面具备该权限，桌面图标、快捷方式或push通知消息可以拉起当前UIAbility组件，但aa命令行工具没有权限无法拉起。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| continuable | 标识当前UIAbility组件是否支持跨端迁移。  - true：表示支持迁移。  - false：表示不支持迁移。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| [skills](module-configuration-file.md#skills标签) | 标识当前UIAbility组件能够接收的[Want](want-overview.md)特征集，为数组格式。  配置规则：  - 对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。  - 对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| backgroundModes | 标识当前UIAbility组件的长时任务集合，指定用于满足特定类型的长时任务。  长时任务类型详情参考[长时任务类型表](continuous-task.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| [startWindow](module-configuration-file.md#startwindow标签) | 标识当前UIAbility组件启动页面profile资源，取值为长度不超过255字节的字符串，如果配置了该标签，startWindowIcon和startWindowBackground标签均不生效。  **说明：**  从API version 19开始，支持使用该字段配置增强启动页。 | 字符串 | 该标签可缺省，缺省值为空。 |
| startWindowIcon | 标识当前UIAbility组件启动页面图标资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 该标签不可缺省。 |
| startWindowBackground | 标识当前UIAbility组件启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。  取值示例：$color:red。 | 字符串 | 该标签不可缺省。 |
| removeMissionAfterTerminate | 标识当前UIAbility组件销毁后，是否从任务列表中移除任务。  - true表示销毁后移除任务。  - false表示销毁后不移除任务。  **说明：**  2in1设备和平板设备的自由多窗模式下配置不生效，默认移除任务。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| allowSelfRedirect | 标识应用是否允许通过[App Linking](app-linking-startup.md)跳转自己。  - true表示允许通过App Linking跳转自己。  - false表示不允许通过App Linking跳转自己。  **说明：**  从API version 23开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为true。 |
| orientation | 标识当前UIAbility组件启动时的方向，支持配置枚举，或启动方向资源索引。  **启动方向枚举支持的取值如下：**  - unspecified：未指定方向，由系统自动判断显示方向。  - landscape：横屏。  - portrait：竖屏。  - follow\_recent：跟随背景窗口的旋转模式。  - landscape\_inverted：反向横屏。  - portrait\_inverted：反向竖屏。  - auto\_rotation：随传感器旋转。  - auto\_rotation\_landscape：传感器横屏旋转，包括横屏和反向横屏。  - auto\_rotation\_portrait：传感器竖屏旋转，包括竖屏和反向竖屏。  - auto\_rotation\_restricted：传感器开关打开，方向可随传感器旋转。  - auto\_rotation\_landscape\_restricted：传感器开关打开，方向可随传感器旋转为横屏，包括横屏和反向横屏。  - auto\_rotation\_portrait\_restricted：传感器开关打开，方向可随传感器旋转为竖屏，包括竖屏和反向竖屏。  - locked：传感器开关关闭，方向锁定。  - auto\_rotation\_unspecified：受开关控制和由系统判定的自动旋转模式。  - follow\_desktop：跟随桌面的旋转模式。  **配置启动方向的资源索引时**，取值为长度不超过255字节的字符串，配置示例：$string:orientation。  **说明：**  - 从API version 14开始，支持配置启动方向资源索引。 | 字符串 | 该标签可缺省，缺省值为unspecified。 |
| supportWindowMode | 标识当前UIAbility组件所支持的窗口模式。支持的取值如下：  - fullscreen：全屏模式。  - split：分屏模式。  - floating：悬浮窗模式。  在[自由窗口](window-terminology.md#自由窗口)状态下同时配置fullscreen和split时，如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)小于15，窗口将以悬浮窗模式启动；如果应用的[targetAPIVersion](app-configuration-file.md#配置文件标签)大于等于15，窗口将以全屏模式启动。  此外，还可以通过metadata配置窗口模式，具体的配置规则和优先级请参考[metadata](module-configuration-file.md#metadata标签)。 | 字符串数组 | 该标签可缺省，缺省值为  ["fullscreen", "split", "floating"]。 |
| maxWindowRatio | 标识当前UIAbility组件支持的最大的宽高比。该标签最小取值为0。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的宽高比。 |
| minWindowRatio | 标识当前UIAbility组件支持的最小的宽高比。该标签最小取值为0。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的宽高比。 |
| maxWindowWidth | 标识当前UIAbility组件支持的最大的窗口宽度，宽度单位为vp。  最小取值为minWindowWidth，最大取值为平台支持的最大窗口宽度。窗口尺寸可以参考[窗口大小限制](window-overview.md#约束与限制)。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口宽度。 |
| minWindowWidth | 标识当前UIAbility组件支持的最小的窗口宽度， 宽度单位为vp。  最小取值为平台支持的最小窗口宽度，最大取值为maxWindowWidth。窗口尺寸可以参考[窗口大小限制](window-overview.md#约束与限制)。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口宽度。 |
| maxWindowHeight | 标识当前UIAbility组件支持的最大的窗口高度， 高度单位为vp。  最小取值为minWindowHeight，最大取值为平台支持的最大窗口高度。 窗口尺寸可以参考[窗口大小限制](window-overview.md#约束与限制)。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口高度。 |
| minWindowHeight | 标识当前UIAbility组件支持的最小的窗口高度， 高度单位为vp。  最小取值为平台支持的最小窗口高度，最大取值为maxWindowHeight。窗口尺寸可以参考[窗口大小限制](window-overview.md#约束与限制)。 | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口高度。 |
| excludeFromMissions | 标识当前UIAbility组件是否在最近任务列表中显示。  - true：表示不在任务列表中显示。  - false：表示在任务列表中显示。  **说明：**  三方应用的配置不生效，当前配置仅在系统应用中有效，若要使系统应用配置生效，需申请应用特权，特权申请不对三方应用开放。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| recoverable | 标识当前UIAbility组件是否支持在检测到应用故障后，恢复到应用原界面。  - true：支持检测到出现故障后，恢复到原界面。  - false：不支持检测到出现故障后，恢复到原界面。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| isolationProcess | 标识组件能否运行在独立的进程中。  - true：表示能运行在独立的进程中。  - false：表示不能运行在独立的进程中。  **说明：**  仅2in1和tablet设备支持将UIAbility设置为独立进程。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| excludeFromDock | 标识当前UIAbility组件是否支持从dock区域隐藏图标。  - true：表示在dock区域隐藏。  - false：表示不能在dock区域隐藏。  **说明：**  该标签配置不生效。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| preferMultiWindowOrientation | 标识当前UIAbility组件多窗布局方向：  - default：缺省值，参数不配置默认值，建议其他应用类配置。  - portrait：多窗布局方向为竖向，建议竖向游戏类应用配置。  - landscape：多窗布局方向为横向，配置后支持横屏悬浮窗和上下分屏，建议横向游戏类应用配置。  - landscape\_auto：多窗布局动态可变为横向，需要配合API enableLandScapeMultiWindow/disableLandScapeMultiWindow使用，建议视频类应用配置。 | 字符串 | 该标签可缺省，缺省值为default。 |
| continueType | 标识当前UIAbility组件的跨端迁移类型。 | 字符串数组 | 该标签可缺省，缺省值为当前组件的名称。 |
| continueBundleName | 标识当前应用支持跨端迁移的其它应用名称列表。  **说明：**  不能配置为本应用包名，仅为了做异包名迁移使用。  从API version 13开始，支持该标签。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| process | 标识组件的进程名称。具体使用方式参考[进程模型定义](process-model-stage.md#其他进程类型)中的"静态指定进程"。  **说明：**  1. 仅在[PC/2in1](module-configuration-file.md#devicetypes标签)和[Tablet](module-configuration-file.md#devicetypes标签)设备上生效。  2. UIAbility组件和type为embeddedUI的ExtensionAbility组件标签一致时运行在同一个进程中。  3. 从API version 14开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |

abilities示例：

```
1. {
2. // ...
3. "abilities": [
4. {
5. "name": "EntryAbility",
6. "srcEntry": "./ets/entryability/EntryAbility.ets",
7. "launchType": "singleton",
8. "description": "$string:description_main_ability",
9. "icon": "$media:layered_image",
10. "label": "$string:EntryAbility_label",
11. "permissions": [],
12. "metadata": [],
13. "exported": true,
14. "continuable": true,
15. "skills": [
16. {
17. "actions": [
18. "ohos.want.action.home"
19. ],
20. "entities": [
21. "entity.system.home"
22. ],
23. "uris": []
24. }
25. ],
26. "backgroundModes": [
27. "dataTransfer"
28. ],
29. "startWindowIcon": "$media:icon",
30. "startWindowBackground": "$color:red",
31. "removeMissionAfterTerminate": true,
32. "allowSelfRedirect": true,  // 从API version 23开始，支持该标签
33. "orientation": "$string:orientation",
34. "supportWindowMode": [
35. "fullscreen",
36. "split",
37. "floating"
38. ],
39. "maxWindowRatio": 3.5,
40. "minWindowRatio": 0.5,
41. "maxWindowWidth": 2560,
42. "minWindowWidth": 1400,
43. "maxWindowHeight": 300,
44. "minWindowHeight": 200,
45. "excludeFromMissions": false,
46. "preferMultiWindowOrientation": "default",
47. "isolationProcess": false,
48. "continueType": [
49. "continueType1",
50. "continueType2"
51. ],
52. "continueBundleName": [
53. "com.example.myapplication1",
54. "com.example.myapplication2"
55. ],
56. "process": ":processTag"
57. }
58. ],
59. // ...
60. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L16-L168)

## skills标签

该标签标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](want-overview.md)的特征。

例如：在浏览器中下载PDF文件时，可以通过配置skills标签选择并打开该PDF文件。详情请参考[拉起文件处理类应用](file-processing-apps-startup.md)。

**表7** skills标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| actions | 标识能够接收的Action值集合，取值通常为系统预定义的action值，也允许自定义。  一个skill中不建议配置多个action，否则可能导致无法匹配预期场景。详情请参考[常见action与entities](actions-entities.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| entities | 标识能够接收的Entity值的集合。  一个skill中不建议配置多个entity，否则可能导致无法匹配预期场景。详情请参考[常见action与entities](actions-entities.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| uris | 标识与Want中URI（Uniform Resource Identifier）相匹配的集合。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility或ExtensionAbility组件的权限信息。其他应用访问该组件时，需要申请相应的权限。  一个数组元素为一个权限名称，不超过255字节，取值请参考[应用权限列表](app-permissions.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| domainVerify | 标识是否开启[域名校验](app-linking-startup.md#section4452103365213)。  - true：表示开启域名校验。  - false：表示不开启域名校验。 | 布尔值 | 该标签可缺省，缺省值为false。 |

**表8** uris标签说明

说明

以下字符串类型的标签不支持使用资源索引的方式（$string）配置。

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| scheme | 标识URI的协议名部分，常见的有http、https、file、ftp等。  **说明：**  从API 18开始，该标签在参与隐式Want匹配时不区分大小写。 | 字符串 | uris中仅配置type时可以缺省，缺省值为空，否则不可缺省。 |
| host | 标识URI的主机地址部分，该标签只有当scheme配置时才生效。常见的方式：  - 域名方式，如example.com。  - IP地址方式，如10.10.10.1。  **说明：**  从API 18开始，该标签在参与隐式Want匹配时不区分大小写。 | 字符串 | 该标签可缺省，缺省值为空。 |
| port | 标识URI的端口部分。如http默认端口为80，https默认端口是443，ftp默认端口是21。该标签只有当scheme和host都配置时才生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| path | pathStartWith | pathRegex | 标识URI的路径部分，path、pathStartWith和pathRegex配置时三选一。path标识URI与want中的路径部分全匹配，pathStartWith标识URI与want中的路径部分允许前缀匹配，pathRegex标识URI与want中的路径部分允许正则匹配。该标签只有当scheme和host都配置时才生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| type | 标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范和[UniformDataType](../harmonyos-references/js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型规范。可以与scheme同时配置，也可以单独配置。 | 字符串 | 该标签可缺省，缺省值为空。 |
| utd | 标识与Want相匹配的[标准化数据类型](../harmonyos-references/js-apis-data-uniformtypedescriptor.md)，适用于分享等场景。 | 字符串 | 该标签可缺省，缺省值为空。 |
| maxFileSupported | 对于指定类型的文件，标识一次能接收或打开的最大数量，适用于分享等场景，需要与utd配合使用。 | 整数 | 该标签可缺省，缺省值为0。 |
| linkFeature | 标识URI提供的功能类型（如文件打开、分享、导航等），用于实现应用间跳转。取值为长度不超过127字节的字符串，不支持中文。同一Bundle中声明的linkFeature数量不能超过150个。详情见[linkFeature标签说明](app-uri-config.md#linkfeature标签说明)。 | 字符串 | 该标签可缺省，缺省值为空。 |

skills示例：

说明

如下示例为通用配置，部分组件和模块在实际配置时存在差异，例如[点击消息进入应用首页](push-send-alert.md#section697519219136)的限制，具体请参考对应文档说明。

```
1. {
2. // ...
3. "abilities": [
4. {
5. // ...
6. "skills": [
7. {
8. "actions": [
9. "ohos.want.action.home"
10. ],
11. "entities": [
12. "entity.system.home"
13. ],
14. "uris": [
15. {
16. "scheme":"http",
17. "host":"example.com",
18. "port":"80",
19. "path":"path",
20. "type": "text/*",
21. "linkFeature": "Login"
22. }
23. ],
24. "permissions": [],
25. "domainVerify": false
26. },
27. // ...
28. ],
29. // ...
30. }
31. ],
32. // ...
33. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L18-L184)

## extensionAbilities标签

描述extensionAbilities的配置信息，标签值为数组类型，该标签下的配置只对当前extensionAbilities生效。

**表9** extensionAbilities标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识当前ExtensionAbility组件的名称，确保该名称在整个应用中唯一，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| srcEntry | 标识当前ExtensionAbility组件所对应的代码路径，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| description | 标识当前ExtensionAbility组件的描述，开发者可以通过该标签描述当前组件的功能与作用，取值为长度不超过255字节的字符串，可以是对描述内容的资源索引，用于支持多语言。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识当前ExtensionAbility组件的图标，取值为资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| label | 标识当前ExtensionAbility组件对用户显示的名称，取值为该名称的资源索引，以支持多语言，字符串长度不超过255字节。 | 字符串 | 该标签可缺省，缺省值为空。 |
| type | 标识当前ExtensionAbility组件的类型，支持的取值如下：  - form：卡片的ExtensionAbility。  - workScheduler：延时任务的ExtensionAbility。  - inputMethod：输入法的ExtensionAbility。  - share：提供内容分享处理功能的[ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md)。  - service：后台运行的service组件，三方配置无法安装应用，需要申请特权，特权申请不对三方应用开放。  - accessibility：辅助能力的ExtensionAbility。  - fileAccess：公共数据访问的ExtensionAbility，允许应用程序提供文件和文件夹给文件管理类应用展示，三方应用配置不生效，当前配置仅在系统应用中有效。  - dataShare：数据共享的ExtensionAbility，三方配置无法安装应用，需要申请特权，特权申请不对三方应用开放。  - staticSubscriber：静态广播的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - fileShare：文件共享的ExtensionAbility。  - vpn：为开发者[提供VPN能力](../harmonyos-references/js-apis-vpnextensionability.md)的ExtensionAbility。  - wallpaper：壁纸的ExtensionAbility。  - backup：数据备份的ExtensionAbility。  - enterpriseAdmin：[企业设备管理](mdm-kit-admin.md)的ExtensionAbility。企业设备管理应用必须拥有此类型的ExtensionAbility。  - window：该ExtensionAbility会在启动过程中创建一个window，为开发者提供界面开发。开发者开发出来的界面将通过UIExtensionComponent控件组合到其他应用的窗口中，三方应用配置不生效，当前配置仅在系统应用中有效。  - thumbnail：获取文件缩略图的ExtensionAbility，开发者可以对自定义文件类型的文件提供缩略。  - preview：该ExtensionAbility会将文件解析后在一个窗口中显示，开发者可以通过将此窗口组合到其他应用窗口中。  - print：打印框架的ExtensionAbility。  - push：推送的ExtensionAbility。  - driver：驱动框架的ExtensionAbility。应用配置了driver类型的ExtensionAbility后会被视为驱动应用，驱动应用在安装、卸载和恢复时不会区分用户，且创建新用户时也会安装设备上已有的驱动应用。例如，创建子用户时会默认安装主用户已有的驱动应用，在子用户上卸载驱动应用时，主用户上对应的驱动应用也会同时被卸载。  - remoteNotification：远程通知的ExtensionAbility。  - remoteLocation：远程定位的ExtensionAbility。  - voip：网络音视频通话的ExtensionAbility。  - action：自定义操作业务模板的ExtensionAbility，为开发者提供基于UIExtension的自定义操作业务模板。  - adsService：广告业务的ExtensionAbility，提供广告业务框架，三方应用配置不生效，当前配置仅在系统应用中有效。  - embeddedCashier：支付业务的ExtensionAbility，与CashierComponent控件组合使用，将支付页面展示到其他应用中。从API version 23开始，支持该标签。三方应用配置不生效，当前配置仅在系统应用中有效，仅支持TV设备使用，其他设备配置不生效。  - embeddedUI：嵌入式UI扩展能力，提供跨进程界面嵌入的能力。  - insightIntentUI：为开发者提供能被小艺意图调用，以窗口形态呈现内容的扩展能力。  - ads：广告业务的ExtensionAbility，与AdComponent控件组合使用，将广告页面展示到其他应用中。仅支持设备厂商使用。  - photoEditor：图片编辑业务的ExtensionAbility，为开发者提供基于UIExtension的图片编辑业务模版。  - appAccountAuthorization：应用账号授权扩展能力的ExtensionAbility，用于处理账号授权请求，比如账号登录授权。  - autoFill/password：用于账号和密码自动填充业务的ExtensionAbility，支持数据的保存、填充能力。  - hms/account：应用账号管理能力的ExtensionAbility。  - sysDialog/atomicServicePanel：提供构建元服务服务面板的基础能力的ExtensionAbility，使用时基于UIExtensionAbility实现，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/userAuth：本地用户鉴权的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/common：通用弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/power：关机重启弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/print：打印模态弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/meetimeCall：畅连通话的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/meetimeContact：畅连联系人的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysDialog/meetimeMessage：畅连消息的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/meetimeContact：畅连联系人列表的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/meetimeCallLog：畅连通话记录列表的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/share：系统分享的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/mediaControl：投播组件的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/photoPicker：三方应用通过对应的UIExtensionType拉起图库picker界面，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/filePicker：文件下载弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/audioPicker：音频管理弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/photoEditor：图片编辑弹窗的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sys/commonUI：非通用的ExtensionAbility，提供业务属性强相关的嵌入式显示或弹框，三方应用配置不生效，当前配置仅在系统应用中有效。  - autoFill/smart：用于情景化场景自动填充业务的ExtensionAbility，支持数据的保存、填充能力。  - uiService：弹窗服务组件，在启动过程中会创建window，并支持双向通信，三方应用配置不生效，当前配置仅在系统应用中有效。  - statusBarView：[状态栏开放服务](statusbar-extension-introduction.md)的ExtensionAbility。  - liveViewLockScreen：[实况窗锁屏沉浸态](../harmonyos-references/liveview-lock-screen-ability.md)的ExtensionAbility。  - accountLogout：华为账号登出能力的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/navigation：拉起系统导航类应用面板的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sysPicker/appSelector：拉起系统应用选择弹框的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - sys/visualExtension : 原生智能图片类控件视觉搜索的ExtensionAbility，三方应用配置不生效，当前配置仅在系统应用中有效。  - screenTimeGuard：[屏幕时间守护开放服务](../harmonyos-references/screentimeguard-timeguardextensionability.md)的ExtensionAbility。 从API version 20开始，支持该配置。  - recentPhoto：最近照片推荐的ExtensionAbility。  - fence：地理围栏的ExtensionAbility。  - callerInfoQuery：企业联系人查询的ExtensionAbility。  - assetAcceleration：资源预下载的ExtensionAbility。  - formEdit：卡片编辑的ExtensionAbility。  - distributed：分布式扩展的ExtensionAbility。  - liveForm：互动卡片的[ExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md)。从API version 20开始，支持该标签。  - appService：为应用提供后台服务相关扩展能力[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)，包括后台服务的创建、销毁、连接、断开等生命周期回调。从API version 20开始，支持该标签。  - webNativeMessaging：为开发者提供Web原生消息通信能力的[ExtensionAbility](../harmonyos-references/arkts-apis-web-webnativemessagingextensionability.md)。从API version 21开始，支持该标签。  - faultLog：故障延迟通知的[ExtensionAbility](../harmonyos-references/js-apis-hiviewdfx-faultlogextensionability.md)。从API version 21开始，支持该标签。  - notificationSubscriber：提供通知订阅相关功能的[ExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)。从API version 22开始，支持该标签。  - crypto：外部密钥管理扩展的[ExtensionAbility](huks-extension-ability-support-dev.md)。从API version 22开始，支持该标签。  - partnerAgent：基于蓝牙通信技术，提供设备发现与设备下线的通知功能的[ExtensionAbility](../harmonyos-references/is-fusionconnectivity-partneragentextensionability.md)。从API version 23开始，支持该标签。  - contentEmbed：对象插入编辑框架的ExtensionAbility。从API version 23 开始，支持该标签。  - selection：划词扩展的ExtensionAbility。从API version 20开始，仅支持系统应用配置，三方应用配置不生效。  - awc/webpage：通用网页浏览的ExtensionAbility。  - awc/newsfeed：信息流资讯业务的ExtensionAbility。 | 字符串 | 该标签不可缺省。 |
| permissions | 标识当前ExtensionAbility组件的权限信息。当其他应用访问该ExtensionAbility时，需要申请相应的权限。  一个数组元素为一个权限名称。不超过255字节，取值请参考[应用权限列表](app-permissions.md)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| appIdentifierAllowList | 标识允许启动此ExtensionAbility的应用程序列表。  一个数组元素为一个应用程序的appIdentifier，appIdentifier信息可参考[什么是appIdentifier](common-problem-of-application.md#什么是appidentifier)。  **说明：**  仅当ExtensionAbility组件的type为appService时支持配置该标签。  从API version 20开始，支持该标签。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| readPermission | 标识读取当前ExtensionAbility组件数据所需的权限，取值为长度不超过255字节的字符串。仅当预置的系统应用ExtensionAbility的type配置为dataShare时，该标签生效。dataShare类型仅支持系统应用支持配置，三方应用配置不生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| writePermission | 标识向当前ExtensionAbility组件写数据所需的权限，取值为长度不超过255字节的字符串。仅当预置的系统应用ExtensionAbility的type配置为dataShare时，该标签生效。dataShare类型仅支持系统应用支持配置，三方应用配置不生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| uri | 标识当前ExtensionAbility组件提供的数据URI，取值为长度不超过255字节的字符数组，用反向域名的格式表示。  **说明：**  该标签在type为dataShare类型的ExtensionAbility时，不可缺省。 | 字符串 | 该标签可缺省，缺省值为空。 |
| skills | 标识当前ExtensionAbility组件能够接收的[Want](want-overview.md)的特征集。  配置规则：entry包可以配置多个具有入口能力的skills标签（配置了ohos.want.action.home和entity.system.home）的ExtensionAbility，其中第一个配置了skills标签的ExtensionAbility中的label和icon作为服务或应用的label和icon。  **说明：**  服务的Feature包不支持配置具有入口能力的skills标签。  应用的Feature包支持配置具有入口能力的skills标签。 | 数组 | 该标签可缺省，缺省值为空。 |
| [metadata](module-configuration-file.md#metadata标签) | 标识当前ExtensionAbility组件的元信息。  **说明：**  该标签在type为form时，不可缺省，且必须存在一个name为ohos.extension.form的对象值，其对应的resource值不能缺省，为服务卡片的二级资源引用。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| exported | 标识当前ExtensionAbility组件是否可以被其他应用调用。  - true：表示可以被其他应用调用。  - false：表示不可以被其他应用调用，包括无法被aa工具命令拉起应用。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| extensionProcessMode | 标识当前ExtensionAbility组件的多进程实例模型,当前只对UIExtensionAbility以及从UIExtensionAbility扩展的ExtensionAbility生效。  - instance：表示该ExtensionAbility每个实例一个进程。  - type：表示该ExtensionAbility实例都运行在同一个进程里，与其他ExtensionAbility分离进程。  - bundle：表示该ExtensionAbility实例都运行在应用统一进程里，与其他配置了bundle模型的ExtensionAbility共进程。  - runWithMainProcess：表示该ExtensionAbility和应用主进程共进程，只有[状态栏开放服务](statusbar-extension-introduction.md)的ExtensionAbility可以配置runWithMainProcess。 | 字符串 | 该标签可缺省，缺省值为空。 |
| dataGroupIds | 标识当前ExtensionAbility组件的dataGroupId集合。如果当前ExtensionAbility组件所在的应用在应用市场申请的证书里groupIds也申请了某个dataGroupId，那么当前ExtensionAbility组件可以和应用共享这一个dataGroupId生成的目录，所以ExtensionAbility组件的dataGroupId需要是应用的签名证书中groupIds标签里配置的才能生效。 且该标签仅在当前ExtensionAbility组件存在独立的沙箱目录时生效。详见[dataGroupId申请流程](ime-kit-security.md#section4219152220459)。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| process | 标识组件的进程名称，只有type为embeddedUI时可以配置该标签。具体使用方式参考[进程模型定义](process-model-stage.md#其他进程类型)中的"静态指定进程"。  **说明：**  1. 仅在[PC/2in1](module-configuration-file.md#devicetypes标签)和[Tablet](module-configuration-file.md#devicetypes标签)设备上生效。  2. UIAbility组件和ExtensionAbility组件标签一致时运行在同一个进程中。  3. 从API version 14开始，支持该标签。 | 字符串 | 该标签可缺省，缺省值为空。 |
| isolationProcess | 标识ExtensionAbility组件能否运行在独立的进程中。  - true：表示能运行在独立的进程中。  - false：表示不能运行在独立的进程中。  **说明：**  仅当ExtensionAbility组件的type为"sys/commonUI"时该标签配置生效，且仅支持由系统应用配置type为"sys/commonUI"。  从API version 20开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为false。 |

extensionAbilities示例：

```
1. {
2. // ...
3. "extensionAbilities": [
4. {
5. "name": "FormName",
6. "srcEntry": "./ets/form/MyForm.ets",
7. "icon": "$media:icon",
8. "label" : "$string:extension_name",
9. "description": "$string:form_description",
10. "type": "form",
11. "permissions": ["ohos.permission.ACCESS_BLUETOOTH"],
12. "exported": true,
13. "uri":"scheme://authority/path/query",
14. "skills": [{
15. "actions": [],
16. "entities": [],
17. "uris": [],
18. "permissions": []
19. }],
20. "metadata": [
21. {
22. "name": "ohos.extension.form",
23. "resource": "$profile:form_config",
24. }
25. ],
26. "extensionProcessMode": "instance",
27. "dataGroupIds": [
28. "testGroupId1"
29. ]
30. }
31. ],
32. // ...
33. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L17-L167)

## shortcuts标签

shortcuts标识应用的快捷方式信息。标签值为数组，包含四个子标签shortcutId、label、icon、wants。

[metadata](module-configuration-file.md#metadata标签)中指定shortcut信息，其中：

* name：指定shortcuts的名称，使用ohos.ability.shortcuts作为shortcuts信息的标识。
* resource：指定shortcuts信息的资源位置。

说明

桌面展示快捷方式的数量有上限要求，最多展示4个。

**表10** shortcuts标签说明

| 属性名称 | 含义 | 类型 | 是否可缺省 |
| --- | --- | --- | --- |
| shortcutId | 标识快捷方式的ID，取值为长度不超过63字节的字符串。**不支持通过资源索引的方式（$string）配置该标签。** | 字符串 | 该标签不可缺省。 |
| label | 标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值为长度不超过255字节的字符串，可以是描述性内容，也可以是标识label的资源索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识快捷方式的图标，取值为资源文件的索引。  **说明：**  图标分为单层图标和分层图标，单层图标包含一个图片，分层图标包含前景图和背景图，推荐使用如下配置的分层图标：  1.前景图：图标显示大小为450\*450px，资源大小为1024\*1024px的透明图层。  2.背景图：大小为1024\*1024px。 | 字符串 | 该标签可缺省，缺省值为空。 |
| visible | 标识快捷方式是否显示，取值为true时显示快捷方式，取值为false时不显示快捷方式。  **说明：**  1.从API version 20开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省为true。 |
| [wants](module-configuration-file.md#wants标签) | 标识快捷方式内定义的目标wants信息集合，在调用launcherBundleManager的startShortcut接口时，会拉起wants标签里的第一个目标组件，推荐只配置一个wants元素。 | 对象 | 该标签可缺省，缺省为空。 |

1. 在/resources/base/profile/目录下配置shortcuts\_config.json配置文件。

   ```
   1. {
   2. "shortcuts": [
   3. {
   4. "shortcutId": "id_test1",
   5. "label": "$string:shortcut",
   6. "icon": "$media:aa_icon",
   7. "visible": true,
   8. "wants": [
   9. {
   10. "bundleName": "com.ohos.hello",
   11. "moduleName": "entry",
   12. "abilityName": "EntryAbility",
   13. "parameters": {
   14. "testKey": "testValue"
   15. }
   16. }
   17. ]
   18. }
   19. ]
   20. }
   ```
2. 在module.json5配置文件的abilities标签中，针对需要添加快捷方式的UIAbility进行配置metadata标签，使shortcut配置文件对该UIAbility生效。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. "name": "EntryAbility",
   7. "srcEntry": "./ets/entryability/EntryAbility.ets",
   8. // ...
   9. "skills": [
   10. // ...
   11. {
   12. "entities": [
   13. "entity.system.home"
   14. ],
   15. "actions": [
   16. "ohos.want.action.home"
   17. ]
   18. }
   19. ],
   20. "metadata": [
   21. {
   22. "name": "ohos.ability.shortcuts",
   23. "resource": "$profile:shortcuts_config"
   24. }
   25. ],
   26. // ...
   27. }
   28. ],
   29. // ...
   30. }
   31. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L22-L180)

### wants标签

此标签用于标识快捷方式内定义的目标wants信息集合。

**表11** wants标签说明

| 属性名称 | 含义 | 类型 | 是否可缺省 |
| --- | --- | --- | --- |
| bundleName | 表示快捷方式的目标包名。 | 字符串 | 该标签可缺省。 |
| moduleName | 表示快捷方式的目标模块名。 | 字符串 | 该标签可缺省。 |
| abilityName | 表示快捷方式的目标组件名。 | 字符串 | 该标签可缺省。 |
| parameters | 表示拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。 | 对象 | 该标签可缺省。 |

wants标签示例：

```
1. {
2. "wants": [
3. {
4. "bundleName": "com.ohos.hello",
5. "moduleName": "entry",
6. "abilityName": "EntryAbility",
7. "parameters": {
8. "testKey": "testValue"
9. }
10. }
11. ]
12. }
```

## distributionFilter标签

该标签用于定义HAP对应的细分设备规格的分发策略，以便在应用市场进行云端分发应用包时做精准匹配。

说明

该标签从API version 10及以后版本开始生效，API version 9及以前版本使用distroFilter标签。

* **适用场景：** 当一个工程中存在多个Entry，且多个Entry配置的deviceTypes存在交集时，则需要通过该标签进行区分。比如下面的两个Entry都支持tablet类型，就需要通过该标签进行区分。

  ```
  1. // entry1支持的设备类型
  2. {
  3. "module": {
  4. "name": "entry1",
  5. "type": "entry",
  6. "deviceTypes": [
  7. "tv",
  8. "tablet"
  9. ],
  10. // ...
  11. }
  12. }
  ```

  [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile03/entry1/src/main/module.json5#L16-L83)

  ```
  1. // entry2支持的设备类型
  2. {
  3. "module": {
  4. "name": "entry2",
  5. "type": "entry",
  6. "deviceTypes": [
  7. "tv",
  8. "tablet"
  9. ],
  10. // ...
  11. }
  12. }
  ```

  [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile02/entry2/src/main/module.json5#L16-L71)
* **配置规则：** 该标签支持配置四个属性，包括屏幕形状([screenShape](module-configuration-file.md#screenshape标签))、窗口分辨率([screenWindow](module-configuration-file.md#screenwindow标签))、屏幕像素密度([screenDensity](module-configuration-file.md#screendensity标签) )、设备所在国家与地区([countryCode](module-configuration-file.md#countrycode标签))。详见下表。

  在分发应用包时，通过deviceTypes与这四个属性的匹配关系，唯一确定一个用于分发到设备的HAP。

  + 如果需要配置该标签，则至少包含一个属性。
  + 如果一个Entry中配置了任意一个或多个属性，则其他Entry也必须包含相同的属性。
  + screenShape和screenWindow属性仅适用于轻量级智能穿戴设备。
* **配置方式：** 该标签需要配置在/resources/base/profile资源目录下，并在metadata的resource标签中引用。

**表12** distributionFilter标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| [screenShape](module-configuration-file.md#screenshape标签) | 标识屏幕形状的支持策略。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [screenWindow](module-configuration-file.md#screenwindow标签) | 标识应用运行时的窗口分辨率的支持策略。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [screenDensity](module-configuration-file.md#screendensity标签) | 标识屏幕的像素密度（dpi：Dot Per Inch）的支持策略。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| [countryCode](module-configuration-file.md#countrycode标签) | 标识国家与地区的支持策略，取值参考ISO-3166-1标准。支持多个国家和地区枚举定义。 | 对象数组 | 该标签可缺省，缺省值为空。 |

### screenShape标签

**表13** screenShape标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| policy | 标识条件属性的过滤规则。  - exclude：表示需要排除的value属性。  - include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 支持的取值为circle（圆形）、rect（矩形）。例如，针对智能穿戴设备，可为圆形表盘和矩形表盘分别提供不同的HAP。 | 字符串数组 | 该标签不可缺省。 |

### screenWindow标签

**表14** screenWindow标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| policy | 标识条件属性的过滤规则。当前取值仅支持“include”。  - include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 单个字符串的取值格式为“宽 \* 高”，取值为整数像素值，例如“454 \* 454”。 | 字符串数组 | 该标签不可缺省。 |

### screenDensity标签

**表15** screenDensity标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| policy | 标识条件属性的过滤规则。  - exclude：表示需要排除的value属性。  - include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 标识屏幕的像素密度（dpi :Dot Per Inch）。支持的取值如下：  - sdpi：表示小规模的屏幕密度（Small-scale Dots per Inch），适用于dpi取值为(0,120]的设备。  - mdpi：表示中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120,160]的设备。  - ldpi：表示大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160,240]的设备。  - xldpi：表示大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240,320]的设备。  - xxldpi：表示大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320，480]的设备。  - xxxldpi：表示大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。 | 字符串数组 | 该标签不可缺省。 |

### countryCode标签

**表16** countryCode标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| policy | 标识条件属性的过滤规则。  - exclude：表示需要排除的value属性。  - include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 标识应用需要分发的国家地区码。 | 字符串数组 | 该标签不可缺省。 |

示例如下：

1. 在开发视图的resources/base/profile下定义配置文件，文件名为distributionFilter\_config.json，文件名可以自定义。

   ```
   1. {
   2. "distributionFilter": {
   3. "screenShape": {
   4. "policy": "include",
   5. "value": [
   6. "circle",
   7. "rect"
   8. ]
   9. },
   10. "screenWindow": {
   11. "policy": "include",
   12. "value": [
   13. "454*454",
   14. "466*466"
   15. ]
   16. },
   17. "screenDensity": {
   18. "policy": "exclude",
   19. "value": [
   20. "ldpi",
   21. "xldpi"
   22. ]
   23. },
   24. "countryCode": {
   25. "policy": "include",
   26. "value": [
   27. "CN"
   28. ]
   29. }
   30. }
   31. }
   ```
2. 在module.json5配置文件的module标签中定义metadata信息。

```
1. {
2. "module": {
3. // ...
4. "metadata": [
5. {
6. "name": "ohos.module.distribution",
7. "resource": "$profile:distributionFilter_config"
8. }
9. ],
10. // ...
11. }
12. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile03/entry1/src/main/module.json5#L18-L82)

## testRunner标签

此标签用于支持对测试框架的配置。

**表17** testRunner标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识测试框架对象名称，取值为长度不超过255字节的字符串。 | 字符串 | 不可缺省。 |
| srcPath | 标识测试框架代码路径，取值为长度不超过255字节的字符串。 | 字符串 | 不可缺省。 |

testRunner标签示例：

```
1. {
2. "module": {
3. // ...
4. "testRunner": {
5. "name": "myTestRunnerName",
6. "srcPath": "etc/test/TestRunner.ts"
7. },
8. // ...
9. }
10. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L20-L164)

## atomicService标签

此标签用于支持对元服务的配置。此标签仅在app.json5中将bundleType设置为atomicService时生效。

**表18** atomicService标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| preloads | 标识元服务中预加载列表。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| resizeable | 标识元服务是否支持自适应窗口大小显示。当标签配置成true时，平板横屏模式切换或者折叠屏展开关闭，会自适应屏幕窗口的宽高，使得屏幕显示正常。  **说明：**  1.从API version 20开始，支持该标签。  2.如果已经适配了平板横屏及折叠屏展开态显示，建议将该标签设置为true。  - true：表示元服务可以自适应窗口大小。  - false：表示元服务不可以自适应窗口大小。 | 布尔值 | 可缺省，缺省值为false。 |

**表19** preloads标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| moduleName | 标识元服务中当前模块被加载时，需预加载的模块名。不能配置自身modulename，且必须有对应的模块，取值为长度不超过31字节的字符串。 | 字符串 | 该标签不可缺省。 |

atomicService标签示例：

```
1. {
2. "module": {
3. // ...
4. "atomicService": {
5. "preloads":[
6. {
7. "moduleName":"feature"
8. }
9. ],
10. "resizeable": true
11. },
12. // ...
13. }
14. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile04/entry/src/main/module.json5#L16-L67)

## dependencies标签

此标签标识模块运行时依赖的共享库列表。

**表20** dependencies标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| bundleName | 标识当前模块依赖的共享包包名。取值为长度7~128字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| moduleName | 标识当前模块依赖的共享包模块名。取值为长度不超过31字节的字符串。 | 字符串 | 该标签不可缺省。 |
| versionCode | 标识当前模块依赖的共享包的版本号。取值范围为0~2147483647。 | 数值 | 该标签可缺省，缺省值为空。 |

dependencies标签示例：

```
1. {
2. "module": {
3. // ...
4. "dependencies": [
5. {
6. "bundleName":"com.share.library",
7. "moduleName": "library",
8. "versionCode": 10001
9. }
10. ],
11. // ...
12. }
13. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L19-L165)

## proxyData标签

此标签标识模块提供的数据代理列表，仅限entry和feature配置。

**表21** proxyData标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| uri | 标识用于访问该数据代理的URI，不同的数据代理配置的URI不可重复，且需要满足datashareproxy://当前应用包名/xxx的格式。取值为长度不超过255字节的字符串。 | 字符串 | 该标签不可缺省。 |
| requiredReadPermission | 标识从该数据代理中读取数据所需要的权限。若不配置，则其他应用无法使用该代理。非系统应用配置的权限的等级需为system\_basic或system\_core，系统应用配置的权限的等级没有限制。权限等级可以参考[权限列表](app-permissions.md)。取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| requiredWritePermission | 标识向该数据代理中写入数据所需要的权限。若不配置，则其他应用无法使用该代理。非系统应用配置的权限的等级需为system\_basic或system\_core，系统应用配置的权限的等级没有限制。权限等级可以参考[权限列表](app-permissions.md)。取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [metadata](module-configuration-file.md#metadata标签) | 标识该数据代理的元信息，只支持配置name和resource标签。 | 对象 | 该标签可缺省，缺省值为空。 |

proxyData标签示例：

```
1. {
2. "module": {
3. // ...
4. "proxyData": [
5. {
6. "uri":"datashareproxy://ohos.app.hap.myapplication/event/Meeting",
7. "requiredReadPermission": "ohos.permission.SYSTEM_FLOAT_WINDOW",
8. "requiredWritePermission": "ohos.permission.SYSTEM_FLOAT_WINDOW",
9. "metadata": {
10. "name": "datashare_metadata",
11. "resource": "$profile:datashare"
12. }
13. }
14. ],
15. // ...
16. }
17. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/myHapName/src/main/module.json5#L18-L166)

## routerMap标签

此标签标识模块配置的路由表的路径。

routerMap配置文件描述模块的路由表信息，routerMap标签的值为数组类型。

**表22** routerMap标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识跳转页面的名称。取值为长度不超过1023字节的字符串。 | 字符串 | 该标签不可缺省。 |
| pageSourceFile | 标识页面在模块内的路径。取值为长度不超过255字节的字符串。 | 字符串 | 该标签不可缺省。 |
| buildFunction | 标识被@Builder修饰的函数，该函数描述页面的UI。取值为长度不超过1023字节的字符串。 | 字符串 | 该标签不可缺省。 |
| [data](module-configuration-file.md#data标签) | 标识字符串类型的自定义数据，开发者自行扩展能力，可以通过[HapModuleInfo对象](../harmonyos-references/js-apis-bundlemanager-hapmoduleinfo.md)中routerMap集合对象下的data获取标签内容，该标签已由系统解析，无需开发者自行解析。 每个自定义数据字符串取值不超过128字节。 | 对象 | 该标签可缺省，缺省值为空。 |
| [customData](module-configuration-file.md#customdata标签) | 标识任意类型的自定义数据，开发者自行扩展能力，可以通过[HapModuleInfo对象](../harmonyos-references/js-apis-bundlemanager-hapmoduleinfo.md)中routerMap集合对象下的customData获取标签内容，开发者需要调用JSON.parse函数解析出具体内容。总长度不超过4096字节。 | 对象 | 该标签可缺省，缺省值为空。 |

示例如下：

1. 在开发视图的resources/base/profile下面定义配置文件，文件名可以自定义，例如：router\_map.json。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "DynamicPage1",
   5. "pageSourceFile": "src/main/ets/pages/pageOne.ets",
   6. "buildFunction": "myFunction",
   7. "customData": {
   8. "stringKey": "data1",
   9. "numberKey": 123,
   10. "booleanKey": true,
   11. "objectKey": {
   12. "name": "test"
   13. },
   14. "arrayKey": [
   15. {
   16. "id": 123
   17. }
   18. ]
   19. }
   20. },
   21. {
   22. "name": "DynamicPage2",
   23. "pageSourceFile": "src/main/ets/pages/pageTwo.ets",
   24. "buildFunction": "myBuilder",
   25. "data": {
   26. "key1": "data1",
   27. "key2": "data2"
   28. }
   29. }
   30. ]
   31. }
   ```
2. 在module.json5配置文件的module标签中定义routerMap标签，指向定义的路由表配置文件，例如："routerMap": "$profile:router\_map"。

### data标签

此标签用于支持在路由表中配置自定义的字符串数据。

data标签示例：

```
1. {
2. "routerMap": [
3. {
4. "name": "DynamicPage",
5. "pageSourceFile": "src/main/ets/pages/pageOne.ets",
6. "buildFunction": "myBuilder",
7. "data": {
8. "key1": "data1",
9. "key2": "data2"
10. }
11. }
12. ]
13. }
```

### customData标签

此标签用于支持在路由表中配置自定义数据。

customData对象内部，可以配置任意类型的自定义数据。

customData标签示例：

```
1. {
2. "routerMap": [
3. {
4. "name": "DynamicPage",
5. "pageSourceFile": "src/main/ets/pages/pageOne.ets",
6. "buildFunction": "myBuilder",
7. "customData": {
8. "stringKey": "data1",
9. "numberKey": 123,
10. "booleanKey": true,
11. "objectKey": {
12. "name": "test"
13. },
14. "arrayKey": [
15. {
16. "id": 123
17. }
18. ]
19. }
20. }
21. ]
22. }
```

## appEnvironments标签

此标签标识模块配置的应用环境变量。

**表23** appEnvironments标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| name | 标识环境变量的变量名称。取值为长度不超过4096字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| value | 标识环境变量的值。取值为长度不超过4096字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |

appEnvironments标签示例：

```
1. {
2. "module": {
3. // ...
4. "appEnvironments": [
5. {
6. "name": "name1",
7. "value": "value1"
8. }
9. ],
10. // ...
11. }
12. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L21-L181)

## hnpPackages标签

该标签标识应用包含的Native软件包信息。

**表24** hnpPackages标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| package | 标识Native软件包名称。 | 字符串 | 该标签不可缺省。 |
| type | 标识Native软件包类型。支持的取值如下：  - public：公有类型。  - private：私有类型。 | 字符串 | 该标签不可缺省。 |
| independentSign | 标识Native软件包是否支持独立签名。  **说明：**  从API version 23开始，支持该标签。 | 布尔值 | 该标签可缺省，缺省值为false。 |

hnpPackages示例：

```
1. {
2. "module": {
3. // ...
4. "hnpPackages": [
5. {
6. "package": "hnpsample.hnp",
7. "type": "public",
8. "independentSign": true
9. }
10. ],
11. // ...
12. },
13. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile05/entry/src/main/module.json5#L16-L94)

## fileContextMenu标签

该标签标识当前HAP的右键菜单配置项，是一个profile文件资源，用于指定描述应用注册右键菜单配置文件。仅在PC/2in1设备上生效。仅允许在entry类型模块中配置。

fileContextMenu标签示例

```
1. {
2. "module": {
3. // ...
4. "fileContextMenu": "$profile:menu", // 资源配置，指向profile下面定义的配置文件menu.json
5. // ...
6. }
7. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L20-L182)

在开发视图的resources/base/profile下面定义配置文件menu.json，其中文件名“menu.json”可自定义，需要和fileContextMenu标签指定的信息对应。配置文件中描述了当前应用注册的右键菜单的项目和响应行为。

配置文件根节点名称为fileContextMenu，为对象数组，标识当前module注册右键菜单的数量。（单模块和单应用注册数量不能超过5个，配置超过数量当前只解析随机5个）

**表25** fileContextMenu标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| abilityName | 表示当前右键菜单对应的需要拉起的ability名称。 | 字符串 | 不可缺省。 |
| menuItem | 右键菜单显示的信息。命名建议：  原则一：[动作]+[应用名]，中文示例：用{App}打开、用{App} ({Plugin}插件) 打开；英文示例：Open with {App}、Open with {App} ({Plugin})。  原则二：[动作]+[目的]，示例：压缩为{文件名}、压缩至{路径}、用{App}转换为{格式}。 | 资源id | 不可缺省。 |
| menuHandler | 一个ability可以创建多个右键菜单， 该标签与右键菜单显示项一一对应，用于区分用户拉起的不同右键菜单项。开发者可自定义该标签取值，确保该标签在整个ability中唯一。在用户点击右键菜单拉起应用时，会作为参数传递给应用。 | 字符串 | 不可缺省。 |
| menuContext | 定义展示该菜单项需要的上下文，可以支持多种情况，类型为数组。 | 对象数组 | 不可缺省。 |

**表26** menuContext标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| menuKind | 表示单击如下类型时会触发右键菜单。取值范围如下：  - 0：空白处  - 1：文件  - 2：文件夹  - 3：文件和文件夹 | 数值 | 不可缺省。 |
| menuRule | 表示采用什么方式选择文件或文件夹时，会触发右键菜单。取值范围如下：  - single：单选  - multi：多选  - both：单选或多选 | 字符串 | 仅当menuKind为1或2时，才会读取该标签，此时不可缺省。 |
| fileSupportType | 表示当选中的文件列表里包含指定的文件类型时，显示右键菜单。  当该标签取值为["\*"]时，将会读取fileNotSupportType标签。  当该标签取值为[]时，将不做任何处理。 | 字符串数组 | 仅当menuKind为1时，才会读取该标签，此时不可缺省。 |
| fileNotSupportType | 表示当选中的文件列表里包含这些文件类型时，不显示该右键菜单。  仅当menuKind为1、且fileSupportType为["\*"]时，才会读取该标签。 | 字符串数组 | 可缺省，缺省值为空。 |

resources/base/profile路径下的menu.json资源文件示例如下：

```
1. {
2. "fileContextMenu": [
3. {
4. "abilityName": "EntryAbility",
5. "menuItem": "$string:module_desc",
6. "menuHandler": "openCompress",
7. "menuContext": [
8. {
9. "menuKind": 0
10. },
11. {
12. "menuKind": 1,
13. "menuRule": "both",
14. "fileSupportType": [
15. ".rar",
16. ".zip"
17. ],
18. "fileNotSupportType": [
19. ""
20. ]
21. },
22. {
23. "menuKind": 2,
24. "menuRule": "single"
25. },
26. {
27. "menuKind": 3
28. }
29. ]
30. }
31. ]
32. }
```

**响应行为**

应用进行右键扩展菜单注册后，在文件管理器通过右键操作拉起菜单，该菜单中会有“更多”选项。单击“更多”选项后，会出现注册后的menuItem列表，单击任意一个选项后，文件管理器默认通过startAbility的方式拉起三方应用，除了指定三方应用的包名和ability名之外，want中的parameter中，也会传入如下标签：

**表27** want中parameter标签说明

| 参数名 | 值 | 类型 |
| --- | --- | --- |
| menuHandler | 对应注册配置文件中menuHandler的值。 | 字符串 |
| uriList | 用户在具体文件上触发右键的uri值，如果空白处响应，此值为空，单个文件响应，数组长度1，多个文件响应则传入对应所有文件的uri值。 | 字符串数组 |

## startWindow标签

该标签指向一个profile文件资源，用于指定UIAbility组件启动页面的配置文件，在开发视图的resources/base/profile下面定义配置文件start\_window.json，如果配置了该标签，startWindowIcon和startWindowBackground标签将不生效。

**说明：**

从API version 19开始，支持使用该字段配置增强启动页。

**表28** startWindow标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| startWindowType | 标识当前UIAbility组件是否隐藏启动页。  当前仅支持在2in1设备或平板设备的自由多窗模式下使用。  不同取值含义如下：  - "REQUIRED\_SHOW"：强制显示启动页。不受[Ability管理服务（即StartOptions中hideStartWindow标签）](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)的影响。  - "REQUIRED\_HIDE"：强制隐藏启动页。不受[Ability管理服务（即StartOptions中hideStartWindow标签）](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)的影响。  - "OPTIONAL\_SHOW"：可选显示，默认行为为显示启动页，如果[Ability管理服务（即StartOptions中hideStartWindow标签）](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)设置隐藏启动页，则隐藏启动页。  - 如未配置该标签，默认取值为"REQUIRED\_SHOW"，即强制显示启动页。  从API version 20开始支持该标签。 | 字符串 | 可缺省，缺省值为REQUIRED\_SHOW。 |
| startWindowAppIcon | 标识当前UIAbility组件启动页面图标资源文件的索引，取值为长度不超过255字节的字符串。  从API version 19开始支持该字段。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowIllustration | 标识当前UIAbility组件启动页面插画资源文件的索引，取值为长度不超过255字节的字符串。  从API version 19开始支持该字段。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBrandingImage | 标识当前UIAbility组件启动页面品牌标识资源文件的索引，取值为长度不超过255字节的字符串。  从API version 19开始支持该字段。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBackgroundColor | 标识当前UIAbility组件启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。  从API version 19开始支持该字段。 | 字符串 | 不可缺省。 |
| startWindowBackgroundImage | 标识当前UIAbility组件启动页面背景图片资源文件的索引，取值为长度不超过255字节的字符串。  从API version 19开始支持该字段。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBackgroundImageFit | 标识当前UIAbility组件启动页面背景图像适应方式，支持的取值如下：  - Contain：按照宽高比进行缩小或放大，图片完全显示在显示边界内。  - Cover：按照宽高比进行缩小或放大，图片两边都大于或等于显示边界。  - Auto：自适应显示。  - Fill：不按照宽高比进行放大或缩小，图片充满显示边界。  - ScaleDown：按照宽高比显示，图片缩小或保持不变。  - None：保持原有尺寸显示。  从API version 19开始支持该字段。 | 字符串 | 可缺省，缺省值为Cover。 |
| startWindowColorModeType | 标识当前UIAbility组件启动页深浅色模式，仅作用于同进程间拉起场景。  不同取值含义如下：  - "FOLLOW\_SYSTEM"：启动页颜色模式跟随系统深浅色。  - "FOLLOW\_APPLICATION"：启动页颜色模式跟随应用深浅色。  - 如未配置该字段，默认取值为"FOLLOW\_SYSTEM"，即启动页颜色模式跟随系统深浅色。  从API version 20开始支持该字段。 | 字符串 | 可缺省，缺省值为FOLLOW\_SYSTEM。 |

resources/base/profile路径下的start\_window.json资源文件示例如下：

```
1. {
2. "startWindowType": "REQUIRED_SHOW",
3. "startWindowColorModeType": "FOLLOW_SYSTEM",
4. "startWindowAppIcon": "$media:start_window_app_icon",
5. "startWindowIllustration": "$media:start_window_illustration",
6. "startWindowBrandingImage": "$media:start_window_branding_image",
7. "startWindowBackgroundColor": "$color:start_window_back_ground_color",
8. "startWindowBackgroundImage": "$media:start_window_back_ground_image",
9. "startWindowBackgroundImageFit": "Cover"
10. }
```

## systemTheme标签

该标签指向一个profile文件资源，用于指定当前应用使用的系统主题配置文件。从API version 20开始，支持该标签。

systemTheme标签示例：

```
1. {
2. "module": {
3. // ...
4. "systemTheme": "$profile:theme_config", // 资源配置，指向profile下面定义的配置文件theme_config.json
5. }
6. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/ModuleConfigurationFile01/entry/src/main/module.json5#L19-L183)

在开发视图的resources/base/profile下面定义配置文件theme\_config.json，其中文件名“theme\_config.json”可自定义为“theme\_config”开头文件名，例如"theme\_config"、"theme\_config\_1"。需要和systemTheme标签指定的信息对应。配置文件中标识当前应用使用的系统主题。

**表29** theme\_config.json配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| systemTheme | 标识当前应用使用的系统主题，取值为引用系统主题名称的枚举。枚举支持的取值如下：  - $ohos:theme:ohos\_theme 系统默认的主题 | 字符串 | 该标签不可缺省。 |

resources/base/profile路径下的theme\_config.json资源文件示例如下：

```
1. {
2. "systemTheme": "$ohos:theme:ohos_theme"
3. }
```

## requiredDeviceFeatures标签

**表30** requiredDeviceFeatures标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| --- | --- | --- | --- |
| phone | 手机设备需要支持的设备特性，当前支持取值如下：  - large\_screen：表示设备需要支持[大屏横屏](../best-practices/bpta-multi-device-screen-layout.md#section6493354468)。  - paint：表示设备屏幕需要支持手写笔绘画能力。从API version 23开始，支持使用该字段配置。 | 字符串数组 | 可缺省，缺省值为空数组。 |
| 2in1 | PC/2in1设备需要支持的设备特性，当前支持取值如下：  - paint：表示设备屏幕需要支持手写笔绘画能力。从API version 23开始，支持使用该字段配置。 | 字符串数组 | 可缺省，缺省值为空数组。 |

requiredDeviceFeatures示例：

```
1. {
2. "module": {
3. "requiredDeviceFeatures": {
4. "phone": [
5. "large_screen"
6. ],
7. "2in1": [
8. "paint"
9. ]
10. },
11. }
12. }
```
