---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-432
title: Navigation组件，使用customNavContentTransition自定义转场动效，如何实现动效逻辑跟组件解耦
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件，使用customNavContentTransition自定义转场动效，如何实现动效逻辑跟组件解耦
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9f5d1c4159a842bcfd67f86d425ee3d27031580617606197d8f8e346ae200cee
---

**问题描述**

使用Navigation作为路由框架之后，默认Component跳转是有右进右出的动画的。 但是dialog以及从dialog中再跳转其他page是没有动画的。

1. 如果使用customNavContentTransition之后，原来的默认page动画会失效。

2. Navigation的示例，customNavContentTransition的动画必须在目标component的布局中去关联参数，这个太麻烦了，没法统一封装。

这两问题有解决方案么？

**解决措施**

1.customNavContentTransition是自定义转场动画，若返回未定义（undefined），是可以执行默认转场动效的，当需要根据不同条件返回动画时，可使用条件判断返回undefined或自定义动画。

2.目前Navigation转场动画设计如此，若感觉实现过于复杂，可以考虑使用HMRouter，该框架底层对Navigation相关能力进行了封装，帮助开发者减少对Navigation相关细节内容的关注、提高开发效率，其中也封装了全局动画方法。

**参考链接**

[基于HMRouter的页面跳转](../best-practices/bpta-hmrouter.md)

[HMRouter仓库地址](https://gitcode.com/openharmony-sig/ohrouter)
