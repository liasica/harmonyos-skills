---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-61
title: 如何在指定文件夹内备份关系型数据库
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何在指定文件夹内备份关系型数据库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:242816dc8757a600ac797da67e597c3724649edd6d1c092dbe745ca84fa409e6
---

## 问题现象

通过rdbStore.backup备份关系型数据库时，如何指定备份目录呢？

## 背景知识

* [关系型数据库](../harmonyos-guides/data-persistence-by-rdb-store.md)：ArkTS关系型数据库基于SQLite实现，为应用提供数据持久化能力。
* [关系型数据库备份](../harmonyos-guides/data-backup-and-restore.md#关系型数据库备份)：通过[rdbStore.backup(name)](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#backup-1)指定名称的形式进行数据库备份。
* [fs.moveFile](../harmonyos-references/js-apis-file-fs.md#fileiomovefile)：将源文件移动至目标目录当中。
* [保存文件至公共目录](../harmonyos-guides/save-user-file.md#保存文档类文件)：将文件保存至设备公共目录当中。

## 解决方案

1. ArkTS创建数据库的时候，如果没有指定目录，数据库db文件会保存在默认数据库目录当中。提供一个数据库工具类：

   ```ts
   import { relationalStore } from '@kit.ArkData';

   export class DBUtil {
     private static rdbStore: relationalStore.RdbStore | null = null;
     private static context: Context;

     static readonly createTableSql: string = `
         CREATE TABLE IF NOT EXISTS Employee (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL
         )`;

     static async init(context: Context) {
       DBUtil.context = context;
       if (!DBUtil.rdbStore) {
         let config: relationalStore.StoreConfig = {
           name: 'RdbTest.db',
           securityLevel: relationalStore.SecurityLevel.S1
         };
         relationalStore.getRdbStore(DBUtil.context, config).then(rdbStore => {
           DBUtil.rdbStore = rdbStore;
           try {
             rdbStore.executeSync(DBUtil.createTableSql);
           } catch (error) {
             console.error(JSON.stringify(error));
           }
         });
       }
     }

     static testData() {
       let emps: relationalStore.ValuesBucket[] = [];
       for (let i = 0; i < 20; i++) {
         emps.push({
           id: i,
           name: `test${i}`
         });
       }
       DBUtil.rdbStore?.batchInsertSync('Employee', emps);
     }

     static getRdbStore() {
       return DBUtil.rdbStore!;
     }

     static queryData() {
       let emps: Employee[] = [];
       let predicates = new relationalStore.RdbPredicates('Employee');
       let resultSet = DBUtil.rdbStore!.querySync(predicates);
       while (resultSet.goToNextRow()) {
         let emp: Employee = {
           id: resultSet.getLong(resultSet.getColumnIndex('id')),
           name: resultSet.getString(resultSet.getColumnIndex('name'))
         };
         emps.push(emp);
       }
       return emps;
     }

     static deleteData() {
       let predicates = new relationalStore.RdbPredicates('Employee');
       DBUtil.rdbStore?.deleteSync(predicates);
     }
   }

   export interface Employee {
     id: number,
     name: string
   }
   ```
2. 在指定目录当中备份数据，此处以files下面的backup目录为例。

   ```ts
   try {
     await DBUtil.getRdbStore().backup('RdbTestBackup.db');
     let dbDir = this.getUIContext().getHostContext()!.databaseDir;
     let backDir = `${this.getUIContext().getHostContext()!.filesDir}/backup`;
     if (!fileIo.accessSync(backDir)) {
       fileIo.mkdirSync(backDir);
     }
     if (fileIo.accessSync(`${backDir}/RdbTestBackup.db`)) {
       fileIo.unlinkSync(`${backDir}/RdbTestBackup.db`);
     }
     fileIo.moveFileSync(`${dbDir}/rdb/RdbTestBackup.db`, `${backDir}/RdbTestBackup.db`);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`backup failed, code is ${err.code},message is ${err.message}`);
   }
   ```

完整示例参考如下：

```ts
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DBUtil, Employee } from './DBUtil';

@Entry
@Component
struct DataBackupPage {
  @State emps: Employee[] = [];

  aboutToAppear(): void {
    DBUtil.init(this.getUIContext().getHostContext()!);
  }

  build() {
    Scroll() {
      Column({ space: 20}) {
        Button('添加测试数据')
          .onClick(() => {
            DBUtil.testData();
          })

        Button('查询所有数据')
          .onClick(() => {
            this.emps = DBUtil.queryData();
          })

        Button('删除所有数据')
          .onClick(() => {
            DBUtil.deleteData();
            this.emps = DBUtil.queryData();
          })

        Button('备份数据到指定目录')
          .onClick(async () => {
            try {
              await DBUtil.getRdbStore().backup('RdbTestBackup.db');
              let dbDir = this.getUIContext().getHostContext()!.databaseDir;
              let backDir = `${this.getUIContext().getHostContext()!.filesDir}/backup`;
              if (!fileIo.accessSync(backDir)) {
                fileIo.mkdirSync(backDir);
              }
              if (fileIo.accessSync(`${backDir}/RdbTestBackup.db`)) {
                fileIo.unlinkSync(`${backDir}/RdbTestBackup.db`);
              }
              fileIo.moveFileSync(`${dbDir}/rdb/RdbTestBackup.db`, `${backDir}/RdbTestBackup.db`);
            } catch (error) {
              const err = error as BusinessError;
              console.error(`backup failed, code is ${err.code},message is ${err.message}`);
            }
          })

        Button('恢复数据')
          .onClick(() => {
            let backDir = `${this.getUIContext().getHostContext()!.filesDir}/backup`;
            let dbDir = this.getUIContext().getHostContext()!.databaseDir;
            try {
              if (!fileIo.accessSync(`${backDir}/RdbTestBackup.db`)) {
                return;
              }
              fileIo.copyFileSync(`${backDir}/RdbTestBackup.db`, `${dbDir}/rdb/RdbTestBackup.db`);
              DBUtil.getRdbStore().restore('RdbTestBackup.db').catch((err: BusinessError) => {
                console.error(`Restore failed, code is ${err.code},message is ${err.message}`);
              });
            } catch (error) {
              const err = error as BusinessError;
              console.error(`backup failed, code is ${err.code},message is ${err.message}`);
            }
          })

        Column() {
          if (this.emps.length > 0) {
            ForEach(this.emps, (emp: Employee) => {
              Row() {
                Text(`${emp.id}---${emp.name}`)
              }
              .width('80%')
              .padding(5)
              .borderWidth(1)
            })
          } else {
            Text('没有数据！')
          }
        }
        .width('100%')
        .padding(10)
        .backgroundColor('#d0e6fb')
      }
      .height('100%')
      .width('100%')
    }.height('100%')
    .width('100%')
  }
}
```
