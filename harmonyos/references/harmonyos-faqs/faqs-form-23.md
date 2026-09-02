---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-23
title: 如何将卡片添加至桌面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何将卡片添加至桌面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79b6877eedea37f436349723ec69b3280825c84be449659cd0468edd9f25beb7
---

## 问题现象

如何将应用的卡片添加至桌面？在桌面以及在应用内分别有哪些方式？

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* 从API 18起，Form Kit提供[formProvider.openFormManager](../harmonyos-references/js-apis-app-form-formprovider.md#formprovideropenformmanager18)接口，可从应用内拉起卡片管理页面，将卡片添加至桌面。
* [FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)组件封装了一个“添加至桌面”菜单，用于实现应用内长按组件生成“添加至桌面”菜单，点击该菜单，触发卡片添加至桌面操作。

## 解决方案

可以通过以下四种方式将卡片添加至桌面。

* 桌面长按应用图标，点击卡片，拉起卡片管理页面，将卡片添加至桌面。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/IxH7rWgWSdyyJlaXR8_W_Q/zh-cn_image_0000002658990873.png "点击放大")
* 桌面双指捏合，进入桌面管理，点击下方卡片，拉起卡片页面，将卡片添加至桌面。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/OccMChWSTTeTA7SjIkXhlg/zh-cn_image_0000002628631664.png "点击放大")
* 应用内调用formProvider.openFormManager接口，拉起卡片管理页面，将卡片添加至桌面。[formProvider.openFormManager](../harmonyos-references/js-apis-app-form-formprovider.md#formprovideropenformmanager18)接口根据传入的want参数，拉起卡片管理页面并优先显示参数对应的卡片。若want参数错误，则无法拉起卡片管理页面；若want参数的parameters字段不完整或指定的卡片不存在，则默认展示form\_config.json中配置的默认卡片。
  + want参数需包含字段包括：
    - bundleName：卡片所属应用的包名。
    - abilityName：卡片所属的ability名称。
    - parameters：展示卡片的参数，详见下文。
  + parameters需包含的字段包括：
    - ohos.extra.param.key.form\_dimension：卡片尺寸，参考[FormDimension](../harmonyos-references/js-apis-app-form-forminfo.md#formdimension)。
    - ohos.extra.param.key.form\_name：卡片名称，即form\_config.json中卡片对应的name。
    - ohos.extra.param.key.module\_name：卡片所属的模块名称。

  示例代码如下：

  ```ts
  import { formProvider } from '@kit.FormKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { Want } from '@kit.AbilityKit';
  import { promptAction } from '@kit.ArkUI';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;

  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column() {
          // 添加拉起卡片管理页面按钮
          Button('添加卡片')
            .onClick(() => {
              const want: Want = {
                bundleName: 'com.example.myapplication', // 包名
                abilityName: 'EntryFormAbility', // 模块ability名称
                parameters: {
                  'ohos.extra.param.key.form_dimension': 2, // 卡片尺寸
                  'ohos.extra.param.key.form_name': 'widget', // 卡片名称
                  'ohos.extra.param.key.module_name': 'entry' // 卡片所属的模块名称
                },
              };
              try {
                // 点击按钮后调用openFormManager方法，拉起卡片管理页面
                formProvider.openFormManager(want);
              } catch (error) {
                promptAction.openToast({ message: (error as BusinessError).message });
                hilog.info(DOMAIN, 'testTag', 'catch error ', 'code:', (error as BusinessError).code, 'message:',
                  (error as BusinessError).message);
              }
            })
            .margin({ top: 10, bottom: 10 });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  实现效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/yxWL3GK5SfSAZmInwmnf6w/zh-cn_image_0000002658870937.png "点击放大")
* 使用[FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)组件，通过长按组件弹出“添加至桌面”菜单，将卡片添加至桌面。以[Menu](../harmonyos-references/ts-basic-components-menu.md)组件为菜单容器，通过[AddFormMenuItem](../harmonyos-references/ohos-arkui-advanced-formmenu.md#addformmenuitem)添加菜单子项，根据AddFormMenuItem中传入的参数want，将指定的卡片添加至桌面，添加时会根据传入的组件ID获取组件快照和位置，用于添加桌面时的过渡动效。若want参数或组件ID错误、指定的卡片不存在或未在form\_config.json中配置，则无法将卡片添加至桌面。
  + want参数需包含字段包括：
    - bundleName：卡片所属应用的包名。
    - abilityName：卡片所属的ability名称。
    - parameters：展示卡片的参数，详见下文。
  + parameters需包含的字段包括：
    - ohos.extra.param.key.form\_dimension：卡片尺寸，参考[FormDimension](../harmonyos-references/js-apis-app-form-forminfo.md#formdimension)。
    - ohos.extra.param.key.form\_name：卡片名称，即form\_config.json中卡片对应的name。
    - ohos.extra.param.key.module\_name：卡片所属的模块名称。

  示例代码如下：

  ```ts
  import { AddFormMenuItem } from '@kit.ArkUI';
  import { formBindingData } from '@kit.FormKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const tag = 'AddFormMenuItem';

  @Entry
  @Component
  struct FormMenuDemo {
    private compId: string = 'addforms@d46313145';

    @Builder
    MyMenu() {
      Menu() {
        AddFormMenuItem(
          {
            bundleName: 'com.example.myapplication', // 包名
            abilityName: 'EntryFormAbility', // 模块ability名称
            parameters: {
              'ohos.extra.param.key.form_dimension': 2, // 卡片尺寸
              'ohos.extra.param.key.form_name': 'widgetImage', // 卡片名称
              'ohos.extra.param.key.module_name': 'entry' // 卡片所属的模块名称
            },
          },
          this.compId,
          {
            formBindingData: formBindingData.createFormBindingData({}),
            callback: (error, formId) => {
              hilog.info(0x3900, tag, `callback info：error = ${JSON.stringify(error)}, formId = ${formId}`);
              if (error?.code === 0) {
                hilog.info(0x3900, tag, '添加至桌面成功');
              } else {
                hilog.info(0x3900, tag, '添加至桌面失败，请尝试其它添加方式');
              }
            }
          }
        );
      };
    }

    build() {
      Row() {
        Column({ space: 36 }) {
          Text('长按图片添加卡片到桌面')
            .fontSize('18fp');

          Image($r('app.media.startIcon')) // 自定义图片
            .id(this.compId)
            .width(150)
            .height(150)
            // 绑定菜单
            .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
              placement: Placement.TopLeft
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  实现效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/bbMtMiBrS0WFtWN18-dNPA/zh-cn_image_0000002628791568.png "点击放大")

## 总结

将卡片添加至桌面，可以在桌面或应用内添加：

* 桌面添加卡片，可以通过长按应用图标，或双指捏合进入的桌面管理中拉起卡片管理页面，在卡片管理页面将卡片添加至桌面。
* 应用内添加卡片，需应用通过调用formProvider.openFormManager接口或使用FormMenu组件，将对应卡片添加至桌面。

## 常见FAQ

Q：桌面实际有空间，但卡片加桌时提示桌面空间已满。

A：卡片在加桌时，桌面布局会判断当前页与下一页是否有空间添加卡片。若当前页与下一页没有可容纳卡片的空间，则会新建一屏；当桌面达到18屏，且桌面布局判断无满足空间添加卡片时，系统会提示桌面空间已满。

Q：卡片添加到桌面后，卡片下方显示的名称是否可以修改？

A：卡片下方显示的内容是应用名称，不支持修改。
