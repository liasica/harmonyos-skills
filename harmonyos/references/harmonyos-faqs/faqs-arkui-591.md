---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-591
title: Text组件如何渲染包含em标签的html字符串
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件如何渲染包含em标签的html字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1e4a272d5b0f389085f4e7ba819d77d2dd31a2b6c727fa85e1e3d98a2a25413f
---

## 问题现象

html字符串中包含em标签，使用Text组件如何增强对于文本的渲染？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/i75lXJMGTge-ISIz1YWVXA/zh-cn_image_0000002658791787.png "点击放大")

## 背景知识

* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：接口基于数组类型数据来进行循环渲染。
* [Span](../harmonyos-references/ts-basic-components-span.md)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。

## 解决方案

1. 创建方法heightLightWord，使用正则表达式对html字符串进行解析，返回包含content和light字段的数组。
2. 使用ForEach遍历数组，根据light字段设置文本的渲染样式。

```ts
interface isHeightLight {
  content: string,
  light: boolean
}

@Entry
@Component
struct IndexOfPage {
  value: string = '<em>第</em>二届海南<em>岛</em>国际<em>电</em>影节开幕式';

  heightLightWord(word: string) {
    // 先将需要高亮的字符筛选出来，待会高亮
    let str = word;
    let result: string[] = [];
    let index = 0;
    while ((index = str.indexOf("<em>", index)) !== -1) {
      if (index + 4 < str.length) {
        result.push(str[index + 4]);
      }
      index += 4;
    }
    // 将字符之间的html格式全部去除
    let rt: string = this.value.replace('<p></p><p></p>', '\n').replace('<p>', '\n').replace('\n\n', '\n');
    rt = rt.replace(/<br\s*\/?>/g, '\n');
    rt = rt.replace(/<\/?p/gi, '\n');
    rt = rt.replace(/<[^>]+>/g,
      '');
    // 取'>'反的集合[^>]，+匹配集合元素一次或多次
    rt = rt.replace(/>/g, '');
    if (this.value) {
      rt = rt.trim();
    }
    const wordArr = rt.split('');
    const indexArr: number[] = [];
    // 获取所有符合条件的下标
    result.forEach((item: string) => {
      let index = wordArr.indexOf(item);
      while (index !== -1) {
        indexArr.push(index);
        index = wordArr.indexOf(item, index + 1);
      }
    });
    return wordArr.map((item: string, index: number): isHeightLight => {
      if (indexArr.indexOf(index) !== -1) {
        return { content: item, light: true };
      } else {
        return { content: item, light: false };
      }
    });
  }

  build() {
    Column() {
      Text() {
        ForEach(this.heightLightWord(this.value), (item: isHeightLight) => {
          Span(item.content)
            .fontColor(item.light ? Color.Blue : Color.Black)
            .fontWeight(item.light ? FontWeight.Bolder : FontWeight.Normal)
            .fontSize(item.light ? 20 : 14)
        })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
