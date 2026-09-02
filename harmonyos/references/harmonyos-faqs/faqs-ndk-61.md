---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-61
title: 传入自定义类型对象到Native侧时，index.d.ts文件如何声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 传入自定义类型对象到Native侧时，index.d.ts文件如何声明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:580c4a6719d61b365833768c487ba038968faa1fa2f211858000f2121992837c
---

此处以testCb为例

```ts
class testCb {
  testNum: number = 0;
  testString: string = "";
}
```

方法一：

在index.d.ts文件中使用object类型进行声明。

```ts
export const modifyObject: (a: object) => object;
```

方法二：

创建xx.ts文件，并在该文件中导出类。然后在index.d.ts文件中导入并使用该类。

test.ts 导出类声明。

```ts
export class testCa {
  testNum: number = 0;
  testString: string = "";
}
```

在index.d.ts中导入并使用。

```ts
import { testCa } from "../../../ets/pages/interface/CustomObject"
export const test1: (a: testCa) => void;
```
