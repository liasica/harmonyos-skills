---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-20
title: 如何解决mock中继承Base64Helper不生效的问题
breadcrumb: FAQ > DevEco Studio > 应用测试 > 如何解决mock中继承Base64Helper不生效的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:92119187a966422417d4d8a1e47335f7d6ed735b0b9e0e41508d84291b7d9915
---

## 问题现象

mock中继承Base64Helper不生效。

问题代码示例参考如下：

```ts
// Base64HelperMock.mock.ets
import { util } from '@kit.ArkTS'

export class Base64HelperMock extends util.Base64Helper {
  decodeSync(src: string | Uint8Array, options?: util.Type | undefined): Uint8Array {
    return new Uint8Array([99,97,10]);
  }
  encodeSync(src: Uint8Array, options?: util.Type | undefined) {
    return new Uint8Array([99,97,10]);
  }
  encodeToStringSync(src: Uint8Array, options?: util.Type | undefined): string {
    return '';
  }
}
```

```json
// mock-config.json5
{
  "@ohos.util": {
    "source": "src/mock/Base64HelperMock.mock.ets"
  }
}
```

```ts
// 测试文件
import { util } from '@kit.ArkTS'
import { describe, it } from '@ohos/hypium';

export default function localUnitTest() {
  describe('localUnitTest', () => {
    it('assertContain', 0, () => {
      const array = new util.Base64Helper().decodeSync('')
    });
  });
}
```

运行报错如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/wtkWrTbfTKyLeVlLxbjdAg/zh-cn_image_0000002658808815.png "点击放大")

## 背景知识

[Mock能力](../harmonyos-guides/ide-test-mock.md)：在实际开发中，一些接口或者对象依赖于外部资源或复杂的逻辑，这些依赖在测试环境中难以复现，导致这些接口或者对象难以测试，此时，可以使用mock能力，对这些接口或对象进行模拟。

## 问题定位

请按以下方案进行排查：

1. 确认mock文件的导出方式和被mock接口的导出方式一致。

   查看被mock接口的导出方式，可以用Ctrl+鼠标左键点击被mock的接口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/i5etq4F7S8uAXh7qXE9NHA/zh-cn_image_0000002628409548.png "点击放大")

   查看mock文件的导出方式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/VExXDQuJSCSYZVctRgxvmw/zh-cn_image_0000002628569446.png "点击放大")

## 分析结论

mock文件的导出方式和被mock接口的导出方式不一致。

## 修改建议

mock文件的导出方式要与mock的接口（util接口）的导出方式一致，[util](../harmonyos-references/js-apis-util.md)接口的导出方式为export default util，所以这边mock文件的导出方式要为export default mockUtil。

1. 在“src/mock”目录下新建一个ArkTS文件，例如Base64HelperMock.mock.ets，在这个文件内定义目标模块的mock实现。

   ```ts
   import { util } from '@kit.ArkTS'
   type MockUtil = Record<string, Object>;

   export class Base64HelperMock {
     decodeSync(src: string | Uint8Array, options?: util.Type | undefined): Uint8Array {
       console.info('run mock')
       return new Uint8Array([99,97,10]);
     }
     encodeSync(src: Uint8Array, options?: util.Type | undefined) {
       return new Uint8Array([99,97,10]);
     }
     encodeToStringSync(src: Uint8Array, options?: util.Type | undefined): string {
       return '';
     }
   }

   const mockUtil: MockUtil = {
     'Base64Helper': Base64HelperMock,
   }

   export default mockUtil
   ```
2. 在mock配置文件“src/mock/mock-config.json5”中定义目标模块与mock实现的映射关系。

   ```json
   {
     "@ohos.util": {
       "source": "src/mock/Base64HelperMock.mock.ets"
     }
   }
   ```
3. 在测试文件中编写如下代码。

   ```ts
   import { util } from '@kit.ArkTS'
   import { describe, it } from '@ohos/hypium';

   export default function localUnitTest() {
     describe('localUnitTest', () => {
       it('assertContain', 0, () => {
         const array = new util.Base64Helper().decodeSync('')
       });
     });
   }
   ```
