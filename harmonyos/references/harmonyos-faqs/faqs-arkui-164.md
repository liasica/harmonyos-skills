---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-164
title: 如何获取router.back传递的参数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取router.back传递的参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba0e8c6d6a1a05c914fe4047889c5550c3fdc03f3ca65af21c56b35e65819d30
---

在 onPageShow 回调方法中使用 Router模块的getParams方法来获取传递过来的参数。参考代码如下：

```ts
class InfoTmp {
  age: number = 0
}

class RouTmp {
  id: object = () => {
  }
  info: InfoTmp = new InfoTmp()
}

const context = AppStorage.get("context") as UIContext;
const params: RouTmp = context.getRouter().getParams() as RouTmp; // Get the parameter object passed
const id: object = params.id // Get the value of the id property
const age: number = params.info.age // Get the value of the age property
```

**参考链接**

[页面跳转](../harmonyos-guides/arkts-routing.md#页面跳转)
