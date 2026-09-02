---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-171
title: 如何使用泛型定义接口数据
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何使用泛型定义接口数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:67ddd856705138c3ec8ff17cc867a3d91e77c446f53c25064e004a462c242c20
---

## 问题现象

接口返回数据里的data字段类型不固定，如何对不同类型的数据使用同一个入口进行接收管理。

## 背景知识

泛型：使代码能够以类型安全的方式操作多种数据类型，而无需为每种类型编写重复的逻辑。

## 解决方案

定义API接口返回的数据类型，其中data属性使用泛型T，使用的时候再指定类型。示例代码如下：

```ts
import { buffer } from '@kit.ArkTS';

// 通过泛型定义api响应接口模型
interface ApiResponse<T> {
  code: number;
  message: string;
  data: T;
}

class User {
  id: number = 0;
  name: string = '';
}

// 定义不同接口返回的数据类型
function fetchData(context: Context): Promise<ApiResponse<string | number[]>> {
  // 模拟网络请求
  return new Promise((rs, rj) => {
    try {
      const value = context.resourceManager.getRawFileContentSync('data.json');
      const str = buffer.from(value.buffer).toString();
      const res = JSON.parse(str) as ApiResponse<string | number[]>;
      rs(res);
    } catch (e) {
      rj(e);
    }
  });
}

function fetchUsers(context: Context): Promise<ApiResponse<User[]>> {
  return new Promise((rs, rj) => {
    try {
      const value = context.resourceManager.getRawFileContentSync('user.json');
      const str = buffer.from(value.buffer).toString();
      const res = JSON.parse(str) as ApiResponse<User[]>;
      rs(res);
    } catch (e) {
      rj(e);
    }
  });
}

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext();

  build() {
    Column() {
      Button('fetchData')
        .onClick(() => {
          fetchData(this.context!!).then(resp => {
            const data = resp.data;
            // 根据类型走不同的逻辑处理
            if (typeof data === 'string') {
              // ...
              console.info(`fetch data: ${data}`);
            } else if (Array.isArray(data)) {
              // ...
            }
          }).catch((e: ESObject) => {
            console.info(`fetch error: ${JSON.stringify(e)}`);
          });
        })
      Button('fetchUsers')
        .onClick(() => {
          fetchUsers(this.context!!).then(resp => {
            const data = resp.data;
            console.info(`fetch user list: ${JSON.stringify(data)}`);
          });
        })
        .margin({ top: 30 })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

本地模拟接口数据：

在rawfile/data/data.json中。

```json
{
    "code": 200,
    "message": "success",
    "data": "my data"
  }
```

在rawfile/data/user.json中。

```json
{
    "code": 200,
    "message": "success",
    "data": [
      {
        "id": 1,
        "name": "aa"
      },
      {
        "id": 2,
        "name": "bb"
      }
    ]
  }
```
