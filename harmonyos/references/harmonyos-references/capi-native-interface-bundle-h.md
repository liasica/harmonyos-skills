---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h
title: native_interface_bundle.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > native_interface_bundle.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:59+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:f0a20363059826ffcea06e65927bd1b3c0acbb6d7156c6a28eeca239abb5c4de
---

## 概述

PhonePC/2in1TabletTVWearable

提供查询应用包信息的功能，包括应用包名、应用指纹、应用appId等。

**引用文件：** <bundle/native\_interface\_bundle.h>

**库：** libbundle\_ndk.z.so

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 9

**相关模块：** [Native\_Bundle](capi-native-bundle.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeBundle\_ApplicationInfo](capi-native-bundle-oh-nativebundle-applicationinfo.md) | OH\_NativeBundle\_ApplicationInfo | 应用包信息数据结构，包含应用包名和应用指纹信息。 |
| [OH\_NativeBundle\_ElementName](capi-native-bundle-oh-nativebundle-elementname.md) | OH\_NativeBundle\_ElementName | elementName信息。 |
| [OH\_NativeBundle\_Metadata](capi-native-bundle-oh-nativebundle-metadata.md) | OH\_NativeBundle\_Metadata | 元数据信息。 |
| [OH\_NativeBundle\_ModuleMetadata](capi-native-bundle-oh-nativebundle-modulemetadata.md) | OH\_NativeBundle\_ModuleMetadata | 模块元数据的信息。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_NativeBundle\_ApplicationInfo OH\_NativeBundle\_GetCurrentApplicationInfo()](capi-native-interface-bundle-h.md#oh_nativebundle_getcurrentapplicationinfo) | 获取当前应用信息，包含应用包名和应用指纹信息。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回对象下的字段的指针。 |
| [char\* OH\_NativeBundle\_GetAppId()](capi-native-interface-bundle-h.md#oh_nativebundle_getappid) | 获取当前应用的appId。appId是应用的唯一标识，由应用包名和签名信息决定。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。 |
| [char\* OH\_NativeBundle\_GetAppIdentifier()](capi-native-interface-bundle-h.md#oh_nativebundle_getappidentifier) | 获取当前应用的应用程序标识符。该应用程序标识符在应用的整个生命周期中不会发生变化，包括版本更新、证书更改、公钥和私钥更改以及应用程序迁移。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。 |
| [OH\_NativeBundle\_ElementName OH\_NativeBundle\_GetMainElementName()](capi-native-interface-bundle-h.md#oh_nativebundle_getmainelementname) | 获取当前应用入口元素mainElement的信息，包括包名、模块名和组件名。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回对象下的字段的指针。 |
| [char\* OH\_NativeBundle\_GetCompatibleDeviceType()](capi-native-interface-bundle-h.md#oh_nativebundle_getcompatibledevicetype) | 获取当前应用适用的设备类型。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。 |
| [bool OH\_NativeBundle\_IsDebugMode(bool\* isDebugMode)](capi-native-interface-bundle-h.md#oh_nativebundle_isdebugmode) | 查询当前应用的调试模式。 |
| [OH\_NativeBundle\_ModuleMetadata\* OH\_NativeBundle\_GetModuleMetadata(size\_t\* size)](capi-native-interface-bundle-h.md#oh_nativebundle_getmodulemetadata) | 获取当前应用程序的模块元数据数组。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。 |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityResourceInfo(char\* fileType, OH\_NativeBundle\_AbilityResourceInfo\*\* abilityResourceInfo, size\_t\* size)](capi-native-interface-bundle-h.md#oh_nativebundle_getabilityresourceinfo) | 获取支持打开特定文件类型的组件资源信息列表。在使用完该接口之后，为了防止内存泄漏，需要调用[OH\_AbilityResourceInfo\_Destroy](capi-ability-resource-info-h.md#oh_abilityresourceinfo_destroy)进行释放。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NativeBundle\_GetCurrentApplicationInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeBundle_ApplicationInfo OH_NativeBundle_GetCurrentApplicationInfo()
```

**描述**

获取当前应用信息，包含应用包名和应用指纹信息。

**起始版本：** 9

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeBundle\_ApplicationInfo](capi-native-bundle-oh-nativebundle-applicationinfo.md) | 返回新创建的OH\_NativeBundle\_ApplicationInfo对象。如果返回的对象为NULL，则表示创建失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_GetAppId()

PhonePC/2in1TabletTVWearable

```
1. char* OH_NativeBundle_GetAppId()
```

**描述**

获取当前应用的appId。appId是应用的唯一标识，由应用包名和签名信息决定。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\* | 返回一个新创建的字符串，用于指示appID信息。如果返回的对象为NULL，则表示创建失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_GetAppIdentifier()

PhonePC/2in1TabletTVWearable

```
1. char* OH_NativeBundle_GetAppIdentifier()
```

**描述**

获取当前应用的应用程序标识符。该应用程序标识符在应用的整个生命周期中不会发生变化，包括版本更新、证书更改、公钥和私钥更改以及应用程序迁移。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\* | 返回一个新创建的字符串，用于指示应用程序标识符信息。如果返回的对象为NULL，则表示创建失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_GetMainElementName()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeBundle_ElementName OH_NativeBundle_GetMainElementName()
```

**描述**

获取当前应用入口元素mainElement的信息，包括包名、模块名和组件名，在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeBundle\_ElementName](capi-native-bundle-oh-nativebundle-elementname.md) | 返回新创建的OH\_NativeBundle\_ElementName对象。如果返回的对象为NULL，则表示创建失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_GetCompatibleDeviceType()

PhonePC/2in1TabletTVWearable

```
1. char* OH_NativeBundle_GetCompatibleDeviceType()
```

**描述**

获取当前应用适用的设备类型。用于将手机应用分发到平板/2in1设备时，合理适配布局和字体大小。在使用此接口后，为了避免内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\* | 返回一个新创建的字符串，用于指示兼容设备类型。如果返回的对象为NULL，则表示创建失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_IsDebugMode()

PhonePC/2in1TabletTVWearable

```
1. bool OH_NativeBundle_IsDebugMode(bool* isDebugMode)
```

**描述**

查询当前应用是否处于调试模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool\* isDebugMode | 表示应用是否处于调试模式，取值为true表示可调试模式，取值为false表示不可调试模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果调用成功，则返回true，否则返回false。 |

### OH\_NativeBundle\_GetModuleMetadata()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeBundle_ModuleMetadata* OH_NativeBundle_GetModuleMetadata(size_t* size)
```

**描述**

获取当前应用程序的模块元数据数组。在使用该接口之后，为了防止内存泄漏，需要手动释放接口返回的指针。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| size\_t\* size | 表示模块元数据数组大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeBundle\_ModuleMetadata](capi-native-bundle-oh-nativebundle-modulemetadata.md)\* | 返回模块元数据数组，如果返回的对象为NULL，则表示获取失败。  失败的可能原因是应用程序地址空间已满，导致空间分配失败。 |

### OH\_NativeBundle\_GetAbilityResourceInfo()

PhonePC/2in1TabletTVWearable

```
1. BundleManager_ErrorCode OH_NativeBundle_GetAbilityResourceInfo(char* fileType, OH_NativeBundle_AbilityResourceInfo** abilityResourceInfo, size_t* size)
```

**描述**

获取支持打开特定文件类型的组件资源信息列表。在使用完该接口之后，为了防止内存泄漏，需要调用[OH\_AbilityResourceInfo\_Destroy](capi-ability-resource-info-h.md#oh_abilityresourceinfo_destroy)进行释放。

**起始版本：** 21

**需要权限：** ohos.permission.GET\_ABILITY\_INFO

**设备行为差异：** 该接口仅在PC/2in1设备中可正常调用，在其他设备中返回201错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* fileType | 表示待查询的特定文件类型，推荐使用[UTD类型](../harmonyos-guides/uniform-data-type-descriptors.md)，比如：'general.plain-text'、'general.image'。目前也可以兼容使用[MIME type类型](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)和文件后缀名称，如：'text/xml' 、 '.png'等。文件后缀与文件类型的映射关系参见[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)。不支持传'\*/\*'。 |
| [OH\_NativeBundle\_AbilityResourceInfo](-native-bundle-oh-nativebundle-abilityresourceinfo.md)\*\* abilityResourceInfo | 表示返回的组件资源信息列表。 |
| size\_t\* size | 表示返回的组件资源信息列表大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [BundleManager\_ErrorCode](capi-bundle-manager-common-h.md#bundlemanager_errorcode) | 如果调用成功，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](capi-bundle-manager-common-h.md#bundlemanager_errorcode)。  如果调用方没有正确的权限，返回[BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED](capi-bundle-manager-common-h.md#bundlemanager_errorcode)。 |
