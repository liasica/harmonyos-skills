---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-35
title: Unit Test如何Mock系统API i18n
breadcrumb: FAQ > DevEco Studio > 应用测试 > Unit Test如何Mock系统API i18n
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ee60838f42f7716cd6192796cc5614db2bf7c3c195c0888302bcdd0bac704072
---

## 问题现象

想对[setAppPreferredLanguage](../harmonyos-references/js-apis-i18n.md#setapppreferredlanguage11)和[getDisplayLanguage](../harmonyos-references/js-apis-i18n.md#getdisplaylanguage9)系统API进行Mock，应该如何Mock这两个接口？

## 背景知识

在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用[Mock能力](../harmonyos-guides/ide-test-mock.md)，对这些接口或对象进行模拟。当前[Instrument Test](../harmonyos-guides/ide-instrument-test.md)和[Local Test](../harmonyos-guides/ide-local-test.md)支持对本地模块进行Mock，也支持对系统模块API或外部依赖模块的Mock。

## 解决方案

1. 在src/mock目录下新建一个ArkTS文件：Language.mock.ets，在这个文件内定义目标模块的Mock实现。

   ```ts
   import { i18n } from '@kit.LocalizationKit';

   class MockPreferredLanguage extends i18n.System {
     public static setAppPreferredLanguage(language: string): void {
       console.info('run setAppPreferredLanguage mock')
       throw new Error('setAppPreferredLanguage Error');
     }

     public static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string {
       console.info('run getDisplayLanguage mock')
       return 'en'
     }
   }

   interface I18n {
     System: MockPreferredLanguage
   }

   const mockI18n: I18n = {
     System: MockPreferredLanguage
   }

   export default mockI18n;
   ```
2. 在Mock配置文件src/mock/mock-config.json5中定义目标模块与Mock实现的替换关系。

   ```json
   {
     "@ohos.i18n": {
       "source": "src/mock/Language.mock.ets"
     }
   }
   ```
3. 在测试文件src/test/LocalUnit.test.ets编写如下代码:

   ```ts
   import { i18n } from '@kit.LocalizationKit';
   import { describe, it } from '@ohos/hypium';

   export default function localUnitTest() {
     describe('localUnitTest', () => {
       it('assertContain', 0, () => {
         let language = 'zh';
         let locale = 'en-GB';
         let displayLanguag = i18n.System.getDisplayLanguage(language, locale);
         console.info(`displayLanguag: ${displayLanguag}`)
         try {
           i18n.System.setAppPreferredLanguage(language);
         } catch (error) {
           console.debug('error')
         }
       });
     });
   }
   ```
