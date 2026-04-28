---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-localization
title: 多语言支持
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > 多语言支持
category: harmonyos-references
scraped_at: 2026-04-28T08:03:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:af856cb2b482ad0bb60fae747aa100c66dfc0d07db3edf43626fb746db1412d7
---

基于开发框架的应用会覆盖多个国家和地区，开发框架支持多语言能力后，可以让应用开发者无需开发多个不同语言的版本，就可以同时支持多种语言的切换，为项目维护带来便利。

开发者仅需要通过[定义资源文件](js-lite-framework-localization.md#定义资源文件)和[引用资源](js-lite-framework-localization.md#引用资源)两个步骤，就可以使用开发框架的多语言能力；如果需要在应用中获取当前系统语言，请参考[获取语言](js-lite-framework-localization.md#获取语言)。

## 定义资源文件

PhonePC/2in1TabletTVWearableLite Wearable

资源文件用于存放应用在多种语言场景下的资源内容，开发框架使用JSON文件保存资源定义。

在[文件组织](js-lite-framework-file.md)中指定的i18n文件夹内放置每个语言地区下的资源定义文件即可，资源文件命名为“语言-地区.json”格式，例如英文（美国）的资源文件命名为en-US.json。当开发框架无法在应用中找到系统语言的资源文件时，默认使用en-US.json中的资源内容。

资源文件内容格式如下：

en-US.json

```
1. {
2. "strings": {
3. "hello": "Hello world!",
4. "object": "Object parameter substitution-{name}",
5. "array": "Array type parameter substitution-{0}",
6. "symbol": "@#$%^&*()_+-={}[]\\|:;\"'<>,./?"
7. },

9. "files": {
10. "image": "image/en_picture.PNG"
11. }
12. }
```

## 引用资源

PhonePC/2in1TabletTVWearableLite Wearable

* 在应用中使用$t方法引用资源，$t既可以在hml中使用，也可以在js中使用。系统将根据当前语言环境和指定的资源路径（通过$t的path参数设置），显示对应语言的资源文件中的内容。

  | 参数 | 类型 | 必填 | 描述 |
  | --- | --- | --- | --- |
  | path | string | 是 | 资源路径 |
  | params | Array|Object | 否 | 运行时用来替换占位符的实际内容，占位符分为两种：具名占位符，例如{name}。实际内容必须用Object类型指定，例如：$t('strings.object', **{ name: 'Hello world' }**)。数字占位符，例如{0}。实际内容必须用Array类型指定，例如：$t('strings.array', **['Hello world']**)。 |
* 示例代码

  ```
  1. <!-- xxx.hml -->
  2. <div>
  3. <!-- 不使用占位符，text中显示“Hello world!” -->
  4. <text>{{ $t('strings.hello') }}</text>
  5. <!-- 具名占位符格式，运行时将占位符{name}替换为“Hello world” -->
  6. <text>{{ $t('strings.object', { name: 'Hello world' }) }}</text>
  7. <!-- 数字占位符格式，运行时将占位符{0}替换为“Hello world” -->
  8. <text>{{ $t('strings.array', ['Hello world']) }}</text>
  9. <!-- 先在js中获取资源内容，再在text中显示“Hello world” -->
  10. <text>{{ hello }}</text>
  11. <!-- 先在js中获取资源内容，并将占位符{name}替换为“Hello world”，再在text中显示“Object parameter substitution-Hello world” -->
  12. <text>{{ replaceObject }}</text>
  13. <!-- 先在js中获取资源内容，并将占位符{0}替换为“Hello world”，再在text中显示“Array type parameter substitution-Hello world” -->
  14. <text>{{ replaceArray }}</text>

  16. <!-- 获取图片路径 -->
  17. <image src="{{ $t('files.image') }}" class="image"></image>
  18. <!-- 先在js中获取图片路径，再在image中显示图片 -->
  19. <image src="{{ replaceSrc }}" class="image"></image>
  20. </div>
  ```

  ```
  1. // xxx.js
  2. // 下面为在js文件中的使用方法。
  3. export default {
  4. data: {
  5. hello: '',
  6. replaceObject: '',
  7. replaceArray: '',
  8. replaceSrc: '',
  9. },
  10. onInit() {
  11. this.hello = this.$t('strings.hello');
  12. this.replaceObject = this.$t('strings.object', { name: 'Hello world' });
  13. this.replaceArray = this.$t('strings.array', ['Hello world']);
  14. this.replaceSrc = this.$t('files.image');
  15. },
  16. }
  ```

## 获取语言

PhonePC/2in1TabletTVWearableLite Wearable

获取语言功能请参考[应用配置](js-apis-system-configuration.md)。
