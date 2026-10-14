---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0001
title: ArkTS-ArrayList元素获取与截取常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 常见问题 > ArkTS-ArrayList元素获取与截取常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:47+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:2445d9705f936a6f35c034579f333b49d65e54bc4dcf4935d67231035d9fe96a
---

**Q：如何通过Index获取ArrayList中的元素？**

**A**：获取ArrayList中的元素有以下两种方式：

* 方式一：JS语法基础中可以通过数组元素的下标直接访问数组中的对象。示例如下：

  ```ts
  import { ArrayList } from '@kit.ArkTS';

  let arrayList: ArrayList<number> = new ArrayList();
  arrayList.add(0);
  arrayList.add(1);
  arrayList.add(2);
  arrayList.add(3);
  arrayList.add(4);
  arrayList.add(5);
  arrayList.add(6);
  arrayList.add(7);
  arrayList.add(8);
  arrayList.add(9);

  @Entry
  @Component
  struct Index {
    @State message: string = 'get arrayList value';

    build() {
      Row() {
        Column() {
          Button(this.message)
            .onClick(() => {
              console.info('arrayList[6]:', arrayList[6]);
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* 方式二：使用[subArrayList](../harmonyos-references/js-apis-arraylist.md#subarraylist)，subArrayList可以截取ArrayList中的一段元素，并返回这一段ArrayList实例。示例如下：

  ```ts
  import { ArrayList } from '@kit.ArkTS';

  let arrayList: ArrayList<number> = new ArrayList();
  arrayList.add(0);
  arrayList.add(1);
  arrayList.add(2);
  arrayList.add(3);
  arrayList.add(4);
  arrayList.add(5);
  arrayList.add(6);
  arrayList.add(7);
  arrayList.add(8);
  arrayList.add(9);

  let result: ArrayList<number> = arrayList.subArrayList(2, 4);

  @Entry
  @Component
  struct Index {
    @State message: string = 'subArrayList result';

    build() {
      Row() {
        Column() {
          Button(this.message)
            .onClick(() => {
              console.info('subArrayList result:', JSON.stringify(result)); // subArrayList result {"0":"2","1":"3"}
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
