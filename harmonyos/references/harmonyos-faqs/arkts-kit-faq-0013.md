---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0013
title: ArkTS语法使用与错误排查常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > ArkTS语法使用与错误排查常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:45874d94787878eeb82eb0e55ef58d9f8efdfe101a7ab2cc6c8e6e1c84f2a53e
---

**Q：如何遍历JSON对象？**

**A**：具体请参考如下示例代码：

```ts
import { ArrayList } from '@kit.ArkTS';

interface Winner { num: number };
let tmpStr: Record<string, Winner> = JSON.parse('{ "0": {"num": 1}, "1": {"num": 2} }');
const arrayList: ArrayList<Winner> = new ArrayList();
Object.entries(tmpStr).forEach((item) => {
  const value = item[1];
  arrayList.add(value);
})
```

**Q：如何获取对象的类名？**

**A**：获取类的实例，通过constructor的name属性获取类名。示例如下：

```ts
class TestClass {
  a: string = 'A';
  b: string = 'B';
}

let testClassObj: TestClass = new TestClass();

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get Class Name')
          .onClick(() => {
            console.log('TestClass Name:', testClassObj.constructor.name);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**Q：工程构建时出现ArkTS语法告警提示，如何处理？**

**A**：该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](../harmonyos-guides/arkts.md)。

报错信息：

1. ERROR: ArkTS:ERROR File: C:/Users/... ,Use“let”instead of“var”(arkts-no-var)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9hLLjX2RRyixccjQSsTJqA/zh-cn_image_0000002774075424.png "点击放大")
2. ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The“@Sendable”decorator can only be used on“class”,“function”and“typeAlias”(arkts-sendable-decorator-limited)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/uPvEFmj6QH-jw1-K70SSbQ/zh-cn_image_0000002773914854.png "点击放大")

**Q：ArkTS是否支持TypeScript中的闭包函数？**

**A**：ArkTS不支持在函数内声明函数，可以使用lambda函数作为替代。

参考链接：[不支持在函数内声明函数](../harmonyos-guides/typescript-to-arkts-migration-guide.md#不支持在函数内声明函数)。
