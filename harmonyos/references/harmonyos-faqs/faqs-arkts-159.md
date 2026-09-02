---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-159
title: 如何解析URL信息
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何解析URL信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50211c6e152ffde234313830dca9ff9e8a7e09d1ffc111115740871f8ce73e05
---

## 问题现象

如何解析URL网址并获取所携带的参数信息？

## 背景知识

URL（Uniform Resource Locator）统一资源定位器，计算机Web网络相关的术语，译为网页地址。

## 解决方案

[@ohos.url (URL字符串解析)](../harmonyos-references/js-apis-url.md)提供了常用的工具函数，实现了解析URL字符串和构造URL对象等功能。

```ts
import { url } from '@kit.ArkTS';

@Entry
@Component
struct ParseUrl {
  build() {
    Column() {
      Button('解析url信息').onClick(() => {
        let that = url.URL.parseURL('https://username:password@host:8080/directory/file?foo=1&bar=2#fragment');
        console.info(`hash:${that.hash}`); // #fragment
        console.info(`host:${that.host}`); // host:8080
        console.info(`hostname:${that.hostname}`); // host
        console.info(`href:${that.href}`); // https://username:password@host:8080/directory/file?foo=1&bar=2#fragment
        console.info(`origin:${that.origin}`); // https://host:8080
        console.info(`password:${that.password}`); // password
        console.info(`pathname:${that.pathname}`); // /directory/file
        console.info(`port:${that.port}`); // 8080
        console.info(`protocol:${that.protocol}`); // https:
        console.info(`search:${that.search}`); // ?foo=1&bar=2
        console.info(`username:${that.username}`); // username
        // that.params返回值为URLParams对象
        console.info(`params: foo${that.params.get('foo')}`); // 1
      });

      Button('解析url中#后的数据').onClick(() => {
        let result =
          this.isUrlHasSomeKey('https://username:password@host:8080/#/directory/file?foo=1&bar=666',
            'bar');
        console.info(`是否成功解析url中#后的数据：${result}`);
      });
    };
  }

  //判断URL中是否包含某个key
  isUrlHasSomeKey(urlStr: string, key: string) {
    if (urlStr.length === 0) {
      return false;
    }
    console.info(`待解析的url：${urlStr}`);
    let urlTemp = url.URL.parseURL(urlStr);
    let paramsString = urlTemp.search.slice(1);
    let paramsObject = new url.URLParams(paramsString);
    // 先按照正常方式判断，如果成功就返回，失败再获取hash值，再继续判断
    if (paramsObject.has(key)) {
      return true;
    } else {
      // 如果正常方式判断不含有对应的key，有可能是URL中有#的hash值，所以通过获取hash值，最终确定是否有对应的key
      let paramsObject1 = new url.URLParams(urlTemp.hash);
      if (paramsObject1.has(key)) {
        console.info(`解析url中#后的数据为：${paramsObject1.get(key)}`);
        return true;
      } else {
        return false;
      }
    }
  }
}
```

## 常见FAQ

Q：URL的参数放置在哈希路由符号"#"之后，通过URL解析接口获取不到参数？

A：URL标准规范中，哈希路由符号"#"后的内容属于页面片段标识，URL解析接口默认不处理该部分参数，可通过字符串处理后获取URL参数，参考如下代码。

```ts
//判断URL中是否包含某个key
isUrlHasSomeKey(urlStr: string, key: string) {
  if (urlStr.length === 0) {
    return false;
  }
  console.info(`待解析的url：${urlStr}`);
  let urlTemp = url.URL.parseURL(urlStr);
  let paramsString = urlTemp.search.slice(1);
  let paramsObject = new url.URLParams(paramsString);
  // 先按照正常方式判断，如果成功就返回，失败再获取hash值，再继续判断
  if (paramsObject.has(key)) {
    return true;
  } else {
    // 如果正常方式判断不含有对应的key，有可能是URL中有#的hash值，所以通过获取hash值，最终确定是否有对应的key
    let paramsObject1 = new url.URLParams(urlTemp.hash);
    if (paramsObject1.has(key)) {
      console.info(`解析url中#后的数据为：${paramsObject1.get(key)}`);
      return true;
    } else {
      return false;
    }
  }
}
```
