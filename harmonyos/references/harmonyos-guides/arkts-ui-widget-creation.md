---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-creation
title: 创建ArkTS卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 创建ArkTS卡片
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f1cefa7a7790d57a9ea166552465358e52605e83eda64332e0ed9c319df4d1f0
---

ArkTS卡片有两种创建卡片包的方式。开发者在开发过程中任选其一即可。

方式一：卡片和应用共包方式，创建步骤请参考[共包方式创建卡片](arkts-ui-widget-creation.md#方式一共包方式创建卡片)，此时卡片UI和应用代码在一个module内，最终编译产物也在同一个HAP包内。

方式二：独立卡片包方式，创建步骤请参考[独立包方式创建卡片](arkts-ui-widget-creation.md#方式二独立包方式创建卡片)，此时卡片UI和应用代码在不同module内，最终编译产物分为卡片包和应用包。从API version 20开始支持。

ArkTS卡片创建完成，在开发卡片过程中，支持对卡片进行[实时预览](ide-service-widget.md#section18171652015)。

## 方式一：共包方式创建卡片

### 创建步骤

**1. 新建工程**

在DevEco Studio中，选择创建Application或Atomic Service工程，这两种都支持创建卡片。工程创建指导具体请参考[创建一个新的工程](ide-create-new-project.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/8DfKunvLSqqgyN5nuzf19A/zh-cn_image_0000002815558941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D264186F4559BD8CE5175281EB1E702CBD2CF07276410EAE8BB9A4EE30EDCA7)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

在已有的应用工程中，右键新建ArkTS卡片，具体操作如下。

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget】。在API 10及以上 Stage模型的工程中，开发者可通过Service Widget菜单直接选择创建动态卡片（Dynamic Widget）或静态卡片（Static Widget）。创建卡片后，也可在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/piHo1kwwSWGUeHmDiy0gvw/zh-cn_image_0000002815399025.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=376E3BF6FEEED9EF8325D57EE1DFC094E45342D6D070094B051422016F3980A2)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ix8KJH3_QYeLPZ2Do5o24A/zh-cn_image_0000002786519450.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDD2F199194DFC4E4D4E14DD3D8B4E0089D6737D448186A2D82035FE07863A71)
* 在选择卡片的开发语言类型（Language）时，选择ArkTS选项。选择卡片支持的外观规格（Support dimension）时，选择期望的卡片尺寸，然后选择默认的外观规格（Default dimension），最后点击“Finish”，即可完成ArkTS卡片创建。详细的卡片外观规格可参考[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件，后续也可以在form\_config.json配置文件中修改卡片规格。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/gyUZfez3R_qE-H-rrk6MAg/zh-cn_image_0000002786359522.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=75071BBC496F533C5260DEADA38FC10AA77DCBA9CDC05757A9C0CB63922F0397)

  建议根据实际使用场景命名卡片名称，ArkTS卡片创建完成后，工程中会新增如下卡片相关文件：卡片生命周期管理文件（EntryFormAbility.ets）、卡片页面文件（WidgetCard.ets）和卡片配置文件（form\_config.json）。填写卡片配置之后点击【Finish】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Y5u56rJURzupIgBD9BT_0g/zh-cn_image_0000002815558943.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E5EE2C90FF8E9FA946CC3B8C78A55B1296E56A7748002BB1995159A471E839D)

### 工程结构介绍

**图1** ArkTS卡片工程目录、相关模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/fexdco-pQLaUFY6Co8ptYw/zh-cn_image_0000002815399027.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5E05BA31A94230C36D88530948271540116B07DED3CCE4921BB4EA2986434F8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/UHkzQyowSXiH8Imw4lIw5g/zh-cn_image_0000002815558941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=71E5D588BAC64990E276A59AA3348071ED7D429F699C932335B9C21FEFAC60C1)

**说明** 

基于不同版本的DevEco Studio，请以实际界面为准。

**2. 新建卡片**

* 选中entry目录单击右键选择【New】->【Service Widget】->【Dynamic Widget(Standalone)】。在Service Widget菜单可直接选择创建独立包的动态卡片（Dynamic Widget(standalone)）或静态卡片（Static Widget(standalone)）。创建服务卡片后，也可以在卡片的[form\_config.json配置文件](arkts-ui-widget-configuration.md#配置文件字段说明)中，通过isDynamic参数修改卡片类型：isDynamic置空或赋值为“true”，则该卡片为[动态卡片](arkts-form-overview.md#动态卡片)；isDynamic赋值为"false"，则该卡片为[静态卡片](arkts-form-overview.md#静态卡片)。静态卡片和动态卡片切换之后用户交互实现也需要修改，具体参考ArkTS卡片概述中的[动态卡片](arkts-form-overview.md#动态卡片)和[静态卡片](arkts-form-overview.md#静态卡片)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NccVyxlWT1iFmFmdJmW8VQ/zh-cn_image_0000002786519452.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=1286CCBB9E2CF1F54A00C80A78DC254D071339E47F06FCEB08409F2483CCC62C)
* 选择模板后，点击【Next】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Z1tuHUCjTb-fR8AUL1x-5Q/zh-cn_image_0000002786519450.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FF5A126363FDE542F8B8695C1E55901498364035C8674933FB006BE20B23E89)
* 填写卡片配置之后点击【Finish】。卡片创建成功后，entry包中包含应用和卡片后端能力；library包中包含卡片UI侧能力。entry模块下的module.json5配置文件中的formWidgetModule字段需关联library模块，library模块下的module.json5配置文件中的formExtensionModule字段需关联entry模块，以实现卡片包和应用包相互关联。创建完成后，会自动生成配置文件并配置，后续也可以按照[卡片配置文件](arkts-ui-widget-configuration.md)修改配置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/e0E0rGakQk2daMpWQY8dzQ/zh-cn_image_0000002786359524.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=B987436439264683901BB6D3A69D11883B6517597B3E559B7C1E4F1BC2761013)

### 工程结构介绍

独立卡片包与卡片共包方式创建卡片，仅工程结构存在差异，生成的文件是一致的，各文件具体内容请参考[共包方式工程结构介绍](arkts-ui-widget-creation.md#工程结构介绍)。

**图2** 独立卡片包工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/oFuOv2TcQAmZkTYl5Z5sOw/zh-cn_image_0000002815558945.png?HW-CC-KV=V1&HW-CC-Date=20261112T233222Z&HW-CC-Expire=31536000000&HW-CC-Sign=10D0091D32835C4C45872FA7A80157CBDBA0FC8740C340AE125EBCD2495764E7)

**说明** 

独立卡片包中应用包和卡片包为2个独立模块，因此需要关注同时安装的应用包和卡片包版本号一致。
