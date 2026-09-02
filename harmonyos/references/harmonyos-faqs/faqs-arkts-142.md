---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-142
title: 如何在调用处实现接口中的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在调用处实现接口中的方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c0ceead45e7f0ddfeed5328d6b10f27f12dc7f05b548e92671736dad9712588
---

示例代码如下：

```screen
// The custom interface is as follows:
export interface OnTrustListener {
  OnSuccess: (data: string) => void;
  OnError: (error: string) => void;
}

@Component
export struct InterfaceUse {
  private listener: OnTrustListener = {
    OnSuccess: (data: string) => {
      console.info('data is:' + data);
    },
    OnError: (error: string) => {
      console.info('error is:' + error);
    }
  };

  build() {
    Column() {
      Button('click me')
        .onClick((event: ClickEvent) => {
          this.listener.OnSuccess('success');
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
