---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-228
title: 自定义组件是否能通过容器保存
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义组件是否能通过容器保存
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b790ead9cfe95422ee6afd926cc46de87a5dd79a97b29c0bbe8834aff9d9c4a
---

自定义组件是 struct 而非 class，因此无法直接存储在容器中。可以通过将自定义组件封装在 Builder 函数中，利用 Builder 的封装来实现存储。

参考代码如下：

```ts
@Component
struct ComA {
  build() {
    Text('ComA').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

@Component
struct ComB {
  build() {
    Text('ComB').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

@Component
struct ComC {
  build() {
    Text('ComC').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

//if else logical branch writing
@Builder
function buildCom(param: string) {
  if (param == 'ComA') {
    ComA()
  } else if (param == 'ComB') {
    ComB()
  } else if (param == 'ComC') {
    ComC()
  }
}

@Builder
function buildComA() {
  ComA()
}

@Builder
function buildComB() {
  ComB()
}

@Builder
function buildComC() {
  ComC()
}

//Encapsulate in container through map
let map: Map<string, WrappedBuilder<[]>> = new Map();
map.set('ComA', wrapBuilder(buildComA));
map.set('ComB', wrapBuilder(buildComB));
map.set('ComC', wrapBuilder(buildComC));

@Component
struct Page12 {
  @State message: string = 'Hello World';
  @State arr: string[] = ['ComA', 'ComB', 'ComC'];

  build() {
    Column() {
      ForEach(this.arr, (item: string) => {
        //Retrieve based on the key during use
        map.get(item)?.builder()
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

**参考链接：**

[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)
