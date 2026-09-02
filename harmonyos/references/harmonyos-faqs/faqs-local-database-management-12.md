---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-12
title: 如何读取本地/预制数据库
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何读取本地/预制数据库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:47dabcb3df3fdf3cead8c3b0c5374ae0c0d725710b47764e6800458d066d6ba9
---

**解决措施**

1. 将db文件推送到数据存储沙箱路径：/data/app/el2/100/database/(bundleName)/entry/rdb/。实现方式为使用文件管理接口打开本地数据库，读取其内容并写入沙箱路径下的db文件中。

   ```ts
   import { fileIo } from '@kit.CoreFileKit';
   import { relationalStore } from '@kit.ArkData';
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   // Obtaining the Context in EntryAbility, save it to AppStorage, then use AppStorage to retrieve it in the utility class.
   let context = AppStorage.get('context') as UIContext;
   let UiAbilityContent = context.getHostContext() as common.UIAbilityContext;
   let RDBDirectory = UiAbilityContent.databaseDir;
   let resource = UiAbilityContent.resourceManager;

   function initDatabase() {
     // Create a database sandbox directory
     try {
       let dirPath = RDBDirectory + '/rdb';
       fileIo.mkdirSync(dirPath);
     } catch (error) {
       console.error(`mkdir rdbPath failed, error code: ${error.code}, message: ${error.message}.`);
     }

     // Set db name
     let dbName: string = 'Objective.db';

     // Read the db file in the rawfile directory
     try {
       let content = resource.getRawFileContentSync(dbName);
       let cFile = RDBDirectory + '/rdb/' + dbName;
       let cacheFile = fileIo.openSync(cFile, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
       fileIo.write(cacheFile.fd, content.buffer);
       fileIo.closeSync(cacheFile.fd);
     } catch (error) {
       console.error(`callback getRawFd failed, error code: ${error.code}, message: ${error.message}.`);
     }
   }
   ```
2. 通过[getRdbStore](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore)获取保存在沙箱路径下的db文件

   ```ts
   async function getRDB(): Promise<relationalStore.RdbStore | undefined> {
     let result: relationalStore.RdbStore | undefined = undefined;
     const STORE_CONFIG: relationalStore.StoreConfig = {
       name: 'Objective.db',
       securityLevel: relationalStore.SecurityLevel.S1
     };

     await relationalStore.getRdbStore(UiAbilityContent, STORE_CONFIG).then((rdbStore: relationalStore.RdbStore) => {
       result = rdbStore;
       console.info('Get RdbStore successfully.');
     }).catch((err: BusinessError) => {
       console.error(`Get RdbStore failed, code is ${err.code}, message is ${err.message}`);
     });
     return result;
   }
   ```
