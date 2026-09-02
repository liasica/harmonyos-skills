---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-19
title: 点分版本号变更后API兼容性判断方式说明
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 点分版本号变更后API兼容性判断方式说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d46a624e8f720b285da4f2a90d99c0987a66763e39ea1d6766bb7e0ad62ae593
---

**问题描述**

7.0版本支持点分版本号，使用点分版本号时，API兼容性判断方式与之前有差异，如新增的API兼容性判断方式、@[Available](../harmonyos-references/js-apis-annotation.md#available)注解等差异。

**解决措施**

* 新增的API兼容性判断方式
  1. ArkTS语言新增的API兼容性判断方式。

     apiAvailable()接口使用方式。

     ```screen
     getTestData(): void {
       if (deviceInfo.sdkApiVersion >= 24 && deviceInfo.apiAvailable('26.0.0')) {
         // Calling APIs of 26.0.0
       } else {
         // Downgrade Scheme
       }
     }
     ```
  2. C/C++语言新增的API兼容性判断方式。

     APIAVAILABLE()接口使用方式。

     ```screen
     void testFunction(){
         if(APIAVAILABLE(24, 0, 0)){
             // method invocation
         }
     }
     ```

* 通过@[Available](../harmonyos-references/js-apis-annotation.md#available)注解进行API兼容性判断的差异

  在点分版本号变更后，可支持使用三位数字的版本号参数。（仅支持ArkTS，从API 22版本开始支持。）

  ```screen
  // HarmonyOS
  @Available({ minApiVersion: 'HarmonyOS 7.0.0' })
  function  func2(){}
  ```

  ```screen
  // OpenHarmony
  @Available({ minApiVersion: '26' })
  function  func1(){
    func2()
  }
  ```
