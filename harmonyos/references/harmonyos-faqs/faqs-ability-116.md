---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-116
title: 如何跳转到系统文件管理App界面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何跳转到系统文件管理App界面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ef4199064bef4e15b580c174070f8031edeba98d5f8cbc3975565f6269d3bf1
---

可以使用openLink的方式打开，在[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口的link字段中传入系统文件管理页面的URL信息，示例代码如下：

```screen
import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  @State message: string = '拉起文件管理';
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button(this.message)
          .width('100%')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context: common.UIAbilityContext = this.context.getHostContext() as common.UIAbilityContext;
            let link: string = 'filemanager://openDirectory';
            let openLinkOptions: OpenLinkOptions = {
              parameters: {
                'fileUri': ''
              }
            };
            try {
              context.openLink(link, openLinkOptions)
                .then(() => {
                  hilog.info(DOMAIN_NUMBER, TAG, 'Open link success.');
                }).catch((err: BusinessError) => {
                hilog.error(DOMAIN_NUMBER, TAG, `Open link failed. Code is ${err.code}, message is ${err.message}`);
              });
            } catch (paramError) {
              hilog.error(DOMAIN_NUMBER, TAG,
                `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
            }
          })
      }
      .padding({ left: 16, right: 16 })
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接：**

[UIAbilityContext.openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)
