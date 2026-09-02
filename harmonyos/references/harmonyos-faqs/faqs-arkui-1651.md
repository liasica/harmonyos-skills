---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1651
title: 平板设备上访问应用内页面时出现请用手机访问的弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 平板设备上访问应用内页面时出现请用手机访问的弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:793a91a8f44241ffef711cd6b5c8d155c82daa07ba60e6488c1c54a7a7a95550
---

## 问题现象

使用平板打开应用，在跳转部分二级页面时，出现请用手机访问的弹窗。

## 背景知识

* [promptAction](../harmonyos-references/js-apis-promptaction.md)：可创建并显示文本提示框、对话框和操作菜单。
* [媒体查询](../harmonyos-guides/arkts-layout-development-media-query.md)中的[媒体特征](../harmonyos-guides/arkts-layout-development-media-query.md#媒体特征media-feature)可实现查询当前设备的类型device-type。

## 问题定位

1. 对比平板上出现弹窗和不出现弹窗页面的区别，出现弹窗和不出现弹窗的页面组件不一致，表明采用的是两个页面。
2. 查阅跳转到出现弹窗页面的代码逻辑中是否针对设备类型为tablet做了弹窗适配，例如下面代码。

   ```ts
   import { mediaquery } from '@kit.ArkUI';

   @Entry
   @Component
   struct MediaQueryExample {
     @State text: string = 'Portrait';
     // 当设备为tablet类型时条件成立
     listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(device-type: tablet)');

     build() {
       Column({ space: 50 }) {
         Text(this.text).fontSize(50)
           .onClick(() => {
             if (this.listener.matches) {
               this.getUIContext().getPromptAction().showToast({
                 message: '请用手机访问',
                 duration: 1500
               });
             }

             // 跳转到详情页
           });
       }
       .width('100%').height('100%');
     }
   }
   ```

## 分析结论

应用代码中，针对tablet类型的设备，在部分二级页面跳转时设置了请用手机访问的弹窗，怀疑是当初tablet类型设备适配时，股票详情页未开发时添加的友好弹窗。

## 修改建议

建议在功能实现后及时删除友好提示弹窗代码。

```ts
@Entry
@Component
struct MediaQueryExample {
  private text: string = 'Portrait';

  build() {
    Column({ space: 50 }) {
      Text(this.text).fontSize(50)
        .onClick(() => {
          // 跳转到详情页
        });
    }
    .width('100%').height('100%');
  }
}
```
