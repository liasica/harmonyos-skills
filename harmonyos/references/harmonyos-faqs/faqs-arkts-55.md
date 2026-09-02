---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-55
title: ArkTS中this的常用场景及使用
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中this的常用场景及使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1845d87427df658b13693f710698697c13c9e7c34fcea7375b119dea77597777
---

在ArkTS中，this 用于类中访问对象属性和方法，或在自定义组件的回调中使用UIContext.getHostContext(this)。

* 类中使用 this，this 实际指向实例化后的对象。

  ```ts
  class UserInfo {
    name: string = 'xxx';

    getName() {
      return this.name;
    }
  }

  const user: UserInfo = new UserInfo();
  ```
* 在自定义组件中使用 this，通常是在回调事件中，此时 this 指向自定义组件本身。常用的方法是通过UIContext.getHostContext(this)获取上下文。
