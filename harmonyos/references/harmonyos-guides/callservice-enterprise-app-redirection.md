---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-app-redirection
title: 应用跳转陌生号码和信息识别页面
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 应用跳转陌生号码和信息识别页面
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:24+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:8a15a8dab5a53c23f3e0081032aab4fe5a222e1d259f91c98671e35ed9f1a26d
---

从6.1.0(23)版本开始，新增支持从应用直接跳转到“电话 > 更多 > 设置 > 陌生号码和信息识别"。

通过[Deep Linking](deep-linking-startup.md)方式应用可以直接跳转“陌生号码和信息识别”页面。

以使用openLink实现应用跳转举例，在openLink接口的link字段中传入目标应用的URL信息，并将options字段中的appLinkingOnly配置为false、跳转的URL固定为"callsetting://number\_identity"。

其他跳转方式参考使用Deep Linking实现应用间跳转[拉起方应用实现应用跳转](deep-linking-startup.md#拉起方应用实现应用跳转)章节。

示例代码：

```typescript
import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Button('start link', { type: ButtonType.Capsule, stateEffect: true })
      .width('87%')
      .height('5%')
      .margin({ bottom: '12vp' })
      .onClick(() => {
        let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let link: string = 'callsetting://number_identity';
        let openLinkOptions: OpenLinkOptions = {
          appLinkingOnly: false
        };
       try {
          context.openLink(link, openLinkOptions)
            .then(() => {
                hilog.info(0, 'TAG','Successed in opening link.');
            }).catch((err: BusinessError) => {
              hilog.error(0, 'TAG',`Failed to open link. Code is ${err.code}, message is ${err.message}`);
            });
        } catch (paramError) {
           hilog.error(0, 'TAG',`Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
        }
      })
  }
}
```
