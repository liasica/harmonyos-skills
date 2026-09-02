---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-18
title: 通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c54a51497caac6844448604de4d844d2a47ce2979467405bbd63f9b4211e6de
---

**问题现象**

通过this.resourceManager.getStringResource($r('app.string.PlayCount').id)获取HSP资源文件时出现错误。

错误消息：资源ID无效。

错误代码：9001001

SourceCode：returnResource = this.context.resourceManager.getStringSync(id)。

**可能原因**

传入的id值不存在，未创建相应的context。

**解决措施**

根据模块名创建上下文Context，然后使用getStringByNameSync方法获取指定资源名称对应的字符串。具体示例代码如下：

```typescript
import { common, application } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button()
        .onClick(() => {
          // Create a context based on the module name
          let moduleName: string = 'library';
          application.createModuleContext(this.context, moduleName)
            .then((data: common.Context) => {
              console.info(`CreateModuleContext success, data: ${JSON.stringify(data)}`);
              if (data !== null) {
                this.getUIContext().getPromptAction().showToast({
                  message: ('get Context success')
                });
              }

              // Then run getStringByNameSync to obtain the string corresponding to the specified resource name
              try {
                let str = data.resourceManager.getStringByNameSync('shared_desc');
                console.info(`getStringByNameSync, data: ${JSON.stringify(str)}`);
              } catch (error) {
                let code = (error as BusinessError).code;
                let message = (error as BusinessError).message;
                console.error(`getStringByNameSync failed, error code: ${code}, message: ${message}.`);
              }
            })
            .catch((err: BusinessError) => {
              console.error(`CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}`);
            });
        })
    }
  }
}
```

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)、[获取本应用中其他module的context](../harmonyos-guides/application-context-stage.md#获取本应用中其他module的context模块级别的上下文)、[getStringByNameSync](../harmonyos-references/js-apis-resource-manager.md#getstringbynamesync9)
