---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-103
title: 如何设置应用自动重启
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何设置应用自动重启
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6691c2615a4dcc865ea56276e42f50656b5bfda6ce10a2a73554995667b84a81
---

可以通过ApplicationContext.restartApp实现，具体请参考示例代码：

```typescript
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

      Button('RESTART').onClick(() => {
        let applicationContext = this.context.getApplicationContext();
        let want: Want = {
          bundleName: 'com.example.myapp',
          abilityName: 'EntryAbility'
        };
        try {
          applicationContext.restartApp(want);
          hilog.info(0x0000, 'testTag', '%{public}s', 'applicationContext.restartApp');
        } catch (error) {
          console.error(`restartApp fail, error: ${JSON.stringify(error)}`);
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

**参考链接**

[ApplicationContext.restartApp](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextrestartapp12)
