---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-uds-h
title: uds.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > uds.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d2fd1e0a03d91957c50294dd15c87b2d4fbcbb16dc235dc3d4fd3cf13842364
---

## 概述

提供标准化数据结构相关接口函数、结构体定义。当参数类型为char\*时，字符串必须以空字符（'\0'）结尾。

**引用文件：** <database/udmf/uds.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：** [UDMF](capi-udmf.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md) | OH\_UdsPlainText | 描述纯文本类型数据的统一数据结构。 |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md) | OH\_UdsHyperlink | 描述超链接类型的统一数据结构。 |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md) | OH\_UdsHtml | 描述超文本标记语言类型的统一数据结构。 |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md) | OH\_UdsAppItem | 描述桌面图标类型的统一数据结构。 |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md) | OH\_UdsFileUri | 描述文件Uri类型的统一数据结构。 |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md) | OH\_UdsPixelMap | 描述像素图片类型的统一数据结构。 |
| [OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md) | OH\_UdsArrayBuffer | 描述ArrayBuffer类型的统一数据结构。 |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md) | OH\_UdsContentForm | 描述内容卡片类型的统一数据结构。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md) | OH\_UdsDetails | 描述字典类型的统一数据结构。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Udmf\_AuthPermission](capi-uds-h.md#udmf_authpermission) | Udmf\_AuthPermission | 拖拽场景下的URI授权策略。  说明：此授权策略仅在拖拽场景下生效，其他场景不生效。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_UdsPlainText\* OH\_UdsPlainText\_Create()](capi-uds-h.md#oh_udsplaintext_create) | 创建纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsPlainText\_Destroy](capi-uds-h.md#oh_udsplaintext_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsPlainText\_Destroy(OH\_UdsPlainText\* pThis)](capi-uds-h.md#oh_udsplaintext_destroy) | 销毁纯文本类型数据[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)指针指向的实例对象。 |
| [const char\* OH\_UdsPlainText\_GetType(OH\_UdsPlainText\* pThis)](capi-uds-h.md#oh_udsplaintext_gettype) | 从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取类型ID。 |
| [const char\* OH\_UdsPlainText\_GetContent(OH\_UdsPlainText\* pThis)](capi-uds-h.md#oh_udsplaintext_getcontent) | 从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取纯文本内容信息。 |
| [const char\* OH\_UdsPlainText\_GetAbstract(OH\_UdsPlainText\* pThis)](capi-uds-h.md#oh_udsplaintext_getabstract) | 从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取纯文本摘要信息。 |
| [int OH\_UdsPlainText\_SetContent(OH\_UdsPlainText\* pThis, const char\* content)](capi-uds-h.md#oh_udsplaintext_setcontent) | 设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的纯文本内容参数。 |
| [int OH\_UdsPlainText\_SetAbstract(OH\_UdsPlainText\* pThis, const char\* abstract)](capi-uds-h.md#oh_udsplaintext_setabstract) | 设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的纯文本摘要参数。 |
| [OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create()](capi-uds-h.md#oh_udshyperlink_create) | 创建超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsHyperlink\_Destroy](capi-uds-h.md#oh_udshyperlink_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis)](capi-uds-h.md#oh_udshyperlink_destroy) | 销毁超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)指针指向的实例对象。 |
| [const char\* OH\_UdsHyperlink\_GetType(OH\_UdsHyperlink\* pThis)](capi-uds-h.md#oh_udshyperlink_gettype) | 从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取类型ID。 |
| [const char\* OH\_UdsHyperlink\_GetUrl(OH\_UdsHyperlink\* pThis)](capi-uds-h.md#oh_udshyperlink_geturl) | 从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取URL参数。 |
| [const char\* OH\_UdsHyperlink\_GetDescription(OH\_UdsHyperlink\* pThis)](capi-uds-h.md#oh_udshyperlink_getdescription) | 从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取描述参数。 |
| [int OH\_UdsHyperlink\_SetUrl(OH\_UdsHyperlink\* pThis, const char\* url)](capi-uds-h.md#oh_udshyperlink_seturl) | 设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中URL参数。 |
| [int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description)](capi-uds-h.md#oh_udshyperlink_setdescription) | 设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中描述参数。 |
| [OH\_UdsHtml\* OH\_UdsHtml\_Create()](capi-uds-h.md#oh_udshtml_create) | 创建超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsHtml\_Destroy](capi-uds-h.md#oh_udshtml_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsHtml\_Destroy(OH\_UdsHtml\* pThis)](capi-uds-h.md#oh_udshtml_destroy) | 销毁超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)指针指向的实例对象。 |
| [const char\* OH\_UdsHtml\_GetType(OH\_UdsHtml\* pThis)](capi-uds-h.md#oh_udshtml_gettype) | 获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中类型ID。 |
| [const char\* OH\_UdsHtml\_GetContent(OH\_UdsHtml\* pThis)](capi-uds-h.md#oh_udshtml_getcontent) | 获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中HTML格式内容参数。 |
| [const char\* OH\_UdsHtml\_GetPlainContent(OH\_UdsHtml\* pThis)](capi-uds-h.md#oh_udshtml_getplaincontent) | 获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中的纯文本内容参数。 |
| [int OH\_UdsHtml\_SetContent(OH\_UdsHtml\* pThis, const char\* content)](capi-uds-h.md#oh_udshtml_setcontent) | 设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的HTML格式内容参数。 |
| [int OH\_UdsHtml\_SetPlainContent(OH\_UdsHtml\* pThis, const char\* plainContent)](capi-uds-h.md#oh_udshtml_setplaincontent) | 设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的纯文本内容参数。 |
| [OH\_UdsAppItem\* OH\_UdsAppItem\_Create()](capi-uds-h.md#oh_udsappitem_create) | 创建桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsAppItem\_Destroy](capi-uds-h.md#oh_udsappitem_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsAppItem\_Destroy(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_destroy) | 销毁桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)指针指向的实例对象。 |
| [const char\* OH\_UdsAppItem\_GetType(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_gettype) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例获取类型ID。 |
| [const char\* OH\_UdsAppItem\_GetId(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_getid) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取应用ID。 |
| [const char\* OH\_UdsAppItem\_GetName(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_getname) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取应用名称。 |
| [const char\* OH\_UdsAppItem\_GetIconId(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_geticonid) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取图片ID。 |
| [const char\* OH\_UdsAppItem\_GetLabelId(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_getlabelid) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取标签ID。 |
| [const char\* OH\_UdsAppItem\_GetBundleName(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_getbundlename) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取bundle名称。 |
| [const char\* OH\_UdsAppItem\_GetAbilityName(OH\_UdsAppItem\* pThis)](capi-uds-h.md#oh_udsappitem_getabilityname) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取ability名称。 |
| [int OH\_UdsAppItem\_SetId(OH\_UdsAppItem\* pThis, const char\* appId)](capi-uds-h.md#oh_udsappitem_setid) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的应用ID。 |
| [int OH\_UdsAppItem\_SetName(OH\_UdsAppItem\* pThis, const char\* appName)](capi-uds-h.md#oh_udsappitem_setname) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的应用名称。 |
| [int OH\_UdsAppItem\_SetIconId(OH\_UdsAppItem\* pThis, const char\* appIconId)](capi-uds-h.md#oh_udsappitem_seticonid) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的图片ID。 |
| [int OH\_UdsAppItem\_SetLabelId(OH\_UdsAppItem\* pThis, const char\* appLabelId)](capi-uds-h.md#oh_udsappitem_setlabelid) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的标签ID。 |
| [int OH\_UdsAppItem\_SetBundleName(OH\_UdsAppItem\* pThis, const char\* bundleName)](capi-uds-h.md#oh_udsappitem_setbundlename) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的bundle名称。 |
| [int OH\_UdsAppItem\_SetAbilityName(OH\_UdsAppItem\* pThis, const char\* abilityName)](capi-uds-h.md#oh_udsappitem_setabilityname) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的ability名称。 |
| [OH\_UdsFileUri\* OH\_UdsFileUri\_Create()](capi-uds-h.md#oh_udsfileuri_create) | 创建文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsFileUri\_Destroy](capi-uds-h.md#oh_udsfileuri_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsFileUri\_Destroy(OH\_UdsFileUri\* pThis)](capi-uds-h.md#oh_udsfileuri_destroy) | 销毁文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)的实例对象。 |
| [const char\* OH\_UdsFileUri\_GetType(OH\_UdsFileUri\* pThis)](capi-uds-h.md#oh_udsfileuri_gettype) | 从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取类型ID。 |
| [const char\* OH\_UdsFileUri\_GetFileUri(OH\_UdsFileUri\* pThis)](capi-uds-h.md#oh_udsfileuri_getfileuri) | 从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取文件Uri。 |
| [const char\* OH\_UdsFileUri\_GetFileType(OH\_UdsFileUri\* pThis)](capi-uds-h.md#oh_udsfileuri_getfiletype) | 从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取文件类型。 |
| [int OH\_UdsFileUri\_SetFileUri(OH\_UdsFileUri\* pThis, const char\* fileUri)](capi-uds-h.md#oh_udsfileuri_setfileuri) | 设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的Uri信息。 |
| [int OH\_UdsFileUri\_SetFileType(OH\_UdsFileUri\* pThis, const char\* fileType)](capi-uds-h.md#oh_udsfileuri_setfiletype) | 设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的文件类型。 |
| [OH\_UdsPixelMap\* OH\_UdsPixelMap\_Create()](capi-uds-h.md#oh_udspixelmap_create) | 创建像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsPixelMap\_Destroy](capi-uds-h.md#oh_udspixelmap_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsPixelMap\_Destroy(OH\_UdsPixelMap\* pThis)](capi-uds-h.md#oh_udspixelmap_destroy) | 销毁像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)的实例对象。 |
| [const char\* OH\_UdsPixelMap\_GetType(OH\_UdsPixelMap\* pThis)](capi-uds-h.md#oh_udspixelmap_gettype) | 从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取类型ID。 |
| [void OH\_UdsPixelMap\_GetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)](capi-uds-h.md#oh_udspixelmap_getpixelmap) | 从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取像素图片[OH\_PixelmapNative](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel)实例的指针。 |
| [int OH\_UdsPixelMap\_SetPixelMap(OH\_UdsPixelMap\* pThis, OH\_PixelmapNative\* pixelmapNative)](capi-uds-h.md#oh_udspixelmap_setpixelmap) | 设置像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)对象的像素图片内容。 |
| [OH\_UdsArrayBuffer\* OH\_UdsArrayBuffer\_Create()](capi-uds-h.md#oh_udsarraybuffer_create) | 创建ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsArrayBuffer\_Destroy](capi-uds-h.md#oh_udsarraybuffer_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [int OH\_UdsArrayBuffer\_Destroy(OH\_UdsArrayBuffer\* buffer)](capi-uds-h.md#oh_udsarraybuffer_destroy) | 销毁ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)的实例对象。 |
| [int OH\_UdsArrayBuffer\_SetData(OH\_UdsArrayBuffer\* buffer, unsigned char\* data, unsigned int len)](capi-uds-h.md#oh_udsarraybuffer_setdata) | 设置ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)对象的数据内容。 |
| [int OH\_UdsArrayBuffer\_GetData(OH\_UdsArrayBuffer\* buffer, unsigned char\*\* data, unsigned int\* len)](capi-uds-h.md#oh_udsarraybuffer_getdata) | 从ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例中获取用户自定义的ArrayBuffer数据内容。 |
| [OH\_UdsContentForm\* OH\_UdsContentForm\_Create()](capi-uds-h.md#oh_udscontentform_create) | 创建内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsContentForm\_Destroy](capi-uds-h.md#oh_udscontentform_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsContentForm\_Destroy(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_destroy) | 销毁内容卡片类型数据[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)指针指向的实例对象。 |
| [const char\* OH\_UdsContentForm\_GetType(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_gettype) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取类型ID。 |
| [int OH\_UdsContentForm\_GetThumbData(OH\_UdsContentForm\* pThis, unsigned char\*\* thumbData, unsigned int\* len)](capi-uds-h.md#oh_udscontentform_getthumbdata) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取图片数据。 |
| [const char\* OH\_UdsContentForm\_GetDescription(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_getdescription) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取描述信息。 |
| [const char\* OH\_UdsContentForm\_GetTitle(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_gettitle) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取标题信息。 |
| [int OH\_UdsContentForm\_GetAppIcon(OH\_UdsContentForm\* pThis, unsigned char\*\* appIcon, unsigned int\* len)](capi-uds-h.md#oh_udscontentform_getappicon) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取应用图标数据。 |
| [const char\* OH\_UdsContentForm\_GetAppName(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_getappname) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取应用名称信息。 |
| [const char\* OH\_UdsContentForm\_GetLinkUri(OH\_UdsContentForm\* pThis)](capi-uds-h.md#oh_udscontentform_getlinkuri) | 从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取超链接信息。 |
| [int OH\_UdsContentForm\_SetThumbData(OH\_UdsContentForm\* pThis, const unsigned char\* thumbData, unsigned int len)](capi-uds-h.md#oh_udscontentform_setthumbdata) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的图片数据。 |
| [int OH\_UdsContentForm\_SetDescription(OH\_UdsContentForm\* pThis, const char\* description)](capi-uds-h.md#oh_udscontentform_setdescription) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的描述信息。 |
| [int OH\_UdsContentForm\_SetTitle(OH\_UdsContentForm\* pThis, const char\* title)](capi-uds-h.md#oh_udscontentform_settitle) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的标题信息。 |
| [int OH\_UdsContentForm\_SetAppIcon(OH\_UdsContentForm\* pThis, const unsigned char\* appIcon, unsigned int len)](capi-uds-h.md#oh_udscontentform_setappicon) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的应用图标数据。 |
| [int OH\_UdsContentForm\_SetAppName(OH\_UdsContentForm\* pThis, const char\* appName)](capi-uds-h.md#oh_udscontentform_setappname) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的应用名称数据。 |
| [int OH\_UdsContentForm\_SetLinkUri(OH\_UdsContentForm\* pThis, const char\* linkUri)](capi-uds-h.md#oh_udscontentform_setlinkuri) | 设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的超链接数据。 |
| [int OH\_UdsPlainText\_GetDetails(OH\_UdsPlainText\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsplaintext_getdetails) | 从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsPlainText\_SetDetails(OH\_UdsPlainText\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsplaintext_setdetails) | 设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [int OH\_UdsHyperlink\_GetDetails(OH\_UdsHyperlink\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udshyperlink_getdetails) | 从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsHyperlink\_SetDetails(OH\_UdsHyperlink\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udshyperlink_setdetails) | 设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [int OH\_UdsHtml\_GetDetails(OH\_UdsHtml\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udshtml_getdetails) | 从超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsHtml\_SetDetails(OH\_UdsHtml\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udshtml_setdetails) | 设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [int OH\_UdsAppItem\_GetDetails(OH\_UdsAppItem\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsappitem_getdetails) | 从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsAppItem\_SetDetails(OH\_UdsAppItem\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsappitem_setdetails) | 设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [int OH\_UdsFileUri\_GetDetails(OH\_UdsFileUri\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsfileuri_getdetails) | 从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsFileUri\_SetDetails(OH\_UdsFileUri\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udsfileuri_setdetails) | 设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [int OH\_UdsPixelMap\_GetDetails(OH\_UdsPixelMap\* pThis, OH\_UdsDetails\* details)](capi-uds-h.md#oh_udspixelmap_getdetails) | 从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| [int OH\_UdsPixelMap\_SetDetails(OH\_UdsPixelMap\* pThis, const OH\_UdsDetails\* details)](capi-uds-h.md#oh_udspixelmap_setdetails) | 设置像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。 |
| [OH\_UdsDetails\* OH\_UdsDetails\_Create()](capi-uds-h.md#oh_udsdetails_create) | 创建字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)指针及实例对象。  当不再需要使用指针时，请使用[OH\_UdsDetails\_Destroy](capi-uds-h.md#oh_udsdetails_destroy)销毁实例对象，否则会导致内存泄漏。 |
| [void OH\_UdsDetails\_Destroy(OH\_UdsDetails\* pThis)](capi-uds-h.md#oh_udsdetails_destroy) | 销毁字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)指针指向的实例对象。 |
| [bool OH\_UdsDetails\_HasKey(const OH\_UdsDetails\* pThis, const char\* key)](capi-uds-h.md#oh_udsdetails_haskey) | 检查字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中是否存在指定键。 |
| [int OH\_UdsDetails\_Remove(OH\_UdsDetails\* pThis, const char\* key)](capi-uds-h.md#oh_udsdetails_remove) | 删除字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中指定键值对。 |
| [int OH\_UdsDetails\_Clear(OH\_UdsDetails\* pThis)](capi-uds-h.md#oh_udsdetails_clear) | 清除字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中所有数据。 |
| [int OH\_UdsDetails\_SetValue(OH\_UdsDetails\* pThis, const char\* key, const char\* value)](capi-uds-h.md#oh_udsdetails_setvalue) | 向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中添加键值对数据。 |
| [const char\* OH\_UdsDetails\_GetValue(const OH\_UdsDetails\* pThis, const char\* key)](capi-uds-h.md#oh_udsdetails_getvalue) | 获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中指定的键对应的值。 |
| [char\*\* OH\_UdsDetails\_GetAllKeys(OH\_UdsDetails\* pThis, unsigned int\* count)](capi-uds-h.md#oh_udsdetails_getallkeys) | 获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中所有键的结果集。 |
| [int OH\_UdsHtml\_SetAuthPolicy(OH\_UdsHtml\* pThis, uint32\_t authPolicy)](capi-uds-h.md#oh_udshtml_setauthpolicy) | 给[OH\_UdsHtml](capi-udmf-oh-udshtml.md)设置授权策略。  说明：此授权策略仅在拖拽场景下生效，其他场景不生效。 |
| [int OH\_UdsFileUri\_SetAuthPolicy(OH\_UdsFileUri\* pThis, uint32\_t authPolicy)](capi-uds-h.md#oh_udsfileuri_setauthpolicy) | 给[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)设置授权策略。  说明：此授权策略仅在拖拽场景下生效，其他场景不生效。 |

## 枚举类型说明

### Udmf\_AuthPermission

```c
enum Udmf_AuthPermission
```

**描述**

拖拽场景下的URI授权策略。

**说明** 

此授权策略仅在拖拽场景下生效，其他场景不生效。

支持不授权、读、写、持久化四种权限策略，可组合使用，仅以下组合生效：

* 仅使用NONE：不做任何文件授权。
* 仅使用READ：仅做单次只读授权。
* 仅使用WRITE：做单次读、写授权（写授权包含读授权）。
* READ+WRITE：做单次读、写授权，与仅写授权等同。
* READ+PERSIST：做持久化读授权。
* WRITE+PERSIST：做持久化读写授权。
* READ+WRITE+PERSIST：做持久化读写授权。

拖拽授权策略应用规则（按优先级从高到低）：

* 单个数据级别：FileUri、HTML两个UDS支持配置授权策略参数，仅对单个record单次生效，优先级最高。
* [OH\_UdmfData](capi-udmf-oh-udmfdata.md)级别：[OH\_UdmfProperty](capi-udmf-oh-udmfproperty.md)中提供的授权参数对单次拖拽有效。若某个数据中配置了授权策略，则优先按照该数据的配置进行，优先级次之。
* 默认级别：若单个数据和[OH\_UdmfProperty](capi-udmf-oh-udmfproperty.md)均未配置授权策略，则按照拖拽默认逻辑进行代理授权。默认逻辑如下：
* FileUri类型数据：拖拽场景下默认授权为READ+WRITE+PERSIST（读+写+持久化授权）。
* HTML类型数据：仅针对HTML文本中img标签下的uri做读授权。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| UDMF\_PERM\_NONE = 0 | 表示未授予任何权限。 |
| UDMF\_PERM\_READ = 1u << 0 | 表示读取或查看数据的权限。 |
| UDMF\_PERM\_WRITE = 1u << 1 | 表示修改数据的权限（包含READ）。 |
| UDMF\_PERM\_PERSIST = 1u << 2 | 表示持久化文件的权限。 |

## 函数说明

### OH\_UdsPlainText\_Create()

```c
OH_UdsPlainText* OH_UdsPlainText_Create()
```

**描述**

创建纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsPlainText\_Destroy](capi-uds-h.md#oh_udsplaintext_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* | 执行成功则返回一个指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsPlainText\_Destroy()

```c
void OH_UdsPlainText_Destroy(OH_UdsPlainText* pThis)
```

**描述**

销毁纯文本类型数据[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |

### OH\_UdsPlainText\_GetType()

```c
const char* OH_UdsPlainText_GetType(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取类型ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsPlainText\_GetContent()

```c
const char* OH_UdsPlainText_GetContent(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取纯文本内容信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回纯文本内容信息的字符串指针，否则返回nullptr。 |

### OH\_UdsPlainText\_GetAbstract()

```c
const char* OH_UdsPlainText_GetAbstract(OH_UdsPlainText* pThis)
```

**描述**

从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取纯文本摘要信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回纯文本摘要信息的字符串指针，否则返回nullptr。 |

### OH\_UdsPlainText\_SetContent()

```c
int OH_UdsPlainText_SetContent(OH_UdsPlainText* pThis, const char* content)
```

**描述**

设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的纯文本内容参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |
| const char\* content | 表示纯文本内容参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPlainText\_SetAbstract()

```c
int OH_UdsPlainText_SetAbstract(OH_UdsPlainText* pThis, const char* abstract)
```

**描述**

设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的纯文本摘要参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |
| const char\* abstract | 表示纯文本摘要参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHyperlink\_Create()

```c
OH_UdsHyperlink* OH_UdsHyperlink_Create()
```

**描述**

创建超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsHyperlink\_Destroy](capi-uds-h.md#oh_udshyperlink_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_UdsHyperlink\* | 执行成功则返回一个指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsHyperlink\_Destroy()

```c
void OH_UdsHyperlink_Destroy(OH_UdsHyperlink* pThis)
```

**描述**

销毁超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |

### OH\_UdsHyperlink\_GetType()

```c
const char* OH_UdsHyperlink_GetType(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取类型ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsHyperlink\_GetUrl()

```c
const char* OH_UdsHyperlink_GetUrl(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取URL参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回URL参数的字符串指针，否则返回nullptr。 |

### OH\_UdsHyperlink\_GetDescription()

```c
const char* OH_UdsHyperlink_GetDescription(OH_UdsHyperlink* pThis)
```

**描述**

从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取描述参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回描述参数的字符串指针，否则返回nullptr。 |

### OH\_UdsHyperlink\_SetUrl()

```c
int OH_UdsHyperlink_SetUrl(OH_UdsHyperlink* pThis, const char* url)
```

**描述**

设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中URL参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |
| const char\* url | 表示URL参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHyperlink\_SetDescription()

```c
int OH_UdsHyperlink_SetDescription(OH_UdsHyperlink* pThis, const char* description)
```

**描述**

设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中描述参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |
| const char\* description | 表示描述信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHtml\_Create()

```c
OH_UdsHtml* OH_UdsHtml_Create()
```

**描述**

创建超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsHtml\_Destroy](capi-uds-h.md#oh_udshtml_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* | 执行成功则返回一个指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsHtml\_Destroy()

```c
void OH_UdsHtml_Destroy(OH_UdsHtml* pThis)
```

**描述**

销毁超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |

### OH\_UdsHtml\_GetType()

```c
const char* OH_UdsHtml_GetType(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中类型ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsHtml\_GetContent()

```c
const char* OH_UdsHtml_GetContent(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中HTML格式内容参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回HTML格式内容的字符串指针，否则返回nullptr。 |

### OH\_UdsHtml\_GetPlainContent()

```c
const char* OH_UdsHtml_GetPlainContent(OH_UdsHtml* pThis)
```

**描述**

获取超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中的纯文本内容参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回纯文本内容的字符串指针，否则返回nullptr。 |

### OH\_UdsHtml\_SetContent()

```c
int OH_UdsHtml_SetContent(OH_UdsHtml* pThis, const char* content)
```

**描述**

设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的HTML格式内容参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |
| const char\* content | 表示HTML格式内容参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHtml\_SetPlainContent()

```c
int OH_UdsHtml_SetPlainContent(OH_UdsHtml* pThis, const char* plainContent)
```

**描述**

设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的纯文本内容参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |
| const char\* plainContent | 表示纯文本内容参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_Create()

```c
OH_UdsAppItem* OH_UdsAppItem_Create()
```

**描述**

创建桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsAppItem\_Destroy](capi-uds-h.md#oh_udsappitem_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* | 执行成功则返回一个指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsAppItem\_Destroy()

```c
void OH_UdsAppItem_Destroy(OH_UdsAppItem* pThis)
```

**描述**

销毁桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

### OH\_UdsAppItem\_GetType()

```c
const char* OH_UdsAppItem_GetType(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例获取类型ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetId()

```c
const char* OH_UdsAppItem_GetId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取应用ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回应用ID的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetName()

```c
const char* OH_UdsAppItem_GetName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取应用名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回应用名称的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetIconId()

```c
const char* OH_UdsAppItem_GetIconId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取图片ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回图片ID的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetLabelId()

```c
const char* OH_UdsAppItem_GetLabelId(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取标签ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回标签ID的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetBundleName()

```c
const char* OH_UdsAppItem_GetBundleName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取bundle名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回bundle名称的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_GetAbilityName()

```c
const char* OH_UdsAppItem_GetAbilityName(OH_UdsAppItem* pThis)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取ability名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回ability名称的字符串指针，否则返回nullptr。 |

### OH\_UdsAppItem\_SetId()

```c
int OH_UdsAppItem_SetId(OH_UdsAppItem* pThis, const char* appId)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的应用ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* appId | 表示应用ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetName()

```c
int OH_UdsAppItem_SetName(OH_UdsAppItem* pThis, const char* appName)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的应用名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* appName | 表示应用名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetIconId()

```c
int OH_UdsAppItem_SetIconId(OH_UdsAppItem* pThis, const char* appIconId)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的图片ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* appIconId | 表示图片ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetLabelId()

```c
int OH_UdsAppItem_SetLabelId(OH_UdsAppItem* pThis, const char* appLabelId)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的标签ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* appLabelId | 表示标签ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetBundleName()

```c
int OH_UdsAppItem_SetBundleName(OH_UdsAppItem* pThis, const char* bundleName)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的bundle名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* bundleName | 表示bundle名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetAbilityName()

```c
int OH_UdsAppItem_SetAbilityName(OH_UdsAppItem* pThis, const char* abilityName)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的ability名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const char\* abilityName | 表示ability名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsFileUri\_Create()

```c
OH_UdsFileUri* OH_UdsFileUri_Create()
```

**描述**

创建文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsFileUri\_Destroy](capi-uds-h.md#oh_udsfileuri_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* | 执行成功则返回一个指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsFileUri\_Destroy()

```c
void OH_UdsFileUri_Destroy(OH_UdsFileUri* pThis)
```

**描述**

销毁文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)的实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |

### OH\_UdsFileUri\_GetType()

```c
const char* OH_UdsFileUri_GetType(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取类型ID。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsFileUri\_GetFileUri()

```c
const char* OH_UdsFileUri_GetFileUri(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取文件Uri。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回文件Uri的字符串指针，否则返回nullptr。 |

### OH\_UdsFileUri\_GetFileType()

```c
const char* OH_UdsFileUri_GetFileType(OH_UdsFileUri* pThis)
```

**描述**

从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取文件类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回文件类型的字符串指针，否则返回nullptr。 |

### OH\_UdsFileUri\_SetFileUri()

```c
int OH_UdsFileUri_SetFileUri(OH_UdsFileUri* pThis, const char* fileUri)
```

**描述**

设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的Uri信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |
| const char\* fileUri | 表示文件Uri。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsFileUri\_SetFileType()

```c
int OH_UdsFileUri_SetFileType(OH_UdsFileUri* pThis, const char* fileType)
```

**描述**

设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的文件类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |
| const char\* fileType | 表示文件类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPixelMap\_Create()

```c
OH_UdsPixelMap* OH_UdsPixelMap_Create()
```

**描述**

创建像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsPixelMap\_Destroy](capi-uds-h.md#oh_udspixelmap_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* | 执行成功则返回一个指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsPixelMap\_Destroy()

```c
void OH_UdsPixelMap_Destroy(OH_UdsPixelMap* pThis)
```

**描述**

销毁像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)的实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |

### OH\_UdsPixelMap\_GetType()

```c
const char* OH_UdsPixelMap_GetType(OH_UdsPixelMap* pThis)
```

**描述**

从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取类型ID。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsPixelMap\_GetPixelMap()

```c
void OH_UdsPixelMap_GetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)
```

**描述**

从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取像素图片[OH\_PixelmapNative](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel)实例的指针。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |
| OH\_PixelmapNative\* pixelmapNative | 该参数是输出参数，表示指向像素图片[OH\_PixelmapNative](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel)实例的指针。 |

### OH\_UdsPixelMap\_SetPixelMap()

```c
int OH_UdsPixelMap_SetPixelMap(OH_UdsPixelMap* pThis, OH_PixelmapNative* pixelmapNative)
```

**描述**

设置像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)对象的像素图片内容。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |
| OH\_PixelmapNative\* pixelmapNative | 表示指向像素图片[OH\_PixelmapNative](capi-pixelmap-native-h.md#oh_pixelmapnative_antialiasinglevel)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsArrayBuffer\_Create()

```c
OH_UdsArrayBuffer* OH_UdsArrayBuffer_Create()
```

**描述**

创建ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)的实例对象以及指向它的指针。当不再需要使用指针时，请使用[OH\_UdsArrayBuffer\_Destroy](capi-uds-h.md#oh_udsarraybuffer_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)\* | 执行成功则返回一个指向ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsArrayBuffer\_Destroy()

```c
int OH_UdsArrayBuffer_Destroy(OH_UdsArrayBuffer* buffer)
```

**描述**

销毁ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)的实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)\* buffer | 表示指向ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsArrayBuffer\_SetData()

```c
int OH_UdsArrayBuffer_SetData(OH_UdsArrayBuffer* buffer, unsigned char* data, unsigned int len)
```

**描述**

设置ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)对象的数据内容。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)\* buffer | 表示指向ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例的指针。 |
| unsigned char\* data | 表示用户自定义的ArrayBuffer数据。 |
| unsigned int len | 表示用户自定义的ArrayBuffer数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsArrayBuffer\_GetData()

```c
int OH_UdsArrayBuffer_GetData(OH_UdsArrayBuffer* buffer, unsigned char** data, unsigned int* len)
```

**描述**

从ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例中获取用户自定义的ArrayBuffer数据内容。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)\* buffer | 表示指向ArrayBuffer类型[OH\_UdsArrayBuffer](capi-udmf-oh-udsarraybuffer.md)实例的指针。 |
| unsigned char\*\* data | 该参数是输出参数，表示用户自定义的ArrayBuffer数据。 |
| unsigned int\* len | 该参数是输出参数，表示用户自定义的ArrayBuffer数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_Create()

```c
OH_UdsContentForm* OH_UdsContentForm_Create()
```

**描述**

创建内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)指针及实例对象。当不再需要使用指针时，请使用[OH\_UdsContentForm\_Destroy](capi-uds-h.md#oh_udscontentform_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* | 执行成功则返回一个指向内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsContentForm\_Destroy()

```c
void OH_UdsContentForm_Destroy(OH_UdsContentForm* pThis)
```

**描述**

销毁内容卡片类型数据[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)指针指向的实例对象。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

### OH\_UdsContentForm\_GetType()

```c
const char* OH_UdsContentForm_GetType(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取类型ID。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回类型ID的字符串指针，否则返回nullptr。 |

### OH\_UdsContentForm\_GetThumbData()

```c
int OH_UdsContentForm_GetThumbData(OH_UdsContentForm* pThis, unsigned char** thumbData, unsigned int* len)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取图片数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| unsigned char\*\* thumbData | 该参数是输出参数，表示内容卡片中的图片二进制数据。 |
| unsigned int\* len | 该参数是输出参数，表示内容卡片中的图片二进制数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。  若返回UDMF\_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_GetDescription()

```c
const char* OH_UdsContentForm_GetDescription(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取描述信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回描述信息的字符串指针，否则返回nullptr。 |

### OH\_UdsContentForm\_GetTitle()

```c
const char* OH_UdsContentForm_GetTitle(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取标题信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回标题信息的字符串指针，否则返回nullptr。 |

### OH\_UdsContentForm\_GetAppIcon()

```c
int OH_UdsContentForm_GetAppIcon(OH_UdsContentForm* pThis, unsigned char** appIcon, unsigned int* len)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取应用图标数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| unsigned char\*\* appIcon | 该参数是输出参数，表示内容卡片中的应用图标二进制数据。 |
| unsigned int\* len | 该参数是输出参数，表示内容卡片中的应用图标二进制数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。  若返回UDMF\_ERR，表示内部数据错误。可能的原因是服务故障或者内存不足等。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_GetAppName()

```c
const char* OH_UdsContentForm_GetAppName(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取应用名称信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回应用名称信息的字符串指针，否则返回nullptr。 |

### OH\_UdsContentForm\_GetLinkUri()

```c
const char* OH_UdsContentForm_GetLinkUri(OH_UdsContentForm* pThis)
```

**描述**

从内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中获取超链接信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 输入有效入参时返回超链接的字符串指针，否则返回nullptr。 |

### OH\_UdsContentForm\_SetThumbData()

```c
int OH_UdsContentForm_SetThumbData(OH_UdsContentForm* pThis, const unsigned char* thumbData, unsigned int len)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的图片数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const unsigned char\* thumbData | 表示内容卡片中的图片二进制数据。 |
| unsigned int len | 表示内容卡片中的图片二进制数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_SetDescription()

```c
int OH_UdsContentForm_SetDescription(OH_UdsContentForm* pThis, const char* description)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的描述信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const char\* description | 表示描述信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_SetTitle()

```c
int OH_UdsContentForm_SetTitle(OH_UdsContentForm* pThis, const char* title)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的标题信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const char\* title | 表示标题信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_SetAppIcon()

```c
int OH_UdsContentForm_SetAppIcon(OH_UdsContentForm* pThis, const unsigned char* appIcon, unsigned int len)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的应用图标数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const unsigned char\* appIcon | 表示内容卡片中的应用图标二进制数据。 |
| unsigned int len | 表示内容卡片中的应用图标二进制数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_SetAppName()

```c
int OH_UdsContentForm_SetAppName(OH_UdsContentForm* pThis, const char* appName)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的应用名称数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const char\* appName | 表示内容卡片中的应用名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsContentForm\_SetLinkUri()

```c
int OH_UdsContentForm_SetLinkUri(OH_UdsContentForm* pThis, const char* linkUri)
```

**描述**

设置内容卡片类型[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)中的超链接数据。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)\* pThis | 表示指向[OH\_UdsContentForm](capi-udmf-oh-udscontentform.md)实例的指针。 |
| const char\* linkUri | 表示内容卡片中的超链接。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPlainText\_GetDetails()

```c
int OH_UdsPlainText_GetDetails(OH_UdsPlainText* pThis, OH_UdsDetails* details)
```

**描述**

从纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPlainText\_SetDetails()

```c
int OH_UdsPlainText_SetDetails(OH_UdsPlainText* pThis, const OH_UdsDetails* details)
```

**描述**

设置纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)\* pThis | 表示指向纯文本类型[OH\_UdsPlainText](capi-udmf-oh-udsplaintext.md)实例的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHyperlink\_GetDetails()

```c
int OH_UdsHyperlink_GetDetails(OH_UdsHyperlink* pThis, OH_UdsDetails* details)
```

**描述**

从超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHyperlink\_SetDetails()

```c
int OH_UdsHyperlink_SetDetails(OH_UdsHyperlink* pThis, const OH_UdsDetails* details)
```

**描述**

设置超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)\* pThis | 表示指向超链接类型[OH\_UdsHyperlink](capi-udmf-oh-udshyperlink.md)实例的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHtml\_GetDetails()

```c
int OH_UdsHtml_GetDetails(OH_UdsHtml* pThis, OH_UdsDetails* details)
```

**描述**

从超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)对象中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsHtml\_SetDetails()

```c
int OH_UdsHtml_SetDetails(OH_UdsHtml* pThis, const OH_UdsDetails* details)
```

**描述**

设置超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)中的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向超文本标记语言类型[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_GetDetails()

```c
int OH_UdsAppItem_GetDetails(OH_UdsAppItem* pThis, OH_UdsDetails* details)
```

**描述**

从桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsAppItem\_SetDetails()

```c
int OH_UdsAppItem_SetDetails(OH_UdsAppItem* pThis, const OH_UdsDetails* details)
```

**描述**

设置桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)\* pThis | 表示指向桌面图标类型[OH\_UdsAppItem](capi-udmf-oh-udsappitem.md)对象的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsFileUri\_GetDetails()

```c
int OH_UdsFileUri_GetDetails(OH_UdsFileUri* pThis, OH_UdsDetails* details)
```

**描述**

从文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsFileUri\_SetDetails()

```c
int OH_UdsFileUri_SetDetails(OH_UdsFileUri* pThis, const OH_UdsDetails* details)
```

**描述**

设置文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向文件Uri类型[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPixelMap\_GetDetails()

```c
int OH_UdsPixelMap_GetDetails(OH_UdsPixelMap* pThis, OH_UdsDetails* details)
```

**描述**

从像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例中获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 该参数是输出参数，表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsPixelMap\_SetDetails()

```c
int OH_UdsPixelMap_SetDetails(OH_UdsPixelMap* pThis, const OH_UdsDetails* details)
```

**描述**

设置像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)对象的字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)参数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)\* pThis | 表示指向像素图片类型[OH\_UdsPixelMap](capi-udmf-oh-udspixelmap.md)实例的指针。 |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* details | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针，该指针不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsDetails\_Create()

```c
OH_UdsDetails* OH_UdsDetails_Create()
```

**描述**

创建字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)指针及实例对象。

当不再需要使用指针时，请使用[OH\_UdsDetails\_Destroy](capi-uds-h.md#oh_udsdetails_destroy)销毁实例对象，否则会导致内存泄漏。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* | 执行成功则返回一个指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例对象的指针，否则返回nullptr。 |

### OH\_UdsDetails\_Destroy()

```c
void OH_UdsDetails_Destroy(OH_UdsDetails* pThis)
```

**描述**

销毁字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)指针指向的实例对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |

### OH\_UdsDetails\_HasKey()

```c
bool OH_UdsDetails_HasKey(const OH_UdsDetails* pThis, const char* key)
```

**描述**

检查字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中是否存在指定键。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| const char\* key | 表示字典类型中键值对的键。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回查找结果的状态。返回false表示不存在指定键，返回true表示存在指定键。 |

### OH\_UdsDetails\_Remove()

```c
int OH_UdsDetails_Remove(OH_UdsDetails* pThis, const char* key)
```

**描述**

删除字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中指定键值对。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| const char\* key | 表示字典类型中键值对的键。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsDetails\_Clear()

```c
int OH_UdsDetails_Clear(OH_UdsDetails* pThis)
```

**描述**

清除字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中所有数据。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsDetails\_SetValue()

```c
int OH_UdsDetails_SetValue(OH_UdsDetails* pThis, const char* key, const char* value)
```

**描述**

向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中添加键值对数据。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| const char\* key | 表示字典类型中键值对的键。 |
| const char\* value | 表示字典类型中键值对的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsDetails\_GetValue()

```c
const char* OH_UdsDetails_GetValue(const OH_UdsDetails* pThis, const char* key)
```

**描述**

获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中指定的键对应的值。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| const char\* key | 表示字典类型中键值对的键。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 当入参有效时返回指向字典类型中值的指针，否则返回nullptr。 |

### OH\_UdsDetails\_GetAllKeys()

```c
char** OH_UdsDetails_GetAllKeys(OH_UdsDetails* pThis, unsigned int* count)
```

**描述**

获取字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)中所有键的结果集。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsDetails](capi-udmf-oh-udsdetails.md)\* pThis | 表示指向字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)实例的指针。 |
| unsigned int\* count | 该参数是输出参数，表示结果集的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\*\* | 执行成功时返回字典类型中键的结果集，否则返回nullptr。  当使用[OH\_UdsDetails\_Destroy](capi-uds-h.md#oh_udsdetails_destroy)销毁字典类型[OH\_UdsDetails](capi-udmf-oh-udsdetails.md)指针指向的实例对象，该返回值也会被释放。 |

### OH\_UdsHtml\_SetAuthPolicy()

```c
int OH_UdsHtml_SetAuthPolicy(OH_UdsHtml* pThis, uint32_t authPolicy)
```

**描述**

给[OH\_UdsHtml](capi-udmf-oh-udshtml.md)设置授权策略。

**说明** 

此授权策略仅在拖拽场景下生效，其他场景不生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsHtml](capi-udmf-oh-udshtml.md)\* pThis | 表示指向[OH\_UdsHtml](capi-udmf-oh-udshtml.md)实例的指针。 |
| uint32\_t authPolicy | 表示拖拽场景下的URI授权策略，默认值为READ（仅读授权），仅在img标签等场景下生效。只针对单个record使用，优先级最高。具体策略见[Udmf\_AuthPermission](capi-uds-h.md#udmf_authpermission)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  返回UDMF\_E\_OK表示执行成功。  返回UDMF\_E\_INVALID\_PARAM表示传入了无效参数。  具体请参见[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |

### OH\_UdsFileUri\_SetAuthPolicy()

```c
int OH_UdsFileUri_SetAuthPolicy(OH_UdsFileUri* pThis, uint32_t authPolicy)
```

**描述**

给[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)设置授权策略。

**说明** 

此授权策略仅在拖拽场景下生效，其他场景不生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)\* pThis | 表示指向[OH\_UdsFileUri](capi-udmf-oh-udsfileuri.md)实例的指针。 |
| uint32\_t authPolicy | 表示拖拽场景下的URI授权策略，默认值为READ+WRITE+PERSIST（读+写+持久化授权），只针对单个record使用，优先级最高。具体策略见[Udmf\_AuthPermission](capi-uds-h.md#udmf_authpermission)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。  若返回UDMF\_E\_OK，表示执行成功。  若返回UDMF\_E\_INVALID\_PARAM，表示传入了无效参数。具体请参阅错误码定义[Udmf\_ErrCode](capi-udmf-err-code-h.md#udmf_errcode)。 |
