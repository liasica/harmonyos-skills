---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:56+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:49a8d6efc16a32585e3d975aba218209747c15af2514945a3321d8e88676e62e
---

ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/e367slbHQtaDwJ--fZRA_A/zh-cn_image_0000002791565580.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC5B829FBF6957F790FC391FA13DC4290A69BB2959945824E9D7BF13D8C948BB)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/801G_93PRlel20CupTVs1g/zh-cn_image_0000002820525533.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E9FC794CDA9BAD0AAF3B80F1F64D555865A98E7D9A9E77AFF6D9003E39927F9)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/vmbhpJV8QNWsaYyVGzYmOA/zh-cn_image_0000002820405533.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=475F0EEE1B8A50CCC8FF281652BA77688361FA8B87D5407E3EFC2E01AA392BC6)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/vIMkxesCSfewTZSN_0KiHw/zh-cn_image_0000002791725554.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA3195537D19BF9FFCB1BEBE9D405877B2340955A4283835C330EF020D25A6DC)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ATPvK8e5SdOFvrN7CbC-mw/zh-cn_image_0000002791565582.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1171BB5724EB8602DD7CCE69B21D1FEBC7FEA392C1733D293EBF92927E0E822)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ThAiwfSHSTC4-nkpR0k-_A/zh-cn_image_0000002820525535.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFAB727333281AA379A05C1EAEAA9C43EA4A631770716535EF9A174020B41C5C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/nzngxt5pRNSr2BQN0aAIjw/zh-cn_image_0000002791565580.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4351846291476243E67A557BE18B251DCC56C4BDC0EEBC0919A3C7118757B54)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/N8X0qqosRM2mD-d53CXTqA/zh-cn_image_0000002820405535.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=146972C53A52C184981EFF15DB7C612927D1ADABB008A576A786AA0300E34C4E)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/4SjLfoD_SNKU-EaJITqygA/zh-cn_image_0000002820405533.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=A681D9806277C039AE82B514877D04035DD74E0DA361EA4BEA2DB1FC07C76498)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/eMFe4UJpRrOARjgimVdhVA/zh-cn_image_0000002791725556.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=28F6B809B8ED7F2E72F38D5A5E7E5130419F438E7F14670160693D0196AA2CA5)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/TZnEy6oER1iJrTwzngVTsw/zh-cn_image_0000002791565584.png?HW-CC-KV=V1&HW-CC-Date=20261119T014705Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0A924ECD082BD129D178E9FDDFDDEDCB7C6D464FABD3D3A3450DDF775D7E1E0)

**说明** 

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
