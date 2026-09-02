---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-7002
title: 针对所有应用的变更
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > OS平台行为变更说明 > 26.0.0 Beta2引入的行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:27+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1df23ec507ae327742b8f99da3bbf5cd180396ab77368ff2e442063d904cea13
---

## ArkUI

### List组件onScrollVisibleContentChange事件行为变更

**变更原因**

[List](../harmonyos-references/ts-container-list.md)组件[onScrollVisibleContentChange](../harmonyos-references/ts-container-list.md#onscrollvisiblecontentchange12)事件索引输出规则与空列表参数设计定义不符，原列表从有数据切换成没有数据时复用旧start和end参数，优化后该场景start和end参数的index成员均为-1，itemGroupArea和itemIndexInGroup成员均为undefined，符合空列表参数设计定义。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：[List](../harmonyos-references/ts-container-list.md)组件[onScrollVisibleContentChange](../harmonyos-references/ts-container-list.md#onscrollvisiblecontentchange12)事件从有子组件切换到没有子组件时，上报的start和end参数均为原值。
* 变更后：[List](../harmonyos-references/ts-container-list.md)组件[onScrollVisibleContentChange](../harmonyos-references/ts-container-list.md#onscrollvisiblecontentchange12)事件从有子组件切换到没有子组件时，上报的start和end参数的index成员均为-1，itemGroupArea和itemIndexInGroup成员均为undefined。

```ts
@Entry
@Component
struct ListExample {
  @State listData: string[] = ['item1', 'item2', 'item3'];

  build() {
    Column() {
      Button('清空列表数据')
        .onClick(() => {
          this.listData = [];
        })
      List() {
        ForEach(this.listData, (item: string) => {
          ListItem() {
            Text(item)
              .width('100%')
              .height(100)
              .textAlign(TextAlign.Center)
          }
        })
      }
      .width('100%')
      .height('100%')
      .onScrollVisibleContentChange((start, end) => {
        console.info(`start: ${start.index}, end: ${end.index}`);
        // 变更前：当listData从['item1', 'item2', 'item3']变为[]时，打印 start: 0, end: 2
        // 变更后：当listData从['item1', 'item2', 'item3']变为[]时，打印 start: -1, end: -1
      })
    }
  }
}
```

**起始 API Level**

12

**变更发生版本**

从OpenHarmony SDK 7.0.0.28开始。

**变更的接口/组件**

[onScrollVisibleContentChange](../harmonyos-references/ts-container-list.md#onscrollvisiblecontentchange12)事件。

**适配指导**

如果应用依赖[onScrollVisibleContentChange](../harmonyos-references/ts-container-list.md#onscrollvisiblecontentchange12)事件的start和end参数来判断列表内容变化，当列表从有内容变为空时，开发者需要适配start和end参数的index为-1的场景。例如，开发者需要在事件回调中判断index是否为-1，以区分列表为空的情况。

```ts
@Entry
@Component
struct ListExample {
  @State listData: string[] = ['item1', 'item2', 'item3'];

  build() {
    Column() {
      Button('清空列表数据')
        .onClick(() => {
          this.listData = [];
        })
      List() {
        ForEach(this.listData, (item: string) => {
          ListItem() {
            Text(item)
              .width('100%')
              .height(100)
              .textAlign(TextAlign.Center)
          }
        })
      }
      .width('100%')
      .height('100%')
      .onScrollVisibleContentChange((start, end) => {
        // 适配指导：判断列表是否为空
        if (start.index === -1 && end.index === -1) {
          console.info('列表为空');
        } else {
          console.info(`可见列表项范围：start: ${start.index}, end: ${end.index}`);
        }
      })
    }
  }
}
```

## ArkWeb

### Cookie存储目录变更

**变更原因**

ArkWeb产生的Cookie目前存储在应用的缓存目录下，清空应用缓存会同时清除Cookie数据，导致Web页面内的登录态丢失。

**变更影响**

此变更涉及应用适配。

变更前：ArkWeb的Cookie存储在应用的缓存目录（/data/storage/el2/base/cache/web/Cookies）下，清空应用缓存（/data/storage/el2/base/cache）会同时清除Cookie数据。

变更后：ArkWeb的Cookie存储在应用的数据目录下，清空应用缓存（/data/storage/el2/base/cache）不会清除Cookie数据。

**起始 API Level**

9

**变更发生版本**

从OpenHarmony SDK 7.0.0.23开始。

**变更的接口/组件**

不涉及

**适配指导**

若应用期望在清空应用缓存时同时清除Cookie，需使用[clearAllCookiesSync11+](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearallcookiessync11)、[clearAllCookies11+](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearallcookies11)（callback）或[clearAllCookies11+](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearallcookies11-1)（Promise）接口清除Cookie。
