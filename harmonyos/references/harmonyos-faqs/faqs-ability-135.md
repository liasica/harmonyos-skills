---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-135
title: 华为浏览器拉起应用类型错误
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 华为浏览器拉起应用类型错误
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:13f88c185afe5e227389cf6b757216dc0463c0bb47d1823123c90e56cb02eb7c
---

## 问题现象

华为浏览器拉起特定类型应用时，弹窗推荐列表中出现非目标类型应用（如非支付类应用和非导航类应用），导致用户误选，影响使用体验。

## 背景知识

* [使用Deep Linking实现应用间跳转](../harmonyos-guides/deep-linking-startup.md)：采用Deep Linking进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。当匹配到多个应用时，会拉起应用选择框。
* [uris标签说明](../harmonyos-guides/app-uri-config.md#uris标签说明)：
  + scheme：协议名称。常见的取值有http、https、file、ftp等，也可以自定义。
  + host：域名或IP地址。例如域名developer.huawei.com或IP地址127.0.0.1。
  + port：端口号。例如developer.huawei.com:80后面的80即为端口号。
* [URL的基本格式](../harmonyos-guides/app-uri-config.md#url的基本格式)：按照配置的字段不同，uris可以拼接为不同的URL表达式。其中，scheme为必选字段，其他字段仅当scheme存在时才有意义。
  + 只配置scheme：scheme://。
  + 只配置scheme和host：scheme://host。
  + 只配置scheme、host和port：scheme://host:port。
* 如果被拉起应用有多个应用的uri配置相同，则主应用跳转时就会匹配到同多个应用，就会拉起应用选择框。为了更好的用户体验，开发者可以通过链接的path字段去区分同一域名下的不同应用。

## 问题定位

1. 通过如下日志multiple abilities support this deeplink可以确认：华为浏览器网页中跳转三方应用使用的是Deep Linking的方式。

   ```shell
   C01120/com.huawei.example.app/BMS  com.huawei.example.app  I     QueryAbilityInfosComplete before return
   A06666/com.huawei.example.app/xxx  com.huawei.example.app  I     queryAbilityInfo success
   A06666/com.huawei.example.app/xxx  com.huawei.example.app  I     multiple abilities support this deeplink
   A06666/com.huawei.example.app/xxx  com.huawei.example.app  I     queryAbilityInfo reason 0
   A06666/com.huawei.example.app/xxx  com.huawei.example.app  I     startApp result consumedClickEvent true
   ```
2. 排查被拉起应用配置的scheme，是否配置了和自身不匹配的uris。
3. 场景一（弹窗推荐列表中出现非支付类型应用）：查看除了支付类应用以外，其他两个应用在module.json5配置文件里skills标签的uri配置，查到的配置如下：

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           // ...
           "skills": [
             {
               "entities": [
                 "entity.system.browsable"
               ],
               "actions": [
                 "ohos.want.action.viewData"
               ],
               "uris": [
                 {
                   "scheme": "xxxpay"
                 }
               ]
             }
           ]
         }
       ]
     }
   }
   ```

   场景二（弹窗推荐列表中出现非导航类型应用）：查看其他两个非导航类型应用在module.json5配置文件里skills标签的uri配置，查到的配置如下：

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           // ...
           "skills": [
             {
               "entities": [
                 "entity.system.browsable"
               ],
               "actions": [
                 "ohos.want.action.viewData"
               ],
               "uris": [
                 {
                   "scheme": "***map"
                 }
               ]
             }
           ]
         }
       ]
     }
   }
   ```

## 分析结论

### 场景一

支付类应用误匹配（Deep Linking scheme冲突）

由于非支付类应用错误配置了与支付类应用相同的 scheme（如 xxxpay://），当用户在华为浏览器中访问支付相关链接并点击打开支付类应用时，系统通过Deep Linking匹配所有注册了xxxpay:// 的应用，导致弹窗中出现支付类应用和其他非支付类应用多个选项，造成用户混淆与误操作。

### 场景二

导航类应用误匹配（Deep Linking scheme冲突）

类似地，非导航类应用错误注册了与主流导航应用相同的 scheme（如 \*\*\*map:// 或 \*\*\*map://），当用户在华为浏览器中点击导航链接（如“导航到此位置”）时，系统会匹配所有注册了该 scheme 的应用。因此，弹窗中不仅出现主流导航应用，还混入了其他非导航类应用。

## 修改建议

### 场景一

对于非支付类应用，删除在module.json5配置文件里skills标签的uri配置的"xxxpay"等scheme配置。

### 场景二

对于非导航类应用，删除在module.json5配置文件里skills标签的uri配置的"\*\*\*map"等scheme配置。
