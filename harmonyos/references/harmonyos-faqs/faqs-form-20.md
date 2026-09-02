---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-20
title: 如何判断卡片是否添加到桌面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何判断卡片是否添加到桌面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a345fb95f7dcc6f569fdd002888b0984c28ae5aec237e43829c2465b1fcee7bb
---

## 问题现象

如何判断应用的卡片是否已被添加至桌面。

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* 卡片扩展模块[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)提供了卡片的创建、销毁、刷新等生命周期回调函数。
* 从API 20起，[formProvider](../harmonyos-references/js-apis-app-form-formprovider.md)提供[getPublishedRunningFormInfos](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfos20)和[getPublishedRunningFormInfoById](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfobyid20)接口，可以获取应用已加桌的卡片的信息。

## 解决方案

* 应用获取当前已加桌的卡片。

  从API 20起，使用[getPublishedRunningFormInfos](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfos20)获取当前应用已加桌的所有卡片的信息，若无卡片加桌，则报错误码[16500100](../harmonyos-references/errorcode-form.md#section16500100-获取卡片配置信息失败)；使用[getPublishedRunningFormInfoById](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfobyid20)获取当前应用已加桌的指定ID卡片的信息，若指定ID的卡片不存在或未加桌，则报错误码[16500100](../harmonyos-references/errorcode-form.md#section16500100-获取卡片配置信息失败)。

  ```ts
  import { formInfo, formProvider } from '@kit.FormKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Index {
    @State widgetCount: number = 0;
    @State isGettingOne: boolean = false;
    @State isGettingTwo: boolean = false;
    @State widgetInfoGotten: string = '';
    @State formIdTmp: string = '';
    @State formId: string = '';
    @StorageProp('FormArr') widgetCountByLifeCycle: string[] = [];

    build() {
      Column({ space: 16 }) {
        Button('获取加桌卡片数量')
          .type(ButtonType.Capsule)
          .onClick(() => {
            this.isGettingOne = true;
            // 获取本应用全部已加桌卡片的信息
            try {
              formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo[]) => {
                // 当前应用有卡片已加桌，卡片信息获取成功
                console.info(`promise success.`);
                this.formIdTmp = data[0].formId;
                this.widgetCount = data.length;
              }).catch((error: BusinessError) => {
                // 当前应用无卡片加桌，进入报错
                this.widgetCount = 0;
                console.error(`promise error, code: ${error.code}, message: ${error.message}`);
              });
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
            }
          });

        if (this.isGettingOne) {
          Text(`本应用已加桌卡片数量：${this.widgetCount}`)
            .fontSize('18fp')
            .fontWeight(FontWeight.Bold)
            .height(40);
        } else {
          Row()
            .height(40);
        }

        Button('获取指定ID的加桌卡片信息')
          .type(ButtonType.Capsule)
          .onClick(() => {
            this.isGettingTwo = true;
            // 获取本应用已加桌的指定ID卡片的信息
            try {
              this.formId = this.formIdTmp;
              formProvider.getPublishedRunningFormInfoById(this.formId).then((data: formInfo.RunningFormInfo) => {
                // 指定卡片已加桌，卡片信息获取成功
                console.info(`promise success, form id: ${data.formId}`);
                this.widgetInfoGotten = 'Got';
              }).catch((error: BusinessError) => {
                // 指定卡片不存在或未加桌，进入报错
                console.error(`promise error, code: ${error.code}, message: ${error.message}`);
                this.widgetInfoGotten = 'No got';
              });
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
              this.widgetInfoGotten = 'error';
            }
          });

        if (this.isGettingTwo) {
          Text(`卡片id：${this.formId}，信息获取：${this.widgetInfoGotten}`)
            .fontSize('18fp')
            .fontWeight(FontWeight.Bold)
            .height(40);
        } else {
          Row()
            .height(40);
        }
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```
* 加桌时确认卡片是否成功加桌。
  + 从API 20起，卡片扩展模块[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)提供[onFormLocationChanged](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformlocationchanged20)生命周期回调函数，当卡片从卡片管理器中添加至桌面时，会触发onFormLocationChanged回调，[FormLocation](../harmonyos-references/js-apis-app-form-forminfo.md#formlocation20)结果返回0，表示当前卡片位置为桌面。
  + 在API 20前，卡片在加桌时会触发onAddForm生命周期回调函数，可以通过want.parameters的ohos.extra.param.key.form\_location字段获取卡片位置，当字段值为0时，表示卡片位置为桌面。

    ```ts
    import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
    import { Want } from '@kit.AbilityKit';

    export default class EntryFormAbility extends FormExtensionAbility {
      onAddForm(want: Want) {
        // Called to return a FormBindingData object.
        const formData = '';
        if (want.parameters) {
          console.info(`====> Form location: ${want.parameters['ohos.extra.param.key.form_location']}`);
        }
        return formBindingData.createFormBindingData(formData);
      }

      onRemoveForm() {
        // Called to notify the form provider that a specified form has been destroyed.
      }

      onCastToNormalForm() {
        // Called when the form provider is notified that a temporary form is successfully
        // converted to a normal form.
      }

      onUpdateForm() {
        // Called to notify the form provider to update a specified form.
      }

      onFormEvent() {
        // Called when a specified message event defined by the form provider is triggered.
      }

      onAcquireFormState() {
        // Called to return a {@link FormState} object.
        return formInfo.FormState.READY;
      }

      onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void {
        console.info(`formId: ${formId}, now location: ${newFormLocation}`);
      }
    };
    ```

## 总结

* 从API 20起，可以通过接口getPublishedRunningFormInfos或getPublishedRunningFormInfoById获取已加桌卡片的信息，或在生命周期的onFormLocationChanged回调函数中确认卡片是否添加到桌面。
* 在API 20前，可以通过onAddForm回调函数中的卡片位置字段，确认卡片是否添加到桌面。
