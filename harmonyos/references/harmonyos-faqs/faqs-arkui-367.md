---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-367
title: 如何获取ArkTS状态管理框架代理前的原始对象
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何获取ArkTS状态管理框架代理前的原始对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:84c4e6af19aa36cdedc32f151484ec0b2b48b6d6530c31006579ae8d1e364f1e
---

使用getTarget接口获取状态管理框架代理前的原始对象。

参考示例如下：

```ts
import { UIUtils } from '@kit.ArkUI';

@Observed
class UserInfo {
  name: string = 'Tom';
}

@Entry
@Component
struct GetTargetDemo {
  @State info: UserInfo = new UserInfo();

  build() {
    Column() {
      Text(`info.name: ${this.info.name}`)
      Button('Change the properties of the proxy object')
        .onClick(() => {
          this.info.name = 'Alice'; // The Text component can refresh
        })
      Button('更改原始对象的属性')
        .onClick(() => {
          let rawInfo: UserInfo = UIUtils.getTarget(this.info);
          if (rawInfo) {
            rawInfo.name = 'Bob'; // The Text component cannot be refreshed
          }
        })
    }
  }
}
```

参考链接

[getTarget接口：获取状态管理框架代理前的原始对象](../harmonyos-guides/arkts-new-gettarget.md)
