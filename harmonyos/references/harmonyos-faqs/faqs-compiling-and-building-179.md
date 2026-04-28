---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-179
title: 在.ts文件中使用“import { export } from 'xxx.so';”方式导入.so文件编译告警：“Currently module for 'xxx.so' is not verified. ”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 在.ts文件中使用“import { export } from 'xxx.so';”方式导入.so文件编译告警：“Currently module for 'xxx.so' is not verified. ”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d14fa3ce1545928545616c72607c0d92438541f65739d812bd400e387df404b9
---

**问题现象**

在.ts文件中，按照编辑器修复建议使用“import { export } from 'xxx.so';”的方式导入.so文件后，编译告警（Currently module for 'xxx.so' is not verified. If you're importing napi, its verification will be enabled in later SDK version. Please make sure the corresponding .d.ts file is provided and the napis are correctly declared.）并出现相关类型报错。

**问题原因**

若使用“import { export } from 'xxx.so';”方式导入.so文件，编译器不会对.so文件中的变量、属性或方法进行解析，类型均为any，因此出现告警。

**解决措施**

方案一：使用类型断言为从.so文件引入的变量、属性、方法赋予确定的类型。

方案二：若.so文件与.ts文件同时存在于同一个模块中，可以通过相对路径的方式引入.so文件。例如：“import { export } from './index';”，其中当前文件与.so的实际入口文件index位于同一目录下。
