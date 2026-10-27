---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-27
title: List组件如何实现多列效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List组件如何实现多列效果
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:23f63f892257c76fa2d8d241f4eceb1177397beb73cabc74f20aeb4dd6b9be2d
---

设置[List](../harmonyos-references/ts-container-list.md)组件的lanes属性，以实现交叉轴上的多列布局。示例代码如下：

```ts
// xxx.ets
@Entry
@Component
struct ListExample {
  @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

  build() {
    Column() {
      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Row() {
              Text(item)
                .fontColor(Color.Red)
                .fontSize(40)
            }
          }
          .width('100%')
          .border({
            width: 1,
            color: Color.Black,
            radius: 5
          })
        })
      }
      .lanes(3)
      .alignListItem(ListItemAlign.Center)
    }
    .padding({ top: 30 })
  }
}
```

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/9EU_LUoQSDi-VRtdKxk8SA/zh-cn_image_0000002624475914.png "点击放大")
