---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/compatibility-warning-suppress
title: 兼容性告警屏蔽
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护和告警屏蔽 > 兼容性告警屏蔽
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:40+08:00
doc_updated_at: 2026-07-06
content_hash: sha256:068bc32155c3c94506af29b75ad506c70a2026278599cea78fa09a923a947077
---

从DevEco Studio 6.1.0 Beta2开始，DevEco Studio新增ArkTS API接口兼容性告警屏蔽能力，支持通过添加@SuppressWarnings注解或@SuppressWarnings单行注释的方式消除COMPATIBILITY类型的告警。

## 通过注解屏蔽

注解可以添加在变量声明、类型声明、函数声明、命名空间声明、注解声明、结构体成员、类成员、接口成员上，消除内部或自身产生的告警，注解语句为@SuppressWarnings({ rules: [SuppressWarningsType.COMPATIBILITY] })。

**使用示例：**

```screen
import { Available, SuppressWarnings, SuppressWarningsType } from '@ohos.annotation';

// 标记最小可用版本为API 23，当工程兼容版本低于API 23时会触发告警
@Available({ minApiVersion: "23" })
function test(): string {
  return "hello world";
}

// 通过@SuppressWarnings注解屏蔽类成员中的告警提示
@SuppressWarnings({ rules: [SuppressWarningsType.COMPATIBILITY] })
class TestClass {
  a = test(); // 告警会被屏蔽

  testFunction() {
    test(); // 告警会被屏蔽
  }
}
```

## 通过单行注释屏蔽

对于不支持添加注解的场景，可在需要屏蔽的告警提示代码行上方添加单行注释来屏蔽告警提示，单行注释语句为@SuppressWarnings compatibility。

**使用示例：**

```screen
import { Available } from '@ohos.annotation';

// 标记最小可用版本为API 23，当工程兼容版本低于API 23时会触发告警
@Available({ minApiVersion: "23" })
function test(): string {
  return "hello world";
}

// 通过@SuppressWarnings注释屏蔽非声明式元素的告警提示
class TestClass {
  testFunction() {
    // @SuppressWarnings compatibility
    test(); // 告警会被屏蔽
  }
}
```
