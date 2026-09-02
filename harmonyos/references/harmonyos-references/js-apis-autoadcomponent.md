---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent
title: "@ohos.advertising.AutoAdComponent (轮播广告展示组件)"
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS组件 > @ohos.advertising.AutoAdComponent (轮播广告展示组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a8f318c48fae5752f24f4db623e19f361603ae7fbde3a6dd256c73e78d170304
---

本模块提供展示轮播广告的能力。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```typescript
import { AutoAdComponent } from '@kit.AdsKit';
```

## AutoAdComponent

```typescript
AutoAdComponent({
  adParam: advertising.AdRequestParams,
  adOptions: advertising.AdOptions,
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener
})
```

用于展示轮播广告的组件。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **名称** | **类型** | 必填 | **装饰器类型** | 说明 |
| --- | --- | --- | --- | --- |
| adParam | advertising.[AdRequestParams](js-apis-advertising.md#adrequestparams) | 是 | - | 广告请求参数。 |
| adOptions | advertising.[AdOptions](js-apis-advertising.md#adoptions) | 是 | - | 广告配置参数。 |
| displayOptions | advertising.[AdDisplayOptions](js-apis-advertising.md#addisplayoptions) | 是 | - | 广告展示参数。 |
| interactionListener | advertising.[AdInteractionListener](js-apis-advertising.md#adinteractionlistener) | 是 | - | 广告状态变化回调。 |

**示例：**

```typescript
import { advertising, AutoAdComponent } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 广告请求参数
  private adRequestParams: advertising.AdRequestParams = {
    // 广告位ID
    adId: 'h5xkz3mbr2',
    // 广告类型
    adType: 8,
    // 广告位宽，单位vp
    adWidth: 360,
    // 广告位高，单位vp
    adHeight: 57
  };
  // 广告配置参数
  private adOptions: advertising.AdOptions = {};
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {
    // 广告轮播的时间间隔，单位ms，取值范围[30000, 120000]
    refreshTime: 30000
  };
  private ratio: number = -1;

  aboutToAppear() {
    if (this.adRequestParams.adWidth && this.adRequestParams.adHeight) {
      this.ratio = this.adRequestParams.adWidth / this.adRequestParams.adHeight;
    }
  }
  
  build() {
    Column() {
      AutoAdComponent({
        adParam: this.adRequestParams,
        adOptions: this.adOptions,
        displayOptions: this.adDisplayOptions,
        interactionListener: {
          onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
            switch (status) {
              case 'onAdOpen':
                hilog.info(0x0000, 'testTag', 'onAdOpen');
                break;
              case 'onAdClick':
                hilog.info(0x0000, 'testTag', 'onAdClick');
                break;
              case 'onAdClose':
                hilog.info(0x0000, 'testTag', 'onAdClose');
                break;
            }
          }
        }
      })
        .width('100%')
        .aspectRatio(this.ratio)
    }
    .width('100%')
    .height('100%')
  }
}
```

### build

build(): void

用于创建AutoAdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
