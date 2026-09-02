---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-49
title: 一个HSP模块如何快速切换成HAR模块
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 一个HSP模块如何快速切换成HAR模块
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:29+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:f8acde1503b7273765c6764309a32c025ef3f3be0850a97bcca82bd259048a8d
---

**解决方案**

1.在HSP下的module.json5中，把"type": "shared"修改为"type": "har"，删除"deliveryWithInstall"、"pages"字段。

2.删除HSP下的oh-package.json5中"packageType"字段。

3.删除HSP中的页面，如果要以页面的形式使用的话，就需要改为命名路由的写法。

4.然后再找到HSP下的hvigorfile.ts文件，将里面的hspTasks改为harTasks。

5.最后编译该模块即可。

编译过程中遇到其他错误时，根据提示找到对应位置并进行修改。

**说明** 

部分组件和模块在HAP、HSP、HAR中集成使用时存在差异，例如[加载HAR中Worker线程文件相比HSP存在单独的使用约束](../harmonyos-guides/worker-introduction.md#文件路径注意事项)，因此按照以上步骤完成HSP转HAR后，请关注对应组件和模块介绍并进行适配。
