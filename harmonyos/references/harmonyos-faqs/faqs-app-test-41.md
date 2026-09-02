---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-41
title: Mock使用中的常见问题和解决方案
breadcrumb: FAQ > DevEco Studio > 应用测试 > Mock使用中的常见问题和解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b4b65b5c6d8805d8f1424badaaa23b12f8a3473ca7b7bfb03c5d19ff18a7917b
---

## 问题现象

* **问题一：**

  原函数不在类中，如何对被Mock对象实例进行还原处理？
* **问题二：**

  如何对函数中需要调用的回调函数进行Mock？
* **问题三：**

  使用mocker.verify('receiptToServiceDynamics',[params]).once()是否可以像Java的Mockito一样，实现参数匹配？

## 解决方案

* **问题一解决方案：**

  参考[使用hamock/hypium插件包的mock接口](../harmonyos-guides/ide-test-mock.md#section1644161411818)，将函数加入类中，创建Mock对象，使用ignoreMock或者clear进行还原即可，具体实现可参考[Mock能力](../harmonyos-guides/unittest-guidelines.md#mock能力)示例代码6和示例代码7。
* **问题二解决方案：**

  参考[Mock能力](../harmonyos-guides/unittest-guidelines.md#mock能力)，afterAction接口可以设定预期返回一个函数执行的动作。

  假设函数为func1，回调函数为func2，对func1进行Mock之后，通过when(mockfunc)(‘参数是anyFunction类型’).afterAction(func2)执行回调，实现对应业务逻辑。
* **问题三解决方案：**
  1. mocker.verify：HarmonyOS单元测试中mocker.verify通常用于验证被Mock的方法是否被调用，以及调用的次数、参数等，该方法本身没有自带参数匹配器的用法，只支持全等比较，目前做不到Java-mockito的argThat()。mocker.verify(methodName, argsArray)，返回VerificationMode实例。根据传入的methodName和argsArray.toString()拼接的key在recordCallsMap中查找次数，没找到计为0，然后创建VerificationMode(times)。VerificationMode可用断言方法：times(count)，once()，never()，atLeast(count)，atMost(count)。verify匹配基于args的toString()值，因此对对象/数组/复杂类型不可靠。
  2. afterAction(x：action)：设定预期返回一个函数执行的操作。对复杂对象可以使用afterAction记录结构化参数并计数。
  3. 只有在保证参数字符串化稳定时，才使用mocker.verify的现有字符串匹配。对复杂对象可以先执行所有调用，通过afterAction使用变量记录满足条件的结果，最后通过断言进行判断。
