---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-85
title: 如何通过Index获取ArrayList中的元素
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过Index获取ArrayList中的元素
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f276812c1e0e2da92927388f78de6bb449d300ff275ee1ff7b12f26b0eb0997f
---

* 方式一：

  JS语法基础中可以通过数组元素的下标直接访问数组中的对象。示例如下：

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
* 方式二：

  使用[subArrayList](../harmonyos-references/js-apis-arraylist.md#subarraylist)，subArrayList可以截取ArrayList中的一段元素，并返回这一段ArrayList实例。示例如下：

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
