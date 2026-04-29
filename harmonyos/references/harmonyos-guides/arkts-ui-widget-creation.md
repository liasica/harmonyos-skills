---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28019f01af5ed0cf8616d88421825566e6788be2fa2f23a981f08c1bc4598c8c
---

ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/vV8LPhVdTJ-fw_lZl9-2Lw/zh-cn_image_0000002558605128.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=019CDC7056BF74BD26F0DD91088EAF0470E24E746CF67529C5EB91FF8A31CE64)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Lz9l10rBTD-Rfr2NNs4jIA/zh-cn_image_0000002589324653.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=F23653B81C4D96CB0C684D1E82702E611B86F16E4D6FCB43AC10EE9A5E9A3F4B)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ks9vpLJxQZG0zvosiJav6w/zh-cn_image_0000002589244591.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=7E203A95D6E4DA6403B2807CD2B17CF079469ABBBAE3822D29EF3D37F359BA6A)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/zTs02B0fSFC9_GzzOdaDYw/zh-cn_image_0000002558764786.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=23A5D561C6DB6CDBF90E9958BB96F70F48B1BAFEFB6760A875E09D4EBD5658D7)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/qHrMYAOdQbGcE4ERS3eSRg/zh-cn_image_0000002558605130.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=B233CC6D77DEA019F5511C485C18662B0D332849F90E2FD8B4A32DF5F1EA6B1E)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/iuP-T2yuQ4C-eDl8XyRoGg/zh-cn_image_0000002589324655.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=8FD73ECC62DFB1D778783E0761B46ECF3D23C7F6CC94E5099AA176E6D308FC1C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/tDOmgzz8RVi6icVm5VuFRA/zh-cn_image_0000002558605128.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=A83CE28BCFF018B20EC714D8DDD2AE0C92354D95C35504D1083B2E4D23BE6CC2)

说明

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/I2tib_73Sw-721BjovkUIg/zh-cn_image_0000002589244593.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=3DAB20C70A86B9B514222089FC18DCCB65AE1E0F1370EA549545C08CBE5BC505)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/hivpR02yTh-4qPsMSmNDIQ/zh-cn_image_0000002589244591.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=8418842E085C1AD9A7F448086473171E9347E09F64D09E7E4C8908937E454B08)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/EU0D31xbToyJUNv4fOzetw/zh-cn_image_0000002558764788.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=800ACF9B352E82110F75D435EF265D428C4C3F5B9A728F36EF1A517C81A0FD46)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/siSk9445QK2_2SaOhc75Dw/zh-cn_image_0000002558605132.png?HW-CC-KV=V1&HW-CC-Date=20260429T052952Z&HW-CC-Expire=86400&HW-CC-Sign=A5F5CCE12634472BC8F3750170A60179592AEAF765E527D102DDD64D8667E3AA)

说明

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
