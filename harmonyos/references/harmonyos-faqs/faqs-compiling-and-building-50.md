---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-50
title: 如何解决自定义组件struct内不支持定义成员变量get/set方法的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决自定义组件struct内不支持定义成员变量get/set方法的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d0df705be24b75cebdb69348244d55964161e0dd48ea1c2e2a28a5138d1827bb
---

**问题现象**

运行DevEco Studio的build编译构建功能后，产物中不会生成get/set方法的代码逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/zdgMZ9qoTd2waL4jMRkrQg/zh-cn_image_0000002654837825.png)

错误示例如下：

```typescript
@Entry
@Component
struct GetSetDemo {
  private get value(): string {
    return "Hello";
  }
  private set value(value: string) {
    this.value = value;
  }

  build() {
    Row() {
      Column() {
        Text("Hello World")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
    }
  }
}
```

**解决措施**

1.可以使用以下方法替代get方法：

private value: string = "Hello";

2.可以使用以下方式替代 set方法：

this.value = "World"；
