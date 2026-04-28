---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00303-1
title: 配置错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 配置错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:573296f2eda0b7d0ab6528bf71a0066fe30a0b74c272d0231dd7da5430ec59d0
---

## 00303002 找不到某个任务对应的模块

**错误信息**

Cannot find hvigor node in XXX with task YYY.

**错误描述**

找不到任务YYY对应的模块XXX。

**可能原因**

模块名称配置错误。

**处理步骤**

确保hvigorfile.ts中的模块名称配置正确。

## 00303003 找不到某个依赖任务的模块

**错误信息**

Cannot find dependent hvigor node XXX with task YYY.

**错误描述**

找不到某个依赖任务YYY的模块XXX。

**可能原因**

模块名称配置错误。

**处理步骤**

确保hvigorfile.ts中的模块名称配置正确。

## 00303004 找不到依赖的任务

**错误信息**

Cannot find hvigor task XXX in module YYY required by ZZZ.

**错误描述**

找不到任务ZZZ依赖的任务XXX。

**可能原因**

依赖任务名称配置错误。

**处理步骤**

确保hvigorfile.ts中的依赖任务名称配置正确。

## 00303010 工程级build-profile.json5的modules字段应该是数组类型

**错误信息**

modules' property should be an array in root project build-profile.json5.

**错误描述**

工程级build-profile.json5的modules字段应该是数组类型。

**可能原因**

工程级build-profile.json5的modules字段不是数组类型。

**处理步骤**

确保modules是数组类型。

## 00303011 找不到模块

**错误信息**

No modules found.

**错误描述**

找不到模块。

**可能原因**

工程级build-profile.json5中modules配置缺失。

**处理步骤**

确保modules配置存在且正确。

## 00303012 parameterFile配置不正确

**错误信息**

XXX corresponding to the parameterFile is not find, Check the parameterFile is valid.

**错误描述**

找不到与parameterFile对应的XXX，请检查parameterFile是否有效。

**可能原因**

工程级oh-package.json5中的parameterFile路径配置不正确。

**处理步骤**

1、确保在工程级oh-package.json5中正确配置[parameterFile](ide-oh-package-json5.md#section122411462820)字段。

2、确保parameterFile文件存在且命名正确。

## 00303013 Hvigor仅支持API 8及以上的版本

**错误信息**

Hvigor only works with API version 8 and later versions.

**错误描述**

Hvigor仅支持API 8及以上的版本。

**可能原因**

工程级oh-package.json5中compatibleSdkVersion的值低于8。

**处理步骤**

请选择API 8及以上的SDK版本进行新建工程。

## 00303015 SDK版本关系不符合规则

**错误信息**

Configure the API version according to the rule of compatibleSdkVersion <= targetSdkVersion <= compileSdkVersion.

**错误描述**

根据compatibleSdkVersion <= targetSdkVersion <= compileSdkVersion的规则配置API 版本。

**可能原因**

API 版本不符合以上规则。

**处理步骤**

检查工程级build-profile.json5中的compileSdkVersion/compatibleSdkVersion/targetSdkVersion字段，确保符合以上规则。

## 00303017 srcEntry或configEntry的值应该是相对路径

**错误信息**

Invalid app startup configuration XXX in the module YYY: the value of 'srcEntry' or 'configEntry' should be a relative path. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：srcEntry或configEntry的值应该是相对路径。

**可能原因**

ZZZ文件的configEntry字段或startupTasks下的srcEntry字段的值是绝对路径。

**处理步骤**

确保值是相对路径。

## 00303018 srcEntry或configEntry配置的文件后缀必须是ets,ts或js

**错误信息**

Invalid app startup configuration XXX in the module YYY: the suffix of the code file specified by the field 'srcEntry' under 'startupTasks' and 'configEntry' should be ets,ts or js. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：startupTasks下的srcEntry和configEntry配置的代码文件后缀应该是ets，ts或js。

**可能原因**

ZZZ文件startupTasks下的srcEntry字段或configEntry字段配置的文件后缀不是ets，ts或js。

**处理步骤**

确保文件后缀是ets，ts或js。

## 00303019 srcEntry或configEntry配置的文件必须是本模块下的文件

**错误信息**

Invalid app startup configuration XXX in the module YYY: the file of 'srcEntry' or 'configEntry' in startupTasks should be the module file where it is configuration. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：srcEntry或configEntry配置的文件必须是本模块下的文件。

**可能原因**

ZZZ文件的configEntry字段或startupTasks下的srcEntry字段配置的文件不是本模块下的文件。

**处理步骤**

确保文件是本模块下的文件。

## 00303020 srcEntry或configEntry配置的文件必须存在

**错误信息**

Invalid app startup configuration XXX in the module YYY: the code file specified by the field 'srcEntry' or 'configEntry' in startupTasks must exist. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：srcEntry或configEntry配置的文件必须存在。

**可能原因**

ZZZ文件的configEntry字段或startupTasks下的srcEntry字段配置的文件不存在。

**处理步骤**

确保文件存在。

## 00303021 appPreloadHintStartupTasks下的srcEntry配置的文件后缀应该为so

**错误信息**

Invalid app startup configuration XXX in the module YYY: the suffix of the code file specified by the field 'srcEntry' in appPreloadHintStartupTasks should be so. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：appPreloadHintStartupTasks下的srcEntry配置的文件后缀应该为so。

**可能原因**

ZZZ文件中appPreloadHintStartupTasks下的srcEntry字段配置的文件后缀不是so。

**处理步骤**

确保文件后缀是so。

## 00303022 name值必须唯一

**错误信息**

Duplicate name 'XXX' exists in the 'YYY' attribute in the startup configuration file of the 'ZZZ' module.

**错误描述**

模块ZZZ和有依赖关系的其他模块的启动框架文件的YYY属性下的元素的name值XXX重复。

**可能原因**

模块ZZZ和与ZZZ模块有依赖关系的其他模块的所有启动框架配置文件中，startupTasks或appPreloadHintStartupTasks下的元素的name属性有重复值。

**处理步骤**

检查ZZZ模块和与ZZZ模块有依赖关系的其他模块的所有启动框架配置文件，确保startupTasks或appPreloadHintStartupTasks下的元素的name属性值唯一。

## 00303023 .so文件必须存在且在依赖中正确配置

**错误信息**

Invalid app startup configuration XXX in the module YYY: the .so file must exist and be correctly configured in the dependency. At file: ZZZ.

**错误描述**

模块YYY中的启动框架配置XXX不正确：.so文件必须存在且在依赖中正确配置。

**可能原因**

ZZZ文件中appPreloadHintStartupTasks下的srcEntry字段配置的.so文件不存在或没有在依赖中正确配置。

**处理步骤**

确保文件存在，并且在模块YYY的oh-package.json5中正确配置依赖。

## 00303024 项目结构和配置需要升级

**错误信息**

The project structure and configuration need to be upgraded before use.

**错误描述**

项目结构和配置需要升级。

**可能原因**

使用一体化DevEco Studio打开了历史工程。

**处理步骤**

参考[一体化工程迁移](../harmonyos-guides-V14/ide-integrated-project-migration-V14.md)，对历史工程进行迁移。

## 00303025 hvigor的modelVersion类型不兼容

**错误信息**

Incompatible types of hvigor modelVersion.

**错误描述**

hvigor的modelVersion类型不兼容。

**可能原因**

hvigor-config.json5的modelVersion不是string类型。

**处理步骤**

将hvigor-config.json5的modelVersion修改为string类型。

## 00303026 oh-package.json5的modelVersion类型不兼容

**错误信息**

Incompatible types of oh-package.json5 modelVersion.

**错误描述**

oh-package.json5的modelVersion类型不兼容。

**可能原因**

oh-package.json5的modelVersion不是string类型。

**处理步骤**

将oh-package.json5的modelVersion修改为string类型。

## 00303027 hvigor-config.json5和oh-package.json5的modelVersion不一致

**错误信息**

The modelVersion in hvigor-config.json5 is XXX,and the modelVersion in oh-package.json5 is YYY.

**错误描述**

hvigor-config.json5中的modelVersion为XXX，oh-package.json5中的modelVersion为YYY。

**可能原因**

hvigor-config.json5和oh-package.json5的modelVersion不一致。

**处理步骤**

确保hvigor-config.json5和工程级oh-package.json5的modelVersion一致。

## 00303028 Hvigor的modelVersion不支持

**错误信息**

Unsupported modelVersion of Hvigor XXX.

**错误描述**

使用了不支持的modelVersion。

**可能原因**

hvigor-config.json5中的modelVersion配置了不支持的版本号。

**处理步骤**

根据报错信息，将modelVersion修改为支持的版本号。

## 00303029 oh-package.json5的modelVersion不支持

**错误信息**

Unsupported modelVersion of oh-package.json5 XXX.

**错误描述**

使用了不支持的modelVersion。

**可能原因**

oh-package.json5中的modelVersion配置了不支持的版本号。

**处理步骤**

根据报错信息，将modelVersion修改为支持的版本号。

## 00303030 OpenHarmony工程需要在product中配置compileSdkVersion

**错误信息**

For the OpenHarmony project, you need to configure the compileSdkVersion in the product, at file: %s.

**错误描述**

OpenHarmony工程需要在product中配置compileSdkVersion。

**可能原因**

OpenHarmony工程没有在工程级build-profile.json5中配置compileSdkVersion。

**处理步骤**

在工程级build-profile.json5中配置compileSdkVersion。

## 00303031 compileSdkVersion不支持

**错误信息**

Unsupported compileSdkVersion XXX.

**错误描述**

配置的compileSdkVersion版本不支持。

**可能原因**

compileSdkVersion配置了不支持使用的版本。

**处理步骤**

根据报错信息，将compileSdkVersion修改为支持的版本。

## 00303032 compatibleSdkVersion不支持

**错误信息**

Unsupported compatibleSdkVersion XXX.

**错误描述**

配置的compatibleSdkVersion版本不支持。

**可能原因**

compatibleSdkVersion配置了不支持使用的版本。

**处理步骤**

根据报错信息，将compatibleSdkVersion修改为支持的版本。

## 00303033 compatibleSdkVersion未配置

**错误信息**

Please configure compatibleSdkVersion in the product.

**错误描述**

请在product中配置compatibleSdkVersion。

**可能原因**

compatibleSdkVersion未配置。

**处理步骤**

根据报错信息，在工程级build-profile.json5中配置compileSdkVersion字段。

## 00303034 compileSdkVersion未配置

**错误信息**

Please configure compileSdkVersion in the product.

**错误描述**

请在product中配置compileSdkVersion。

**可能原因**

runtimeOS为OpenHarmony时，未配置compileSdkVersion。

**处理步骤**

根据报错信息，在工程级build-profile.json5中配置compileSdkVersion字段。

## 00303035 FA模型项目仅支持API 8及以上版本

**错误信息**

According to the compatibility specifications, fa-model project can only support the development of API version 8 or later.

**错误描述**

根据兼容性规范，FA模型项目仅支持API 8及以上版本。

**可能原因**

FA模型项目中compatibleSdkVersion配置为8以下的版本。

**处理步骤**

将工程级build-profile.json5中的compatibleSdkVersion配置为8或以上版本。

## 00303036 Stage模型项目仅支持API 9及以上版本

**错误信息**

According to the compatibility specifications,stage-model project can only support the development of API version 9 or later.

**错误描述**

根据兼容性规范，Stage模型项目仅支持API 9及以上版本。

**可能原因**

Stage模型项目中compatibleSdkVersion配置为9以下的版本。

**处理步骤**

将工程级build-profile.json5中的compatibleSdkVersion配置为9或以上版本。

## 00303037 API版本与设备版本不兼容

**错误信息**

According to the compatibility specifications, apps of API version XXX or stage mode can only run on devices of API version XXX or later.

**错误描述**

根据兼容性规范，API版本为XXX或stage模型的应用只能运行在API版本为XXX或更高版本的设备上。

**可能原因**

工程级build-profile.json5中compatibleSdkVersion版本高于设备API版本。

**处理步骤**

将设备API 版本升级到与compatibleSdkVersion相同或更高的版本，或将compatibleSdkVersion配置为与设备API相同的版本。

## 00303038 Schema校验失败

**错误信息**

Schema validate failed.

**错误描述**

Schema校验失败。

**可能原因**

配置文件中的schema配置存在问题。

**处理步骤**

不同场景，根据具体报错信息修改。

## 00303039 name配置重复

**错误信息**

Duplicated XXX: YYY.

**错误描述**

name配置重复。

**可能原因**

name字段重复导致报错，如moduleName、targetName等。

**处理步骤**

根据报错信息，在对应的文件中修改name，确保每个名称唯一。

## 00303040 找不到默认product

**错误信息**

Unable to find or load the default product.

**错误描述**

无法找到或加载默认product。

**可能原因**

工程中name为default的product不存在。

**处理步骤**

根据报错信息，在对应的文件添加default的product。

## 00303041 不允许同时配置标准系统设备和轻量系统设备

**错误信息**

It's not allowed to configure mini-system device when standard-system device exists.

**错误描述**

存在标准系统设备时，不允许配置轻量系统设备。

**可能原因**

同时配置了标准系统设备和轻量系统设备。

**处理步骤**

根据报错信息的文件检查是否存在异常的设备类型。

## 00303042 设备类型不能包含多个轻量系统设备

**错误信息**

The device types cannot include multiple mini-system devices.

**错误描述**

设备类型不能包含多个轻量系统设备。

**可能原因**

设备类型包含多个轻量系统设备。

**处理步骤**

检查报错信息的文件，确保没有包含多个轻量系统设备。

## 00303043 FA模型工程不支持配置轻量系统设备

**错误信息**

Mini-system devices cannot be configured in an FA project.

**错误描述**

FA模型工程不支持配置轻量系统设备。

**可能原因**

FA模型工程中配置了轻量系统设备。

**处理步骤**

检查报错信息的文件，确保不包含轻量系统设备。

## 00303044 form\_config.json文件中只能配置一个默认卡片

**错误信息**

Only one default card can be configured in the form\_config.json file.

**错误描述**

form\_config.json文件中只能配置一个默认卡片。

**可能原因**

form\_config.json文件中存在多个isDefault为true的卡片**。**

**处理步骤**

确保form\_config.json文件中只存在一个isDefault为true的卡片。

## 00303045 updateDuration和scheduleUpdateTime字段不能同时为空

**错误信息**

In the form\_config.json file, if the value of the updateEnabled field is true,the updateDuration and scheduleUpdateTime fields cannot be both empty.

**错误描述**

在form\_config.json文件中，如果updateEnabled字段的值为true，updateDuration和scheduleUpdateTime字段不能同时为空。

**可能原因**

在form\_config.json文件中配置updateEnabled为true，并且未配置updateDuration和scheduleUpdateTime字段。

**处理步骤**

如果updateEnabled字段的值为true，需要配置updateDuration或scheduleUpdateTime字段。

## 00303046 parameterFile对应的key不可用

**错误信息**

Invalid key: XXX in parameterFile.at YYY.

**错误描述**

在YYY路径下的parameterFile中存在不可用的key XXX。

**可能原因**

请检查对应的key值是否存在于parameterFile中。

**处理步骤**

修改@param:key确保能找到一个对应的value值在对应的parameterFile中。

## 00303047 parameterFile中的key不符合校验规则

**错误信息**

The key: XXX in parameterFile is invalid, only support at(@), slashe(/), letters, digits, dots(.), hyphens(-), and underscores(\_). For details, see the package name verification rules.

**错误描述**

parameterFile中的键XXX无效，仅支持@、/、字母、数字、点（.）、中划线（-）和下划线(\_)，请参考包名校验规则。

**可能原因**

parameterFile中的key不符合校验规则。

**处理步骤**

根据报错信息修改parameterFile中的key，确保符合校验规则。

## 00303048 parameterFile中的版本必须符合semver规范

**错误信息**

Invalid version: XXX in parameterFile, the version must comply with the semver specifications.

**错误描述**

parameterFile中的版本XXX无效，版本必须符合[semver](https://semver.org/)规范。

**可能原因**

parameterFile中的版本不符合semver规范。

**处理步骤**

确保parameterFile中的版本符合semver规范。

## 00303050 main字段的值必须是.ets、.ts、.js文件

**错误信息**

The value of 'main' must be a .ets, .ts, or .js file.

**错误描述**

main字段的值必须是.ets、.ts、.js文件。

**可能原因**

main字段配置了后缀不是.ets、.ts、.js的文件。

**处理步骤**

检查模块的oh-package.json5文件，确保main字段配置正确。

## 00303051 workers字段的值必须是.ets、.ts、.js文件

**错误信息**

Field 'workers' only accepts path ends with '.js', '.ts' or '.ets' but get: XXX.

**错误描述**

workers字段的值必须是.ets、.ts、.js文件。

**可能原因**

workers字段配置了后缀不是.ets、.ts、.js的文件。

**处理步骤**

从workers配置中移除XXX。

## 00303052 API9及以上的LiteWearable工程仅支持JS

**错误信息**

Lite-wearable devices with API version 9 or later support only JS.

**错误描述**

API9及以上的LiteWearable工程仅支持JS。

**可能原因**

模块的src/main下存在ets目录。

**处理步骤**

移除模块src/main下的ets目录。

## 00303053 build-profile.json5/hvigorconfig.ts和module.json5中的模块名称需要保持一致

**错误信息**

The module name XXX in build-profile.json5 or hvigorconfig.ts must be same as moduleName in module.json5.

**错误描述**

build-profile.json5/hvigorconfig.ts和module.json5中的模块名称需要保持一致。

**可能原因**

工程级build-profile.json5/hvigorconfig.ts中的modules的name，与module.json5中的module.name不一致。

**处理步骤**

两者的模块名称需要保持一致。

## 00303054 types字段仅支持在ArkTS工程中配置

**错误信息**

Only ArkTS project supports custom types.

**错误描述**

types字段仅支持在ArkTS工程中配置。

**可能原因**

在JS模块添加了types配置。

**处理步骤**

切换为ArkTS模块。

## 00303055 types字段的文件不需要.d.ets或.d.ts后缀

**错误信息**

The custom type's declaration file XXX does not require the suffix YYY.

**错误描述**

types字段的文件XXX不需要YYY后缀。

**可能原因**

types字段的文件存在.d.ets或.d.ts后缀。

**处理步骤**

移除types字段的后缀.d.ets或.d.ts。

## 00303056 types字段的文件后缀无效

**错误信息**

The suffix of custom type's declaration file 'XXX' is not valid.

**错误描述**

types字段的文件XXX后缀无效。

**可能原因**

types字段配置了后缀不是.d.ets或.d.ts的文件。

**处理步骤**

确保types字段的文件均为.d.ets或.d.ts文件。

## 00303057 FA模型工程不支持配置dynamicDependencies

**错误信息**

Current module XXX do not support dynamicDependencies.

**错误描述**

XX模块不支持配置dynamicDependencies。

**可能原因**

当前工程为FA模型工程，且在oh-package.json5中配置了dynamicDependencies。

**处理步骤**

将依赖配置dynamicDependencies切换为dependencies。

## 00303058 defaultDimension的值无效

**错误信息**

Invalid default dimension settings in these widgets: XXX.

**错误描述**

defaultDimension的值无效。

**可能原因**

defaultDimension的值不在supportDimensions的声明范围内。

**处理步骤**

确保defaultDimension的值在supportDimensions中已定义。

## 00303059 权限名称重复

**错误信息**

Duplicate permission names detected under "XXX": "YYY".

**错误描述**

在XXX中检测到重复的权限名称YYY。

**可能原因**

在XXX中配置了多个name相同的权限。

**处理步骤**

移除重复的权限。

## 00303060 为多设备配置的SystemCapability的交集为空

**错误信息**

The intersection of the system capability sets configured for multiple devices is empty.

**错误描述**

为多设备配置的SystemCapability的交集为空。

**可能原因**

每种设备类型都有对应的SystemCapability，当syscap.json的custom和general配置的设备类型的SystemCapability交集为空时，会出现此报错。

**处理步骤**

确保general和custom中配置的设备类型的SystemCapability存在交集。

## 00303061 自定义SystemCapability不合法

**错误信息**

The device type defined in the module.json5 of the module 'XXX' is empty, and the general and custom fields in the syscap.json file are not specified or their values are empty.

**错误描述**

XXX模块的module.json5中的deviceTypes字段值为空，同时，syscap.json文件中的general和custom字段值也为空。

**可能原因**

XXX模块的module.json5中的deviceTypes字段值为空，同时，syscap.json文件中的general和custom字段值也为空。

**处理步骤**

1. 设置module.json5中的deviceTypes。
2. 设置syscap.json中的general，需要与deviceTypes的值保持一致。

## 00303062 target的deviceType无效

**错误信息**

Invalid target deviceType.

**错误描述**

target的deviceType无效。

**可能原因**

模块级build-profile.json5的targets下的deviceType的值，在module.json5的deviceTypes中不存在。

**处理步骤**

确保targets下的deviceType的值，在module.json5的deviceTypes中已定义。

## 00303065 target和product的runtimeOS不一致

**错误信息**

The runtimeOS configuration of the target XXX:YYY does not match the product ZZZ.

**错误描述**

target和product的runtimeOS不一致。

**可能原因**

模块级build-profile.json5和工程级build-profile.json5的runtimeOS不一致。

**处理步骤**

确保工程级和模块级build-profile.json5的runtimeOS一致。

## 00303071 target对应的product不存在

**错误信息**

Invalid product for target XXX.

**错误描述**

target对应的product不存在。

**可能原因**

工程级build-profile.json5中target XXX的applyToProducts字段配置错误。

**处理步骤**

确保target XXX的applyToProducts字段配置正确的product。

## 00303072 ohosTest target被关联到某个product

**错误信息**

The 'ohosTest' target does not need to be packaged into the application. 'ohosTest' target cannot be applied to product.

**错误描述**

'ohosTest' target不会被打包到APP产物中，所以此target不能关联到某个product。

**可能原因**

在工程级build-profile.json5的targets中，存在name为ohosTest的配置，并且同时配置了applyToProduct。

**处理步骤**

工程级build-profile.json5中移除name为ohosTest的配置。

## 00303073 存在未知target

**错误信息**

Unknown target XXX.

**错误描述**

存在未知target。

**可能原因**

target XXX在build-profile.json5中未定义。

**处理步骤**

确保模块级build-profile.json5中targets字段下存在name为XXX的target。

## 00303074 签名材料和工程配置的bundleName不一致

**错误信息**

BundleName in the project configuration does not match that in the SigningConfigs.

**错误描述**

签名材料和工程配置的bundleName不一致。

**可能原因**

生成签名材料时的bundleName与app.json5或工程级build-profile.json5中的bundleName不一致。

**处理步骤**

1. 如果在工程级build-profile.json5中配置了bundleName，确保签名材料和工程级build-profile.json5中的bundleName一致。
2. 如果没有在工程级build-profile.json5中配置bundleName，确保签名材料和app.json5中的bundleName一致。

## 00303075 version字段必须为字符串

**错误信息**

The version number of the module must be a string, but received a XXX.

**错误描述**

version字段必须为字符串，但却设置了类型XXX。

**可能原因**

oh-package.json5中的version字段不是字符串。

**处理步骤**

将version字段设置为字符串类型。

## 00303076 name字段必须为字符串

**错误信息**

The name of the module must be a string, but received a XXX.

**错误描述**

name字段必须为字符串，但却设置了类型XXX。

**可能原因**

oh-package.json5中的name字段不是字符串。

**处理步骤**

将name字段设置为字符串类型。

## 00303077 当前模块配置的deviceType与entryModules的deviceType不存在交集

**错误信息**

The deviceType values XXX of XXX in the XXX don't overlap that XXX of XXX in the associated XXX module.

**错误描述**

当前模块配置的deviceType与entryModules的deviceType不存在交集。

**可能原因**

在FA模型中，当前模块配置的deviceType与entryModules的deviceType不存在交集。

**处理步骤**

需要变更当前模块配置的deviceType，使其与entryModules的deviceType存在交集。

## 00303078 config.json中不允许js和abilities存在name字段相同的配置

**错误信息**

Forms referenced in the config. In the configuration item named 'XXX', the type field does not match between 'module.abilities' and 'module.js'.

**错误描述**

config.json中不允许js和abilities存在name字段相同的配置。

**可能原因**

在FA模型工程中，config.json的js和abilities存在name字段相同的配置。

**处理步骤**

确保两者之间name字段的值唯一。

## 00303082 找不到对应的SDK

**错误信息**

Unable to find the XXX in SDK Manager.

**错误描述**

找不到compatibleSdkVersion/compileSdkVersion/targetSdkVersion对应的SDK。

**可能原因**

Hvigor和SDK版本不配套**。**

**处理步骤**

1. 从NEXT Developer Beta1开始，DevEco Studio提供了开箱即用的开发体验，将SDK、Node.js、Hvigor、Ohpm等工具链打包在一起，简化了DevEco Studio的安装和配置过程，并提供历史工程迁移的能力，帮助您快速完成工程转换。
2. [下载](https://developer.huawei.com/consumer/cn/download/)一体化DevEco Studio工具。

## 00303083 SDK版本号配置错误

**错误信息**

The platform version XXX and API version YYY of ZZZ in build-profile.json5 do not match.

**错误描述**

build-profile.json5的ZZZ字段的XXX和API 版本YYY不匹配。

**可能原因**

工程级build-profile.json5中的compatibleSdkVersion/compileSdkVersion/targetSdkVersion字段中的XXX和YYY不匹配。

**处理步骤**

创建新工程时，在工程配置页面查看**Compatible SDK**，点击下拉框可查看所有支持的SDK版本号。

## 00303087 不允许动态导入工程外模块

**错误信息**

Invalid dynamic import configuration XXX in current module XXX.

**错误描述**

当前模块中的动态导入配置无效。

**可能原因**

动态导入的文件不在当前模块或项目的其他模块中。

**处理步骤**

确保动态导入的文件路径位于当前模块或项目的其他模块中。

## 00303088 动态导入文件后缀不正确

**错误信息**

Invalid file XXX found in the module XXX dynamic import files.

**错误描述**

模块的动态导入文件无效。

**可能原因**

动态导入的文件后缀不是.ts或.ets。

**处理步骤**

检查动态导入的文件，确保后缀为.ts或.ets。

## 00303089 不允许跨模块动态导入

**错误信息**

Invalid dynamic import configuration XXX in module XXX.

**错误描述**

模块中的动态导入配置无效。

**可能原因**

工程级build-profile.json5中noExternalImportByPath设置为true时，runtimeOnly不允许跨模块动态导入。

**处理步骤**

1. 确保动态导入的文件在本模块下。
2. 如果需要跨模块导入，检查是否可以调整noExternalImportByPath配置。

## 00303090 动态导入配置无效

**错误信息**

Invalid dynamic import configurations in current module XXX.

**错误描述**

当前模块中的动态导入配置无效。

**可能原因**

配置的动态导入的路径未在oh-package.json5的dependencies中定义，不支持配置三方包内的某个文件路径。

**处理步骤**

确保所有动态导入文件或相对路径在oh-package.json5的dependencies中已定义。

## 00303091 srcEntry格式错误

**错误信息**

Invalid configuration of XXX field.

**错误描述**

XXX字段无效。

**可能原因**

module.json5中srcEntry字段没有使用相对路径。

**处理步骤**

确保srcEntry字段使用相对路径（如 ./\*\*）。

## 00303092 卡片配置文件缺少src字段

**错误信息**

The required field form.src is missing.

**错误描述**

缺少必需的字段src。

**可能原因**

卡片配置文件缺少src字段。

**处理步骤**

确保卡片配置文件中包含src字段。

## 00303093 卡片src的值不在模块下

**错误信息**

The value of form.src: XXX, is not under module YYY.

**错误描述**

form.src的值不在模块YYY下。

**可能原因**

卡片配置文件中src字段的值不在模块YYY下。

**处理步骤**

确保src字段的值在模块YYY下。

## 00303094 找不到mainElement字段

**错误信息**

The 'mainElement' field was not found in the module.json5 file.

**错误描述**

module.json5文件中找不到mainElement字段。

**可能原因**

元服务工程的module.json5文件中缺少mainElement字段。

**处理步骤**

确保元服务工程的module.json5中包含mainElement字段。

## 00303096 mock-config.json5文件中的路径无效

**错误信息**

XXX is a invalid path. At file: YYY.

**错误描述**

在mock-config.json5文件中配置的路径无效，或者路径不存在。

**可能原因**

在mock-config.json5文件中配置的路径无效，或者路径不存在。

**处理步骤**

确保在mock-config.json5文件中配置的路径正确且存在。

## 00303098 app.json5中configuration字段无效

**错误信息**

Invalid configuration in the app.json5.

**错误描述**

app.json5中configuration字段无效。

**可能原因**

app.json5中configuration字段对应的路径不存在。

**处理步骤**

确保configuration字段对应的文件路径存在。

## 00303099 路径不存在

**错误信息**

Invalid configuration. The path of XXX does not exist. At file: YYY.

**错误描述**

XXX字段对应的路径不存在。

**可能原因**

XXX字段对应的路径不存在。

**处理步骤**

确保XXX字段对应的路径存在。

## 00303100 general字段错误

**错误信息**

The value of general in the syscap.json file must be the same as that of XXX in the YYY file.

**错误描述**

syscap.json文件中general的值必须和YYY文件中XXX的值相同。

**可能原因**

两个文件中字段的值不一致。

**处理步骤**

确保两个文件中字段的值一致。

## 00303101 general字段配置的设备类型不一致

**错误信息**

Unable to find the general field or its value is invalid. At file: XXX.

**错误描述**

general未配置，或者配置的设备类型和模块的deviceTypes中配置的不一致。

**可能原因**

general未配置，或者配置的设备类型和模块的deviceTypes中配置的不一致。

**处理步骤**

确保字段存在，并且其值与deviceTypes的值保持一致。

## 00303104 routerMap配置中的pageSourceFile字段格式无效

**错误信息**

Invalid pageSourceFile format in the XXX routerMap configuration. At file: XXX.

**错误描述**

routerMap配置中的pageSourceFile字段格式无效。

**可能原因**

pageSourceFile字段格式没有以src/开头。

**处理步骤**

确保pageSourceFile字段是以src/开头的相对路径。

## 00303105 srcLanguage字段没有定义

**错误信息**

Module-Abilities-srcLanguage in XXX is not defined. At file: YYY.

**错误描述**

Module-Abilities-srcLanguage字段没有定义。

**可能原因**

srcLanguage标签缺失。

**处理步骤**

确保YYY文件中的Module-Abilities-srcLanguage字段已定义。

## 00303106 signingConfigs中没有找到签名材料

**错误信息**

The material has not been configured in signingConfigs. At file: XXX.

**错误描述**

signingConfigs中没有找到签名材料。

**可能原因**

工程级build-profile.json5文件里的signingConfigs下没有配置material。

**处理步骤**

确保工程级build-profile.json5文件的material已配置。

## 00303107 签名材料无效

**错误信息**

Invalid XXX value. Make sure it is not null or empty. The file must be included in YYY.

**错误描述**

签名材料中的XXX值是个无效的文件或文件夹。

**可能原因**

XXX字段没有配置或者配置的值无效。

**处理步骤**

确保工程级build-profile.json5文件中的XXX字段已配置。若该字段值是某个文件路径，请确保该文件路径存在。

## 00303108 签名配置的type字段和runtimeOS不匹配

**错误信息**

Signing configuration XXX does not apply to YYY.

**错误描述**

签名配置XXX不能在类型为YYY的工程中使用。

**可能原因**

签名配置的type字段和runtimeOS不匹配。

**处理步骤**

确保工程级build-profile.json5文件中**products**下**runtimeOS**字段**，**和**signingConfigs**下**type**字段取值保持一致。

## 00303110 找不到pages字段

**错误信息**

Unable to replace pages. Cannot find moduleJsonObj.module.pages in module XXX.

**错误描述**

替换page失败，模块XXX里不存在pages字段。

**可能原因**

模块的module.json5文件里不存在pages字段。

**处理步骤**

确保模块的module.json5文件中存在pages字段。

## 00303111 buildProfileFields的值仅支持number、string、boolean类型

**错误信息**

buildProfileFields only support number/string/boolean,not support XXX, the value YYY does not meet the requirements.

**错误描述**

buildProfileFields的值仅支持number、string、boolean类型，不支持XXX，值YYY不符合要求。

**可能原因**

buildProfileFields中存在类型不是number、string、boolean的值。

**处理步骤**

确保buildProfileFields的值符合要求。

## 00303112 当useNormalizedOHMUrl不为true时，不支持字节码har

**错误信息**

byteCodeHar not supported when useNormalizedOHMUrl is not true.

**错误描述**

当useNormalizedOHMUrl不为true时，不支持字节码har。

**可能原因**

当useNormalizedOHMUrl不为true时，不支持字节码har。

**处理步骤**

检查工程级的build-profile.json5文件中的useNormalizedOHMUrl字段配置。

## 00303113 externalNativeOptions下的path字段的值不能为空

**错误信息**

The configured cmake script in externalNativeOptions/path cannot be empty. At file: XXX.

**错误描述**

externalNativeOptions下的path字段的值不能为空。

**可能原因**

externalNativeOptions下的path字段的值为空。

**处理步骤**

确保模块级/工程级的build-profile.json5文件中的externalNativeOptions/path取值有效。

## 00303114 HarmonyOS工程不支持armeabi-v7a

**错误信息**

"armeabi-v7a" not supported for HarmonyOS. At file: XXX.

**错误描述**

HarmonyOS工程不支持armeabi-v7a。

**可能原因**

HarmonyOS工程中，abiFilters字段配置为armeabi-v7a。

**处理步骤**

确保[abiFilters](ide-hvigor-cpp.md#section0721057575)配置的是有效值。

## 00303115 armeabi-v7a不能是OpenHarmony工程的唯一配置

**错误信息**

"armeabi-v7a" not supported for OpenHarmony as the only option. At file: XXX.

**错误描述**

armeabi-v7a不能是OpenHarmony工程的唯一配置。

**可能原因**

OpenHarmony工程中，abiFilters字段只配置了armeabi-v7a一个值。

**处理步骤**

将"arm64-v8a"或者"x86\_64"添加到abiFilters字段中。

## 00303116 签名材料中的storePassword或keyPassword字段的值长度小于32

**错误信息**

The length of the storePassword or keyPassword field in the signature configuration is less than 32. At file: XXX.

**错误描述**

签名材料中的storePassword或keyPassword字段的值长度小于32。

**可能原因**

签名材料中的storePassword或keyPassword字段的值长度小于32。

**处理步骤**

清除XXX文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303117 签名材料中的storePassword或keyPassword字段的值长度为偶数

**错误信息**

The length of the storePassword or keyPassword field in the signature configuration is an even number. At file: XXX.

**错误描述**

签名材料中的storePassword或keyPassword字段的值长度为偶数。

**可能原因**

签名材料中的storePassword或keyPassword字段的值长度为偶数。

**处理步骤**

清除XXX文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303118 签名材料数据错误

**错误信息**

Signing failed: Signing material data error!. At file: XXX.

**错误描述**

签名材料数据错误。

**可能原因**

签名材料损坏。

**处理步骤**

清除XXX文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303119 签名材料无效

**错误信息**

Signing failed: Signing materials XXX is illegal!.At file: YYY.

**错误描述**

签名材料XXX无效。

**可能原因**

签名材料损坏。

**处理步骤**

清除YYY文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303120 签名失败：签名材料为空或不是文件夹

**错误信息**

Signing failed: signing material XXX is empty or not a directory.At file: YYY.

**错误描述**

签名材料XXX为空或不是文件夹。

**可能原因**

签名材料为空或不是文件夹。

**处理步骤**

清除YYY文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303121 签名材料错误

**错误信息**

Signing failed: Signing material error. At file: XXX.

**错误描述**

签名材料错误。

**可能原因**

签名材料损坏。

**处理步骤**

清除XXX文件中的signingConfigs字段，点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303127 apPath后缀无效

**错误信息**

The suffix of apPath at XXX is invalid.

**错误描述**

apPath后缀无效。

**可能原因**

apPath字段对应的路径后缀不是.ap。

**处理步骤**

确保apPath字段对应的路径后缀是.ap。

## 00303128 minAPIVersion字段未配置

**错误信息**

The minAPIVersion was not configured. At file: XXX.

**错误描述**

minAPIVersion字段未配置。

**可能原因**

minAPIVersion字段缺失。

**处理步骤**

确保XXX文件中minAPIVersion字段存在。

## 00303130 找不到指定的product

**错误信息**

Unable to find the product XXX for module YYY. At file: ZZZ.

**错误描述**

无法在指定的文件中找到模块YYY所需的product XXX。

**可能原因**

工程级build-profile.json5文件中的product缺失或错误。

**处理步骤**

检查工程级build-profile.json5文件，确保product正确配置。

## 00303136 插件的ID重复

**错误信息**

Plugin with ID XXX has been registered. Please check.

**错误描述**

插件的ID重复，该ID已经被使用。

**可能原因**

插件配置的ID与其他插件的ID重复。

**处理步骤**

检查hvigorfile.ts文件，确保插件ID不重复。

## 00303137 用户目录下不存在.npmrc文件

**错误信息**

The hvigor depends on the npmrc file. No npmrc file is matched in the current user folder. Configure the npmrc file first.

**错误描述**

hvigor依赖于npmrc文件，当前用户目录下不存在.npmrc文件。

**可能原因**

用户目录下不存在.npmrc文件。

**处理步骤**

在用户目录下创建.npmrc文件，配置信息如下：

```
1. registry=https://repo.huaweicloud.com/repository/npm/
2. @ohos:registry=https://repo.harmonyos.com/npm/
```

## 00303138 模块名称不能为空字符串

**错误信息**

Error module name, can not be empty string!

**错误描述**

模块名称不能为空字符串。

**可能原因**

hvigorfile.ts中模块的名称是空字符串。

**处理步骤**

检查hvigorfile.ts文件，确保模块名称是非空字符串。

## 00303139 hook必须是beforeNodeEvaluate或afterNodeEvaluate

**错误信息**

node Hook must be beforeNodeEvaluate or afterNodeEvaluate.

**错误描述**

hook必须是beforeNodeEvaluate或afterNodeEvaluate。

**可能原因**

hook不是beforeNodeEvaluate或afterNodeEvaluate。

**处理步骤**

确保hook类型是beforeNodeEvaluate或afterNodeEvaluate。

## 00303140 找不到节点

**错误信息**

Cannot find Node, at file:XXX.

**错误描述**

通过节点名找不到节点。

**可能原因**

模块名称配置错误。

**处理步骤**

确保XXX文件中的模块名称配置正确。

## 00303143 找不到任务

**错误信息**

Can not find task XXX.At file:YYY.

**错误描述**

通过任务名找不到任务XXX。

**可能原因**

任务名称配置错误。

**处理步骤**

确保YYY文件中的模块名称配置正确。

## 00303144 任务路径不是有效的值

**错误信息**

XXX is not a valid task node key. The values of moduleName and taskName cannot contain ':'.

**错误描述**

XXX不是有效的任务节点的key，moduleName和taskName的值不能包含':'。

**可能原因**

hvigorfile.ts中moduleName和taskName包含':'这种字符。

**处理步骤**

确保hvigorfile.ts中moduleName和taskName的值不包含':'。

## 00303145 任务名重复

**错误信息**

Duplicate task: XXX. Rename the task. At file: YYY.

**错误描述**

任务名重复。

**可能原因**

自定义任务与已有任务名称重复。

**处理步骤**

确保自定义任务与已有任务名称不重复。

## 00303146 oh-package.json5中version字段格式不符合要求

**错误信息**

XXX file version format is not compliant, please check.

**错误描述**

文件XXX中version字段格式不符合要求**。**

**可能原因**

模块级oh-package.json5的version字段不符合[semver](https://semver.org/)规范。

**处理步骤**

按照semver规范修改version字段。

## 00303147 bundleType为shared时，模块类型也必须是shared

**错误信息**

module type must be shared when bundleType is shared.module name : XXX.

**错误描述**

bundleType配置为shared时，模块类型也必须是shared。

**可能原因**

app.json5中bundleType配置为shared，但XXX模块module.json5的type不是shared。

**处理步骤**

通过以下任意一种方式解决：

* 将XXX模块module.json5中的type设置为shared。
* 将app.json5中的bundleType设置为非shared。

## 00303148 找不到hvigorfile.ts

**错误信息**

Hvigorfile not found: XXX.

**错误描述**

找不到hvigorfile.ts。

**可能原因**

可能hvigorfile.ts的文件名被修改或文件被删除。

**处理步骤**

确保工程和模块下各包含一个hvigorfile.ts。

## 00303149 通过文件路径找不到文件

**错误信息**

Path not found: XXX.

**错误描述**

通过文件路径找不到文件。

**可能原因**

文件路径配置错误。

**处理步骤**

根据报错提示信息，检查对应的文件路径。

## 00303153 json5文件路径不存在

**错误信息**

XXX is not exist.

**错误描述**

json5文件路径不存在。

**可能原因**

文件路径拼写错误。

**处理步骤**

确保文件路径是正确的。

## 00303155 路径不是文件路径

**错误信息**

the path: XXX is not a file path.

**错误描述**

路径XXX不是文件路径。

**可能原因**

XXX是文件夹。

**处理步骤**

确保文件路径正确且存在。

## 00303157 config.json文件中ability名称重复

**错误信息**

Check the ability name in the config.json file and make sure it is unique.

**错误描述**

检查config.json文件中的ability名称，确保唯一。

**可能原因**

config.json文件中ability名称重复。

**处理步骤**

检查config.json文件中的ability名称，确保唯一。

## 00303158 config.json文件中卡片名称重复

**错误信息**

Check the form name in the config.json file and make sure it is unique.

**错误描述**

检查config.json文件中的卡片名称，确保唯一。

**可能原因**

config.json文件中表单名称重复。

**处理步骤**

检查config.json文件中的卡片名称，确保唯一。

## 00303159 FA模型不支持修改XXX文件

**错误信息**

FA mode does not support modifying the XXX.

**错误描述**

FA模型不支持修改XXX文件。

**可能原因**

在FA模型下修改了XXX文件。

**处理步骤**

改为使用Stage模型。

## 00303160 插件配置只能使用相对路径

**错误信息**

Only relative path is allowed.

**错误描述**

只允许相对路径。

**可能原因**

hvigorfile.ts中插件配置使用了绝对路径。

**处理步骤**

确保hvigorfile.ts中的插件配置是相对路径。

## 00303161 插件路径不存在

**错误信息**

plugin path XXX not exists.

**错误描述**

插件路径XXX不存在。

**可能原因**

路径可能拼写错误。

**处理步骤**

确保插件路径正确。

## 00303164 插件文件必须以.ts结尾

**错误信息**

plugin file XXX must end with .ts.

**错误描述**

插件文件XXX必须以.ts结尾。

**可能原因**

插件文件不是以.ts结尾。

**处理步骤**

确保插件文件以.ts结尾。

## 00303166 copyFrom存在循环依赖

**错误信息**

buildOptionSet config buildOption: XXX copyFrom has circle.

**错误描述**

buildOptionSet下的XXX配置，copyFrom路径存在循环依赖。

**可能原因**

buildOptionSet下的XXX配置，copyFrom路径存在循环依赖。

**处理步骤**

检查copyFrom路径，确保不存在循环依赖。

## 00303168 SDK组件缺失

**错误信息**

SDK component missing. Please verify the integrity of your SDK.

**错误描述**

SDK组件缺失。

**可能原因**

配置了错误的SDK。

**处理步骤**

* 确保SDK路径正确：$DevEco Studio安装目录/sdk/default。
* 重新[下载DevEco Studio](https://developer.huawei.com/consumer/cn/download/)。

## 00303169 har模块中找不到对应的target

**错误信息**

Unable to find target 'XXX' in module 'YYY'. Make sure module 'YYY' has the same target as module 'ZZZ'.

**错误描述**

YYY模块中找不到target XXX，确保YYY模块和ZZZ模块有相同的target。

**可能原因**

模块ZZZ依赖模块YYY，通过命令行编译ZZZ模块时，同时给模块YYY和ZZZ指定了target XXX，但模块YYY中没有target XXX。

**处理步骤**

确保YYY模块和ZZZ模块有相同的target XXX。

## 00303170 hsp模块中找不到对应的target

**错误信息**

Unable to find target 'XXX' in module 'YYY'. Make sure module 'YYY' has the same target as module 'ZZZ'.

**错误描述**

YYY模块中找不到target XXX，确保YYY模块和ZZZ模块有相同的target。

**可能原因**

模块ZZZ依赖模块YYY，通过命令行编译ZZZ模块时，同时给模块YYY和ZZZ指定了target XXX，但模块YYY中没有target XXX。

**处理步骤**

确保YYY模块和ZZZ模块有相同的target XXX。

## 00303172 transformLib的值不是文件

**错误信息**

Invalid transformLib value XXX is not File.

**错误描述**

无效的transformLib值，XXX不是文件。

**可能原因**

transformLib对应的文件路径错误。

**处理步骤**

确保transformLib对应的文件路径正确。

## 00303173 在Windows上transformLib的值需要是.dll文件

**错误信息**

Invalid transformLib value, it requires a .dll file in Windows.

**错误描述**

无效的transformLib值，在Windows上需要一个.dll文件。

**可能原因**

在Windows系统上，transformLib的值不是需.dll文件类型。

**处理步骤**

确保transformLib的值是.dll文件。

## 00303179 metadata.resource必须是字符串

**错误信息**

metadata.resource must be string in file: XXX.

**错误描述**

metadata.resource必须是字符串。

**可能原因**

metadata.resource配置为其他类型的值。

**处理步骤**

确保metadata.resource为字符串类型。

## 00303181 metadata.resource存在无法解析的符号

**错误信息**

Cannot resolve symbol metadata.resource. At file XXX.

**错误描述**

metadata.resource存在无法解析的符号。

**可能原因**

metadata.resource对应的文件路径配置错误。

**处理步骤**

确保路径正确，且文件存在。

## 00303183 版本号不是string类型

**错误信息**

Invalid dependency: Version XXX is not a string.

**错误描述**

无效的依赖：版本号XXX不是string类型。

**可能原因**

hvigorfile.ts中的版本号不是string类型。

**处理步骤**

检查hvigorfile.ts文件的setVersion接口，确保接口的参数为string类型。

## 00303184 依赖值不是string类型

**错误信息**

Invalid dependency: DependencyVersion XXX is not a string.

**错误描述**

无效的依赖：依赖值XXX不是string类型。

**可能原因**

hvigorfile.ts文件的依赖值XXX不是string类型。

**处理步骤**

检查hvigorfile.ts文件，确保XXX是string类型。

## 00303185 不能动态新增或删除products

**错误信息**

Cannot add or delete products, at file:XXX.

**错误描述**

不能新增或删除products。

**可能原因**

通过hvigorfile.ts插件的setBuildProfileOpt接口新增或删除了工程级build-profile.json5文件中的products。

**处理步骤**

检查hvigorfile.ts文件，确保没有新增或删除products。

## 00303186 不能重命名products或runtimeOS

**错误信息**

Cannot rename products or runtimeOS. Keep the name or runtimeOS XXX unchanged.

**错误描述**

不能重命名products或runtimeOS，保持名称XXX不变。

**可能原因**

通过hvigorfile.ts插件的setBuildProfileOpt接口修改了工程级build-profile.json5文件中products下的name和runtimeOS。

**处理步骤**

检查hvigorfile.ts文件，确保没有修改products下的name和runtimeOS。

## 00303188 moduleType值无效

**错误信息**

moduleType: XXX is an invalid value.

**错误描述**

moduleType值XXX无效。

**可能原因**

moduleType配置错误或拼写错误。

**处理步骤**

请修改module.json5或config.json文件中**module > type**字段的值。可取值范围包含：entry、feature、har、shared。

## 00303189 runtimeOS值无效

**错误信息**

runtimeOS: XXX is an invalid value. Please check it.

**错误描述**

runtimeOS值XXX无效。

**可能原因**

runtimeOS配置错误或拼写错误。

**处理步骤**

确保build-profile.json5文件中，runtimeOS的值为OpenHarmony或HarmonyOS。

## 00303190 Page Ability缺少对应的JS组件

**错误信息**

A Page ability requires a JS component with the same name at XXX.

**错误描述**

Page Ability需要一个与其同名的JS组件。

**可能原因**

config.json文件中未定义对应的JS组件，或者JS组件名称与Page Ability不匹配或拼写错误。

**处理步骤**

确保在config.json文件中包含一个与Page Ability同名的JS组件。

## 00303191 FA模型Ability名称不存在

**错误信息**

Ability name XXX does not exist in config.json.

**错误描述**

config.json文件中找不到名为XXX的Ability。

**可能原因**

config.json文件中未定义XXX Ability或者拼写错误。

**处理步骤**

确保config.json文件中Ability XXX存在且正确。

## 00303192 FA模型项目中feature模块必须配置entryModules

**错误信息**

entryModules must be configured for a feature module in FA project.

**错误描述**

FA模型项目的feature模块必须配置entryModules。

**可能原因**

模块级build-profile.json5文件中未配置entryModules。

**处理步骤**

在模块级build-profile.json5文件中配置entryModules。

## 00303193 FA模型中找不到模块的deviceType配置

**错误信息**

Unable to obtain the module deviceType.

**错误描述**

无法获取模块的deviceType。

**可能原因**

config.json文件中缺少deviceType字段。

**处理步骤**

确保config.json文件存在且格式正确，并正确配置deviceType字段信息。

## 00303194 Stage模型中找不到模块的deviceTypes配置

**错误信息**

Unable to obtain the module deviceTypes.

**错误描述**

无法获取模块的deviceTypes。

**可能原因**

module.json5文件中缺少deviceTypes字段。

**处理步骤**

确保module.json5文件存在且格式正确，并正确配置deviceTypes字段信息。

## 00303195 无法获取模块信息

**错误信息**

Unable to obtain the module information at file: XXX.

**错误描述**

无法从module.json5文件中获取模块信息。

**可能原因**

module.json5文件缺少module字段。

**处理步骤**

确保module.json5文件中的module字段已正确配置。

## 00303196 无法获取模块类型

**错误信息**

Unable to obtain the module type at file: XXX.

**错误描述**

无法获取模块类型。

**可能原因**

module.json5文件中缺少type字段。

**处理步骤**

确保module.json5文件中的module.type字段已正确配置。

## 00303197 缺少或无效的parameterFile配置

**错误信息**

Missing or invalid config of parameterFile in the project-level oh-package.json5 file. Check at file: XXX.

**错误描述**

工程级oh-package.json5文件中缺少parameterFile字段，或该字段的配置无效。

**可能原因**

工程级oh-package.json5文件中未定义parameterFile字段或者parameterFile配置错误或格式无效。

**处理步骤**

在工程级oh-package.json5文件中添加[parameterFile](ide-oh-package-json5.md#section122411462820)字段，并确保配置正确。

## 00303198 build-profile.json5文件不符合schema规范

**错误信息**

The project-level build-profile.json5 file does not comply with the schema.

**错误描述**

工程级build-profile.json5文件未遵循schema规范。

**可能原因**

1. build-profile.json5文件直接从其他模块复制，导致格式或字段不兼容。
2. 模块级hvigorfile.ts文件的system字段错误地配置为appTasks。

**处理步骤**

1. 检查工程级build-profile.json5文件，移除从其他模块直接复制的字段，确保字段符合规范。
2. 检查模块级hvigorfile文件，根据模块类型选择以下插件进行配置：hapTasks/hspTasks/harTasks。

## 00303199 build-profile.json5中找不到product信息

**错误信息**

No products found in the build-profile.json5 file. At file: XXX.

**错误描述**

工程级build-profile.json5文件中找不到products配置。

**可能原因**

工程级build-profile.json5文件中缺少products字段。

**处理步骤**

在工程级build-profile.json5文件中配置products。

## 00303200 模块名称无效

**错误信息**

Invalid module name settings in these modules: 'XXX'. Check whether the module is valid.

**错误描述**

模块名称XXX无效。

**可能原因**

ArkUI-X工程的arkui-x-config.json5文件中，模块名称modules错误。

**处理步骤**

确保modules对应的模块名称正确。

## 00303201 模块target不存在

**错误信息**

The module target XXX is not found in the YYY.

**错误描述**

在模块YYY中未找到target XXX。

**可能原因**

模块YYY中未定义target XXX。

**处理步骤**

检查命令行的target，或者模块build-profile.json5中的target配置是否正确。

## 00303202 entry模块缺失

**错误信息**

No available entry module found.

**错误描述**

找不到可用的entry模块。

**可能原因**

1. 模块级build-profile.json5文件中缺少entryModules配置。
2. 所关联的entry模块未正确定义或拼写错误。

**处理步骤**

检查feature模块级build-profile.json5文件，确保存在entryModules且字段正确配置。

## 00303203 命令行中的构建模式没有在buildModeSet中定义

**错误信息**

Build mode XXX used in command line is not declared in buildModeSet in file: YYY.

**错误描述**

命令行中使用的构建模式XXX没有在YYY文件的buildModeSet字段中定义。

**可能原因**

工程级build-profile.json5中未定义XXX构建模式。

**处理步骤**

在工程级build-profile.json5的buildModeSet字段中添加XXX构建模式。

## 00303204 buildModeBinder中的构建模式没有在buildModeSet中定义

**错误信息**

Build mode XXX used in buildModeBinder is not declared in buildModeSet in file: YYY.

**错误描述**

buildModeBinder中使用的构建模式XXX没有在YYY文件的buildModeSet字段中定义。

**可能原因**

YYY文件中未定义XXX构建模式。

**处理步骤**

在YYY文件的buildModeSet字段中添加XXX构建模式。

## 00303205 buildModeBinder中的target未定义

**错误信息**

Target XXX used in buildModeBinder is not declared in file: YYY.

**错误描述**

buildModeBinder中使用的targetName XXX没有在YYY文件中定义。

**可能原因**

YYY文件中未定义XXX target。

**处理步骤**

在YYY文件的targets字段中添加XXX。

## 00303206 buildModeBinder中的构建选项未定义

**错误信息**

Build option XXX used in buildModeBinder is not declared in file: YYY.

**错误描述**

buildModeBinder中使用的buildOptionName XXX没有在YYY文件的buildOptionSet字段中定义。

**可能原因**

YYY文件中未定义XXX构建选项。

**处理步骤**

在YYY文件的buildOptionSet字段中添加XXX构建选项。

## 00303207 找不到ArkUI-X SDK目录

**错误信息**

Unable to find XXX in local.properties or YYY in the system environment path. Check at file: ZZZ.

**错误描述**

在local.properties或系统环境变量中找不到ArkUI-X SDK目录。

**可能原因**

1. 未下载ArkUI-X SDK。
2. local.properties文件未配置SDK路径XXX，或路径配置错误。
3. 本地系统中未配置环境变量YYY，或环境变量对应的SDK路径错误。

**处理步骤**

1. 在**File > Settings > ArkUI-X**（macOS为**DevEco Studio > Preferences/Settings > ArkUI-X**）下载SDK。
2. 在local.properties或本地系统环境变量中配置SDK路径，并且路径和SDK实际安装路径一致。

## 00303208 找不到SDK目录

**错误信息**

Unable to find XXX in local.properties or YYY in the system environment path. Check at file: ZZZ.

**错误描述**

系统未能找到XXX，导致SDK配置异常。

**可能原因**

1. local.properties文件中缺少XXX配置项。
2. 环境变量YYY未正确设置或路径错误。

**处理步骤**

1. 确保local.properties中已正确配置SDK路径，运行hvigorw--stop-daemon停止守护进程后重试。
2. 将YYY添加到系统环境变量路径中。

## 00303209 FA的entry模块缺少Target

**错误信息**

Unable to find target 'YYY' in module 'XXX'.

**错误描述**

在模块XXX中找不到target YYY。

**可能原因**

target YYY在XXX模块中未正确配置或缺失。

**处理步骤**

检查FA模型feature模块所关联的entry模块是否存在对应的target。

## 00303210 Arkdata JSON文件名称相同

**错误信息**

The XXX file in the YYY module has the same name as the ZZZ file in the AAA module.

**错误描述**

YYY模块中的XXX文件与AAA模块中的ZZZ文件名称相同。

**可能原因**

两个模块中存在同名的Arkdata JSON文件。

**处理步骤**

重命名其中一个文件，避免命名冲突。

## 00303211 模块缺少ohosTest target

**错误信息**

The module XXX does not exist ohosTest target, Failed to execute the command YYY.

**错误描述**

生成ohos测试覆盖率报告场景下，模块XXX未定义ohosTest target，导致命令 'ohosTest' 执行失败。

**可能原因**

模块级build-profile.json5文件中未配置ohosTest target。

**处理步骤**

检查XXX模块的build-profile.json5文件，确保存在name为ohosTest的target。

## 00303214 目标设备类型不一致

**错误信息**

The type of target device does not match the device type configured by module: XXX.Required device type:XXX, current module device type:XXX.

**错误描述**

目标设备类型与模块中配置的设备类型不一致。

**可能原因**

执行hvigorw命令时，指定的设备类型在module.json5或模块级build-profile.json5中未定义，或者设备类型被错误修改。

**处理步骤**

1. 确保在模块module.json5中配置的deviceTypes包含所需的设备类型。
2. 如果模块级build-profile.json5中targets字段下已定义deviceType，确保deviceType包含所需的设备类型。
3. 确保hvigorfile.ts或hvigorconfig.ts文件中没有修改设备类型。

## 00303215 依赖名称与包名不一致

**错误信息**

There are some dependency names that are inconsistent with the actual package names.

**错误描述**

有一些依赖名称与实际包名不一致。

**可能原因**

依赖名称配置与实际包名不一致。

**处理步骤**

根据报错提示信息检查依赖名称，确保和依赖包oh-package.json5中的name保持一致。

## 00303216 parameterFile文件格式无法识别

**错误信息**

Unrecognized archive format in parameterFile.

**错误描述**

ParameterFile文件格式无法识别。

**可能原因**

ParameterFile配置文件的依赖配置不是文件目录也不是har/tgz文件。

**处理步骤**

确保依赖配置是目录，或者是har/tgz文件。

## 00303217 环境路径无效

**错误信息**

Invalid value of 'XXX' in the system environment path.

**错误描述**

系统环境变量中的'XXX'值无效。

**可能原因**

系统环境路径中的'XXX'值设置错误。

**处理步骤**

修改环境路径XXX的值，再执行hvigorw --stop-daemon命令，然后重试。

## 00303218 配置user\_grant权限必须有reason和usedScene属性

**错误信息**

The reason and usedScene attributes are mandatory for user\_grant permissions.

**错误描述**

对于user\_grant权限，reason和usedScene属性是必需的。

**可能原因**

在module.json5文件中配置user\_grant类型的权限缺少reason或usedScene属性。

**处理步骤**

1. 对于HAP模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。
2. 对于HAR/HSP模块，在module.json5文件的requestPermissions中添加reason字段。

## 00303219 routerMap对象名称重复

**错误信息**

Duplicate 'routerMap' object names detected.

**错误描述**

检测到重复的“routerMap”对象名称。

**可能原因**

当前模块的router\_map.json中存在name重复的routerMap配置，或者当前模块与依赖模块存在name重复的routerMap配置。

**处理步骤**

修改router\_map.json文件中的name字段，保证name的值唯一。

## 00303220 获取模块类型失败

**错误信息**

Failed to obtain the module type.

**错误描述**

获取模块类型失败。

**可能原因**

1. 在FA模型中，config.json文件不存在。
2. 在FA模型中，config.json文件中的module/distro/moduleType字段缺失或者配置错误。

**处理步骤**

1. 确保config.json文件存在。
2. 确保在FA模型中，config.json文件中的module/distro/moduleType字段存在且配置正确。

## 00303221 权限未定义

**错误信息**

The XXX permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.

**错误描述**

requestPermissions下的XXX权限必须是SDK中预定义的值，或者是在definePermissions下包含的自定义值。

**可能原因**

在module.json5文件的requestPermissions中配置name时，配置了不存在的权限名称。

**处理步骤**

在module.json5文件的requestPermissions中配置name字段，必须是SDK中预定义的权限，或者在definePermissions下自定义的权限。

## 00303222 reason属性是必需的

**错误信息**

The reason attribute are mandatory for user\_grant permissions.

**错误描述**

对于user\_grant权限，reason属性是必需的。

**可能原因**

在module.json5文件中配置user\_grant类型的权限缺少reason属性。

**处理步骤**

1. 对于HAP模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。
2. 对于HAR/HSP模块，在module.json5文件的requestPermissions中添加reason字段。

## 00303223 FormExtensionAbility中的metadata字段不能为空或为空数组

**错误信息**

The metadata field in FormExtensionAbility cannot be left blank or as an empty array.

**错误描述**

FormExtensionAbility中的metadata字段不能为空或为空数组。

**可能原因**

module.json5中type为form的ExtensionAbility中的metadata字段为空或者空数组。

**处理步骤**

在module.json5中type为form的ExtensionAbility中配置[metadata字段](arkts-ui-widget-configuration.md)。

## 00303224 FormExtensionAbility中的metadata必须包含ohos.extension.form

**错误信息**

In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.

**错误描述**

在FormExtensionAbility中，metadata必须包含一个对象，其名称设置为“ohos.extension.form”，资源设置为二级资源引用。

**可能原因**

module.json5中type为form的ExtensionAbility中的metadata缺少name为“ohos.extension.form”的对象值，或者缺少resource字段。

**处理步骤**

在module.json5中type为form的ExtensionAbility中增加metadata字段，补充一个name为“ohos.extension.form”的对象值，并配置对应的resource值，具体配置方式参考[配置卡片的配置文件](arkts-ui-widget-configuration.md)。

## 00303225 “Module-Abilities”对象的名称重复

**错误信息**

Duplicate 'Module-Abilities' object names detected.

**错误描述**

“Module-Abilities”对象的名称重复。

**可能原因**

本模块和依赖har模块的module.json5中存在name值相同的abilities对象或extensionAbilities对象。

**处理步骤**

检查本模块和依赖har模块的module.json5中的abilities对象或extensionAbilities对象的name值，确保name值唯一。

## 00303226 卡片名称无效

**错误信息**

Invalid form name 'XXX'.

**错误描述**

卡片名称无效。

**可能原因**

卡片名称XXX在form\_config.json中未定义。

**处理步骤**

确保卡片名称在form\_config.json文件中已配置。

## 00303227 缺失“string”属性

**错误信息**

File 'string.json' is missing the required property 'string'.

**错误描述**

资源文件“string.json”缺少必需的属性“string”。

**可能原因**

资源文件“string.json”缺少必需的属性“string”。

**处理步骤**

确保“string.json”文件包含名为“string”的属性。

## 00303228 version字段不允许使用tag标签

**错误信息**

The 'tag' keyword is not allowed for 'version' at XXX.

**错误描述**

oh-package.json5的version字段不允许使用tag标签。

**可能原因**

使用parameterFile参数化配置版本号时，oh-package.json5的version字段不允许使用tag标签。

**处理步骤**

oh-package.json5中的version字段引用parameterFile时，不使用tag标签。

## 00303229 找不到模块名

**错误信息**

The required attribute: module-name is missing.

**错误描述**

缺少必需属性：module-name。

**可能原因**

1. 工程级build-profile.json5中modules下的name字段缺失。
2. hvigorconfig.ts动态添加模块时未设置name参数。

**处理步骤**

1. 检查项目根目录下的build-profile.json5文件，确保modules下的name字段存在且非空。
2. 检查项目根目录下的[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)，确保includeNode方法的参数name字段存在且非空。

## 00303230 找不到模块的srcPath

**错误信息**

The required attribute module-srcPath is missing.

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

1. 工程级build-profile.json5中modules下的srcPath字段缺失。
2. hvigorconfig.ts动态添加模块时未设置srcPath参数。

**处理步骤**

1. 检查项目根目录下的build-profile.json5文件，确保modules下的srcPath字段存在且非空。
2. 检查项目根目录下的[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)，确保includeNode方法的参数srcPath字段存在且非空。

## 00303231 srcPath属性值不是相对路径

**错误信息**

The srcPath is not a relative path: XXX.

**错误描述**

srcPath属性值不是相对路径。

**可能原因**

hvigorconfig.ts动态添加模块时srcPath属性值不是相对路径。

**处理步骤**

检查项目根目录下的[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)，确保includeNode方法的参数srcPath字段为相对路径。

## 00303232 设置任务依赖时找不到模块

**错误信息**

Failed to find the XXX node while setting the task dependencies in the YYY module's task: ZZZ.

**错误描述**

设置任务依赖时找不到模块。

**可能原因**

任务依赖中的模块名字配置错误。

**处理步骤**

检查hvigorfile.ts文件，确保任务依赖中的模块名字配置正确。

## 00303234 找不到路径

**错误信息**

Path not found. At path: XXX.

**错误描述**

找不到路径。

**可能原因**

路径配置错误。

**处理步骤**

根据报错信息提示，确保路径配置正确。

## 00303236 hvigor-config.json5文件中存在语法错误

**错误信息**

以实际语法错误为准。

**错误描述**

hvigor-config.json5文件中存在语法错误。

**可能原因**

hvigor-config.json5文件中存在语法错误，具体错误请参阅报错信息。

**处理步骤**

根据报错信息处理hvigor-config.json5文件中的语法错误。

## 00303237 hvigor-config.json5中ohos.align.target的值必须是字符串类型

**错误信息**

The value of 'ohos.align.target' in hvigor-config.json5 must be a string.

**错误描述**

hvigor-config.json5中ohos.align.target的值必须是字符串类型。

**可能原因**

hvigor-config.json5中ohos.align.target的值不是字符串类型。

**处理步骤**

确保ohos.align.target的值是字符串类型。

## 00303238 ability名称无效

**错误信息**

Invalid ability name XXX. At file: YYY.

**错误描述**

ability名称XXX无效。

**可能原因**

意图框架配置文件insight\_intent.json中的insightIntents字段下的uiAbility对象的ability属性值无效。

**处理步骤**

确保在module.json5文件中abilities字段下配置了name为XXX的ability。

## 00303242 签名材料校验失败

**错误信息**

Signature material verification failed, as: XXX.

**错误描述**

签名材料校验失败。

**可能原因**

签名材料损坏。

**处理步骤**

点击**File > Project Structure > Project > Signing Configs**重新签名。

## 00303243 ability名称无效

**错误信息**

Invalid ability name XXX. At file: YYY.

**错误描述**

ability名称XXX无效。

**可能原因**

意图框架配置文件insight\_intent.json中insightIntents字段下的serviceExtension对象的ability属性值无效。

**处理步骤**

确保在module.json5文件中的extensionAbilities字段下存在name值为XXX的extension ability，并且type类型为service。

## 00303244 ability名称无效

**错误信息**

Invalid ability name XXX. At file: YYY.

**错误描述**

ability名称XXX无效。

**可能原因**

意图框架配置文件insight\_intent.json中insightIntents字段下的form对象的ability属性值无效。

**处理步骤**

确保在module.json5文件中的extensionAbilities字段下存在name值为XXX的extension ability，并且type类型为form。

## 00303245 ability名称无效

**错误信息**

Invalid ability name XXX. At file: YYY.

**错误描述**

ability名称XXX无效。

**可能原因**

意图框架配置文件insight\_intent.json中insightIntents字段下的uiExtension对象的ability属性值无效。

**处理步骤**

确保在module.json5文件中的abilities或extensionAbilities字段下配置了name为XXX的ability。

## 00303249 任务之间存在循环依赖关系

**错误信息**

Circular dependency between the following tasks.

**错误描述**

任务之间存在循环依赖关系。

**可能原因**

用户配置自定义任务的依赖关系，任务之间存在循环依赖。

**处理步骤**

根据提示信息，移除导致循环依赖的任务。

## 00303250 FA模型工程不支持preloadSystemSo

**错误信息**

FA mode does not support 'preloadSystemSo'.

**错误描述**

FA模型工程不支持preloadSystemSo。

**可能原因**

工程级build-profile.json5的buildOption下配置preloadSystemSo为true。

**处理步骤**

移除preloadSystemSo，或将preloadSystemSo配置为false。

## 00303251 preloadSystemSo与ohos.arkCompile.singleFileEmit不能同时开启

**错误信息**

'ohos.arkCompile.singleFileEmit' does not support when 'preloadSystemSo' is set to true.

**错误描述**

preloadSystemSo与ohos.arkCompile.singleFileEmit不能同时开启。

**可能原因**

工程级build-profile.json5的preloadSystemSo配置为true，同时hvigor-config.json5的ohos.arkCompile.singleFileEmit配置为true。

**处理步骤**

* 移除ohos.arkCompile.singleFileEmit，或将ohos.arkCompile.singleFileEmit配置为false。
* 移除preloadSystemSo，或将preloadSystemSo配置为false。

## 00303252 找不到模块

**错误信息**

Referenced module XXX not found.

**错误描述**

工程中找不到配置的模块。

**可能原因**

formExtensionModule/formWidgetModule对应的模块名称不存在。

**处理步骤**

确保模块在工程中存在。

## 00303253 formExtensionModule配置的模块类型错误

**错误信息**

formExtensionModule can only reference entry or feature modules, but XXX is of type YYY.

**错误描述**

formExtensionModule只能指向feature模块或者entry模块，但是模块XXX的类型是YYY。

**可能原因**

formExtensionModule指向的模块类型不是entry或feature。

**处理步骤**

确保formExtensionModule指向一个entry或者feature类型的模块。

## 00303254 独立卡片包关联的模块错误

**错误信息**

Referenced module XXX must have formWidgetModule/formExtensionModule pointing back to YYY to establish a bidirectional reference.

**错误描述**

模块XXX的formWidgetModule/formExtensionModule需要指向模块YYY来确保两个模块双向关联。

**可能原因**

formWidgetModule/formExtensionModule字段没有配置为模块XXX或YYY。

**处理步骤**

1. 确保XXX模块中的formWidgetModule/formExtensionModule字段配置为YYY。
2. 确保YYY模块中的formWidgetModule/formExtensionModule字段配置为XXX。

## 00303255 共包卡片和独立卡片包不能同时存在

**错误信息**

Embedded widgets and standalone widgets must not be used together.

**错误描述**

共包卡片和独立卡片包不能同时存在。

**可能原因**

当使用独立卡片包时，在应用包entry和卡片包library中同时存在form\_config.json文件。

**处理步骤**

移除独立卡片包或移除共包卡片。

## 00303256 独立卡片包的library模块只允许依赖HAR模块

**错误信息**

When a module is a standalone widget, all of its dependencies must be HAR modules.

**错误描述**

独立卡片包的library模块只允许依赖HAR模块。

**可能原因**

独立卡片包的library模块的oh-package.json5中依赖了HSP模块。

**处理步骤**

将独立卡片包的library模块的oh-package.json5中的HSP依赖移除。

## 00303257 deliveryWithInstall未配置为true

**错误信息**

Field deliveryWithInstall was not set to true.

**错误描述**

deliveryWithInstall未配置为true。

**可能原因**

deliveryWithInstall未配置为true。

**处理步骤**

独立卡片包的应用包entry和卡片包library的module.json5中的deliveryWithInstall字段都需配置为true。

## 00303258 独立卡片包不支持在低于API 20的工程中使用

**错误信息**

Standalone widgets are not supported on API versions earlier than 20. Set compatibleSdkVersion to 6.0.0(20) or higher in the project-level build-profile.json5 file.

**错误描述**

独立卡片包不支持在低于API 20的工程中使用。

**可能原因**

使用独立卡片包的工程的compatibleSdkVersion低于6.0.0(20)。

**处理步骤**

将工程级build-profile.json5的compatibleSdkVersion配置为6.0.0(20)及以上。

## 00303259 formWidgetModule配置的模块类型错误

**错误信息**

formWidgetModule can only reference a hsp module, but XXX is of type YYY.

**错误描述**

formWidgetModule只能指向HSP模块，但是模块XXX的类型是YYY。

**可能原因**

formWidgetModule指向的模块类型不是HSP。

**处理步骤**

确保formWidgetModule指向一个HSP模块。

## 00303260 合并后的共享配置文件的uri重复

**错误信息**

Duplicate 'crossAppSharedConfig' object uris detected.

**错误描述**

不同模块合并后的共享配置文件的crossAppSharedConfig对象中存在重复的uri。

**可能原因**

当前模块和依赖模块的共享配置文件中存在重复的uri。

**处理步骤**

修改uri值，确保不重复。

## 00303261 当前模块的共享配置文件的uri重复

**错误信息**

Duplicate uri exists in the crossAppSharedConfig configuration file of the current module.

**错误描述**

当前模块的共享配置文件的crossAppSharedConfig对象中存在重复的uri。

**可能原因**

共享配置文件的crossAppSharedConfig对象中存在重复的uri。

**处理步骤**

修改uri值，确保不重复。

## 00303262 FA模型工程不支持expandImportPath

**错误信息**

FA mode does not support 'expandImportPath'.

**错误描述**

FA模型工程不支持expandImportPath。

**可能原因**

build-profile.json5中配置了expandImportPath。

**处理步骤**

移除expandImportPath。

## 00303263 expandImportPath.exclude配置不合法

**错误信息**

Dependency names: '[XXX]' configured in 'expandImportPath.exclude' are prohibited in current module.

**错误描述**

expandImportPath.exclude中不允许配置依赖XXX。

**可能原因**

build-profile.json5的expandImportPath.exclude配置的依赖别名不是本地HAR模块。

**处理步骤**

expandImportPath.exclude中移除依赖别名XXX。

## 00303265 sourceRoots文件路径无效

**错误信息**

Invalid value 'XXX' in module 'YYY'. At file: 'ZZZ'.

**错误描述**

模块YYY中的配置XXX无效。

**可能原因**

模块YYY的build-profile.json5中的sourceRoots字段的值无效。

**处理步骤**

确保sourceRoots字段对应的所有路径满足以下条件：

1. 每个路径都存在且唯一。
2. 路径是相对路径。
3. 路径在模块下，并且是一个目录。

## 00303267 找不到product XXX

**错误信息**

Can not find product XXX. At File: YYY.

**错误描述**

找不到product XXX。

**可能原因**

编译命令中指定的product在工程级build-profile.json5中未找到。

**处理步骤**

修改编译参数，使用正确的product。

## 00303268 hspA和hspB共同依赖的har包需要配置在hap的依赖中

**错误信息**

${har}: the common dependency of ${hspA} and ${hspB} must be declared in dependencies of ${hap}.

**错误描述**

hspA和hspB共同依赖的har包需要配置在hap的依赖中。

**可能原因**

har包没有配置在hap的依赖中。

**处理步骤**

在hap中配置har包依赖。

## 00303269 FA模型工程不支持deduplicateHar配置

**错误信息**

The FA model does not support the 'deduplicateHar' field. At file: XXX.

**错误描述**

FA模型工程不支持deduplicateHar配置。

**可能原因**

当前工程是FA模型工程。

**处理步骤**

移除deduplicateHar，或将其配置为false。

## 00303270 compatibleSdkVersion大于或等于21时才能启用deduplicateHar

**错误信息**

'deduplicateHar' can be enabled only when 'compatibleSdkVersion' is greater than or equal to 21. At file: XXX.

**错误描述**

compatibleSdkVersion大于或等于21时才能启用deduplicateHar。

**可能原因**

工程级build-profile.json5的compatibleSdkVersion小于21。

**处理步骤**

配置compatibleSdkVersion大于或等于21，或者将deduplicateHar配置为false。

## 00303271 idDefinedFilePath必须是实际存在的json5文件

**错误信息**

'idDefinedFilePath': XXX must be an existing json5 file. At file: YYY.

**错误描述**

idDefinedFilePath必须是实际存在的json5文件。

**可能原因**

idDefinedFilePath路径不存在或者不是json5文件。

**处理步骤**

确保idDefinedFilePath是一个实际存在的json5文件。

## 00303272 当deduplicateHar为true时必须配置idDefinedFilePath字段

**错误信息**

When 'deduplicateHar' is enabled, the 'idDefinedFilePath' field must be configured. At file: XXX.

**错误描述**

当deduplicateHar为true时必须配置idDefinedFilePath字段。

**可能原因**

缺少idDefinedFilePath配置。

**处理步骤**

在buildOption/resOptions下配置idDefinedFilePath字段。

## 00303273 deduplicateHar字段仅支持一个product中包含一个HAP的场景

**错误信息**

The 'deduplicateHar' field supports only one HAP per product. Now there are XXX haps: YYY in product ZZZ

**错误描述**

deduplicateHar字段仅支持一个product中包含一个HAP的场景。

**可能原因**

当前product中有多个HAP。

**处理步骤**

确保每个product中只有一个HAP。

## 00303274 当deduplicateHar为true时, libIsolation不能配置为true

**错误信息**

When 'deduplicateHar' is enabled, the 'libIsolation' field cannot be set to true. At file: XXX.

**错误描述**

当deduplicateHar为true时, libIsolation不能配置为true。

**可能原因**

deduplicateHar和libIsolation同时配置为true。

**处理步骤**

将libIsolation配置为false。

## 00303275 当deduplicateHar为true时, useNormalizedOHMUrl必须配置为true

**错误信息**

When 'deduplicateHar' is enabled, the 'useNormalizedOHMUrl' field must be set to true. At file: XXX.

**错误描述**

当deduplicateHar为true时, useNormalizedOHMUrl必须配置为true。

**可能原因**

useNormalizedOHMUrl没有配置为true。

**处理步骤**

将useNormalizedOHMUrl配置为true。

## 00303276 构建定制化har时，当前模块必须为字节码har

**错误信息**

The har module must be set to byte code har when building customized har. At file: XXX.

**错误描述**

构建定制化har时，当前模块必须为字节码har。

**可能原因**

当在har模块的buildOption下配置packingOptions.customizedOptions.basePackage开启构建定制化har后，当前模块并未配置为字节码har。

**处理步骤**

将当前har模块配置为[字节码har](ide-hvigor-build-har.md#section16598338112415)。

## 00303277 构建定制化har时，ohos.compile.lib.entryfile不能设置为true

**错误信息**

ohos.compile.lib.entryfile must not set to true when building customized har. At file: XXX.

**错误描述**

构建定制化har时，ohos.compile.lib.entryfile不能设为true。

**可能原因**

当在har模块的buildOption下配置packingOptions.customizedOptions.basePackage开启构建定制化har后，hvigor-config.json5中ohos.compile.lib.entryfile配置为true。

**处理步骤**

将ohos.compile.lib.entryfile配置为false或者删除该配置项。

## 00303278 模块下的hvigorfile.ts中获取不到插件

**错误信息**

Unable to get plugin in hvigorfile.ts of module 'XXX'. At file: YYY.

**错误描述**

模块下的hvigorfile.ts中获取不到插件。

**可能原因**

1. 模块下的hvigorfile.ts中使用了未定义的属性或方法。
2. 模块下的hvigorfile.ts中导出的deafult对象的system字段值和本模块module.json5中的type字段值不匹配。

**处理步骤**

1. 检查模块下的hvigorfile.ts中是否使用了未定义的属性或方法。
2. 确保模块下的hvigorfile.ts中导出的deafult对象的system字段值和本模块module.json5中的type字段相匹配，匹配规则如下图。

   | type字段 | system字段 |
   | --- | --- |
   | entry | hapTasks |
   | feature | hapTasks |
   | shared | hspTasks |
   | har | harTasks |

## 00303280 开启binxo时，确保-DOHOS\_ENABLE\_HWASAN和-DOHOS\_ENABLE\_BINXO参数设置为ON

**错误信息**

Before enabling binxo, ensure that both '-DOHOS\_ENABLE\_HWASAN' and '-DOHOS\_ENABLE\_BINXO' parameters are set to ON. At file: XXX.

**错误描述**

在开启binxo之前，确保-DOHOS\_ENABLE\_HWASAN和-DOHOS\_ENABLE\_BINXO两个参数都设置为ON。

**可能原因**

开启binxo时，-DOHOS\_ENABLE\_HWASAN未设置或设置为OFF，-DOHOS\_ENABLE\_BINXO设置为ON，参数设置不正确。

**处理步骤**

将'externalNativeOptions > arguments'设置为'-DOHOS\_ENABLE\_HWASAN=ON -DOHOS\_ENABLE\_BINXO=ON'。

## 00303282 useNormalizedOHMUrl为true时才能配置oh-exports

**错误信息**

'oh-exports' is configurable only when 'useNormalizedOHMUrl' is true.

**错误描述**

useNormalizedOHMUrl为true时才能配置oh-exports。

**可能原因**

useNormalizedOHMUrl为false。

**处理步骤**

检查工程级build-profile.json5的useNormalizedOHMUrl字段，确保配置为true。

## 00303283 仅支持模块内有效的相对路径

**错误信息**

Invalid path XXX. Only valid relative paths within the module are supported.

**错误描述**

路径无效，仅支持模块内有效的相对路径。

**可能原因**

oh-exports中包含无效的路径。

**处理步骤**

检查oh-exports中配置的路径，确保是模块内有效的相对路径。

## 00303284 仅支持目录或者以ets/ts/js为后缀的文件

**错误信息**

Invalid path XXX. Only directories or .ets/.ts/.js files are supported.

**错误描述**

路径无效，仅支持目录或者以ets/ts/js为后缀的文件。

**可能原因**

文件后缀不是ets/ts/js。

**处理步骤**

检查oh-exports中配置的路径，确保是目录或以ets/ts/js为后缀的文件。

## 00303285 hvigor命令行参数buildVersion无效

**错误信息**

-p buildVersion=XXX is invalid.

**错误描述**

hvigor命令行参数buildVersion无效。

**可能原因**

hvigor命令行参数buildVersion不符合要求。

**处理步骤**

确保buildVersion是一个有效值，具体要求请参考[app.json5的buildVersion](app-configuration-file.md#配置文件标签)。
