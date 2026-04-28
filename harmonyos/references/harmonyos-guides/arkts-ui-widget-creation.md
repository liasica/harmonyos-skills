---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aae685e652cdb9bcaf332ff96301320e5fd9b22cf388416932d9cfdcadbc4e51
---

ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aznZw9MYRueH32rAklPzGg/zh-cn_image_0000002583438331.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=E4D4607FF01CCD2B91DF4465DDC531B65D767750A9F85A5CA62BC16407EE0206)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/fPFsbOl8RZ2mfUXbQ8A_MQ/zh-cn_image_0000002552958286.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=E261F477ED6C387B08D455D29B3C73571BAF8BA9A74294FBBF6A61BC9BE630CB)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/1XyGTD2KT6e--u0pE4i-0Q/zh-cn_image_0000002583478287.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=43E82A5087725BE8711E584B7C5E0697CCDE77C678E5C357262F03B7307B68DF)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/suvpamvpSISG1XMwuTemvQ/zh-cn_image_0000002552798638.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=B2F1E0DCE32AE1C60B3F68B60C72F8D4655F2AB29DEB1AF1786DC616DA7DD756)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/t4DjiIhNRUqUaPzh3P5k8g/zh-cn_image_0000002583438333.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=A6106CF130BB67A9FEFE9785577640376594820E2F2BD01C16E109A11BC238D6)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ZppxbxDDQuGB84C8JLtomA/zh-cn_image_0000002552958288.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=DB05D475D881565C812DBA22C7AFB5B50C5D511E48588BA0DC536D869FB1676B)

* [FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)：卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。
* [FormExtensionContext](../harmonyos-references/js-apis-inner-application-formextensioncontext.md)：FormExtensionAbility的上下文环境，提供FormExtensionAbility具有的接口和能力。
* [formProvider](../harmonyos-references/js-apis-app-form-formprovider.md)：提供了获取卡片信息、更新卡片、设置卡片更新时间等能力。
* [formInfo](../harmonyos-references/js-apis-app-form-forminfo.md)：提供了卡片信息和状态等相关类型和枚举。
* [formBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md)：提供卡片数据绑定的能力，包括FormBindingData对象的创建、相关信息的描述。
* [页面布局（WidgetCard.ets）](arkts-ui-widget-page-overview.md)：基于ArkUI提供卡片UI开发能力。

  + [ArkTS卡片通用能力](arkts-ui-widget-page-overview.md#arkts卡片支持的页面能力)：提供了能在ArkTS卡片中使用的组件、属性和API。
  + [ArkTS卡片特有能力](arkts-ui-widget-event-overview.md)：postCardAction用于卡片内部和提供方应用间的交互，仅在卡片中可以调用。
* [卡片配置](arkts-ui-widget-configuration.md)：包含FormExtensionAbility的配置和卡片的配置。

  + 在[module.json5配置文件](module-configuration-file.md)中的extensionAbilities标签下，配置FormExtensionAbility相关信息。
  + 在resources/base/profile/目录下的[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件中，配置卡片（WidgetCard.ets）相关信息。

## 方式二：独立包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/rA9kxkvARhiDGU3jIGHc_w/zh-cn_image_0000002583438331.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=DC70F0FB1EBA0F3582E04C05DEB4A4E21736E2F78C6320D474EAB881757D19CE)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/EtHaaA9LRh6RNk1ewoR0Tg/zh-cn_image_0000002583478289.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=2B91030EC6D28985E37F0D7C8F20548D1D42F3772516364A42252FC56DD44496)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/lkJBd6sxQj6yfn9RGEZqAw/zh-cn_image_0000002583478287.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=6FBA9E25763F23F3053B29FACD3EBFD7345C48F7BD18738B47220CB55DA17515)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/DsDbqlayRlGtd8tq7Q_lag/zh-cn_image_0000002552798640.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=D21EFCC09E6DB5B25EA8FFFB21E64066BC53229E735F12784EC752CD951D39C7)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/GlOTQsnJQ_SfKR8Etr0svA/zh-cn_image_0000002583438335.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=B68FF17B507FB9B0538FE2F3D4CE6804F052C3139E37ED9A37741702173ECBB9)

说明

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
