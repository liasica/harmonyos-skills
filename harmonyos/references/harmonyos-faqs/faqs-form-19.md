---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-19
title: 如何根据不同尺寸的卡片适配不同的UI
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何根据不同尺寸的卡片适配不同的UI
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ef067175146ee2214582fc5a7b5d60693ea00085a358701f3f211845ab55d358
---

## 问题现象

开发服务卡片如何针对不同尺寸的卡片适配不同的UI？

## 背景知识

Form Kit（卡片开发框架）提供了一种在桌面、锁屏等系统入口嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片上，通过将卡片添加到桌面上，以达到信息展示、服务直达的便捷体验效果。卡片的创建可参考[创建一个ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)，卡片的生命周期可参考[卡片生命周期管理](../harmonyos-guides/arkts-ui-widget-lifecycle.md)。

## 解决方案

* 在创建卡片的生命周期[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)中，通过want.parameters.[formInfo.FormParam.DIMENSION\_KEY]取出卡片尺寸的相关信息，再通过[formBindingData.createFormBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md#formbindingdatacreateformbindingdata)创建FormBindingData对象并将尺寸信息传入卡片，在卡片页面根据不同尺寸信息结合业务场景适配不同的UI。

  卡片尺寸枚举请参考[FormDimension](../harmonyos-references/js-apis-app-form-forminfo.md#formdimension)。

  EntryFormAbility示例代码如下：

  ```ts
  import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
  import { Want } from '@kit.AbilityKit';

  export default class EntryFormAbility extends FormExtensionAbility {
    transNumToStrName(dim: formInfo.FormDimension) {
      switch (dim) {
        case formInfo.FormDimension.Dimension_1_2:
          return 'Dimension_1_2';
        case formInfo.FormDimension.Dimension_2_2:
          return 'Dimension_2_2';
        case formInfo.FormDimension.Dimension_2_4:
          return 'Dimension_2_4';
        case formInfo.FormDimension.Dimension_4_4:
          return 'Dimension_4_4';
        case formInfo.FormDimension.DIMENSION_1_1:
          return 'DIMENSION_1_1';
        case formInfo.FormDimension.DIMENSION_6_4:
          return 'DIMENSION_6_4';
        case formInfo.FormDimension.DIMENSION_2_3:
          return 'DIMENSION_2_3';
        case formInfo.FormDimension.DIMENSION_3_3:
          return 'DIMENSION_3_3';
        default:
          return 'error';
      }
    }

    onAddForm(want: Want) {
      // Called to return a FormBindingData object.
      let dimension: string = '';
      if (want.parameters) {
        dimension = JSON.stringify(want.parameters[formInfo.FormParam.DIMENSION_KEY]); // 获取要创建的卡片的尺寸
        console.info('dimension=' + dimension);
      }
      let obj: Record<string, string> = {
        'dimension': this.transNumToStrName(Number(dimension))
      };
      return formBindingData.createFormBindingData(obj);
    }

    onCastToNormalForm(formId: string) {
      // Called when the form provider is notified that a temporary form is successfully
      // converted to a normal form.
      console.info('onCastToNormalForm', formId);
    }

    onUpdateForm(formId: string) {
      // Called to notify the form provider to update a specified form.
      console.info('onUpdateForm', formId);
    }

    onFormEvent(formId: string, message: string) {
      // Called when a specified message event defined by the form provider is triggered.
      console.info('onFormEvent', formId, message);
    }

    onRemoveForm(formId: string) {
      // Called to notify the form provider that a specified form has been destroyed.
      console.info('onRemoveForm', formId, formId);
    }

    onAcquireFormState(want: Want) {
      // Called to return a {@link FormState} object.
      console.info('onAcquireFormState', want.bundleName);
      return formInfo.FormState.READY;
    }
  };
  ```

  WidgetCard示例代码如下：

  ```ts
  let storageUpdateByMsg = new LocalStorage();

  @Entry(storageUpdateByMsg)
  @Component
  export struct WidgetCard {
    // 卡片页面接收尺寸信息
    @LocalStorageProp("dimension") dimension: string = '';

    build() {
      Column() {
        Text(this.dimension)
          .fontSize(16);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 若卡片内容差异较大，可以通过单独的[卡片配置](../harmonyos-guides/arkts-ui-widget-configuration.md#卡片配置)实现。在widget的pages目录下创建并实现多个卡片页面布局，在form\_config.json文件中配置多个卡片，并根据需求配置卡片的尺寸和页面内容。

## 常见FAQ

Q：卡片预览有3种尺寸Minimum、Default、Maximum的展示，不同尺寸的留白不同，是否需要关注每种尺寸的效果，能否做到自动适配？

A：服务卡片内请保留四周各12vp的安全间距，服务卡片内容尽可能保证在安全范围内，在圆角剪裁时避免对内容造成影响。卡片字体大小，边距等需自行调配，不会自动适配大小。具体布局建议可参考[卡片内容设计](../design-guides/system-features-service-widget-0000002087671904.md#section248mcpsimp)。开发者应确保三种尺寸的显示效果均正常，以便适应不同屏幕尺寸的设备。

Q：Form Kit（卡片开发框架）是否支持自定义卡片大小？

A：Form Kit（卡片开发框架）不支持自定义卡片大小，但可以预定义卡片尺寸。通过卡片支持的外观规格[supportDimensions](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)可知，卡片大小有如下取值：

* 1\*1：表示1行1列的一宫格。（仅支持在锁屏上使用）
* 1\*2：表示1行2列的二宫格。
* 2\*2：表示2行2列的四宫格。
* 2\*4：表示2行4列的八宫格。
* 2\*3：表示2行3列的六宫格。（仅支持手表设备）
* 3\*3：表示3行3列的九宫格。（仅支持手表设备）
* 4\*4：表示4行4列的十六宫格。
* 6\*4：表示6行4列的二十四宫格。

Q：在form\_config.json中修改defaultDimension为3×3会有红线报错？

A：defaultDimension取值必须在该卡片supportDimensions配置的列表中，supportDimensions列表中需要添加3×3的外观规格。

Q：HarmonyOS不同设备卡片尺寸不同，如何理解[尺寸与基础参数](../design-guides/system-features-service-widget-0000002087671904.md#section250mcpsimp)中介绍的卡片尺寸？

A：[尺寸与基础参数](../design-guides/system-features-service-widget-0000002087671904.md#section250mcpsimp)中提供的卡片尺寸是设计的标准画板（方便设计师使用一个尺寸画图），实际真机卡片尺寸各不相同。由于不同真机（直板机/阔折叠/折叠屏等）设备尺寸的不确定性会导致卡片的尺寸发生变化，设计师在交付卡片布局的过程中，推荐采用[使用百分比](../design-guides/system-features-service-widget-0000002087671904.md#section1422033919410)进行标注。

Q：元服务添加到桌面的卡片大小是否可以更改？

A：加桌之后的元服务卡片的大小是固定尺寸，当前开发者在没有适配其他大小尺寸的卡片前提下，无法改变桌面卡片的大小。所以建议在创建卡片的时候，就规划多个尺寸的卡片，以支持创建多种不同大小的卡片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/X_nyuNyQR4Cfn32cuoG46g/zh-cn_image_0000002628791562.png "点击放大")

Q：如何解决小尺寸卡片中图片显示不完全？

A：根据卡片大小，调整图片尺寸或图片的填充方式[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)，如设置为ImageFit.Contain，使图片完整显示。
