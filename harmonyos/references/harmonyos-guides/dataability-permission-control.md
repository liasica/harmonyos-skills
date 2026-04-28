---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-permission-control
title: DataAbility权限控制
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > DataAbility权限控制
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:08efd050d07ea928e47da2463c36fc3cc2c9d96c007738f4c186ade43790e973
---

DataAbility提供数据服务，并不是所有的Ability都有权限读写它，DataAbility有一套权限控制机制来保证数据安全。分为静态权限控制和动态权限控制两部分。

## 静态权限控制

DataAbility作为服务端，在被拉起的时候，会根据config.json里面配置的权限来进行校验，有"readPermission"、"writePermission"和"Permission"三个配置项，可以不配或者为空。示例如下:

```
1. "abilities": [
2. // ...
3. {
4. "name": ".DataAbility",
5. "srcLanguage": "ets",
6. "srcPath": "DataAbility",
7. "icon": "$media:icon",
8. "description": "$string:DataAbility_desc",
9. "type": "data",
10. "visible": true,
11. "uri": "dataability://com.samples.famodelabilitydevelop.DataAbility",
12. "readPermission": "ohos.permission.READ_CONTACTS",
13. "writePermission": "ohos.permission.WRITE_CONTACTS"
14. },
15. // ...
16. ]
```

客户端在拉起DataAbility的时候，需要校验客户端是否有权限拉起该DataAbility。客户端的权限配置在config.json配置文件的"module"对象的"reqPermissions"对象中，示例如下：

```
1. {
2. // ...
3. "module": {
4. // ...
5. "reqPermissions": [
6. {
7. "name": "ohos.permission.READ_CONTACTS"
8. },
9. {
10. "name": "ohos.permission.WRITE_CONTACTS"
11. },
12. // ...
13. ],
14. // ...
15. }
16. }
```

## 动态权限控制

静态权限校验只能控制某个DataAbility是否能被另一个Ability或应用拉起，无法精确校验每个读写接口的权限，因为拉起DataAbility的时候，还不知道应用是否需要读写它的数据。

动态权限控制是校验每个数据操作的接口是否有对应的权限。客户端调用数据操作接口所需的权限如下表所示。

**表1** 接口对应的读写权限配置

| 需要配置读权限的接口 | 需要配置写权限的接口 | 根据实际操作配置读写权限的接口 |
| --- | --- | --- |
| query、normalizeUri、denormalizeUri、openfile（传入mode有'r'） | insert、batchInsert、delete、update、openfile（传入mode有'w'） | executeBatch |

对于需要配置读权限的接口，服务端需要配置readPermission，客户端必须申请相应的读权限才能调用相关的接口。

对于需要配置写权限的接口，服务端需要配置writePermission，客户端必须申请相应的写权限才能调用相关的接口。
