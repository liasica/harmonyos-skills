---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-115
title: 图片展示页面，图片序号显示有误
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 图片展示页面，图片序号显示有误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02e6429f9f94b6f876e0ae6014d897baab5bed827c84313a21568f3ec853f4a2
---

## 问题现象

在Web页面点击图片进入图片展示页面，图片序号显示有误，比如应该显示为“1/3”，实际显示为“01/3”。且只有在刚进入页面时出现，图片滑动后就恢复正常。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/1tQWIaaYSRaha-BrY8DLWg/zh-cn_image_0000002659258349.png "点击放大")

## 背景知识

* [ArkWeb](../harmonyos-guides/web-component-overview.md)提供了Web组件，用于在应用程序中显示Web页面内容。应用集成Web页面：应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。App通过[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)，与Web页面进行JavaScript交互。
* [@ohos.util.json (JSON解析与生成)](../harmonyos-references/js-apis-json.md)主要是将JSON文本转换为JSON对象或值，以及将对象转换为JSON文本等功能。其转换原理：
  + 将JSON对象转换为字符串的过程是一个从数据结构到文本的转换过程。它依赖于对JSON格式的准确理解和序列化算法的实现。
  + 序列化算法通过遍历数据结构、处理基本类型、递归处理嵌套结构、拼接字符串以及错误处理等步骤，将JSON对象转换为一个符合JSON格式的字符串。

## 问题定位

1. 通过问题复现，原有逻辑是图片展示页面的标题显示为“当前第几张图片/图片总数”，其中“当前第几张图片”是在Web网页中点击当前图片的索引加1得到。所以标题字符串生成：

   ```ts
   let currentIndex:number = 0
   let imageArr:string[] = []
   let titleStr = (currentIndex + 1) + '/' + imageArr.length
   ```
2. 初次显示成“01/3”，主要的原因是currentIndex虽然定义为number类型，但是赋值给它的数据实际可能是string类型。在JSON解析中会出现这样的问题。例如，将jsonStr中string类型的"currentIndex"通过JSON.parse解析后赋值给number类型的currentIndex，使用===判断发现数据类型并不相同，返回false，currentIndex还是原来的类型。

   ```ts
   let jsonStr = '{"currentIndex" : "2", "totalCount" : 4}';
   // json字符串转Record对象
   let data0: Record<number, string> = JSON.parse(jsonStr) as Record<number, string>;
   let currentIndex: number = data0['currentIndex'];
   if (currentIndex === 2) {
     console.info('The type of currentIndex is number');
   } else {
     console.info('The type of currentIndex is not number');
   }
   ```
3. 滑动后显示恢复，通过日志分析，因为UI布局使用的Swiper组件。给currentIndex赋值的是Swiper的index，index是number类型。

   ```txt
   [(100000:100000:scope)] Swiper FireUnselectedEvent id:915, index:1
   [(100000:100000:scope)] Swiper FireUnselectedEvent id:915, index:2
   [(100000:100000:scope)] Swiper FireUnselectedEvent id:915, index:3
   ```

## 分析结论

* 初次显示有误，是Web网页和图片展示页面交互时，传递的JSON字符串数据中，当前图片的索引为string类型，虽然图片展示页面拿到JSON字符串解析为对象时，对象中的当前图片索引定义为number类型，但实际上还是string类型。
* 滑动后显示恢复，是UI布局使用的Swiper组件。滑动时给currentIndex赋值的是Swiper的index，index是number类型。

## 修改建议

JSON.parse解析并不会修改目标字符串的数据类型为解析指定的数据类型，"currentIndex"解析前是string类型，使用JSON.parse解析后仍然是string类型。需要使用强制类型转换Number()后再赋值。

```ts
@Entry
@Component
struct StringChange {
  @State message: string = 'Hello World';

  aboutToAppear(): void {
    let jsonStr = '{"currentIndex" : "2", "totalCount" : 4}';
    // json字符串转Record对象
    let data0: Record<number, string> = JSON.parse(jsonStr) as Record<number, string>;
    let currentIndex: number = Number(data0['currentIndex']);
    if (currentIndex === 2) {
      console.info('The type of currentIndex is number');
    } else {
      console.info('The type of currentIndex is not number');
    }
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('Index1HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
